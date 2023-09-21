
from matplotlib import pyplot as plt
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import rasterio
from rasterio.mask import mask
from rasterio.io import MemoryFile
from glob import glob
import geopandas as gpd
#from osgeo import gdal
import csv
from localtileserver import get_leaflet_tile_layer, TileClient
from ipyleaflet import Map
from ipywidgets import Layout
from ipywidgets import Layout, HBox
#A function to convert linux paths to windows
def convert_path(path):
    if os.name == "nt":
        return path.replace("/", "\\")
    else:
        return path

def get_clipped_chip(file_path,polygon):
      
    """
        Clips a raster image based on the provided polygon shape.

        Args:
            file_path (str): The path to the raster image file.
            polygon (shapely.geometry.Polygon): The polygon shape to clip the raster.

        Returns:
            numpy.ndarray: The clipped raster image as a NumPy array.

    """
    with rasterio.open(file_path) as src:
        out_image, out_transform = rasterio.mask.mask(src,polygon, crop=True)
        out_meta = src.meta

    out_meta.update({"driver": "GTiff",
                    "height": out_image.shape[1],
                    "width": out_image.shape[2],
                    "count": out_image.shape[0],
                    "transform": out_transform})   

    clipped_raster=array_to_raster(out_image,out_meta)

    return clipped_raster

def array_to_raster(array,meta):
    """
    Converts a NumPy array to a rasterio object.
    
    Parameters:
        array (numpy.ndarray): The NumPy array to convert to a rasterio object.
        crs (rasterio.crs.CRS): The CRS of the raster.
        transform (affine.Affine): The geotransform of the raster.
        
    Returns:
        A rasterio DatasetReader object.
    """
    count, height, width = array.shape
    
    # Create a rasterio MemoryFile
    memfile = rasterio.MemoryFile()
    
    # Write the NumPy array to the MemoryFile
    with memfile.open(**meta) as dst:
      for i in range(count):
          dst.write(array[i,:,:], i+1)
        
    # Return a rasterio DatasetReader object
    return memfile.open()

def get_tile_transform(parent_transform, pixel_x:int,pixel_y:int):
    '''
    creating tile transform matrix from parent tif image
    '''
    crs_x = parent_transform.c + pixel_x * parent_transform.a
    crs_y = parent_transform.f + pixel_y * parent_transform.e
    tile_transform = rasterio.Affine(parent_transform.a, parent_transform.b, crs_x,
                                     parent_transform.d, parent_transform.e, crs_y)
    return tile_transform
    
def get_tile_profile(parent_tif:rasterio.io.DatasetReader, pixel_x:int, pixel_y:int):
    '''
    preparing tile profile
    '''
    tile_crs = parent_tif.crs
    tile_nodata = parent_tif.nodata if parent_tif.nodata is not None else 0
    tile_transform = get_tile_transform(parent_tif.transform, pixel_x, pixel_y)
    profile = dict(
                driver="GTiff",
                crs=tile_crs,
                nodata=tile_nodata,
                transform=tile_transform
            )
    return profile

def validate_array(img_array):
    """
    Validates an image array by calculating the percentage of zero values in the first channel.

    Args:
        img_array (numpy.ndarray): The image array to validate.

    Returns:
        float: The percentage of zero values in the first channel of the image array.

    """
    percentage=np.where(img_array[0,:,:].flatten()==0)[0].shape[0]/(img_array.shape[1]*img_array.shape[2])
    return percentage

def generate_tile(tif,coordinates,size,valid_threshold=0.1):

    """
    Generates a tile from a TIFF image based on the given coordinates and size.

    Args:
    
        tif (rasterio.DatasetReader): The TIFF image to generate the tile from.
        coordinates (tuple): The (x, y) coordinates of the tile.
        size (int): The size of the tile (width and height).
        filter_percentage (float, optional): The maximum percentage of anomaly values allowed in the tile.
                                             Defaults to 0.1.
        valid_threshold :Percentage value between 0 to 1 to create valid tiles having no data values less than / equal to 
        the valid_threshold

    Returns:
        rasterio.DatasetReader or None: The generated tile as a rasterio DatasetReader object if it passes
                                        the anomaly filter, or None if it exceeds the filter threshold.

    """
    x,y=coordinates
    # creating the tile specific profile
    profile = get_tile_profile(tif, x, y)
    # extracting the pixel data (couldnt understand as i dont think thats the correct way to pass the argument)
    tile_data = tif.read(window=((y, y + size), (x, x + size)),
                            boundless=True, fill_value=profile['nodata'])

    anomaly_percentage=validate_array(tile_data)
    if anomaly_percentage<=valid_threshold:
        c, h, w = tile_data.shape
        profile.update(
            height=h,
            width=w,
            count=c,
            dtype=tile_data.dtype,
        )

        memfile = rasterio.MemoryFile()
    
        # Write the NumPy array to the MemoryFile
        with memfile.open(**profile) as dst:
            for i in range(c):
                dst.write(tile_data[i,:,:], i+1)
        # Return a rasterio DatasetReader object
        return memfile.open()
    else:
       return None

def open_shp(shp_file,crs="epsg:32644"):

    """
        Opens a shapefile (SHP) using geopandas library.

        Args:
            shp_file (str): The file path to the shapefile.

        Returns:
            geopandas.geodataframe.GeoDataFrame: The opened shapefile as a GeoDataFrame.

    """
    gdf=gpd.read_file(shp_file)
    gdf=gdf.to_crs(crs)
    return gdf

def open_tiff(path): 

    """
        Opens a TIFF file using rasterio library.

        Args:
            path (str): The file path to the TIFF image.

        Returns:
            rasterio.io.DatasetReader: The opened TIFF image.
    """

    img = rasterio.open(path)
    return img 

def extract_tiles(image_file, output_folder,modality,region, date, tile_code,chip_size=512):
    tile_folder_path = os.path.join(output_folder,modality,region, "tiles")
    
    if not os.path.exists(tile_folder_path):
        os.makedirs(tile_folder_path)

    with rasterio.open(image_file) as src:
        width = src.width
        height = src.height

        # Calculate the number of tiles
        num_tiles_x = width // chip_size
        num_tiles_y = height // chip_size

        # Calculate the total number of tiles
        total_tiles = num_tiles_x * num_tiles_y

        # Check if the image size is larger than 256x256
        if num_tiles_x > 0 and num_tiles_y > 0:
            # Calculate the actual tile size considering any remaining pixels
            tile_size_x = width // num_tiles_x
            tile_size_y = height // num_tiles_y

            # Extract and save the tiles
            for i in range(num_tiles_y):
                for j in range(num_tiles_x):
                    left = j * tile_size_x
                    top = i * tile_size_y
                    right = left + tile_size_x
                    bottom = top + tile_size_y

                    chip_number = i * num_tiles_x + j + 1

                    # Generate the tile filename
                    tile_filename = f"tile_{chip_number}_{tile_code}_{date}.tif"
                    tile_path = os.path.join(tile_folder_path, tile_filename)

                    # Generate the tile from the image
                    tile = generate_tile(src, (left, top), tile_size_x)

                    if tile is not None:
                        # Save the tile to a file
                        with rasterio.open(tile_path, 'w', **tile.profile) as dst:
                            dst.write(tile.read())

        else:
            print(f"The image {image_file} is smaller than the tile size.")
        

def parse_satellite_image(filename,modality):
    if modality=='sentinel_data':
        # Extract date, resolution, and tile number from the filename
        parts = filename.split("_")
        date = parts[1][0:8]  # Assuming date is in YYYYMMDD format
        resolution = parts[3].split(".")[0]
        tile_number = parts[0][1:]
    else:
        parts=filename.split("_")
        date=parts[0]
        resolution='3m'
        tile_number='planet'
    return date, resolution

"""
def convert_to_tif(jp2_file):
    # Get the output TIF file path
    tif_file = os.path.splitext(jp2_file)[0] + ".tif"
    jp2_dataset = gdal.Open(jp2_file)
    gdal.Translate(tif_file, jp2_dataset, format='GTiff')
    os.remove(jp2_file)
    tif_file=tif_file.split("/")[-1]
    return tif_file
"""    

def visualize_raster(image_paths):
    # Create a list to hold the tile layers for each image
    tile_layers = []

    # Create tile servers and tile layers for each image
    for image_path in image_paths:
        client = TileClient(image_path)
        tile_layer = get_leaflet_tile_layer(client)
        tile_layers.append(tile_layer)

    # Create maps for each image
    maps = []
    for i in range(len(image_paths)):
        # Get the bounding box of the tile layer
        bounds = tile_layers[i].bounds

        # Calculate the center from the bounding box
        center = [
            (bounds[0][0] + bounds[1][0]) / 2,
            (bounds[0][1] + bounds[1][1]) / 2
        ]

        # Create the map with the calculated center
        map = Map(center=center, zoom=13, basemap={}, layout=Layout(width='50%', height='600px'))
        map.add_layer(tile_layers[i])
        maps.append(map)

    # Display maps side by side
    maps_layout = HBox(maps)
    return maps_layout
    

def create_csv(folder_path,csv_folder,chip_size):
    # List all files in the folder
    modalities = os.listdir(folder_path)
    region_dict={}

    with open(os.path.join(csv_folder,"region.csv"), 'w', newline='') as csvfile_region:
            writer_region = csv.writer(csvfile_region)
            # Write the header row
            writer_region.writerow(['Region_Id',f'Data_Path', 'Timestamp', 'Resolution', 'Tile Code','Modality','Region'])

            for modality in modalities:
                regions = os.listdir(os.path.join(folder_path,modality))


                for i,region in enumerate(regions):
                    if region not in region_dict:
                        region_dict[region]=i+1

                # Create the CSV file
                for i,region in enumerate(regions):

                    files=os.listdir(os.path.join(folder_path,modality,region,"images"))

                    # Iterate over the files
                    for file in files:
                        if file.endswith('.jp2'):
                            # Convert JP2 to TIF
                            file = convert_to_tif(os.path.join(folder_path,modality,region,"images",file))
                            
                        file_path=os.path.join("/".join(folder_path.split("/")[-4:]),modality,region,"images",file)
                        # Parse the TIF image
                        date, resolution, tile_code = parse_satellite_image(file,modality)
                        # Write the information to the CSV file
                        writer_region.writerow([f"{region_dict[region]}_{tile_code}",file_path, date, resolution, tile_code,modality,region])

                        image_file = os.path.join(folder_path,modality,region, "images", file)
                        #extract_tiles(image_file,folder_path,modality,region,date,tile_code,chip_size)

    # Create the tile.csv file
    tile_csv = os.path.join(csv_folder, 'tile.csv')
    with open(tile_csv, 'w', newline='') as csvfile:
        writer_tile = csv.writer(csvfile)
        # Write the header row
        writer_tile.writerow(['Region_Id', f'Data_path', 'Tile_id','Timestamp','Satellite_tile_code','Modality','Region'])            

        for modality in modalities:
            # Iterate over the regions
            regions = os.listdir(os.path.join(folder_path,modality))
            for i, region in enumerate(regions):
                tiles_folder = os.path.join("/".join(folder_path.split("/")[-4:]),modality,region, "tiles")
                tiles = os.listdir(tiles_folder)

                # Iterate over the tiles
                for tile_filename in tiles:
                    # Write the information to the tile.csv file
                    tile_name_array=tile_filename.split("_")
                    satellite_tile_code=tile_name_array[2]
                    tile_id=f"{tile_name_array[1]}_{satellite_tile_code}"
                    date=tile_name_array[3].split(".")[0]

                    region_id=f"{i+1}_{satellite_tile_code}"

                    tile_path_name=os.path.join(tiles_folder,tile_filename)
                    writer_tile.writerow([region_id, tile_path_name, tile_id,date,satellite_tile_code,modality,region])
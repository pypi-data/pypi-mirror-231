from typing import Any
from PIL import Image
import numpy as np
import glob
import geopandas as gpd
import sys
import os 
import csv
from descartes import PolygonPatch
import copy
import matplotlib as mpl

from .utils import *
  
class FarmData():

  """
    A utility class that provides access to farm data and related functionalities.

    Attributes:
        farm_csv_path (str): The file path to the CSV file containing farm data.
        block_csv_path (str): The file path to the CSV file containing block data.
        crs (str): The Coordinate Reference System (CRS) for the geospatial data.

  """

  def __init__(self,farm_csv_path,block_csv_path):  
    """
      Initializes a FarmData instance.

      Args:
          farm_csv_path (str): The file path to the CSV file containing farm data.
          block_csv_path (str): The file path to the CSV file containing block data.
          crs (str, optional): The Coordinate Reference System (CRS) for the geospatial data.
              Defaults to "epsg:32644".

    """ 

    self.farm_csv_path=farm_csv_path
    self.block_csv_path=block_csv_path

    self.farm_df=pd.read_csv(self.farm_csv_path)
    self.block_df=pd.read_csv(self.block_csv_path)

    self.farms_info=self.__get_farm_info__(self.farm_csv_path)
    self.blocks_info=self.__get_blocks_info__(self.block_csv_path)

    self.blocks=self.__get_block_objects__()
    self.farms=self.__get_farm_objects__()


  def __get_farm_objects__(self):
     
    all_farms={}
    for farm_id,farm_properties in self.farms_info.items():
      all_blocks={}
      for block_id,block_properties in self.blocks_info.items():
         if block_properties['farm_id']==farm_id:
            all_blocks[block_id]=self.blocks[block_id]
      all_farms[farm_id]=Farm(farm_properties,all_blocks)
    return all_farms 
  
  def get_farm_by_name(self,farm_name):
     
     for farm_key,farm_obj in self.farms.items():
        
        if farm_obj.info['owner']==farm_name:
           return farm_obj      
        
  def get_block_by_name(self,block_name):
    
    for block_key,block_obj in self.blocks.items():
      
      if block_obj.info['block_name']==block_name:
          return block_obj 
        
  def __get_block_objects__(self):

    all_blocks={}
    for block_id,properties in self.blocks_info.items():
      farm_id=properties['farm_id']
      all_blocks[block_id]=Block(properties,self.farms_info[farm_id])
    return all_blocks        
  
  def __get_farm_info__(self,farm_csv_path):
      # Initialize empty dictionary to store information
      all_info = {}
      with open(farm_csv_path, 'r') as f:
          reader = csv.DictReader(f)
          # Populate owner and area fields

          # Iterate through rows and populate modalities and data fields
          for row in reader:
              info = {'owner': None, 'area': None,'data_path': {}}
              info['owner'] = row['farm_name']
              info['farm_id'] =row['farm_id']
              info['area'] = None
              info['shp'] =row['shp']
              timestamp=row['time']
              
              info['data_path'][timestamp]={}
              for column in row:
                  # Check if the column name contains 'drone_' and get the resolution from the column name
                  if 'drone_' in column:
                      modality = column
                      if modality not in info['data_path'][timestamp]:
                          info['data_path'][timestamp][modality] = row[modality]
                  # Check if the column name contains 'sat_' and add the timestamp and image_path to satellite data
                  elif 'sat_' in column:
                      if row[column]:
                          image_path = row[column]
                          image_path = convert_path(image_path)
                          if column not in info['data_path'][timestamp]:
                              info['data_path'][timestamp][column]=image_path

              if info['farm_id'] in all_info:      
                all_info[info['farm_id']]['data_path'][timestamp]=info['data_path'][timestamp]
                all_info[info['farm_id']]['shp']=row['shp']
              else:
                all_info[info['farm_id']]=info

      return all_info
  
  def __get_blocks_info__(self,block_csv_path):
        # Open CSV file
        with open(block_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Group data by block_id
            output_dict = {}
            for row in reader:
                block_id = row['block_id']
                farm_id = row['farm_id']
                block_name = row['block_name']
                vegetation_type = row['vegetation_type']
                crop_name = row['crop_name']
                yield_val = row['yield']
                shp_val = row['shp']
                time=row['timestamp']

                # Extract drone image paths or shp files
                data_path = {}
                data_path[time]={}
                for column in row:
                    # Check if the column name contains 'drone_' and get the resolution from the column name
                    if 'drone_' in column:
                        modality = column
                        if modality not in data_path[time]:
                            data_path[time][modality] = row[modality]
                    # Check if the column name contains 'sat_' and add the timestamp and image_path to satellite data
                    elif 'sat_' in column:
                        if row[column]:
                            image_path = row[column]
                            image_path = convert_path(image_path)
                            if column not in data_path[time]:
                                data_path[time][column]=image_path    

                # Create output dictionary for block
                block_dict = {
                    'block_id':block_id,
                    'farm_id' : farm_id,
                    'block_name': block_name,
                    'vegetation_type': vegetation_type,
                    'crop_name': crop_name,
                    'yield': yield_val,
                    'shp': shp_val,
                    'data_path': data_path, # Use dynamically generated drone data dictionary
                    'timestamps':[]
                }
                if block_id in output_dict:
                   timestamp_list=output_dict[block_id]['timestamps']
                   timestamp_list.append(time)
                   timestamp_list=list(set(timestamp_list))
                   output_dict[block_id]['timestamps']=timestamp_list
                   output_dict[block_id]['data_path'][time]=block_dict['data_path'][time]
                else:
                   output_dict[block_id] = block_dict   
                   output_dict[block_id]['timestamps'].append(time)
                
            # Return output dictionary 
        return output_dict

      
class Farm():

  """
    A subclass of FarmData that represents farm-specific data.

    Attributes:
        farm_csv_path (str): The file path to the CSV file containing farm data.
        block_csv_path (str): The file path to the CSV file containing block data.
        crs (str): The Coordinate Reference System (CRS) for the geospatial data.

  """

  def __init__(self,farm_info,blocks):

    """
      Initializes a farmdata instance.

      Args:
          farm_csv_path (str): The file path to the CSV file containing farm data.
          block_csv_path (str): The file path to the CSV file containing block data.
          crs (str): The Coordinate Reference System (CRS) for the geospatial data.
    """  

    self.info=farm_info
    self.farm_id=self.info['farm_id']
    self.blocks=blocks          

  def get_modality(self,modality_type="drone_75",timestamp=None,shp_clip=False,only_rgb=False):

    """
      Retrieves a specific modality (e.g., drone or satellite) for the farm.

      Args:
          modality_type (str, optional): The type of modality (e.g., "drone" or "satellite"). Defaults to "drone".
          resolution (int, optional): The resolution of the modality. Defaults to 75.
          timestamp (str, optional): The timestamp of the modality image. Defaults to None.
          shp_clip (bool, optional): Whether to clip the farm shapefile. Defaults to False.

      Returns:
          farmdata: The farmdata object with the requested modality information.

     """

    if not shp_clip:

      farm_image_path=self.info['data_path'][timestamp][modality_type]
      farm_image_path=convert_path(farm_image_path)
      raster=open_tiff(farm_image_path)
      if only_rgb:
        return raster.read([1,2,3])
      else:
         return raster
    else: #to be implemented when accessing satellite images not in use right now.
      farm_image_path=self.info['data_path'][timestamp][modality_type]
      farm_image_path=convert_path(farm_image_path)
      shp_file=self.info["shp"]
      polygon=open_shp(shp_file,"epsg:3857")['geometry'].values[0]
      clipped_chip=get_clipped_chip(farm_image_path,[polygon])
      return clipped_chip
    
  def visualize_blocks(self,modality_type="drone",resolution=75,timestamp=None):

    """
  Displays the farm image with the block polygons overlaid.

  Args:
      clip (bool, optional): Whether to clip the farm image to the extent of the block polygons. Defaults to True.

  Returns:
      numpy.ndarray or None: If `clip` is True, returns the clipped farm image with the block polygons. Otherwise, returns None.
    """
    df_list=[]
    for block_id,block in self.blocks.items():
        shp_file=block.info['shp']
        block_polygon_df=open_shp(shp_file)
        df_list.append(block_polygon_df)
        all_polygon_df=pd.concat(df_list)
        all_polygons=all_polygon_df['geometry'].values
  
    fig, ax = plt.subplots(figsize=(20,20))

    farm_image_path=self.info['data_path'][timestamp][modality_type]
    src=rasterio.open(farm_image_path)
    ax = rasterio.plot.show(src,ax=ax, cmap="pink")
    all_polygon_df.plot(ax=ax)
    patches = [PolygonPatch(feature) for feature in all_polygons]
    ax.add_collection(mpl.collections.PatchCollection(patches))  

  def get_times(self):
     times = self.info['data_path'].keys()
     return list(times)

  def get_times_for_modality(self,modality):
    all_timestamps=self.get_times()
    fetch_timestamps=[]
    for timestamp in all_timestamps:
      if modality in self.info['data_path'][timestamp]:
          fetch_timestamps.append(timestamp)

    return fetch_timestamps 
  
  def get_modalities_for_times(self,time):
      
      valid_mods=[]
      modalities=list(self.info['data_path'][time].keys())
      for mods in modalities:
         if self.info['data_path'][time][mods]!="":
            valid_mods.append(mods)

      return valid_mods

  def get_block_by_name(self,block_name):
  
    for block_key,block_obj in self.blocks.items():
      if block_obj.info['block_name']==block_name:
          return block_obj      
            
class Block():

  def __init__(self,block_info,farm_info):
      
      """
        A subclass of FarmData that represents a block and provides methods to access and manipulate block information.

        Attributes:
            block_csv_path (str): The file path to the CSV file containing block data.
            farm_image_path (str): The file path to the farm image.
            farm_id (int): The ID of the farm.
            crs (str): The Coordinate Reference System (CRS) for the geospatial data.

      """

      self.info=block_info
      self.block_id=self.info['block_id']
      self.farm_info=farm_info
        
  def get_modality(self,modality_type="drone_75",timestamp=None,shp_clip=True):
      
      """
      Retrieves the block geometry from the shapefile and clips it from the farm image.

      Args:
          shp_file (str): The file path to the shapefile.
          farm_image_path (str): The file path to the farm image.

      Returns:
          numpy.ndarray: The clipped block chip.

      """
      
      if self.info['data_path'][timestamp][modality_type]!="":
         if shp_clip:            
            shp_file=self.info['shp']
            block_image_path=self.info['data_path'][timestamp][modality_type]
            if modality_type.startswith("drone_"):
              crs="epsg:32644"
            else:
              crs_x=str(open_tiff(block_image_path).profile['crs']).lower()
              crs=crs_x.split("epsg:")[1].lstrip("(").rstrip(")")
              crs=f"epsg:{crs}"
              print(crs)
            block_polygon=open_shp(shp_file,crs)['geometry'].values[0]
            clipped_chip=get_clipped_chip(block_image_path,[block_polygon])
            return clipped_chip
         else:
            image_path=self.info['data_path'][timestamp][modality_type]
            return open_tiff(image_path)        
      else:
        shp_file=self.info['shp']
        farm_image_path=self.farm_info['data_path'][timestamp][modality_type]
        if modality_type.startswith("drone_"):
           crs="epsg:32644"
        else:
           crs="epsg:3857"
        block_polygon=open_shp(shp_file,crs)['geometry'].values[0]
        clipped_chip=get_clipped_chip(farm_image_path,[block_polygon])
        return clipped_chip
  
  def get_chips(self,chip_size=200,valid_threshold=0.1,modality_type="drone",resolution=75,timestamp=None):
     
      block_image=self.get_modality(modality_type=modality_type,timestamp=timestamp)
      return Chip(block_image,chip_size,valid_threshold)
  
  def get_times(self):
     
     times = self.info['data_path'].keys()
     return list(times)
  
  def get_modality_list(self):
     
     timestamps=self.get_times()
     modality=[]

     for timestamp in timestamps:
        for mod in self.get_modalities_for_times(timestamp):
            modality.append(mod)

     modality=list(set(modality))
     return modality

  
  def get_times_for_modality(self,modality):
     
     all_timestamps=self.get_times()
     fetch_timestamps=[]
     for timestamp in all_timestamps:
        if modality in self.info['data_path'][timestamp]:
           fetch_timestamps.append(timestamp)

     return fetch_timestamps      
             
  def get_modalities_for_times(self,time):
    
    valid_mods=[]
    modalities=list(self.info['data_path'][time].keys())
    for mods in modalities:
        if self.info['data_path'][time][mods]!="":
          valid_mods.append(mods)

    return valid_mods
  
  
class Chip(FarmData):
  def __init__(self,block_chip,size=200,valid_threshold=0.1):

    """
        Represents a chip or tile extracted from a block.

        Args:
            block_chip (numpy.ndarray): The image chip of the block.
            size (int, optional): The size of the chip. Defaults to 200.

        Attributes:
            size (int): The size of the chip.
            block_chip (numpy.ndarray): The image chip of the block.
            all_tile_coords (list): A list of coordinates representing all the possible tile positions within the block chip.
            valid_tiles (int): The number of valid tiles generated.
            total_tiles (int): The total number of tiles generated.
            invalid_tiles (int): The number of invalid tiles generated.

    """
      
    self.size=size
    self.block_chip=block_chip
    self.all_tile_coords = self.__get_coordinates__()
    self.valid_tiles=0
    self.total_tiles=0
    self.invalid_tiles=0
    self.valid_threshold=valid_threshold

  def __get_coordinates__(self,):

    """
        Generates a list of coordinates representing all the possible tile positions within the block chip.

        Returns:
            list: A list of coordinates.

    """
     
    coordinates=[]
    for x in (0, self.block_chip.width, self.size):
      for y in range(0, self.block_chip.height, self.size):
          coordinates.append((x,y))

    return coordinates      
  def __next__(self):

    """
        Generates the next tile from the block chip.

        Returns:
            numpy.ndarray or None: The generated tile or None if there are no more tiles.

        Raises:
            StopIteration: If there are no more tiles to generate.

    """
    while self.index < len(self.all_tile_coords):   
      coordinates=self.all_tile_coords[self.index]
      output = generate_tile(self.block_chip,coordinates,self.size,self.valid_threshold)
      if output!=None:
        self.index+=1
        self.valid_tiles+=1
        self.total_tiles+=1
        return output
      else:
        self.index+=1
        self.invalid_tiles+=1
        self.total_tiles+=1

    raise StopIteration    
      
  def __iter__(self):
    self.index = 0
    
    return self    






      


      
   


          
  

     
  

    

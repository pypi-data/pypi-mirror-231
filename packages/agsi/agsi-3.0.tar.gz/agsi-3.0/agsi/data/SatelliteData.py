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
from .band_info import *
from .utils import *
  
class SatelliteData():


  def __init__(self,region_csv_path,tile_csv_path):  

    self.region_csv_path=region_csv_path
    self.tile_csv_path=tile_csv_path

    self.region_df=pd.read_csv(self.region_csv_path)
    self.tile_df=pd.read_csv(self.tile_csv_path)

    self.region_info=self.__get_region_info__()
    self.tile_info=self.__get_tile_info__()

    self.tiles=self.__get_tile_objects__()
    self.regions=self.__get_region_objects__()


  def __get_region_objects__(self):
     
    all_regions={}
    for region_id,region_properties in self.region_info.items():
      all_tiles={}
      for tile_id,tile_properties in self.tile_info.items():
         if tile_properties['region_id']==region_id:
            all_tiles[tile_id]=self.tiles[tile_id]
      all_regions[region_id]=Region(region_properties,all_tiles)
    return all_regions
  
  def get_region(self,region):
     
     region_objs=[]       
     for region_id,region_obj in self.regions.items():
      if region_obj.info['region']==region:
        region_objs.append(region_obj)
     return region_objs


  def get_tiles_by_region(self,region):
     region_objs=[]       
     for tile_id,tile_obj in self.tiles.items():
      if tile_obj.info['region']==region:
        region_objs.append(tile_obj)
     return region_objs
      
  def get_region_names(self): 
     
     regions=[]       
     for region_id,region_obj in self.regions.items():
      regions.append(region_obj.info['region'])
     regions=list(set(regions)) 
     return regions
  
  def get_region_by_modality(self,modality):
     region_objs=[]       
     for region_id,region_obj in self.regions.items():
      if region_obj.info['modality']==modality:
        region_objs.append(region_obj)
     return region_objs
  
  def get_tiles_by_modality(self,modality):
     region_objs=[]       
     for tile_id,tile_obj in self.tiles.items():
      if tile_obj.info['modality']==modality:
        region_objs.append(tile_obj)
     return region_objs
  
  def get_region_by_time(self,timestamp):
     region_objs=[]       
     for region_id,region_obj in self.regions.items():
      if timestamp in region_obj.info['data_path']:
        region_objs.append(region_obj)
     return region_objs
  
  def get_tiles_by_time(self,timestamp):
     tile_objs=[]       
     for tile_id,tile_obj in self.regions.items():
      if timestamp in tile_obj.info['data_path']:
        tile_objs.append(tile_obj)
     return tile_objs
  
  def get_times(self):
     timestamps=[]       
     for tile_id,tile_obj in self.regions.items():
        timestamps.extend(tile_obj.get_times())
     timestamps=list(set(timestamps))   
     return timestamps
        
  def __get_tile_objects__(self):

    all_tiles={}
    for tile_id,properties in self.tile_info.items():
      region_id=properties['region_id']
      all_tiles[tile_id]=Tile(properties,self.region_info[region_id])
    return all_tiles        
  
  def __get_region_info__(self):
    # Initialize empty dictionary to store information
    all_info = {}
    with open(self.region_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        # Populate owner and area fields

        # Iterate through rows and populate modalities and data fields
        for row in reader:
            info = {'region': None,'data_path': {}}
            info['region'] = row['Region']
            info['region_id'] =row['Region_Id']
            info['modality'] = row['Modality']
            info['resolution'] = row['Resolution']
            
            timestamp=row['Timestamp']
            
            info['data_path'][timestamp]={}

            info['data_path'][timestamp]= row['Data_Path']

            if info['region_id'] in all_info:      
                all_info[info['region_id']]['data_path'][timestamp]=info['data_path'][timestamp]
            else:
                all_info[info['region_id']]=info
                
    return all_info

  def __get_tile_info__(self):
    # Initialize empty dictionary to store information
    all_info = {}
    with open(self.tile_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        # Populate owner and area fields

        # Iterate through rows and populate modalities and data fields
        for row in reader:
            info = {'region_id': None,'data_path': {}}
            info['region_id'] = row['Region_Id']
            info['tile_id'] =row['Tile_id']
            info['satellite_tile_code'] = row['Satellite_tile_code']
            info['modality'] = row['Modality']
            info['region']=row['Region']
            
            timestamp=row['Timestamp']
            
            info['data_path'][timestamp]={}

            info['data_path'][timestamp]= row['Data_path']

            if info['tile_id'] in all_info:      
                all_info[info['tile_id']]['data_path'][timestamp]=info['data_path'][timestamp]
            else:
                all_info[info['tile_id']]=info
    return all_info
  

class Region():


  def __init__(self,region_info,tiles):

    self.info=region_info
    self.region_id=self.info['region_id']
    self.tiles=tiles     

  def get_modality(self,timestamp,bands=None):
      
      region_image_path=self.info['data_path'][timestamp]
      if bands!=None:
         with rasterio.open(region_image_path) as dataset:
          band_data = dataset.read(bands)
          return band_data
      else:   
        raster=open_tiff(region_image_path)
        return raster
     
  def get_times(self):
     times = self.info['data_path'].keys()
     return list(times) 
        
class Tile():

  def __init__(self,tile_info,region_info):
      

      self.info=tile_info
      self.block_id=self.info['tile_id']
      self.region_info=region_info
      self.planet_band_info={
         
      }

  def get_modality(self,timestamp,bands=None):
      
      tile_image_path=self.info['data_path'][timestamp]
      if bands!=None:
         with rasterio.open(tile_image_path) as dataset:
          band_data = dataset.read(bands)
          return band_data
      else:   
        raster=open_tiff(tile_image_path)
        return raster
        
  def get_times(self):
     
     times = self.info['data_path'].keys()
     return list(times)
  







      


      
   


          
  

     
  

    

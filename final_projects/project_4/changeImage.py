#!/usr/bin/env python3

from PIL import Image
import os

def changeImage(dir_path, file_list):
  for filename in file_list:
    with Image.open(dir_path+filename) as img:
     # img = Image.open(file)
      out = img.convert('RGB')
      new_filename = os.path.splitext(filename)
      out.resize((600,400)).save(dir_path+new_filename[0]+'.jpeg', 'JPEG')

def main():
  dir_path = './supplier-data/images/'
  file_list = []
  for file in os.listdir(dir_path):
    if '.tiff' in file:
      file_list.append(file)
  print(file_list)
  changeImage(dir_path, file_list)

if __name__ == "__main__":
  main()



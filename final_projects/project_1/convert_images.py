#!/usr/bin/env python3

'''This program takes an image that in TIFF format, which is rotated counter-clockwise with a size of 192 * 192
and chaning it to .jpeg file type, correcting the rotation, resizing it to 128 * 128 and saving the resultant 
image in new folder /opt/icons/''' 

import os
from PIL import Image

directory = './images/'
new_path = './opt/icons/'

#iterate over each image and modify and save as needed. 
for filename in os.listdir(directory):
  im = Image.open('./images/'+filename)
  if im.mode != 'RGB':
    im = im.convert('RGB')
  im.rotate(90).resize((128, 128)).save(new_path + filename + '.jpeg')
  im.close()


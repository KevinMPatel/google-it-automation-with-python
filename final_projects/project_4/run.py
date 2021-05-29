#!/usr/bin/env python3

import requests
import os

def extract_data(path):
  #get a list of all files in the directory
  list = os.listdir(path)
  file_list=[]
  #pick out the files that has .txt extension.
  for f in list:
    if '.txt' in f:
      file_list.append(f)
  #data will be a list containing each dictionary
  #we generate from each text file.
  data = []
  dict = {}
  print(file_list)
  for filename in file_list:
    with open(path+filename) as file:
      dict['name'] = file.readline().strip('\n')
      dict['weight'] = int(file.readline().strip('lbs\n'))
      dict['description'] = file.readline().strip('\n')
      filename_text = os.path.splitext(filename)
      dict['image_name'] = str(filename_text[0])+'.jpeg'
      dict_copy = dict.copy()
      data.append(dict_copy)
  return data

def post_on_web(url, data):
  for fruit in data:
    r = requests.post(url, json=fruit)
  if r.status_code != 201:
    raise Exception('POST error status={}'.format(r.status_code))
    print('Created feedback ID: {}'.format(r.json()["id"]))

def main():
  url = 'http://35.223.168.222/fruits/'
  path = './supplier-data/descriptions/'
  # extract the data from txt files and store it as dict,
  # and make a list of all the dict collected from the text files.
  data = extract_data(path)
  #post the fruit online
  post_on_web(url, data)

if __name__ == "__main__":
  main()



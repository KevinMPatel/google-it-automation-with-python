#!/usr/bin/env python3

import requests
import os

def upload_images(url, path, file_list):
  for file_name in file_list:
    with open(path+filename, 'rb') as opened:
      r = requests.post(url, files={'file': opened})


def main():
  url = "http://localhost/upload/"
  path = './supplier-data/images/'
  file_list = []
  for filename in os.listdir(path):
    if '.jpeg' in filename:
      file_list.append(filename)
  upload_images(url, path, file_list)

if __name__ == "__main__":
  main()

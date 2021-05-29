#!/usr/bin/env python3

import os
import requests

text_file_path = '/data/feedback/'
files_list = os.listdir(text_file_path)

print('****************************************************************')

d = {}
list = []

for file in files_list:
  with open(text_file_path+file) as f:
    d['title'] = f.readline().strip()
    d['name'] = f.readline().strip()
    d['date'] = f.readline().strip()
    d['feedback'] = f.readline().strip()
    d_copy = d.copy()
  list.append(d_copy)
  f.close()

print(list)

for each_feedback in list:
  response = requests.post('http://34.67.231.64/feedback/', data=each_feedback)
  response.request.body


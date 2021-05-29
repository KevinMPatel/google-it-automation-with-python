#!/usr/bin/env python3

import psutil 
import shutil
import socket
import os
from emails import generate_error_report, send_email


def check_disk(disk):
  du = shutil.disk_usage(disk)
  free = du.free/du.total * 100
  return free > 20

def check_cpu():
  usage = psutil.cpu_percent(1)
  return usage < 80

def check_memory():
  available = (psutil.virtual_memory()[4])/(1024*1024)
  return available > 500 

def check_localhost():
  local_ip = socket.gethostbyname('localhost')
  return local_ip == '127.0.0.1'
    

to_be_checked = {
  check_cpu(): 'CPU usage is over 80%',
  check_disk("/"): 'Available disk space is less than 20%',
  check_memory(): 'Available memory is less than 500MB',
  check_localhost(): 'localhost cannot be resolved to 127.0.0.1'
}

error = False
for action, message in to_be_checked.items():
  if not action:
    error_message = message
    error = True

# send email
if error:
  try:
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    subject = 'Error - {}'.format(error_message)
    body = 'Please check your system and resolve the issue as soon as possible.'
    message = generate_error_report(sender, receiver, subject, body)
    send_email(message)
    print('You may test')
  except NameError:
    pass 

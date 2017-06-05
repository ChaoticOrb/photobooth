#!/usr/bin/env python

import socket

test_server = 'www.google.com' # server location to check for network

def network_connected():
  try:
    host = socket.gethostbyname(test_server)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

connected = network_connected() #check to see if you have an internet connection

if(connected == False):
    print('No internet connection')
else:

    # try using subprocess.call to run the .sh file...
     ./dropbox_uploader.sh -s upload /home/pi/captures/ /photos/

# compare files in dropbox and upload any new files

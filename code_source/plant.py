
# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# 
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/x232.html
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/c212.html

import numpy as np
import pickle
import bluetooth
import time
from func_timeout import func_timeout, FunctionTimedOut

with open ("plantArgs.txt", "r") as plantArgs:
    plantArgs=plantArgs.readlines()

def receiveMessages():
  data = sock.recv(1024)
  print ("received %s" % data)
  return data

def sendMessageTo(message):
  sock.send(message)
  print("message SENT!!")

def sendConnection(targetAddress,port):
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetAddress, port))
  return sock

value = plantArgs[1][:-1]
sock = sendConnection(plantArgs[0][:-1],1)
print("bluetooth CONNECTED!!!")
i = 0
previous = value
while i < 10:
  sendMessageTo(value)
  previous = value
  value = receiveMessages()
  if value == previous:
    i -=1
  print(value)
  i+=1

sock.close()

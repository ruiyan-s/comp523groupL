# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# 
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/x232.html
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/c212.html

import pickle
import bluetooth

def receiveMessages(sock):
  data = sock.recv(1024)
  print ("received %s" % data)
  return data
  
def sendMessageTo(sock,message):
  sock.send(message)
  print("Message sent!!")
  
def lookUpNearbyBluetoothDevices():
  nearby_devices = bluetooth.discover_devices()
  #for bdaddr in nearby_devices:
   # print str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]"
  receiveMessages()
#  sendMessageTo("DC:A6:32:5F:DF:36")
  
    
#lookUpNearbyBluetoothDevices()

def acceptConnection(port):
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  server_sock.bind(("",port))
  server_sock.listen(2)
  print("ready to accept connection")
  client_sock,address = server_sock.accept()
  print ("Accepted connection from " + str(address))
  return client_sock

plant_sock = acceptConnection(1)
controller_sock = acceptConnection(2)
i = 0
bound = 10
while i < bound:
  print(i)
  plantData = receiveMessages(plant_sock)
  if i != 5:
    sendMessageTo(controller_sock, plantData)
    print("sent to controller?")
  else:
    bound +=1
  controllerData = receiveMessages(controller_sock)
  if i != 8:
    sendMessageTo(plant_sock, controllerData)
  else:
    controllerData = receiveMessages(controller_sock)
    sendMessageTo(plant_sock, controllerData)
  i+=1
plant_sock.close()
controller_sock.close()

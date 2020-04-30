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
# from func_timeout import func_timeout, FunctionTimedOut
import signal
from contextlib import contextmanager


@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)

    try:
        yield
    except TimeoutError:
        pass
    finally:
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
def raise_timeout(signum, frame):
    raise TimeoutError

with open ("controllerArgs.txt", "r") as controllerArgs:
    controllerArgs=controllerArgs.readlines()

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

def formula():
  f = controllerArgs[1][:-1].split("=")[1]
  f = f.replace("^", "**")
  f = f.replace("x", "value")
  return f

sock = sendConnection(controllerArgs[0][:-1],2)

print("bluetooth CONNECTED!!!")
i = 0
value = 0
while i < 10:
  # value = receiveMessages()
  # value = int(value)
  # value = eval(formula())
  # sendMessageTo(str(value))
  while True:
    with timeout(controllerArgs[2]):
      value = receiveMessages()
      value = int(value)
      value = eval(formula())
      sendMessageTo(str(value))
      break
    sendMessageTo(str(value))
  i+=1
sock.close()

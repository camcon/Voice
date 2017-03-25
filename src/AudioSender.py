#AudioSender

import pyaudio
import wave
import math
import numpy
import socket, sys
import StreamFactory
import time

port = 8080
host = '10.120.36.193'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port))
    print 'Connected to:', host
except Exception as ex:
    print ex
    
stream = StreamFactory.makeInputStream()
outStream = StreamFactory.makeOutputStream()
CHUNK = 1024

startTime = time.time()
endTime = startTime + 5
message = ""
while startTime < endTime:
    data = stream.read(CHUNK)
    #sock.send(data)
    message = message + data
    startTime = time.time()
    print str(endTime - startTime)
    #outStream.write(data)

print 'writing message'
#outStream.write(message)
sock.send(message)    

#sock.close()

    

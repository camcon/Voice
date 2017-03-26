#AudioSender

import pyaudio
import wave
import math
import numpy
import socket, sys
import StreamFactory
import time

port = 8080
#host = '10.120.43.121'
def connect(host):
    if __name__ == "__main__":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print 'connecting to ', host
            sock.connect((host, port))
            print 'Connected to:', host
        except Exception as ex:
            print ex
            
        stream = StreamFactory.makeInputStream()
        outStream = StreamFactory.makeOutputStream()
        CHUNK = 1024

        startTime = time.time()
        endTime = startTime + 3
        message = ""

        # Continuous audio stream:
        print 'starting audio stream'
        while True:
            data = stream.read(CHUNK)
            sock.send(data)
        print 'writing message'

        # everything below for timed messages:
        ##while startTime < endTime:
        ##    data = stream.read(CHUNK)
        ##    #sock.send(data)
        ##    message = message + data
        ##    startTime = time.time()
        ##    print str(endTime - startTime)
        ##    #outStream.write(data)
        ##    print 'writing message'
        #outStream.write(message)
        ##try:
        ##    while message:
        ##        sent = sock.send(message)
        ##        if not sent:
        ##            break
        ##        message = message[sent:]
        ##    outStream.write(sent)
        ##except Exception as ex:
        ##    print ex
        #sock.send(message)    
        print "sent"
        #sock.close()
connect('localhost')
        

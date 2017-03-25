import DeeAudio as da
import socket, subprocess, select, sys, pyaudio, StreamFactory
# This is the client

# Audio setup
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# Socket setup
connList = [] # List of current connections/users
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 8080))
sock.listen(1)
#listener.listen(10)
print "Client running on ",sock.getsockname()
#allsocks = [listener]

# Main:
outStream = StreamFactory.makeOutputStream()
while True:
    conn, addr = sock.accept()
    print 'New connection from ', addr
    conn.send('plop')
    data = conn.recv(999999)
#    buffer = ''
##    while len(buffer) < 5120:
##        chunk = conn.recv(5120-len(buffer))
##        if not chunk:
##            print "done recieving"
##            break
##        print chunk
##        buffer += chunk
    
    print data
    
    outStream.write(data,1024)
    print "yum"
   # data = conn.recv(1024)
##    
##    if(data != None):
##        print "Recieved data:"
##        print data
##        outStream.write(data)    
##    else:
##        print "No data"

print "hi"

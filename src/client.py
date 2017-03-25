import DeeAudio as da
import socket, subprocess, select, sys, pyaudio
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
p = pyaudio.PyAudio()
# Main:
outStream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)
while True:
    conn, addr = sock.accept()

    print 'New connection from ', addr

    data = sock.recv(1024)
    if(data != None):
        print "Recieved data"
    outStream.write(data)    

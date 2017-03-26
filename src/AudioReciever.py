import socket, subprocess, select, sys, pyaudio, StreamFactory
# This is the audio listener

# Audio setup
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
def startListening():
    if __name__ == "__main__":
        # Socket setup
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', 8080))
        sock.listen(5)
        print "Client running on ",sock.getsockname()
        #allsocks = [listener]

        # Main:
        outStream = StreamFactory.makeOutputStream()
        conn, addr = sock.accept()
        print 'New connection from ', addr
        data = conn.recv(1024)

        #a = 1
        while data != '':
            outStream.write(data)
            data = conn.recv(1024)
            #a = a+1
            #print "Packy: ", a
            
        print "all done"

import AudioReciever
import AudioSender
import multiprocessing
import wx

host = '10.120.36.193'

if __name__ =='__main__':
    sender = multiprocessing.Process(target=AudioSender.connect, args=(host))
    listener = multiprocessing.Process(target=AudioReciever.startListening)

    sender.start()
    listener.start()

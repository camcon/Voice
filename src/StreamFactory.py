#AudioCreator

import pyaudio
import wave
import struct
import math
import numpy

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

MODIFIER = 5.0
OFFSET = 65.0
p = pyaudio.PyAudio()

def makeInputStream():
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    return stream

def makeOutputStream():
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)
    return stream

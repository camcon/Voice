import pyaudio
import wave
import struct
import math
import numpy
# Requires installing numpy and pyaudio libraries through pip install
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

MODIFIER = 5.0
OFFSET = 65.0
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
outStream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

def getAudio():
    data = stream.read(CHUNK)
    outStream.write(data)

def close():
    stream.stop_stream()
    stream.close()
    p.terminate()



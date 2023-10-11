import wave
import numpy as np

def load_data(filename):
    wav_file = wave.open(filename, 'r')
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav_file.getparams()
    frames = wav_file.readframes(nframes)
    data =  {i: frames[i] for i in range(len(frames))}
    wav_file.close()
    return data


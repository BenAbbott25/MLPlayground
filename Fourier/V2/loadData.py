import wave
import numpy as np
import torch
from fourierSeries import fourier

def load_data(filename, order):
    print("Loading data")
    # empty tensors to store data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    wav_file = wave.open(filename, 'r')
    nframes = wav_file.getparams().nframes
    frames = wav_file.readframes(nframes)
    for i in range(nframes):
        if np.random.rand() < 0.5:
            train_data.append(fourier(np.pi*i/nframes,order))
            train_labels.append(frames[i]/32767.0)
        else:
            test_data.append(fourier(np.pi*i/nframes,order))
            test_labels.append(frames[i]/32767.0)
    wav_file.close()
    # convert to tensors
    train_data = torch.tensor(train_data, dtype=torch.float32)
    train_labels = torch.tensor(train_labels, dtype=torch.float32)
    test_data = torch.tensor(test_data, dtype=torch.float32)
    test_labels = torch.tensor(test_labels, dtype=torch.float32)
    
    return train_data, train_labels, test_data, test_labels


# train_data, train_labels, test_data, test_labels = load_data("sine_wave.wav",5)
# print(train_data, train_labels, test_data, test_labels)
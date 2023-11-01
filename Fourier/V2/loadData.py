import wave
import numpy as np
import torch
from fourierSeries import fourier
from tqdm import tqdm

max_amplitude = 32767.0

def load_data(filename, order):
    print("Loading data")
    # empty tensors to store data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    wav_file = wave.open(filename, 'r')
    # Graph the wav file
    import matplotlib.pyplot as plt
    nframes = wav_file.getparams().nframes
    frames = wav_file.readframes(nframes)
    full_data = []
    full_labels = []
    for i in tqdm(range(nframes), desc="Loading data"):
        full_data.append(fourier(((2*np.pi*i/nframes)-np.pi),order))
        full_labels.append(frames[i]/max_amplitude)

    for i in range(len(full_data)):
        if np.random.rand() < 0.65:
            train_data.append(full_data[i])
            train_labels.append(full_labels[i])
        else:
            test_data.append(full_data[i])
            test_labels.append(full_labels[i])

    plt.figure(figsize=(10, 5))
    plt.plot(full_labels, color='blue')
    plt.title('Full Labels Graph')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

    wav_file.close()
    # convert to tensors
    train_data = torch.tensor(train_data, dtype=torch.float32)
    train_labels = torch.tensor(train_labels, dtype=torch.float32)
    test_data = torch.tensor(test_data, dtype=torch.float32)
    test_labels = torch.tensor(test_labels, dtype=torch.float32)
    
    return train_data, train_labels, test_data, test_labels


# train_data, train_labels, test_data, test_labels = load_data("sine_wave.wav",5)
# print(train_data, train_labels, test_data, test_labels)
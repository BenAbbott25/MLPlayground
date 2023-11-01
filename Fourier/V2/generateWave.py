import wave
import math
import numpy as np
from tqdm import tqdm

# filename = "sine_wave.wav"
# duration = 10  # Duration in seconds
# sample_rate = 44100  # Sample rate in Hz


# num_samples = int(duration * sample_rate)
# amplitude = 32767.0 

# wave_file = wave.open(filename, 'w')
# wave_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))

def generate_wav(filename, amplitudes):
    sample_rate = 44100  # Sample rate in Hz
    max_amplitude = 32767.0  # Amplitude of the sine wave (0 to 32767)
    num_samples = len(amplitudes)
    print(f"maxPeak: ${max(amplitudes)}")
    print(f"minPeak: ${min(amplitudes)}")

    wave_file = wave.open(filename, 'w')
    wave_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))

    for i in tqdm(range(num_samples)):
        # Construct the wav file from the amplitudes
        value = int(max_amplitude * amplitudes[i])
        wave_file.writeframesraw(value.to_bytes(2, byteorder='little', signed=True))
        
        

    wave_file.close()

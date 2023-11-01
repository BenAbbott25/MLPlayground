import wave
import math
import numpy as np

filename = "A7_chord.wav"
duration = 0.5  # Duration in seconds
sample_rate = 44100  # Sample rate in Hz
frequency_root = 440.0  # Frequency of the root note (A) in Hz
frequency_Maj_third = 554.37  # Frequency of the major third (C#) in Hz
frequency_fifth = 659.25  # Frequency of the fifth (E) in Hz
# frequency_min_seventh = 415.30  # Frequency of the minor seventh (G) in Hz
frequency_9th = 493.88 #B

amplitude_root = 0.3  # Amplitude for root note
amplitude_third = 0.25  # Amplitude for major third
amplitude_fifth = 0.25  # Amplitude for fifth
amplitude_seventh = 0.175  # Amplitude for minor seventh

num_samples = int(duration * sample_rate)
amplitude = 32767.0  # Maximum amplitude of the sine wave (0 to 32767)

wave_file = wave.open(filename, 'w')
wave_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))

amplitudes = [amplitude_root, amplitude_third, amplitude_fifth, amplitude_seventh]
def generate_sine_wave(amplitudes, num_samples, sample_rate):
    frequencies = [frequency_root, frequency_Maj_third, frequency_fifth, frequency_9th]
    time_points = np.arange(num_samples) / sample_rate

    for i in range(num_samples):
        sine_values = [amp * math.sin(2 * math.pi * freq * time_points[i]) for amp, freq in zip(amplitudes, frequencies)]
        value = int(np.sum(np.array(sine_values) * np.array(amplitudes)) * amplitude)
        print(value)

        wave_file.writeframesraw(value.to_bytes(2, byteorder='little', signed=True))

    wave_file.close()

generate_sine_wave(amplitudes, num_samples, sample_rate)

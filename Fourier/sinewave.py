import wave
import math
import numpy as np

filename = "sine_wave.wav"
duration = 10  # Duration in seconds
sample_rate = 44100  # Sample rate in Hz
frequency_root = 220.0  # Halved frequency of the sine wave in Hz
frequency_Maj_third = 277.185  # Halved frequency of the third in Hz
frequency_min_third = 246.942  # Halved frequency of the minor third in Hz
frequency_fifth = 329.625  # Halved frequency of the fifth in Hz
frequency_Maj_seventh = 392.0  # Added frequency of the seventh in Hz
frequency_min_seventh = 346.5  # Halved frequency of the minor seventh in Hz

amplitude_root = 0.5  # Multiplyer for root
amplitude_third = 0.5  # Multiplyer for third
amplitude_fifth = 0.5  # Multiplyer for fifth
amplitude_seventh = 0.5  # Multiplyer for seventh

lfo_root = 30.0  # LFO for root in Hz
lfo_third = 15.0  # LFO for third in Hz
lfo_fifth = 7.5  # LFO for fifth in Hz
lfo_seventh = 3.75  # LFO for seventh in Hz


num_samples = int(duration * sample_rate)
amplitude = 32767.0  # Amplitude of the sine wave (0 to 32767)

wave_file = wave.open(filename, 'w')
wave_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))

# # Create a list of frequencies
# frequencies = [frequency_root, frequency_third, frequency_fifth]
f_third_shift = frequency_Maj_third - frequency_min_third
f_seventh_shift = frequency_Maj_seventh - frequency_min_seventh


# Create a list of amplitudes
amplitudes = [amplitude_root, amplitude_third, amplitude_fifth, amplitude_seventh]

for i in range(num_samples):
    #x^2    
    # relative_duration = -((i/num_samples - 0.5) ** 2) + 1
    relative_duration = min(i/num_samples,1)

    # Create a list of frequencies
    frequencies = [frequency_root, frequency_Maj_third - (f_third_shift * relative_duration), frequency_fifth, frequency_Maj_seventh - (f_seventh_shift * relative_duration)]    

    # Create a list of sine wave values for each frequency
    sine_values = [math.sin(2.0 * math.pi * freq * i / sample_rate) for freq in frequencies]

    # calculate amplitudes using individual lfo and sine function
    lfos = [lfo_root - 0.5, lfo_third - 0.5, lfo_fifth - 0.5, lfo_seventh - 0.5]
    modified_amplitudes = [amplitude * modifier + ((math.cos(2.0 * math.pi * lfo * i / sample_rate)) / 10) for modifier, lfo in zip(amplitudes, lfos)]

    # Calculate the dot product
    value = int(np.dot(sine_values, modified_amplitudes) / 3)
    print(value)

    wave_file.writeframesraw(value.to_bytes(2, byteorder='little', signed=True))

wave_file.close()
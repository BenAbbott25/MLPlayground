# fourier takes in number and outputs a list of the fourier series of order n
import numpy as np
def fourier(input, order):
    output = [input]
    for i in range(order):
        output.append(np.sin(input * (i+1) * np.pi / 44100 ))
        output.append(np.cos(input * (i+1) * np.pi / 44100 ))
    return output

# print(fourier(10, 5))
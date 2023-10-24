# fourier takes in number and outputs a list of the fourier series of order n
import numpy as np
def fourier(input, order):
    series = [input]
    for i in range(order):
        series.append(np.sin(input*(order+1)))
        series.append(np.cos(input*(order+1)))
    return series

# print(fourier(10, 5))
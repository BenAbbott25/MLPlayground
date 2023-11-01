# fourier takes in number and outputs a list of the fourier series of order n
import numpy as np
def fourier(input, order):
    series = [input]
    for i in range(order):
        series.append(np.sin(input*(i+1)*10))
        series.append(np.cos(input*(i+1)*10))
    return series

# print(fourier(10, 5))
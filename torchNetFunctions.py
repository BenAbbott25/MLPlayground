import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

def generate_new(shape: list):
    # generates new neural network with random weights and biases
    # returns the network
    # shape: list of integers, the shape of the network
    # relu activation function is used for all layers except the last one
    # softmax activation function is used for the last layer

    # check if the shape is valid
    if len(shape) < 2:
        raise ValueError("The network must have at least 2 layers")
    for i in range(len(shape)):
        if shape[i] < 1:
            raise ValueError("The network must have at least 1 neuron in each layer")
    
    # create the network
    net = nn.Sequential()
    for i in range(len(shape) - 1):
        net.add_module("fc" + str(i), nn.Linear(shape[i], shape[i + 1]))
        if i < len(shape) - 2:
            net.add_module("relu" + str(i), nn.ReLU())
        else:
            net.add_module("softmax", nn.Softmax(dim=1))

    return net

    
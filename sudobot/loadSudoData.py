import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import random

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

def load_data(index):
    print("Loading data")
    # empty tensors to store data
    train_data_input = []
    train_data_output = []
    test_data_input = []
    test_data_output = []

    train_sudos = []
    with open('sudokuData/trainData_' + index + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            train_sudos.append(row)
    print(train_sudos[1][0])
    print(train_sudos[1][1])
    # remove header
    train_sudos = train_sudos[1:]
    # split str into list of ints
    for i in range(len(train_sudos)):
        train_sudos[i][0] = [int(x) for x in train_sudos[i][0]]
        train_sudos[i][1] = [int(x) for x in train_sudos[i][1]]
    # convert to np array
    train_sudos = np.array(train_sudos)
    print(len(train_sudos))
    print(len(train_sudos))

    print(type(train_sudos[0][0]))
    print(type(train_sudos[0][1]))
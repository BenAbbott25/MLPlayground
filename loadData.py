import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import random


# load the data
def load_data():
    print("Loading data")
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    with open('mnist_train.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            train_data.append(row[1:])
            train_labels.append(row[0])
    with open('mnist_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            test_data.append(row[1:])
            test_labels.append(row[0])

    # convert to numpy arrays
    train_data = np.array(train_data, dtype=np.float32)
    train_labels = np.array(train_labels, dtype=np.int32)
    test_data = np.array(test_data, dtype=np.float32)
    test_labels = np.array(test_labels, dtype=np.int32)

    # normalize the data
    train_data = train_data / 255.0
    test_data = test_data / 255.0

    print("Data loaded")
    
    return train_data, train_labels, test_data, test_labels


# train_data, train_labels, test_data, test_labels = load_data()
# print("Data loaded")


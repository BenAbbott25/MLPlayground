# runs a forward pass on the network using test_data[0] and returns the output

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import csv


# import the load_data function from loadData.py
from loadData import load_data
train_data, train_labels, test_data, test_labels = load_data()

def runNetwork(data):
    # load the model
    model = tf.keras.models.load_model('model.h5')

    # run a forward pass on the network using data and return the output
    prediction = model.predict(data)
    return prediction

print(runNetwork(test_data[0]))
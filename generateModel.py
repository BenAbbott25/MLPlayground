# generate a base model for the project, and save it to the disk

import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 784 inputs, 10 outputs, 2 hidden layers with 512 neurons each
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

# show the model summary
model.summary()

# save the model to the disk
model.save('model.h5')
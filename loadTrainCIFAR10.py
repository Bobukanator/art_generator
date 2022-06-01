# Python script that loads the CIFAR-10 model, trains, and saves for use in this art generator project.
# Base code from Renu Khandelwal:
# https://towardsdatascience.com/loading-custom-image-dataset-for-deep-learning-models-part-1-d64fa7aaeca6
# additional input thanks to
# https://stackabuse.com/image-recognition-in-python-with-tensorflow-and-keras/
from keras.datasets import cifar10
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from keras.utils import np_utils
from keras.constraints import maxnorm
from tensorflow.keras.models import Sequential, Model
from keras.layers.core import Dense, Flatten
from tensorflow.keras.layers import InputLayer
from tensorflow.keras import layers, Input
from tensorflow import keras
import os
import random
import pandas as pd
import numpy as np
import tensorflow as tf
import cv2
import ssl
# required to download the CIFAR10 dataset, otherwise cert error will occur
ssl._create_default_https_context = ssl._create_unverified_context

IMG_WIDTH = 128
IMG_HEIGHT = 128

# Set random seed for purposes of reproducibility
seed = 21


def readyCIFAR10():
    # load in cifar10 data
    # Loading in the data
    print("Loading CIFAR10 dataset - this will take a while.. ")
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    print("CIFAR10 dataset loaded..")
    # Normalize the inputs from 0-255 to between 0 and 1 by dividing by 255
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    # One-hot encode outputs
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    class_num = y_test.shape[1]

    model = keras.Sequential()
    model.add(keras.layers.Conv2D(
        32, (3, 3), input_shape=X_train.shape[1:], padding='same'))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.Conv2D(32, 3, input_shape=(
        32, 32, 3), activation='relu', padding='same'))
    model.add(keras.layers.Dropout(0.2))

    print("keras model created..")

    print("Starting Batch Normalization..")
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.Conv2D(64, 3, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling2D(2))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.Conv2D(64, 3, activation='relu', padding='same'))
    model.add(keras.layers.MaxPooling2D(2))
    model.add(keras.layers.Dropout(0.2))

    print("Starting Batch Normalization #2..")
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.Conv2D(128, 3, activation='relu', padding='same'))
    model.add(keras.layers.Dropout(0.2))

    print("Starting Batch Normalization #3..")
    model.add(keras.layers.BatchNormalization())

    print("Flattening Data..")
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dropout(0.2))

    model.add(keras.layers.Dense(32, activation='relu'))
    model.add(keras.layers.Dropout(0.3))
    model.add(keras.layers.BatchNormalization())

    model.add(keras.layers.Dense(class_num, activation='softmax'))

    print("Compiling CIFAR dataset..")
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    print(model.summary())

    # train the network time and save that history
    print("Training the network --->")
    np.random.seed(seed)
    history = model.fit(X_train, y_train, validation_data=(
        X_test, y_test), epochs=40, batch_size=64)

    # Model evaluation
    scores = model.evaluate(X_test, y_test, verbose=0)
    print("Accuracy: %.2f%%" % (scores[1]*100))

    # save model to file for loading later
    model.save(r'/cifar10modeltrained')

    # plot the learning curve
    pd.DataFrame(history.history).plot()
    plt.show()


if __name__ == "__main__":
    print("Starting loading and training program for CIFAR-10 dataset..")

    readyCIFAR10()

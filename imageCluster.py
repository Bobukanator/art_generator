# Python script that loads images into
# an Image dataset for use with ML
# Base code from Renu Khandelwal
# https://towardsdatascience.com/loading-custom-image-dataset-for-deep-learning-models-part-1-d64fa7aaeca6
# Will be using the built in CIFAR-10 dataset to help group our existing images into something that looks
# human recognizable
# https://stackabuse.com/image-recognition-in-python-with-tensorflow-and-keras/
import os
import random
import pandas as pd
import numpy as np
import tensorflow as tf
import cv2


from tensorflow import keras
from tensorflow.keras import layers, Input
from tensorflow.keras.layers import InputLayer
from keras.layers.core import Dense, Flatten
from tensorflow.keras.models import Sequential, Model
from keras.constraints import maxnorm
from keras.utils import np_utils
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from keras.datasets import cifar10

IMG_WIDTH = 128
IMG_HEIGHT = 128

# Set random seed for purposes of reproducibility
seed = 21


def create_dataset(img_folder):

    img_data_array = []
    for file in os.listdir(os.path.join(img_folder)):

        image_path = os.path.join(img_folder, file)
        image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH),
                           interpolation=cv2.INTER_AREA)
        image = np.array(image)
        image = image.astype('float32')
        image /= 255
        img_data_array.append(image)

    return img_data_array


def showRandomSampleOfRandomGeneratedImages(img_folder):
    # plt.figure(figsize=(20, 20))
    # Very Cool loading of random images -- save for future use
    for i in range(5):
        file = random.choice(os.listdir(img_folder))
        image_path = os.path.join(img_folder, file)
        img = mpimg.imread(image_path)
        ax = plt.subplot(1, 5, i+1)
        ax.title.set_text(file)
        plt.imshow(img)
    plt.show()


def loadRandomImageDataSet():
    # extract the image array and class name
    img_data = create_dataset(img_folder)
    model = tf.keras.Sequential(
        [
            tf.keras.layers.InputLayer(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
            tf.keras.layers.Conv2D(
                filters=32, kernel_size=3, strides=(2, 2), activation='relu'),
            tf.keras.layers.Conv2D(
                filters=64, kernel_size=3, strides=(2, 2), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(6)
        ])
    model(np.array(img_data, np.float32))
    model.summary()


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

    model = keras.Sequential([
        keras.layers.layer1,
        keras.layers.layer2,
        keras.layers.layer3
    ])

    print("keras model created..")

    model = keras.Sequential()
    model.add(keras.layers.Conv2D(
        32, (3, 3), input_shape=X_train.shape[1:], padding='same'))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.Conv2D(32, 3, input_shape=(
        32, 32, 3), activation='relu', padding='same'))
    model.add(keras.layers.Dropout(0.2))

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
                  optimizer='adam', metrics=['accuracy', 'val_accuracy'])
    print(model.summary())


if __name__ == "__main__":
    print("Starting program..")

    img_folder = r'art_generator/images'
    showRandomSampleOfRandomGeneratedImages(img_folder)
    readyCIFAR10()

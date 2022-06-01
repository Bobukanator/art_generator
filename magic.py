# Loads trained model and examines images
from keras.datasets import cifar10
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from keras.utils import np_utils
from keras.constraints import maxnorm
from tensorflow.keras.models import Sequential, Model
from keras.layers.core import Dense, Flatten
from tensorflow.keras.layers import InputLayer
from tensorflow.keras import layers, Input
from keras.preprocessing import image
from tensorflow import keras
import os
import random
import pandas as pd
import numpy as np
import tensorflow as tf
import cv2
import ssl

IMG_WIDTH = 32
IMG_HEIGHT = 32


def loadImagesToArray(img_folder):

    img_data_array = []
    for file in os.listdir(os.path.join(img_folder)):

        image_path = os.path.join(img_folder, file)
        theImage = image.load_img(
            image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
        theImageArray = image.img_to_array(theImage)
        theImageArray = np.expand_dims(theImageArray, axis=0)

        img_data_array.append(theImageArray)

    return img_data_array


def loadRandomImageDataSet():
    # extract the image array and class name
    img_data = loadImagesToArray(img_folder)
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


def loadCIFarModel():
    print("Loading saved & trained CIFAR10 model...")
    model = tf.keras.models.load_model(r'cifar10modeltrained')
    # Check its architecture
    model.summary()
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    X_test = X_test.astype('float32')
    X_test = X_test / 255.0
    y_test = np_utils.to_categorical(y_test)
    scores = model.evaluate(X_test, y_test, verbose=0)
    print("Accuracy of loaded CIFAR model: %.2f%%" % (scores[1]*100))
    return model


if __name__ == "__main__":
    print("Starting Magic..")
    model = loadCIFarModel()

    img_folder = r'images'
    imageArray = loadImagesToArray(img_folder)
    print("Image Loaded "+str(len(imageArray)))
    for theImage in imageArray:
        result = model.predict(theImage)
        print(result)
        if result[0][0] == 1:
            print("Aeroplane")
        elif result[0][1] == 1:
            print('Automobile')
        elif result[0][2] == 1:
            print('Bird')
        elif result[0][3] == 1:
            print('Cat')
        elif result[0][4] == 1:
            print('Deer')
        elif result[0][5] == 1:
            print('Dog')
        elif result[0][6] == 1:
            print('Frog')
        elif result[0][7] == 1:
            print('Horse')
        elif result[0][8] == 1:
            print('Ship')
        elif result[0][9] == 1:
            print('Truck')
        else:
            print('Error')

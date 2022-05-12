# Python script that loads images into
# an Image dataset for use with ML
# Base code from Renu Khandelwal
# https://towardsdatascience.com/loading-custom-image-dataset-for-deep-learning-models-part-1-d64fa7aaeca6
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
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

IMG_WIDTH = 128
IMG_HEIGHT = 128


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


if __name__ == "__main__":
    print("This program uses ML to cluster randomly created")

    # plt.figure(figsize=(20, 20))
    img_folder = r'art_generator/images'
    # Very Cool loading of random images -- save for future use
    # for i in range(5):
    #    file = random.choice(os.listdir(img_folder))
    #    image_path = os.path.join(img_folder, file)
    #    img = mpimg.imread(image_path)
    #    ax = plt.subplot(1, 5, i+1)
    #    ax.title.set_text(file)
    #    plt.imshow(img)
    # plt.show()

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

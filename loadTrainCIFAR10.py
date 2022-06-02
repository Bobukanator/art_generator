# Python script that loads the CIFAR-10 model, trains, and saves for use in this art generator project.
# Base code from Renu Khandelwal:
# https://towardsdatascience.com/loading-custom-image-dataset-for-deep-learning-models-part-1-d64fa7aaeca6
# Additional input thanks to
# https://stackabuse.com/image-recognition-in-python-with-tensorflow-and-keras/
import ssl
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from tensorflow import keras
from keras.datasets import cifar10
from keras.utils import np_utils

# required to download the CIFAR10 dataset, otherwise cert error will occur
ssl._create_default_https_context = ssl._create_unverified_context

# Set random seed for purposes of reproducibility
SEED = 21


def ready_cifar10():
    """load CIFAR-10 dataset - 60K 32x32 color images in 10 classes"""
    # load in cifar10 data
    # Loading in the data
    print("Loading CIFAR10 dataset - this will take a while.. ")
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    print("CIFAR10 dataset loaded..")
    # Normalize the inputs from 0-255 to between 0 and 1 by dividing by 255
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # One-hot encode outputs
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    class_num = y_test.shape[1]

    model = keras.Sequential()
    model.add(keras.layers.Conv2D(
        32, (3, 3), input_shape=x_train.shape[1:], padding='same'))
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
    np.random.seed(SEED)
    history = model.fit(x_train, y_train, validation_data=(
        x_test, y_test), epochs=50, batch_size=64)

    # Model evaluation
    scores = model.evaluate(x_test, y_test, verbose=0)
    print(F"Accuracy: % {round(scores[1]*100, 2)}")

    # save model to file for loading later
    model.save(r'cifar10modeltrained')

    # plot the learning curve
    pd.DataFrame(history.history).plot()
    plt.show()


if __name__ == "__main__":
    print("Starting loading and training program for CIFAR-10 dataset..")
    ready_cifar10()

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

plt.figure(figsize=(20, 20))
img_folder = r'art_generator/images'
for i in range(5):
    file = random.choice(os.listdir(img_folder))
    image_path = os.path.join(img_folder, file)
    img = mpimg.imread(image_path)
    ax = plt.subplot(1, 5, i+1)
    ax.title.set_text(file)
    plt.imshow(img)

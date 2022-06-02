# Loads trained model and examines images
import os
import random
import time
import concurrent.futures
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from keras.preprocessing import image
import cifar10utils
import artmaker

# globals - CIFAR Image dataset is 32x32 so only need to load images for prediction at the same resolution
IMG_WIDTH = 32
IMG_HEIGHT = 32


def interate_images_and_classify(img_folder):
    """ load images from img_folder, classify using CIFAR-10 model, and save to corresponding directory """

    for file in os.listdir(os.path.join(img_folder)):
        # loading one image at a time
        image_path = os.path.join(img_folder, file)
        if ".png" in image_path:
            the_image = image.load_img(
                image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
            the_image_as_array = image.img_to_array(the_image)
            the_image_as_array = np.expand_dims(the_image_as_array, axis=0)
            # check image and move it to new directory based on what the model thinks it looks like!
            result = cifar10utils.human_readable_result(
                model.predict(the_image_as_array))
            print(result)
            os.renames(image_path, img_folder+"/"+result+"/"+file)


def create_until_10class(target_class):
    """randomly generate image, classify, and continue until we have 1 of each cifar10 class - warning this may never end :) """
    print("Attempting to create random image that is classified as "+target_class)
    result = ""
    start = time.process_time()
    while result != target_class:
        the_image = artmaker.generate_image(100)
        the_small_image = the_image.resize((32, 32))
        the_image_as_array = image.img_to_array(the_small_image)
        the_image_as_array = np.expand_dims(the_image_as_array, axis=0)
        result = cifar10utils.human_readable_result(
            MODEL.predict(the_image_as_array))
        if result == target_class:
            the_image.save("images/"+result+"Image.png")
            print("Success! Image generated and saved as "+result+"Image.png")
            print(f"Time elapsed: {(time.process_time()-start)} seconds")


def show_random_sample_of_images(img_folder):
    """Very Cool loading of random images -- save for future use"""
    for i in range(5):
        file = random.choice(os.listdir(img_folder))
        image_path = os.path.join(img_folder, file)
        img = mpimg.imread(image_path)
        ax = plt.subplot(1, 5, i+1)
        ax.title.set_text(file)
        plt.imshow(img)
    plt.show()


def load_cifar_model():
    """ loads saved cifar10 model"""
    print("Loading saved & trained CIFAR10 model...")
    global MODEL
    MODEL = tf.keras.models.load_model(r'cifar10modeltrained')
    # Check its architecture
    MODEL.summary()


if __name__ == "__main__":
    print("Starting Magic..")
    # interate_images_and_classify(r'images')
    load_cifar_model()
    time.sleep(10)

    cifar10_types = [
        cifar10utils.CiFar10Classes.AUTOMOBILE,
        cifar10utils.CiFar10Classes.AIRPLANE,
        cifar10utils.CiFar10Classes.CAT
    ]

    create_until_10class(cifar10utils.CiFar10Classes.CAT)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #    executor.map(create_until_10class, cifar10_types)

    print("Attempting to create random image that is classified as a Meat Popcyle")
    time.sleep(2)
    print("just kidding!.. ")

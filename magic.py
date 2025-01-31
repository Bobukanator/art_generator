"""Loads trained model and examines images"""
import os
import random
import time
from datetime import datetime as dt
from threading import Thread
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from keras.preprocessing import image
import cifar10utils
import artmaker

# globals - CIFAR Image dataset is 32x32 so only need to load images
# for prediction at the same resolution
IMG_WIDTH = 32
IMG_HEIGHT = 32
IMAGE_DRAW_OPERATIONS = 105
DATED_IMAGE_FOLDER = dt.now().strftime("%m_%d_%Y")
MODEL = tf.keras.models.load_model(r'cifar10modeltrained')


def interate_images_and_classify(img_folder):
    """ load images from img_folder, classify using CIFAR-10 model,
    and save to corresponding directory """

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
                MODEL.predict(the_image_as_array))
            print(result)
            os.renames(image_path, img_folder+"/"+result+"/"+file)


def create_until_target_generated(tracker, thread_id):
    """randomly generate image, classify, and continue until we have 1 of each cifar10 class
    warning this may never end :) """
    print("Create until target with id:"+str(thread_id)+" started!")
    result = ""
    start = time.process_time()
    while not tracker.found_all():
        the_image = artmaker.generate_image(IMAGE_DRAW_OPERATIONS)
        the_small_image = the_image.resize((32, 32))
        the_image_as_array = image.img_to_array(the_small_image)
        the_image_as_array = np.expand_dims(the_image_as_array, axis=0)
        result = cifar10utils.human_readable_result(
            MODEL.predict(the_image_as_array))
        if tracker.add_class(result):
            secondspast = time.process_time()-start
            the_image.save(
                "images/"+DATED_IMAGE_FOLDER+"/"+result+str(secondspast)+"Image.png")
            the_imagef1 = artmaker.apply_random_filter(the_image)
            the_imagef1.save(
                "images/"+DATED_IMAGE_FOLDER+"/"+result+str(secondspast)+"Imagef1.png")
            the_imagef2 = artmaker.apply_random_filter(the_image)
            the_imagef2.save(
                "images/"+DATED_IMAGE_FOLDER+"/"+result+str(secondspast)+"Imagef2.png")
            the_imagef3 = artmaker.apply_random_filter(the_image)
            the_imagef3.save(
                "images/"+DATED_IMAGE_FOLDER+"/"+result+str(secondspast)+"Imagef3.png")
            print("Success in id:" + str(thread_id) + " Images generated and saved as "+result +
                  "Image[f1-f3].png in folder: images/"+DATED_IMAGE_FOLDER)
            print(f"Time elapsed: {str(secondspast)} seconds")
            tracker.state()


def show_random_sample_of_images(img_folder):
    """Very Cool loading of random images -- save for future use"""
    for i in range(5):
        file = random.choice(os.listdir(img_folder))
        image_path = os.path.join(img_folder, file)
        img = mpimg.imread(image_path)
        a_x = plt.subplot(1, 5, i+1)
        a_x.title.set_text(file)
        plt.imshow(img)
    plt.show()


def load_cifar_model():
    """ loads saved cifar10 model"""
    print("Loading saved & trained CIFAR10 model...")
    # Check its architecture
    MODEL.summary()


if __name__ == "__main__":

    # create new folder to store images
    os.mkdir("images/"+DATED_IMAGE_FOLDER)
    print("Creating folder: images/"+DATED_IMAGE_FOLDER)

    print("Starting Magic..")
    # interate_images_and_classify(r'images')
    load_cifar_model()
    time.sleep(10)

    cifar_tracker = cifar10utils.CiFarClassTracker()
    cifar_tracker2 = cifar10utils.CiFarClassTracker()
    cifar_tracker3 = cifar10utils.CiFarClassTracker()

    threads = []
    for n in range(1, 11):
        t = Thread(target=create_until_target_generated,
                   args=(cifar_tracker, n,))
        t2 = Thread(target=create_until_target_generated,
                    args=(cifar_tracker2, n,))
        t3 = Thread(target=create_until_target_generated,
                    args=(cifar_tracker3, n,))

        threads.append(t)
        threads.append(t2)
        threads.append(t3)
        t.start()
        t2.start()
        t3.start()

    for t in threads:
        t.join()

    print("Attempting to create random image that is classified as a Meat Popcyle")
    time.sleep(2)
    print("just kidding!.. ")

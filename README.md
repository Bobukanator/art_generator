Fun NFT phython ART generator inspired by Pixegami's 
"How to create NFT generative art using Python"
  https://youtu.be/BMq2Jrvp9AA

This project contains the following: 
#artmaker.py 
Module to randomly create cool images
#char10utils.py
Utility module to provide helpful functions when dealing with the CIFAR-10 dataset
#generateBasic.py
Utilizes the artmaker module to randomly create images. Currently using the default variables found in artmaker - 100 512x512 random color images saved to images directory
#loadTrainCIFAR10.py
Program that loads the CIFAR-10 model, trains, and saves for use in this art generator project. Currently trains 50 epochs, this can be modified. 
If you don't want to run this, you do not need to as a saved trained model (50 epochs!) is saved in this repository with accuracy of 84.64%
#magic.py
There are two important functions in magic, create_until_10class & interate_images_and_classify

#dependencies
Make sure to install these modules using pip before running

pandas
numpy
tensorflow
opencv-python
matplotlib

Highly recommend you install CUDA 11.2 & cuDNN 8.1 (NOTE IT MUST BE THE EXACT VERSION) to utilize your GPU 
for training if you so desire. Tensorflow training on a CPU is MUCH slower than GPU. 
https://www.tensorflow.org/install/gpu




# importing the required packages for the implementation of CNN architecture
import numpy as np
np.random.seed(2018)
import os
import glob
import cv2
import datetime
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")

from sklearn.cross_validation import KFold
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from keras.utils import np_utils
from sklearn.metrics import log_loss
from keras import __version__ as keras_version

# defining a function to resize the images provided in the dataset
# Parameters
# ----------
# img_path : path
#     path of the image to be resized
def resize_image(img_path):
    # reading image file
    img = cv2.imread(img_path)
    # Resize the image to be 32 by 32
    img_resized = cv2.resize(img, (32, 32), cv2.INTER_LINEAR)
    return img_resized

# loading all the training samples of the dataset and their corresponding labels, and resizing each image
def load_training_samples():
    # Varibales to hold the training input and output variables
    train_input_variables = []
    train_input_variables_id = []
    train_label = []
    # Scanning all images in each folder of a fish type (category)
    print('Start Reading Train Images')
    folders = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
    for fld in folders:
        folder_index = folders.index(fld)
        print('Load folder {} (Index: {})'.format(fld, folder_index))
        imgs_path = os.path.join('..', 'input', 'train', fld, '*.jpg')
        files = glob.glob(imgs_path)
        for file in files:
            file_base = os.path.basename(file)
            # Resize the image
            resized_img = resize_image(file)
            # appending the processed image to the input/output variables or the classifier
            train_input_variables.append(resized_img)
            train_input_variables_id.append(file_base)
            train_label.append(folder_index)
        return train_input_variables, train_input_variables_id, train_label
            
# loading all the testing samples of the dataset and their corresponding labels, and resizing each image
def load_testing_samples():
    # Scanning images from the test folder
    imgs_path = os.path.join('..', 'input', 'test_stg1', '*.jpg')
    files = sorted(glob.glob(imgs_path))
    # Vaiables to hold the testing samples
    testing_samples = []
    testing_samples_id = []
    # Processing the images and appending them to the array that we have
    for file in files:
        file_base = os.path.basename(file)
        # Image resizing
        resized_img = resize_image(file)
        testing_samples.append(resized_img)
        testing_samples_id.append(file_base)
        return testing_samples, testing_samples_id
    
# defining a function to use load_training_samples() for loading and resizing training samples.
def load_normalize_training_samples():
    # Calling the load function in order to load and resize the training samples
    training_samples, training_label, training_sample_id = load_training_samples()
    # Converting the loaded and resized data into Numpy format

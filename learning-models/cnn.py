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
    training_samples = np.array(training_samples, dtype=np.uint8)
    training_label = np.array(training_label, dtype=np.uint8)
    # Reshaping the training samples
    training_samples = training_samples.transpose((0, 3, 1, 2))
    # Converting the training samples and training labeles into float format
    training_samples = training_samples.astype('float32')
    training_samples = training_samples / 255
    training_label = np_utils.to_categorical(training_label, 8)
    return training_samples, training_label, training_sample_id

# defining a function to use load_testing_samples() for loading and resizing testing samples.
def load_normalize_testing_samples():
    # Calling the load function in order to load and resize the testing samples
    testing_samples, testing_samples_id = load_testing_samples()
    # Converting the loaded and resized data into Numpy format
    testing_samples = np.array(testing_samples, dtype=np.uint8)
    # Reshaping the testing samples
    testing_samples = testing_samples.transpose((0, 3, 1, 2))
    # Converting the testing samples into float format
    testing_samples = testing_samples.astype('float32')
    testing_samples = testing_samples / 255
    return testing_samples, testing_samples_id
    
# defining a function to create a CNN architecture
def create_cnn_model_arch():
    pool_ize = 2 # a 2x2 pooling matrix
    conv_depth_1 = 32 # 32 kernels per convolution layers.
    conv_depth_2 = 64 # switching to 64 after the first pooling layer
    kernel_size = 3 # 3x3 kernels per convolution layer
    drop_prob = 0.5 # dropout in the FC layer with probability 0.5
    hidden_size = 32  # the FC layer with 512 neurons
    num_classes = 8 # 8 fish types (8 categories)
    # Conv [32] -> Conv [32] -> Pool
    cnn_model = Sequential()
    cnn_model.add(ZeroPadding2D((1, 1), input_shape=(3, 32, 32), dim_ordering='th'))
    cnn_model.add(Convolution2D(conv_depth_1, kernel_size, kernel_size, activation='relu', dim_ordering='th'))
    cnn_model.add(ZeroPadding2D((1, 1), dim_ordering='th'))
    cnn_model.add(Convolution2D(conv_depth_1, kernel_size, kernel_size, activation='relu', dim_ordering='th'))
    cnn_model.add(MaxPooling2D(pool_size=(pool_size, pool_size), strides=(2, 2), dim_ordering='th'))
    # Conv [64] -> Conv [64] -> Pool
    cnn_model.add(ZeroPadding2D((1, 1), dim_ordering='th'))
    cnn_model.add(Convolution2D(conv_depth_2, kernel_size, kernel_size, activation='relu', dim_ordering='th'))
    cnn_model.add(ZeroPadding2D((1, 1), dim_ordering='th'))
    cnn_model.add(Convolution2D(conv_depth_2, kernel_size, kernel_size, activation='relu', dim_ordering='th'))
    cnn_model.add(MaxPooling2D(pool_size=(pool_size, pool_size), strides=(2, 2), dim_ordering='th'))
    # Now flatten to 1D, apply FC then ReLU (with dropout) and finally softmax(output layer)
    cnn_model.add(Flatten())
    cnn_model.add(Dense(hidden_size, activation='relu'))
    cnn_model.add(Dropout(drop_prob))
    cnn_model.add(Dense(hidden_size, activation='relu'))
    cnn_model.add(Dropout(drop_prob))
    cnn_model.add(Dense(num_classes, activation='softmax'))
    # Initiating the stochastic gradient descent optimiser
    stochastic_gradient_descent = SGD(lr=1e-2, decay=1e-6, momentum=0.9, nesterov=True)
    # Using the stochastic gradient descent optimiser to compile the model with the cross-entropy loss function
    cnn_model.compile(optimizer=stochastic_gradient_descent, loss='categorical_crossentropy')
    return cnn_model
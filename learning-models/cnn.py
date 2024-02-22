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

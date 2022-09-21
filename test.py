# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9RUs86iRIHq0zYeqKS7I8Nyi2hFZbJN
"""

"""from google.colab import drive
drive.mount('/content/drive')"""

#data_path = '/content/drive/MyDrive/PI_DFProject/Data/cats_vs_dogs_small'

import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import sys

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

json_config_path = sys.argv[1]
weights_path = sys.argv[2]
file_path = sys.argv[3]

with open(json_config_path) as json_file:
  json_config = json_file.read()

model = keras.models.model_from_json(json_config)
model.load_weights(weights_path)

image = tf.keras.preprocessing.image.load_img(file_path,target_size =
(150,150,3))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr]) # Convert single image to a batch.

pred = tf.keras.activations.sigmoid(model.predict(input_arr))

if pred < 0.5:
  label = 'cat'
  prob = 1-pred
else:
  label = 'dog'
  prob = pred

print(f'The pet is a {label} with probability {prob}')
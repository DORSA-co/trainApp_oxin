import cv2
import os
from keras.models import load_model
import numpy as np
# Load the model
model = load_model('default_dataset/weights/binary/2023-09-05-16-20-33/binary_model.h5',compile=False)
import tensorflow as tf

model.summary()
x_new = np.ones((8, 256, 256, 1),dtype='uint8')

img = cv2.imread('/home/dorsa/Desktop/milad_dataset/binary/defect_splitted/AXM38739Aup1_56_(0).png',0)
img = img.reshape(1, 256, 256)

# Make predictions
y_pred = model.predict(img)
print(y_pred)
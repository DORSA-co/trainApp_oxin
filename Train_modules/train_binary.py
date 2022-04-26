from tensorflow.python.keras import utils
import models
import dataGenerator
from matplotlib import pyplot as plt
from deep_utils import callbacks
import tensorflow as tf
import numpy as np
import cv2
import os
# import matplotlib.pylab as plt
from matplotlib.pyplot import figure


gpu = tf.config.list_physical_devices('GPU') 
cpu = tf.config.list_physical_devices('CPU') 
tf.config.experimental.set_memory_growth(gpu[0], True)


batch = 8
epochs = 2
fine_tune_epochs=1
dataset_path = 'J:/dataset_oxin/data/binary'
input_size = (128,800,3)
# os.makedirs('models/')          # Creating a directory


data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.1,
                    zoom_range=0.1,
                    horizontal_flip=True,
                    brightness_range=[0.6,1],
                    vertical_flip = True,
                    fill_mode='nearest',
                    )



trainGen, testGen = dataGenerator.get_binarygenerator( dataset_path,
                                                        (128,800),
                                                        'defective',
                                                        'perfect',
                                                        data_gen_args,
                                                        batch_size=batch,
                                                        validation_split=0.2)


model = models.xception_cnn(input_size, num_class=1, mode=models.BINARY)
my_callback = callbacks.CustomCallback('models/checkpoint_bin.h5')


inpt = input('Do you want to train? y/n \n')
if inpt in ['Y','y']:
    history = model.fit(  trainGen,
            steps_per_epoch=trainGen.n//batch + 1,
            epochs=epochs-fine_tune_epochs,
            callbacks=[my_callback ],
            validation_data=testGen,
            validation_steps=testGen.n//batch + 1, 
            initial_epoch=0)
    print(history.history.keys())
    figure(figsize=(8, 6))
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    # model.save('binary_model.h5')
    model.save('models/binary_model.h5')   # Saving model
    #model.load_weights('binary_model.h5')



#_______________________________________________________________________________________________________________
#
#_______________________________________________________________________________________________________________



inpt = input('Do you want to fine tune? y/n \n')
if inpt in ['Y','y']:
    
    model = models.xception_cnn(input_size, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120, weights='models/checkpoint_bin.h5')
    my_callback = callbacks.CustomCallback('models/checkpoint.h5')

    history = model.fit(  trainGen,
                steps_per_epoch=trainGen.n//batch + 1,
                epochs=epochs,
                callbacks=[my_callback ],
                validation_data=testGen,
                validation_steps=testGen.n//batch + 1, 
                initial_epoch=epochs-fine_tune_epochs)

    print(history.history.keys())
    figure(figsize=(8, 6))
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()


    model.save('models/binary_model.h5')
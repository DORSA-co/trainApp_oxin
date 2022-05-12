from tensorflow.python.keras import utils
import Train_modules.models as models
import Train_modules.dataGenerator as dataGenerator
from matplotlib import pyplot as plt
from Train_modules.deep_utils import callbacks
import tensorflow as tf
import numpy as np
import cv2
import os

DEBUG=False

ALGORITHM_NAMES = {'binary': ['Xbc', 'Rbe'], 'localization': ['Rleu', 'Llu', 'uln'], 'classification': ['Xcc', 'Rce']}

if DEBUG:

    gpu = tf.config.list_physical_devices('GPU')
    cpu = tf.config.list_physical_devices('CPU')
    tf.config.experimental.set_memory_growth(gpu[0], True)

data_gen_args = dict(rotation_range=0.2,
                     width_shift_range=0.05,
                     height_shift_range=0.05,
                     shear_range=0.1,
                     zoom_range=0.1,
                     horizontal_flip=True,
                     brightness_range=[0.6, 1],
                     vertical_flip=True,
                     fill_mode='nearest',
                     )


def train_binary(binary_algorithm_name, binary_input_size, binary_input_type, binary_epoch, binary_batch,binary_lr, binary_te, binary_vs, binary_dp, weights_path, api_obj):
    if not binary_input_type:
        trainGen, testGen, train_n, test_n = dataGenerator.get_binarygenerator(binary_dp,
                                                              binary_input_size,
                                                              'defect',
                                                              'perfect',
                                                              data_gen_args,
                                                              batch_size=binary_batch,
                                                              validation_split=binary_vs)
    else:
        trainGen, testGen, train_n, test_n = dataGenerator.get_binarygenerator(binary_dp,
                                                              binary_input_size,
                                                              'defect_splitted',
                                                              'perfect_splitted',
                                                              data_gen_args,
                                                              batch_size=binary_batch,
                                                              validation_split=binary_vs)
    if binary_algorithm_name == ALGORITHM_NAMES['binary'][0]:
        model = models.xception_cnn(input_size=binary_input_size + (3,), lr=binary_lr, num_class=1, mode=models.BINARY)
    elif binary_algorithm_name == ALGORITHM_NAMES['binary'][1]:
        model = models.resnet_cnn(input_size=binary_input_size + (3,), lr=binary_lr, num_class=1, mode=models.BINARY)

    my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint_bin.h5'), model_type='binary', api_obj=api_obj)
    
    model.fit(trainGen,
              steps_per_epoch=train_n// binary_batch + 1,
              epochs=binary_epoch - binary_te,
              callbacks=[my_callback],
              validation_data=testGen,
              validation_steps=test_n // binary_batch + 1,
              initial_epoch=0)

    model.save(os.path.join(weights_path, 'binary_model.h5'))

    if binary_algorithm_name == ALGORITHM_NAMES['binary'][0]:
        model = models.xception_cnn(binary_input_size + (3,), lr=binary_lr, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120,
                                    weights=os.path.join(weights_path, 'checkpoint_bin.h5'))

    if binary_algorithm_name == ALGORITHM_NAMES['binary'][1]:
        model = models.resnet_cnn(binary_input_size + (3,), lr=binary_lr, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120,
                                    weights=os.path.join(weights_path, 'checkpoint_bin.h5'))

    my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint.h5'), model_type='binary', api_obj=api_obj)

    model.fit(trainGen,
              steps_per_epoch=train_n // binary_batch + 1,
              epochs=binary_epoch,
              callbacks=[my_callback],
              validation_data=testGen,
              validation_steps=test_n // binary_batch + 1,
              initial_epoch=binary_epoch - binary_te)

    model.save(os.path.join(weights_path, 'binary_model.h5'))


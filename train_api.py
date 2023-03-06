import torch
from IPython.display import Image 
import os 
import random
import shutil
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import yolov5

from tensorflow.python.keras import utils
import Train_modules.models as models
import Train_modules.dataGenerator as dataGenerator
from matplotlib import pyplot as plt
from Train_modules.deep_utils import callbacks
import tensorflow as tf
import numpy as np
import cv2
import os
import texts
from Train_modules.splitDataset import split_unet_dataset, split_yolo_dataset

from backend import binary_model_funcs, date_funcs, localization_model_funcs, yolo_model_funcs
import segmentation_models as sm

from Train_modules.train_yolo import run

sm.set_framework("tf.keras")
sm.framework()

DEBUG=False
SHAMSI_DATE = False

ALGORITHM_NAMES = {'binary': ['Xbc', 'Rbe'], 'localization': ['Ulnim', 'Ulnpr'], 'classification': ['Xcc', 'Rce'], 'yolo': ['5n', '5s', '5m', '5l', '5x']}
ALGORITHM_CREATOR={'Xbc':models.xception_cnn,'Rbc':models.resnet_cnn,'Blu':models.base_unet,'Rleu':models.resnet_unet,'Llu':models.low_unet,'uln':models.unet
,'Xcc':models.xception_cnn,'Rce':models.resnet_cnn}

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


data_gen_args_2 = dict(rotation_range=15,
                    width_shift_range=0.1,
                    height_shift_range=0.1,
                    shear_range=0.05,
                    zoom_range=0.1,
                    horizontal_flip=True,
                    fill_mode='constant',            
                    )


def train_binary(binary_algorithm_name, binary_input_size, binary_input_type, binary_epoch, binary_batch, binary_lr, binary_te, binary_vs, binary_gpu, binary_dp, weights_path, api_obj):
    """Create and fit binary model

    :param binary_algorithm_name: Name of binary algorithm.
    :type binary_algorithm_name: str
    :param binary_input_size: Shape of input image.
    :type binary_input_size: tuple
    :param binary_input_type: If true, images were splitted. Otherwise images must be resized to a given size.
    :type binary_input_type: bool
    :param binary_epoch: Total number of epochs.
    :type binary_epoch: int
    :param binary_batch: Batch size of images.
    :type binary_batch: int
    :param binary_lr:  Learning rate of model.
    :type binary_lr: float
    :param binary_te: Number of tunning epochs.
    :type binary_te: int
    :param binary_vs: Validation split percentage
    :type binary_vs: float
    :param binary_dp: List of dataset paths
    :type binary_dp: list
    :param weights_path: Path where weights of model should save.
    :type weights_path: str
    :param api_obj: An instance of main API class.
    :type api_obj: api.API
    :return: Dictionary of model parameters and metrics.
    :rtype: dict
    """

    try:
        if binary_gpu >= 0:
            tf.config.run_functions_eagerly(True)
            # GPU config
            gpu = tf.config.list_physical_devices("GPU")
            tf.config.experimental.set_memory_growth(gpu[binary_gpu], True)
            tf.config.experimental.set_visible_devices(gpu[binary_gpu], "GPU")
        else:
            cpu = tf.config.list_physical_devices("CPU")
            # tf.config.experimental.set_memory_growth(cpu[0], True)
            tf.config.experimental.set_visible_devices(cpu[0], "CPU")
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SET_PROCESSOR']['en'])
    except:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SET_PROCESSOR_FAILED']['en'], level=5)
        # api_obj.ui.set_warning(texts.ERRORS['CREATE_BWPATH_FAILED'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['SET_PROCESSOR_FAILED'][api_obj.language], 'train', 3))

    # Create weights path
    weights_path = os.path.join(weights_path, date_funcs.get_datetime(persian=SHAMSI_DATE, folder_path=True))
    try:
        if not os.path.exists(weights_path):
            os.makedirs(weights_path)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_BWPATH']['en'] + weights_path)
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_BWPATH_FAILED']['en'] + weights_path, level=5)
        return (False, (texts.ERRORS['CREATE_BWPATH_FAILED'][api_obj.language], 'train', 3))

    # Get train and test generators
    try:
        if not binary_input_type:
            trainGen, testGen = dataGenerator.get_binarygenerator(binary_dp,
                                                                binary_input_size,
                                                                'defect',
                                                                'perfect',
                                                                data_gen_args,
                                                                api_obj,
                                                                batch_size=binary_batch,
                                                                validation_split=binary_vs)
        else:
            trainGen, testGen = dataGenerator.get_binarygenerator(binary_dp,
                                                                binary_input_size,
                                                                'defect_splitted',
                                                                'perfect_splitted',
                                                                data_gen_args,
                                                                api_obj,
                                                                batch_size=binary_batch,
                                                                validation_split=binary_vs)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_BINARY_GEN']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_BINARY_GEN_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['CREATE_BINARY_GEN_FAILED'][api_obj.language], 'train', 3))

    # Create models
    try:
        if binary_algorithm_name == ALGORITHM_NAMES['binary'][0]:
            model = models.xception_cnn(input_size=binary_input_size + (3,), learning_rate=binary_lr, num_class=1, mode=models.BINARY)
        elif binary_algorithm_name == ALGORITHM_NAMES['binary'][1]:
            model = models.resnet_cnn(input_size=binary_input_size + (3,), learning_rate=binary_lr, num_class=1, mode=models.BINARY)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_MODEL']['en'].format(binary_algorithm_name))
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_MODEL_FAILED']['en'].format(binary_algorithm_name), level=5)
        # api_obj.ui.set_warning(texts.ERRORS['CREATE_MODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', level=3)
        return (False, (texts.ERRORS['CREATE_MODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', 3))

    # Create callback
    try:
        my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint_bin.h5'), model_type='binary', api_obj=api_obj)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CALLBACK_CREATED']['en'])
    except:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CALLBACK_CREATE_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['CALLBACK_CREATE_FAILED'][api_obj.language], 'train', 3))


    spe = (trainGen.n // binary_batch + 1) if ((trainGen.n//binary_batch) != (trainGen.n / binary_batch)) else (trainGen.n // binary_batch)
    vspe = (testGen.n // binary_batch + 1) if ((testGen.n//binary_batch) != (testGen.n / binary_batch)) else (testGen.n // binary_batch)

    if spe < 1 or vspe < 1:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['low_data']['en'], level=5)
        return (False, (texts.ERRORS['low_data'][api_obj.language], 'train', 3))
    
    # Fit model
    try:
        history = model.fit(trainGen,
                steps_per_epoch=spe,
                epochs=binary_epoch - binary_te,
                callbacks=[my_callback],
                validation_data=testGen,
                validation_steps=vspe,
                initial_epoch=0)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['FIT_MODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['FIT_MODEL_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['FIT_MODEL_FAILED'][api_obj.language], 'train', 3))
    # Save weights
    try:
        model.save(os.path.join(weights_path, 'binary_model.h5'))
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_BMODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_BMODEL_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['SAVE_BMODEL_FAILED'][api_obj.language], 'train', 3))

    if binary_te > 0:
        # Create model for fine tunning
        if binary_algorithm_name == ALGORITHM_NAMES['binary'][0]:
            try:
                model = models.xception_cnn(binary_input_size + (3,), learning_rate=binary_lr, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120,
                                            weights=os.path.join(weights_path, 'checkpoint_bin.h5'))
                api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_FTMODEL']['en'].format(binary_algorithm_name))
            except Exception as e:
                api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_FTMODEL_FAILED']['en'].format(binary_algorithm_name), level=5)
                return (False, (texts.ERRORS['CREATE_FTMODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', 3))

        if binary_algorithm_name == ALGORITHM_NAMES['binary'][1]:
            try:
                model = models.resnet_cnn(binary_input_size + (3,), learning_rate=binary_lr, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120,
                                            weights=os.path.join(weights_path, 'checkpoint_bin.h5'))
                api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_FTMODEL']['en'].format(binary_algorithm_name))
            except Exception as e:
                api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_FTMODEL_FAILED']['en'].format(binary_algorithm_name), level=5)
                return (False, (texts.ERRORS['CREATE_FTMODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', 3))

        # Create call back
        my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint.h5'), model_type='binary', api_obj=api_obj)

        # Fit model for fine tunning
        try:
            history = model.fit(trainGen,
                    steps_per_epoch=spe,
                    epochs=binary_epoch,
                    callbacks=[my_callback],
                    validation_data=testGen,
                    validation_steps=vspe,
                    initial_epoch=binary_epoch - binary_te)
            api_obj.ui.logger.create_new_log(message=texts.MESSEGES['FIT_FTMODEL']['en'])
        except Exception as e:
            api_obj.ui.logger.create_new_log(message=texts.ERRORS['FIT_FTMODEL_FAILED']['en'], level=5)
            return (False, (texts.ERRORS['FIT_FTMODEL_FAILED'][api_obj.language], 'train', 3))
        
        try:
            model.save(os.path.join(weights_path, 'binary_model.h5'))
            api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_FTBMODEL']['en'])
        except Exception as e:
            api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_FTBMODEL_FAILED']['en'], level=5)
            return (False, (texts.ERRORS['SAVE_FTBMODEL_FAILED'][api_obj.language], 'train', 3))
    
    try:
        binary_algorithm_name = ALGORITHM_NAMES['binary'].index(binary_algorithm_name)
    except:
        binary_algorithm_name = -1

    return (True, create_binary_model_record_dict([binary_algorithm_name,
                                            '('+str(binary_input_size[0])+','+ str(binary_input_size[1])+')', 
                                            binary_input_type,
                                            binary_epoch,
                                            binary_te,
                                            binary_batch,
                                            binary_lr, binary_vs,
                                            history.history['loss'][-1],
                                            history.history['accuracy'][-1],
                                            history.history['Precision'][-1],
                                            history.history['Recall'][-1],
                                            history.history['val_loss'][-1],
                                            history.history['val_accuracy'][-1],
                                            history.history['val_Precision'][-1],
                                            history.history['val_Recall'][-1],
                                            str(binary_dp),
                                            weights_path,
                                            date_funcs.get_date(persian=SHAMSI_DATE)]))


def create_binary_model_record_dict(records):
    """Convert binary model parameters and metrics list to dictionary

    :param records: Binary model parameters and metrics list of the form: ['algo_name', 'input_size', 'input_type', 'epochs', 'tuning_epochs', 
    'batch_size', 'lr', 'split_ratio', 'loss', 'accuracy', 'precision_', 'recall', 'val_loss', 'val_accuracy', 'val_precision', 
    'val_recall', 'dataset_pathes', 'weights_path', 'date_']
    :type records: list
    :return: Binary model parameters dictionary
    :rtype: dict
    """
    model_records = {}
    for i, header_db in enumerate(binary_model_funcs.binary_headers_db):
        model_records[header_db] = records[i]
    
    return model_records


def train_localization(loc_algorithm_name, loc_pretrain_path, loc_input_size, loc_input_type, loc_epoch, loc_batch, loc_lr, loc_vs, loc_gpu, loc_dp, weights_path, api_obj):
    """Create and fit localization model

    :param loc_algorithm_name: Name of localization algorithm.
    :type loc_algorithm_name: str
    :param loc_input_size: Shape of input image.
    :type loc_input_size: tuple
    :param loc_input_type: If true, images were splitted. Otherwise images must be resized to a given size.
    :type loc_input_type: bool
    :param loc_epoch: Total number of epochs.
    :type loc_epoch: int
    :param loc_batch: Batch size of images.
    :type loc_batch: int
    :param loc_lr:  Learning rate of model.
    :type loc_lr: float
    :param loc_vs: Validation split percentage
    :type loc_vs: float
    :param loc_dp: List of dataset paths
    :type loc_dp: list
    :param weights_path: Path where weights of model should save.
    :type weights_path: str
    :param api_obj: An instance of main API class.
    :type api_obj: api.API
    :return: Dictionary of model parameters and metrics.
    :rtype: dict
    """

    try:
        if loc_gpu >= 0:
            tf.config.run_functions_eagerly(True)
            # GPU config
            gpu = tf.config.list_physical_devices("GPU")
            tf.config.experimental.set_memory_growth(gpu[loc_gpu], True)
            tf.config.experimental.set_visible_devices(gpu[loc_gpu], "GPU")
        else:
            cpu = tf.config.list_physical_devices("CPU")
            # tf.config.experimental.set_memory_growth(cpu[0], True)
            tf.config.experimental.set_visible_devices(cpu[0], "CPU")
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SET_PROCESSOR']['en'])
    except:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SET_PROCESSOR_FAILED']['en'], level=5)
        # api_obj.ui.set_warning(texts.ERRORS['CREATE_BWPATH_FAILED'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['SET_PROCESSOR_FAILED'][api_obj.language], 'l_train', 3))

    # Create weights path
    weights_path = os.path.join(weights_path, date_funcs.get_datetime(persian=SHAMSI_DATE, folder_path=True))
    try:
        if not os.path.exists(weights_path):
            os.makedirs(weights_path)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_LWPATH']['en'] + weights_path)
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_LWPATH_FAILED']['en'] + weights_path, level=5)
        return (False, (texts.ERRORS['CREATE_LWPATH_FAILED'][api_obj.language], 'l_train', 3))

    # Split datasets into train and test
    try:
        if not loc_input_type:
            train_path, test_path, train_data_count, test_data_count = split_unet_dataset(paths=loc_dp, api_obj=api_obj, img_folder='image', label_folder='label', mulit_mask_class=False, split=loc_vs)
        else:
            train_path, test_path, train_data_count, test_data_count = split_unet_dataset(paths=loc_dp, api_obj=api_obj, img_folder='image_splitted', label_folder='label_splitted', mulit_mask_class=False, split=loc_vs)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['dataset_splitted']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['dataset_splitted_failed']['en'], level=5)
        return (False, (texts.ERRORS['dataset_splitted_failed'][api_obj.language], 'l_train', 3))

    # Get train and test generators
    try:
        preprocess_input = sm.get_preprocessing("efficientnetb2")
        train_dataloader = dataGenerator.CustomDataGen(
            path=train_path,
            image_folder='image',
            mask_folder='label',
            batch_size=loc_batch,
            transforms=preprocess_input,
            input_size=loc_input_size,
        )
        val_dataloader = dataGenerator.CustomDataGen(
            path=test_path,
            image_folder='image',
            mask_folder='label',
            batch_size=loc_batch,
            transforms=preprocess_input,
            input_size=loc_input_size,
        )
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_LOC_GEN']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_LOC_GEN_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['CREATE_LOC_GEN_FAILED'][api_obj.language], 'l_train', 3))

    # Create models
    try:
        if loc_algorithm_name == ALGORITHM_NAMES['localization'][0]:
            model = models.unet_model(loc_input_size + (3,), learning_rate=loc_lr, num_class=1, mode=models.BINARY)
        elif loc_algorithm_name == ALGORITHM_NAMES['localization'][1]:
            model = models.unet_model(loc_input_size + (3,), learning_rate=loc_lr, num_class=1, mode=models.BINARY, weights_path=loc_pretrain_path)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_MODEL']['en'].format(loc_algorithm_name))
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_MODEL_FAILED']['en'].format(loc_algorithm_name), level=5)
        return (False, (texts.ERRORS['CREATE_MODEL_FAILED'][api_obj.language].format(loc_algorithm_name), 'l_train', 3))
    
    # Create call back
    try:
        my_callback = callbacks.CustomCallback(None, model_type='localization', api_obj=api_obj)
        modelCheckpoint = tf.keras.callbacks.ModelCheckpoint(
            os.path.join(weights_path, 'localization_model.h5'),
            save_best_only=True,
            save_weights_only=False,
            verbose=1,
            mode="min",
            monitor="val_loss",
        )
        earlyStoppingCallback = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=20, mode="min", verbose=1
        )
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CALLBACK_CREATED']['en'])
    except:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CALLBACK_CREATE_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['CALLBACK_CREATE_FAILED'][api_obj.language], 'l_train', 3))

    spe = (train_data_count // loc_batch + 1) if ((train_data_count//loc_batch) != (train_data_count / loc_batch)) else (train_data_count // loc_batch)
    vspe = (test_data_count // loc_batch + 1) if ((test_data_count//loc_batch) != (test_data_count / loc_batch)) else (test_data_count // loc_batch)

    if spe < 1 or vspe < 1:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['low_data']['en'], level=5)
        return (False, (texts.ERRORS['low_data'][api_obj.language], 'l_train', 3))

    # Fit model
    try:
        history = model.train(
            epochs=loc_epoch,
            callbacks=[my_callback, modelCheckpoint, earlyStoppingCallback],
            train_data_loader=train_dataloader,
            steps_per_epoch=spe,
            validation_data_loader=val_dataloader,
            validation_steps=vspe,
            batch_size=loc_batch,
        )
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['FIT_MODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['FIT_MODEL_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['FIT_MODEL_FAILED'][api_obj.language], 'l_train', 3))
    
    # Save weights
    if os.path.exists(os.path.join(weights_path, 'localization_model.h5')):
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_LMODEL']['en'])
    else:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_LMODEL_FAILED']['en'], level=3)
        return (False, (texts.ERRORS['SAVE_LMODEL_FAILED'][api_obj.language], 'l_train', 3))

    try:
        loc_algorithm_name = ALGORITHM_NAMES['localization'].index(loc_algorithm_name)
    except:
        loc_algorithm_name = -1
    
    return (True, create_localization_model_record_dict([loc_algorithm_name,
                                    loc_pretrain_path,
                                    '('+str(loc_input_size[0])+','+ str(loc_input_size[1])+')', 
                                    loc_input_type,
                                    loc_epoch,
                                    loc_batch,
                                    loc_lr, loc_vs,
                                    history.history['loss'][-1],
                                    history.history['accuracy'][-1],
                                    history.history['iou_score'][-1],
                                    history.history['f1-score'][-1],
                                    history.history['val_loss'][-1],
                                    history.history['val_accuracy'][-1],
                                    history.history['val_iou_score'][-1],
                                    history.history['val_f1-score'][-1],
                                    str(loc_dp),
                                    weights_path,
                                    date_funcs.get_date(persian=SHAMSI_DATE)]))


def create_localization_model_record_dict(records):
    """Convert localization model parameters and metrics list to dictionary

    :param records: Localization model parameters and metrics list of the form: ['algo_name', 'input_size', 'input_type', 'epochs', 
    'batch_size', 'lr', 'split_ratio', 'loss', 'accuracy', 'precision_', 'recall', 'val_loss', 'val_accuracy', 'val_precision', 
    'val_recall', 'dataset_pathes', 'weights_path', 'date_']
    :type records: list
    :return: Localization model parameters dictionary
    :rtype: dict
    """
    model_records = {}
    for i, header_db in enumerate(localization_model_funcs.localization_headers_db):
        model_records[header_db] = records[i]
    return model_records


def train_yolo(y_algorithm_name, y_input_size, y_input_type, y_epoch, y_batch, y_vs, y_gpu, y_dp, weights_path, class_name_to_id_mapping, api_obj):
    # try:
    #     if y_gpu > 0:
    #         device = torch.device('cuda:{}'.format())
    #         torch.cuda.set_device(device)
    #     api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SET_PROCESSOR']['en'])
    # except:
    #     api_obj.ui.logger.create_new_log(message=texts.ERRORS['SET_PROCESSOR_FAILED']['en'], level=5)
    #     return (False, (texts.ERRORS['SET_PROCESSOR_FAILED'][api_obj.language], 'y_train', 3))

    # Create weights path
    # weights_path = os.path.join(weights_path, date_funcs.get_datetime(persian=SHAMSI_DATE, folder_path=True))
    # try:
    #     if not os.path.exists(weights_path):
    #         os.makedirs(weights_path)
    #     api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_YWPATH']['en'] + weights_path)
    # except Exception as e:
    #     api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_YWPATH_FAILED']['en'] + weights_path, level=5)
    #     return (False, (texts.ERRORS['CREATE_YWPATH_FAILED'][api_obj.language], 'y_train', 3))

    try:
        if not y_input_type:
            train_images_path, val_images_path = split_yolo_dataset(paths=y_dp, api_obj=api_obj, img_folder='image', label_folder='annotations', split=y_vs)
        else:
            train_images_path, val_images_path = split_yolo_dataset(paths=y_dp, api_obj=api_obj, img_folder='image_splitted', label_folder='annotations', split=y_vs)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['dataset_splitted']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['dataset_splitted_failed']['en'], level=5)
        return (False, (texts.ERRORS['dataset_splitted_failed'][api_obj.language], 'y_train', 3))

    try:
        path = dataGenerator.create_yolo_yaml_file(train_images_path, val_images_path, class_name_to_id_mapping)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_Y_GEN']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_Y_GEN_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['CREATE_Y_GEN_FAILED'][api_obj.language], 'y_train', 3))
    
    # Create callback
    try:
        my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint_bin.h5'), model_type='yolo', api_obj=api_obj)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CALLBACK_CREATED']['en'])
    except:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CALLBACK_CREATE_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['CALLBACK_CREATE_FAILED'][api_obj.language], 'y_train', 3))
    
    if y_gpu > 0:
        y_gpu = y_gpu
    else:
        y_gpu = 'cpu'

    try:
        date = date_funcs.get_datetime(persian=SHAMSI_DATE, folder_path=True)
        results = run(data=path,
            my_callback=my_callback,
            epochs=y_epoch, 
            batch_size = y_batch,
            imgsz = y_input_size[0], 
            device=y_gpu,
            cfg='yolov{}.yaml'.format(y_algorithm_name),
            weights='models/localization_and_classification/yolov{}.pt'.format(y_algorithm_name),
            # weights = '',
            project=weights_path,
            name=date,
            noplots=True,
        )
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['FIT_MODEL']['en'])
    except:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['FIT_MODEL_FAILED']['en'], level=5)
        return (False, (texts.ERRORS['FIT_MODEL_FAILED'][api_obj.language], 'y_train', 3))

    # Save weights
    if os.path.exists(os.path.join(weights_path, date, 'best.pt')) and \
        os.path.exists(os.path.join(weights_path, date, 'last.pt')):
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_YMODEL']['en'])
    else:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_YMODEL_FAILED']['en'], level=3)
        return (False, (texts.ERRORS['SAVE_YMODEL_FAILED'][api_obj.language], 'y_train', 3))

    try:
        y_algorithm_name = ALGORITHM_NAMES['yolo'].index(y_algorithm_name)
    except:
        y_algorithm_name = -1
    return (True, create_yolo_model_record_dict([y_algorithm_name,
                                    '('+str(y_input_size[0])+','+ str(y_input_size[1])+')', 
                                    y_input_type,
                                    y_epoch,
                                    y_batch,
                                    y_vs,
                                    results['train/box_loss'].item(),
                                    results['train/obj_loss'].item(),
                                    results['train/cls_loss'].item(),
                                    results['metrics/precision'].item(),
                                    results['metrics/recall'].item(),
                                    results['metrics/mAP_0.5'].item(),
                                    results['metrics/mAP_0.5:0.95'].item(),
                                    results['val/box_loss'],
                                    results['val/obj_loss'],
                                    results['val/cls_loss'],
                                    str(y_dp),
                                    os.path.join(weights_path, date),
                                    date_funcs.get_date(persian=SHAMSI_DATE),
                                    ]))


def create_yolo_model_record_dict(records):
    """Convert yolo model parameters and metrics list to dictionary

    :param records: yolo model parameters and metrics list of the form: ['algo_name','input_size','input_type','epochs','batch_size', 
    'split_ratio','dataset_pathes','weights_path',  'date_''box_loss', 'obj_loss', 'cls_loss','val_precision','val_recall',
    'val_mAP_0.5','val_mAP_0.5:0.95','val_box_loss','val_obj_loss','val_cls_loss']
    :type records: list
    :return: yolo model parameters dictionary
    :rtype: dict
    """
    model_records = {}
    for i, header_db in enumerate(yolo_model_funcs.yolo_headers_db):
        model_records[header_db] = records[i]
    return model_records
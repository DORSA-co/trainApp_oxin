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
from Train_modules.splitDataset import split_unet_dataset

from backend import binary_model_funcs, date_funcs, localization_model_funcs

DEBUG=False

ALGORITHM_NAMES = {'binary': ['Xbc', 'Rbe'], 'localization': ['Blu', 'Rleu', 'Llu', 'uln'], 'classification': ['Xcc', 'Rce']}
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
    weights_path = os.path.join(weights_path, date_funcs.get_datetime(persian=True, folder_path=True))
    try:
        if not os.path.exists(weights_path):
            os.makedirs(weights_path)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_BWPATH']['en'] + weights_path)
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_BWPATH_FAILED']['en'] + weights_path, level=5)
        # api_obj.ui.set_warning(texts.ERRORS['CREATE_BWPATH_FAILED'][api_obj.language], 'train', level=3)
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
        # api_obj.ui.set_warning(texts.ERRORS['CREATE_BINARY_GEN_FAILED'][api_obj.language], 'train', level=3)
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
    my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint_bin.h5'), model_type='binary', api_obj=api_obj)

    spe = (trainGen.n // binary_batch + 1) if ((trainGen.n//8) != (trainGen.n / 8)) else (trainGen.n // binary_batch)
    vspe = (testGen.n // binary_batch + 1) if ((testGen.n//8) != (testGen.n / 8)) else (testGen.n // binary_batch)

    if spe < 1 or vspe < 1:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['low_data']['en'], level=5)
        # api_obj.ui.set_warning(texts.ERRORS['low_data'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['low_data'][api_obj.language], 'train', 3))
    
    # Fit model
    try:
        model.fit(trainGen,
                steps_per_epoch=spe,
                epochs=binary_epoch - binary_te,
                callbacks=[my_callback],
                validation_data=testGen,
                validation_steps=vspe,
                initial_epoch=0)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['FIT_MODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['FIT_MODEL_FAILED']['en'], level=5)
        # api_obj.ui.set_warning(texts.ERRORS['FIT_MODEL_FAILED'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['FIT_MODEL_FAILED'][api_obj.language], 'train', 3))

    # Save weights
    try:
        model.save(os.path.join(weights_path, 'binary_model.h5'))
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_BMODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_BMODEL_FAILED']['en'], level=5)
        # api_obj.ui.set_warning(texts.ERRORS['SAVE_BMODEL_FAILED'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['SAVE_BMODEL_FAILED'][api_obj.language], 'train', 3))

    # Create model for fine tunning
    if binary_algorithm_name == ALGORITHM_NAMES['binary'][0]:
        try:
            model = models.xception_cnn(binary_input_size + (3,), learning_rate=binary_lr, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120,
                                        weights=os.path.join(weights_path, 'checkpoint_bin.h5'))
            api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_FTMODEL']['en'].format(binary_algorithm_name))
        except Exception as e:
            api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_FTMODEL_FAILED']['en'].format(binary_algorithm_name), level=5)
            # api_obj.ui.set_warning(texts.ERRORS['CREATE_FTMODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', level=3)
            return (False, (texts.ERRORS['CREATE_FTMODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', 3))

    if binary_algorithm_name == ALGORITHM_NAMES['binary'][1]:
        try:
            model = models.resnet_cnn(binary_input_size + (3,), learning_rate=binary_lr, num_class=1, mode=models.CATEGORICAL, fine_tune_layer=120,
                                        weights=os.path.join(weights_path, 'checkpoint_bin.h5'))
            api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_FTMODEL']['en'].format(binary_algorithm_name))
        except Exception as e:
            api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_FTMODEL_FAILED']['en'].format(binary_algorithm_name), level=5)
            # api_obj.ui.set_warning(texts.ERRORS['CREATE_FTMODEL_FAILED'][api_obj.language].format(binary_algorithm_name), 'train', level=3)
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
        # api_obj.ui.set_warning(texts.ERRORS['FIT_FTMODEL_FAILED'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['FIT_FTMODEL_FAILED'][api_obj.language], 'train', 3))
       
    try:
        model.save(os.path.join(weights_path, 'binary_model.h5'))
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_FTBMODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_FTBMODEL_FAILED']['en'], level=5)
        # api_obj.ui.set_warning(texts.ERRORS['SAVE_FTBMODEL_FAILED'][api_obj.language], 'train', level=3)
        return (False, (texts.ERRORS['SAVE_FTBMODEL_FAILED'][api_obj.language], 'train', 3))

    ##print('model history:', history.history)
    
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
                                            history.history['loss'][0],
                                            history.history['accuracy'][0],
                                            history.history['Precision'][0],
                                            history.history['Recall'][0],
                                            history.history['val_loss'][0],
                                            history.history['val_accuracy'][0],
                                            history.history['val_Precision'][0],
                                            history.history['val_Recall'][0],
                                            str(binary_dp),
                                            weights_path,
                                            date_funcs.get_date(persian=True)]))


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


def train_localization(loc_algorithm_name, loc_input_size, loc_input_type, loc_epoch, loc_batch, loc_lr, loc_vs, loc_dp, weights_path, api_obj):
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

    # Create weights path
    weights_path = os.path.join(weights_path, date_funcs.get_datetime(persian=True, folder_path=True))
    try:
        if not os.path.exists(weights_path):
            os.makedirs(weights_path)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_LWPATH']['en'] + weights_path)
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_LWPATH_FAILED']['en'] + weights_path, level=5)
        api_obj.ui.set_warning(texts.ERRORS['CREATE_LWPATH_FAILED'][api_obj.language], 'l_train', level=3)
        return

    # Split datasets into train and test
    try:
        if not loc_input_type:
            train_path, test_path, train_data_count, test_data_count = split_unet_dataset(paths=loc_dp, img_folder='image', label_folder='label', mulit_mask_class=False, split=loc_vs)
        else:
            train_path, test_path, train_data_count, test_data_count = split_unet_dataset(paths=loc_dp, img_folder='image_splitted', label_folder='label_splitted', mulit_mask_class=False, split=loc_vs)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['dataset_splitted']['en'] + weights_path)
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['dataset_splitted_failed']['en'] + weights_path, level=5)
        api_obj.ui.set_warning(texts.ERRORS['dataset_splitted_failed'][api_obj.language], 'l_train', level=3)
        return

    # Get train and test generators
    try:
        trainGen = dataGenerator.maskGenerator(train_path, 'image','label', data_gen_args_2, target_size=loc_input_size, batch_size=loc_batch)
        testGen = dataGenerator.maskGenerator(test_path , 'image','label', data_gen_args_2, target_size=loc_input_size, batch_size=loc_batch)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_LOC_GEN']['en'] + weights_path)
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_LOC_GEN_FAILED']['en'] + weights_path, level=5)
        api_obj.ui.set_warning(texts.ERRORS['CREATE_LOC_GEN_FAILED'][api_obj.language], 'l_train', level=3)
        return

    # Create models
    try:
        if loc_algorithm_name == ALGORITHM_NAMES['localization'][0]:
            model = models.base_unet(loc_input_size + (1,), learning_rate=loc_lr, num_class=1, mode=models.BINARY)
        elif loc_algorithm_name == ALGORITHM_NAMES['localization'][1]:
            model = models.resnet_unet(loc_input_size + (1,), learning_rate=loc_lr, num_class=1, mode=models.BINARY)
        elif loc_algorithm_name == ALGORITHM_NAMES['localization'][2]:
            model = models.low_unet(loc_input_size + (1,), learning_rate=loc_lr, num_class=1, mode=models.BINARY)
        elif loc_algorithm_name == ALGORITHM_NAMES['localization'][3]:
            model = models.unet(loc_input_size + (1,), learning_rate=loc_lr, num_class=1, mode=models.BINARY)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CREATE_MODEL']['en'].format(loc_algorithm_name))
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['CREATE_MODEL_FAILED']['en'].format(loc_algorithm_name), level=5)
        api_obj.ui.set_warning(texts.ERRORS['CREATE_MODEL_FAILED'][api_obj.language].format(loc_algorithm_name), 'l_train', level=3)
        return
        
    # Create call back
    my_callback = callbacks.CustomCallback(os.path.join(weights_path, 'checkpoint.h5'), model_type='localization', api_obj=api_obj)

    spe = (train_data_count // loc_batch + 1) if ((train_data_count//loc_batch) != (train_data_count / loc_batch)) else (train_data_count // loc_batch)
    vspe = (test_data_count // loc_batch + 1) if ((test_data_count//loc_batch) != (test_data_count / loc_batch)) else (test_data_count // loc_batch)

    # Fit model
    try:
        history = model.fit(trainGen,
                steps_per_epoch=spe,
                epochs=loc_epoch,
                callbacks=[my_callback],
                validation_data=testGen,
                validation_steps=vspe, 
                initial_epoch=0)
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['FIT_MODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['FIT_MODEL_FAILED']['en'], level=5)
        api_obj.ui.set_warning(texts.ERRORS['FIT_MODEL_FAILED'][api_obj.language], 'l_train', level=3)
        return

    # Save weights
    try:
        model.save(os.path.join(weights_path, 'localization_model.h5'))
        api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_LMODEL']['en'])
    except Exception as e:
        api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_LMODEL_FAILED']['en'], level=5)
        api_obj.ui.set_warning(texts.ERRORS['SAVE_LMODEL_FAILED'][api_obj.language], 'l_train', level=3)
        return

    try:
        loc_algorithm_name = ALGORITHM_NAMES['localization'].index(loc_algorithm_name)
    except:
        loc_algorithm_name = -1
    
    return create_localization_model_record_dict([loc_algorithm_name,
                                    '('+str(loc_input_size[0])+','+ str(loc_input_size[1])+')', 
                                    loc_input_type,
                                    loc_epoch,
                                    loc_batch,
                                    loc_lr, loc_vs,
                                    history.history['loss'][0],
                                    history.history['accuracy'][0],
                                    history.history['Precision'][0],
                                    history.history['Recall'][0],
                                    history.history['val_loss'][0],
                                    history.history['val_accuracy'][0],
                                    history.history['val_Precision'][0],
                                    history.history['val_Recall'][0],
                                    str(loc_dp),
                                    weights_path,
                                    date_funcs.get_date(persian=True)])


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

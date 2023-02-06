from cv2 import log
from tensorflow import keras
import os
from backend import logging_funcs
import texts

class CustomCallback(keras.callbacks.Callback):
    """This is a customized callback class that inherits from keras callbacks.callback class 
    and used to save models weights and update train charts on each epoch.

    :param out_path: Path where model weights save there.
    :type out_path: str
    :param model_type: Type of model ('binary', 'localization' or 'classification').
    :type model_type: str
    :param api_obj: An instance of main API class.
    :type api_obj: class API
    """
    def __init__(self, out_path, model_type, api_obj):
        """Constructor method.
        """
        # Set class attributes
        self.out_path = out_path
        self.model_type = model_type
        self.api_obj = api_obj

        # logger object
        self.api_obj.ui.logger.create_new_log(message=texts.MESSEGES['CCALLBACK_CREATED']['en'])

    def on_epoch_end(self, epoch, logs=None):
        """Called at the end of each epoch and save model weights and update train charts.

        :param epoch: Epoch number that ended just now.
        :type epoch: int
        :param logs: The logs dictionary that contain keys for quantities relevant to the current epoch, defaults to None, defaults to None.
        :type logs: dict, optional
        """
        # Set to UI
        epoch += 1
        if self.model_type == 'binary':
            # Update bianry train charts
            try:
                self.api_obj.assign_new_value_to_b_chart(last_epoch=epoch, logs=logs)
                self.api_obj.ui.logger.create_new_log(message=texts.MESSEGES['UPDATE_BCHART']['en'].format(epoch))
            except Exception as e:
                self.api_obj.ui.logger.create_new_log(message=texts.ERRORS['UPDATE_BCHART_FAILED']['en'].format(epoch), level=5)
                self.api_obj.ui.set_warning(texts.ERRORS['UPDATE_BCHART_FAILED'][self.api_obj.language].format(epoch), 'train', level=3)

            # Save model weights to given address
            try:
                self.model.save( self.out_path)
                self.api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_BMODEL_EPOCH']['en'].format(epoch))
            except Exception as e:
                self.api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_BMODEL_EPOCH_FAILED']['en'].format(epoch), level=5)
                self.api_obj.ui.set_warning(texts.ERRORS['SAVE_BMODEL_EPOCH_FAILED'][self.api_obj.language].format(epoch), 'train', level=3)

        if self.model_type == 'localization':
            # Update localization train charts
            try:
                self.api_obj.assign_new_value_to_l_chart(last_epoch=epoch, logs=logs)
                self.api_obj.ui.logger.create_new_log(message=texts.MESSEGES['UPDATE_LCHART']['en'].format(epoch))
            except Exception as e:
                self.api_obj.ui.logger.create_new_log(message=texts.ERRORS['UPDATE_LCHART_FAILED']['en'].format(epoch), level=5)
                self.api_obj.ui.set_warning(texts.ERRORS['UPDATE_LCHART_FAILED'][self.api_obj.language].format(epoch), 'l_train', level=3)

             # Save model weights to given address
            try:
                self.model.save( self.out_path)
                self.api_obj.ui.logger.create_new_log(message=texts.MESSEGES['SAVE_LMODEL_EPOCH']['en'].format(epoch))
            except Exception as e:
                self.api_obj.ui.logger.create_new_log(message=texts.ERRORS['SAVE_LMODEL_EPOCH_FAILED']['en'].format(epoch), level=5)
                self.api_obj.ui.set_warning(texts.ERRORS['SAVE_LMODEL_EPOCH_FAILED'][self.api_obj.language].format(epoch), 'l_train', level=3)
    

        # keys = list(logs.keys())
        # values = list(logs.values())
        # #print("\nEnd epoch {} of training; got log keys: {} got log values {}\n".format(epoch, keys, values))



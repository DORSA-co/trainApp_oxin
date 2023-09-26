from cv2 import log
from tensorflow import keras
import os
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

    def on_epoch_end(self, epoch, logs=None):
        """Called at the end of each epoch and save model weights and update train charts.

        :param epoch: Epoch number that ended just now.
        :type epoch: int
        :param logs: The logs dictionary that contain keys for quantities relevant to the current epoch, defaults to None, defaults to None.
        :type logs: dict, optional
        """
        # Set to UI
        self.model.save_weights('servstal_models/epoch_{}.h5'.format(epoch))
        self.model.save('servstal_models/epoch_{}'.format(epoch))
        epoch += 1
        if self.model_type == 'binary':
            # Update bianry train charts
            self.api_obj.bmodel_train_worker.assign_new_value_to_b_chart(last_epoch=epoch, logs=logs)


            # Save model weights to given address
            self.api_obj.bmodel_train_worker.save_b_model(model=self.model, path=self.out_path, epoch=epoch)

        elif self.model_type == 'localization':
            # Update localization train charts
            self.api_obj.lmodel_train_worker.assign_new_value_to_l_chart(last_epoch=epoch, logs=logs)

             # Save model weights to given address
            # self.api_obj.lmodel_train_worker.save_l_model(model=self.model, path=self.out_path, epoch=epoch)

        elif self.model_type == 'yolo':
            # Update yolo train charts
            self.api_obj.ymodel_train_worker.assign_new_value_to_yolo_chart(last_epoch=epoch, logs=logs)
    

        # keys = list(logs.keys())
        # values = list(logs.values())
        # #print("\nEnd epoch {} of training; got log keys: {} got log values {}\n".format(epoch, keys, values))

    def on_epoch_begin(self, epoch, logs=None):
        
        keys = list(logs.keys())
        print("Start epoch {} of training; got log keys: {}".format(epoch, keys))

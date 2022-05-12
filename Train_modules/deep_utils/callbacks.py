from cv2 import log
from tensorflow import keras
import os

class CustomCallback(keras.callbacks.Callback):
    
    def __init__(self, out_path, model_type, api_obj):
        #super.__init__(self)
        self.out_path = out_path
        self.model_type = model_type
        self.api_obj = api_obj

    def on_epoch_end(self, epoch, logs=None):
        keys = list(logs.keys())
        values = list(logs.values())
        self.model.save(self.out_path)
        print("\nEnd epoch {} of training; got log keys: {} got log values {}\n".format(epoch, keys, values))
        print('logs:', logs)

        # set to UI
        if self.model_type == 'binary':
            self.api_obj.assign_new_value_to_b_chart(last_epoch=epoch, logs=logs)
    
    


    # def on_epoch_begin(self, epoch, logs={}):
    #     self.epoch = epoch
    #
    # def on_batch_end(self, batch, logs={}):
    #     if self.epoch == 1:
    #         print(f"\nStopping at Epoch {self.epoch}, Batch {batch}")
    #         self.model.stop_training = True
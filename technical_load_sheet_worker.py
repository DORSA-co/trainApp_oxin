from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
from backend.data_grabber import sheetOverView
import time


class technical_load_sheet_worker(sQObject):
    """this class is worker for technical load sheet Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()
    update_progressbar = sSignal()
    

    def __init__(self, grabber_obj: sheetOverView,camera_range=None, frame_range=None):
        super(technical_load_sheet_worker, self).__init__()
        self.grabber_obj = grabber_obj
        self.camera_range = camera_range
        self.frame_range = frame_range
        
    
    def progressbar_event_func(self,):
        self.update_progressbar.emit()

    def run(self):
        for frame_idx in range(*self.frame_range):
            for cam_idx in range(*self.camera_range):
                self.grabber_obj.load_custom_images_from_file(
                    self.camera_range,
                    frame_idx,
                    cam_idx
                )
                self.progressbar_event_func()
        self.finished.emit()




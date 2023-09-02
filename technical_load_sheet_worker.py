from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
from backend.data_grabber import sheetOverView
import time


class Alaki:

    def __init__(self,sheet) -> None:
        self.x = sheet


    def set_event(self, func):
        self.func = func
    
    def bikhodi(self):
        a = self.x.get_cameras()
        for i in range(50):
            self.func()


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
        self.grabber_obj.set_loading_callback(self.progressbar_event_func)
        self.camera_range = camera_range
        self.frame_range = frame_range
        ##self.o_alaki = o_alaki
        #self.o_alaki.set_event(self.progressbar_event_func)
        
    
    def progressbar_event_func(self,):
        # print('load3 finish', self.grabber_obj, self)
        self.update_progressbar.emit()

    def run(self):
        #self.o_alaki.bikhodi()
        self.grabber_obj.load_custom_images_from_file(
            self.camera_range, 
            self.frame_range
        )
        time.sleep(3)
        print('load2 finish', self.grabber_obj, self)
        self.finished.emit()




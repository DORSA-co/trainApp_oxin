from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
import os
from Defect_detection_modules.SteelSurfaceInspection import SSI_2
import cv2

class image_processing_worker(sQObject):
    """this class is worker for image processing Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()

    def assign_parameters(self, n_cameras, n_frames, main_path, res_main_path, sheet_id, img_format, img_shape, api_obj, ui_obj, db_obj):
        self.n_cameras = n_cameras
        self.n_frames = n_frames
        self.main_path = main_path
        self.res_main_path = res_main_path
        self.sheet_id = sheet_id
        self.img_format = img_format
        self.img_shape = img_shape
        self.api_obj = api_obj
        self.ui_obj = ui_obj
        self.db_obj = db_obj

    def run_algorithm(self):
        try:
            side=['BOTTOM', 'TOP']
            self.api_obj.l = self.db_obj.get_image_processing_params()
            for s in side:
                for c in range(self.n_cameras[0], self.n_cameras[1]+1):
                    for f in range(self.n_frames[0], self.n_frames[1]+1):
                        self.ui_obj.suggested_defects_progressBar.setValue(self.ui_obj.suggested_defects_progressBar.value() + 1)
                        path = os.path.join(self.main_path, self.sheet_id, s, str(c), str(f)+self.img_format)
                        res_path = os.path.join(self.res_main_path, self.sheet_id, s, str(c))
                        if not os.path.exists(res_path):
                            os.makedirs(res_path)
                        if os.path.exists(path):
                            img = cv2.imread(path, 0)
                            img = cv2.resize(img, (self.img_shape[1], self.img_shape[0]))
                            SSI_2(img, path=os.path.join(res_path, str(f)+'.json'), block_size=self.api_obj.l[0], defect_th=self.api_obj.l[1], noise_th=self.api_obj.l[2])

            self.finished.emit()
        except Exception() as e:
            print(e)
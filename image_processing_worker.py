from typing import Optional
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
import os
from Defect_detection_modules.SteelSurfaceInspection import SSI_2
import cv2
from backend import pathStructure

class image_processing_worker(sQObject):
    """this class is worker for image processing Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()
    update_progressbar = sSignal()

    def __init__(self, n_cameras, n_frames, res_main_path, sheet_id, active_cameras, img_format, img_shape, api_obj, ui_obj, db_obj):
        super(image_processing_worker, self).__init__()

        self.n_cameras = n_cameras
        self.n_frames = n_frames
        self.res_main_path = res_main_path
        self.sheet_id = sheet_id
        self.active_cameras = active_cameras
        self.img_format = img_format
        self.img_shape = img_shape
        self.api_obj = api_obj
        self.ui_obj = ui_obj
        self.db_obj = db_obj

    def run_algorithm(self):
        if self.n_cameras[0] > self.active_cameras[1] or self.n_cameras[1] < self.active_cameras[0]:
            self.finished.emit()
            return
        try:
            side=['BOTTOM', 'TOP']
            self.api_obj.l = self.db_obj.get_image_processing_params()
            for s in side:
                for c in range(self.n_cameras[0], self.n_cameras[1]+1):
                    if self.active_cameras[0] <= c <= self.active_cameras[1]:
                        for f in range(self.n_frames[0], self.n_frames[1]+1):
                            path = pathStructure.sheet_image_path('', self.sheet_id, s, str(c), str(f), self.img_format)
                            res_path = pathStructure.sheet_suggestions_json_path(self.res_main_path, self.sheet_id, s, c, f)
                            if not os.path.exists(path):
                                path = pathStructure.sheet_image_path_operator('', self.sheet_id, s, str(c), str(f), self.img_format)
                            if os.path.exists(path):
                                img = cv2.imread(path, 0)
                                img = cv2.resize(img, (self.img_shape[1], self.img_shape[0]))
                                SSI_2(img, path=res_path, block_size=self.api_obj.l[0], defect_th=self.api_obj.l[1], noise_th=self.api_obj.l[2])
                                self.update_progressbar.emit()
                            else:
                                self.update_progressbar.emit()

            self.finished.emit()
        except:
            self.finished.emit()


class update_defects_worker(sQObject):
    finished = sSignal()
    update_progressbar_update_defects = sSignal()

    def __init__(self, grabber_obj, n_cameras, n_frames) -> None:
        super(update_defects_worker, self).__init__()

        self.grabber_obj = grabber_obj
        self.n_cameras = n_cameras
        self.n_frames = n_frames

    def run(self):
        for frame_idx in range(*self.n_frames):
            for cam_idx in range(*self.n_cameras):
                self.grabber_obj.update_defect(
                    cam_idx,
                    frame_idx,
                )
                self.update_progressbar_update_defects.emit()
        self.finished.emit()


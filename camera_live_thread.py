import time
import cv2
import numpy as np
from backend.pathStructure import create_sheet_path, sheet_image_path, settings
from PySide6.QtCore import Signal as sSignal
from PySide6.QtCore import QObject as sQObject
import database_utils
from backend import date_funcs
from math import ceil
import threading
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from main_UI import SHAMSI_DATE


class ImageManager(sQObject):
    first_check_finished = sSignal()
    second_check_finished = sSignal()

    def __init__(self, user, ui, cameras):
        super().__init__()
        self.user = user
        self.ui = ui
        self.cameras = cameras
        self.n_read_thread = 24
        self.read_thread = []
        self.images = [np.zeros((1200, 1920))] * 24
        self.db = database_utils.dataBaseUtils(ui_obj=self.ui)
        self.sheet_id = 0
        self.coil_dict = {}
        self.image_format = '.png'
        self.nframe = [0] * 24
        self.total_frames = 0
        self.start_cam = 1
        self.stop_cam = 0
        self.main_path = self.db.get_parent_path()
        self.n_camera_live = 1
        self.frame_update_time = 5
        self.stop_capture = 0
        self.live_type = 0
        self.save_flag = 0
        self.manual_flag = 0
        self.check_th = 200
        self.sheet_check_flag = False
        self.last_frame = 0
        self.camera_length = 280
        self.check_length_th = 2

    def set_user(self, user):
        self.user = user

    def set_n_camera_live(self, n):
        self.n_camera_live = n

    def set_live_type(self, type):
        self.live_type = type

    def set_save_flag(self, flag):
        self.save_flag = flag
        if flag:
            create_sheet_path(self.main_path, self.sheet_id)

    def set_stop_capture(self, val=1):
        self.stop_capture = val

    def set_manual_flag(self, val=1):
        self.manual_flag = val

    def get_sheet_check_flag(self):
        return self.sheet_check_flag

    def create_read_threads(self, loop=False):
        self.read_thread = []
        if self.manual_flag:
            connected_cameras = list(map(str, range(1, 25)))
        else:
            connected_cameras = self.cameras.get_connected_cameras_by_id().keys()
        step = int(24 / self.n_read_thread)
        for i in range(self.n_read_thread):
            s = (i * step) + 1
            d = (i + 1) * step
            if self.start_cam <= s <= self.stop_cam or self.start_cam + 12 <= s <= self.stop_cam + 12:
                if any(str(camera_id) in connected_cameras for camera_id in list(range(s, d+1))):
                    self.read_thread.append(threading.Thread(target=self.threads_func, args=(s, d, loop)))

    def create_sheet_checking_thread(self):
        self.sheet_check_thread = threading.Thread(target=self.check_thread_func, args=())

    def start_read_threads(self):
        for t in self.read_thread:
            t.start()

    def start_sheet_checking_thread(self):
        self.sheet_check_thread.start()

    def update_sheet(self, stop_cam, coil_dict):
        self.sheet_id = str(coil_dict['sheet_id'])
        self.nframe = [0] * 24
        self.images = [np.zeros((1200, 1920))] * 24
        self.stop_cam = stop_cam
        if 'length' in coil_dict.keys() and coil_dict['length']:
            self.last_frame = 1000 - self.check_length_th #int(coil_dict['length'] / self.camera_length) - self.check_length_th
        else:
            self.last_frame = 0
        if self.save_flag:
            create_sheet_path(self.main_path, self.sheet_id)
        self.coil_dict = coil_dict

    def update_database(self):
        if self.save_flag:
            self.coil_dict['user'] = self.user
            time = self.coil_dict['time'] = date_funcs.get_time(folder_path=False)
            self.coil_dict['time'] = time
            date = str(date_funcs.get_date(persian=SHAMSI_DATE, folder_path=False))
            self.coil_dict['date'] = date
            self.coil_dict['main_path'] = self.main_path
            self.coil_dict['nframe'] = max(self.nframe)
            if self.stop_cam == 0:
                self.coil_dict['cameras'] = '0-0'
            else:
                self.coil_dict['cameras'] = str(self.start_cam) + '-' + str(self.stop_cam)
            self.coil_dict['Image_format'] = self.image_format

            self.db.set_sheet(coil_dict=self.coil_dict)

    def threads_func(self, s, d, loop=False):
        connected_cameras = self.cameras.get_connected_cameras_by_id()

        if loop:
            while True:
                self.read_image(s, d, connected_cameras)
                if self.stop_capture:
                    return
        else:
            self.read_image(s, d, connected_cameras)
            
    def read_image(self, s, d, connected_cameras):
        for camera_id in range(s, d + 1):
            if self.start_cam <= camera_id <= self.stop_cam or self.start_cam + 12 <= camera_id <= self.stop_cam + 12:
                if str(camera_id) in list(connected_cameras.keys()):
                    ret, img = connected_cameras[str(camera_id)].getPictures()
                    if ret:
                        if self.nframe[int(camera_id) - 1] + 1 >= self.last_frame:
                            check = self.sheet_check(img)
                            if not check:
                                self.second_check_finished.emit()
                                return
                        self.images[int(camera_id) - 1] = img
                        self.nframe[int(camera_id) - 1] += 1
                        if self.save_flag:
                            if int(camera_id) <= 12:
                                side = 'TOP'
                                path = sheet_image_path(self.main_path, self.sheet_id, side, camera_id,
                                                        str(self.nframe[int(camera_id) - 1]),
                                                        self.image_format)
                            else:
                                side = 'BOTTOM'
                                path = sheet_image_path(self.main_path, self.sheet_id, side, str(camera_id - 12),
                                                        str(self.nframe[int(camera_id) - 1]),
                                                        self.image_format)
                            cv2.imwrite(path, self.images[int(camera_id) - 1])
                else:
                    if self.manual_flag:
                        img = np.zeros((1200, 1920), dtype=np.uint8)
                        if self.nframe[int(camera_id) - 1] + 1 >= self.last_frame + 5:
                            img[:, :] = np.random.randint(self.check_th, 255)
                        else:
                            img[:, :] = np.random.randint(0, 150)

                        if self.nframe[int(camera_id) - 1] + 1 >= self.last_frame:
                            check = self.sheet_check(img)
                            if not check:
                                self.second_check_finished.emit()
                                return

                        self.images[int(camera_id) - 1] = img
                        self.nframe[int(camera_id) - 1] += 1

                        if self.save_flag:
                            if int(camera_id) <= 12:
                                side = 'TOP'
                                path = sheet_image_path(self.main_path, self.sheet_id, side, camera_id,
                                                        str(self.nframe[int(camera_id) - 1]),
                                                        self.image_format)
                            else:
                                side = 'BOTTOM'
                                path = sheet_image_path(self.main_path, self.sheet_id, side, str(camera_id - 12),
                                                        str(self.nframe[int(camera_id) - 1]),
                                                        self.image_format)
                            cv2.imwrite(path, self.images[int(camera_id) - 1])
                        cv2.waitKey(1)
            if self.stop_capture:
                return

    def check_thread_func(self):
        connected_cameras = self.cameras.get_connected_cameras_by_id()
        cameras_id = sorted(connected_cameras.keys())
        camera_id = -1
        for id in cameras_id:
            id = int(id)
            if self.start_cam <= id <= self.stop_cam or self.start_cam + 12 <= id <= self.stop_cam + 12:
                camera_id = id
                break
            if self.stop_capture:
                return
        if camera_id < 0:
            if self.manual_flag:
                camera_id = 1
                i=0
            else:
                return
        
        while True:
            if str(camera_id) in list(connected_cameras.keys()):
                ret, img = connected_cameras[str(camera_id)].getPictures()
                if not ret:
                    continue
                check = self.sheet_check(img)
                if check:
                    self.first_check_finished.emit()
                    return
            else:
                if self.manual_flag:
                    img = np.zeros((1200, 1920), dtype=np.uint8)
                    if i < 20:
                        img[:, :] = np.random.randint(self.check_th, 255)
                        i+=1
                    else:
                        img[:, :] = np.random.randint(0, 150)
                    check = self.sheet_check(img)
                    if check:
                        self.first_check_finished.emit()
                        return
            if self.stop_capture:
                return

    def sheet_check(self, img):
        average = img.mean()
        if average >= self.check_th:
            return False
        return True

    def show_live(self):
        if self.live_type == 0:
            fs = sQImage(self.images[self.n_camera_live - 1], self.images[self.n_camera_live - 1].shape[1],
                         self.images[self.n_camera_live - 1].shape[0],
                         self.images[self.n_camera_live - 1].strides[0],
                         sQImage.Format_RGB888)
            self.ui.live.setPixmap(sQPixmap.fromImage(fs))
            if self.ui.full_s:
                self.ui.full_s_window.live.setPixmap(sQPixmap.fromImage(fs))

        if self.live_type == 1:
            list(map(self.set_image, ['t'] * 12, range(12)))

        if self.live_type == 2:
            list(map(self.set_image, ['b'] * 12, range(12, 24)))

        if self.live_type == 3:
            list(map(self.set_image, [''] * 24, list(range(24))))

    def set_image(self, c, i):
        fs = sQImage(self.images[i], self.images[i].shape[1],
                     self.images[i].shape[0],
                     self.images[i].strides[0],
                     sQImage.Format_RGB888)
        s = 'self.ui.' + str(c) + 'live' + str(i + 1) + '.setPixmap(sQPixmap.fromImage(fs))'
        exec(s)
        if eval('self.ui.full_' + str(c)):
            s = 'self.ui.full_'+ str(c) +'_window.' + str(c) + 'live' + str(i + 1) + '.setPixmap(sQPixmap.fromImage(fs))'
            exec(s) 

    def join_all(self):
        for t in self.read_thread:
            t.join()
        self.read_thread = []

    def start(self, loop=False):
        self.set_stop_capture(val=0)

        self.create_read_threads(loop)
        self.start_read_threads()

    def start_sheet_checking(self):
        self.set_stop_capture(val=0)

        self.create_sheet_checking_thread()
        self.start_sheet_checking_thread()

    def stop(self):
        self.set_stop_capture()
        try:
            self.stop_sheet_checking()
        except:
            pass
        self.join_all()

    def stop_sheet_checking(self):
        self.sheet_check_thread.join()
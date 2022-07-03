import time
import cv2
import numpy as np
from backend.pathStructure import create_sheet_path, sheet_image_path, settings
from simulator import plc_simulator
from PySide6.QtCore import QObject
import database_utils
from backend import date_funcs
from math import ceil
import threading
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap


class ImageManager(QObject):
    def __init__(self, user, ui, cameras):
        super().__init__()
        self.user = user
        self.ui = ui
        self.cameras = cameras
        self.plc_thread = None
        self.n_read_thread = 12
        self.n_write_thread = 0
        self.read_thread = []
        self.write_thread = []
        self.qinfo = []
        self.qimage = []
        self.images = [np.zeros((1200, 1920))]*24
        self.db = database_utils.dataBaseUtils()
        self.sheet_id = 0
        self.coil_dict = None
        self.image_format = '.png'
        self.nframe = [0]*24
        self.total_frames = 0
        self.start_cam = 0
        self.stop_cam = 0
        self.camera_width = 40
        self.main_path = self.db.get_parent_path()
        self.n_camera_live = 1
        self.stop_capture = 0
        self.live_type = 0

    def set_user(self, user):
        self.user = user

    def set_n_camera_live(self, n):
        self.n_camera_live = n

    def set_live_type(self, type):
        self.live_type = type

    def set_stop_capture(self):
        self.stop_capture = 1

    def create_read_threads(self):
        step = int(24 / self.n_read_thread)
        for i in range(self.n_read_thread):
            self.read_thread.append(threading.Thread(target=self.read_image, args=((i * step) + 1, (i + 1) * step)))

    def start_read_threads(self):
        for t in self.read_thread:
            t.start()

    def create_write_threads(self):
        for i in range(self.n_write_thread):
            self.write_thread.append(
                threading.Thread(target=self.write_image))

    def start_write_threads(self):
        for p in self.write_thread:
            p.start()

    def read_from_plc(self):
        with open('plc.txt', 'r', encoding='Utf-8') as plc:
            a = plc.read()
            if a != '':
                coil_dict = eval(a)
            else:
                coil_dict = self.coil_dict

        sheet_id_new = str(coil_dict['sheet_id'])
        if sheet_id_new != self.sheet_id:
            print(sheet_id_new, self.sheet_id)
            self.sheet_id = str(sheet_id_new)
            self.total_frames = max(self.nframe)
            self.nframe = [0]*24
            self.stop_cam = ceil(coil_dict['width'] / self.camera_width)
            create_sheet_path(self.main_path, self.sheet_id)
            self.ui.sheet_label.setText(str(coil_dict))
            if self.coil_dict:
                self.update_database()
            self.coil_dict = coil_dict
        if self.stop_capture:
            return
        else:
            self.plc_thread = threading.Timer(1, self.read_from_plc)
            self.plc_thread.start()

    def update_database(self):
        self.coil_dict['user'] = self.user
        time = self.coil_dict['time'] = date_funcs.get_time(folder_path=False)
        self.coil_dict['time'] = time
        date = str(date_funcs.get_date(folder_path=False))
        self.coil_dict['date'] = date
        self.coil_dict['main_path'] = self.main_path
        self.coil_dict['nframe'] = self.total_frames
        start_camera = 0
        stop_camera = ceil(self.coil_dict['width'] / self.camera_width)
        self.coil_dict['cameras'] = str(start_camera) + '-' + str(stop_camera)
        self.coil_dict['Image_format'] = self.image_format

        self.db.set_sheet(coil_dict=self.coil_dict)

    def read_image(self, s, d):
        connected_cameras = self.cameras.get_connected_cameras_by_id()
        for camera_id in range(s, d + 1):
            if self.start_cam < camera_id <= self.stop_cam or self.start_cam + 12 < camera_id <= self.stop_cam + 12:
                if str(camera_id) in list(connected_cameras.keys()):
                    connected_cameras[str(camera_id)].start_grabbing()
                if self.stop_capture:
                    return
        while True:
            # if s == 1:
            #     self.nframe += 1
            # print(self.nframe)
            for camera_id in range(s, d + 1):
                if self.start_cam < camera_id <= self.stop_cam or self.start_cam + 12 < camera_id <= self.stop_cam + 12:
                    self.nframe[int(camera_id) - 1] += 1
                    if str(camera_id) in list(connected_cameras.keys()):
                        self.images[int(camera_id) - 1] = connected_cameras[str(camera_id)].getPictures()
                        # self.qimage.append(self.images[int(camera_id) - 1])
                        # self.qinfo.append((str(self.sheet_id), str(camera_id), str(self.nframe[int(camera_id) - 1])))
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
                        # print(path)
                        cv2.imwrite(path, self.images[int(camera_id) - 1])
                    else:
                        self.images[int(camera_id) - 1] = np.zeros((1200, 1920), dtype=np.uint8)
                        self.images[int(camera_id) - 1][:, :] = np.random.randint(0, 150)
                        # self.qimage.append(self.images[int(camera_id) - 1])
                        # self.qinfo.append((str(self.sheet_id), str(camera_id), str(self.nframe[int(camera_id) - 1])))
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
                        # print(path)
                        cv2.imwrite(path, self.images[int(camera_id) - 1])
                        time.sleep(0.005)
                if self.stop_capture:
                    return
            if self.stop_capture:
                return

    def write_image(self):
        while True:
            if self.stop_capture:
                return
            if not self.qimage or not self.qinfo:
                continue
            img = self.qimage.pop(0)
            info = self.qinfo.pop(0)
            # img = np.zeros((1200, 1920, 3))
            # info = ('890', '1', '8')

            if int(info[1]) <= 12:
                side = 'TOP'
                path = sheet_image_path(self.main_path, info[0], side, info[1], info[2],
                                        self.image_format)
            else:
                side = 'BOTTOM'
                path = sheet_image_path(self.main_path, info[0], side, str(int(info[1]) - 12), info[2],
                                        self.image_format)
            # print(path)
            t = time.time()
            cv2.imwrite(path, img)
            print(time.time() - t)

    def show_live(self):
        if self.live_type == 0:
            fs = sQImage(self.images[self.n_camera_live - 1], self.images[self.n_camera_live - 1].shape[1],
                        self.images[self.n_camera_live - 1].shape[0],
                        self.images[self.n_camera_live - 1].strides[0],
                        sQImage.Format_Grayscale8)
            self.ui.live.setPixmap(sQPixmap.fromImage(fs))

        if self.live_type == 1:
            list(map(self.set_image, ['t']*12, range(12)))

        if self.live_type == 2:
            list(map(self.set_image, ['b']*12, range(12, 24)))

        if self.live_type == 3:
            list(map(self.set_image, ['']*24, list(range(24))))

    def set_image(self, c, i):
        fs = sQImage(self.images[i], self.images[i].shape[1],
                     self.images[i].shape[0],
                     self.images[i].strides[0],
                     sQImage.Format_Grayscale8)
        s = 'self.ui.' + str(c) + 'live' + str(i + 1) + '.setPixmap(sQPixmap.fromImage(fs))'
        exec(s)

    def join_all(self):
        for t in self.read_thread:
            t.join()
        # for t in self.write_thread:
        #     t.join()

    def start(self):
        # self.create_queues()
        self.create_read_threads()
        # self.create_write_threads()
        plc_simulator()
        self.read_from_plc()
        self.start_read_threads()
        # self.start_write_threads()

    def stop(self):
        self.set_stop_capture()
        self.join_all()

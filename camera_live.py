import cv2
import numpy as np
import database_utils
from backend.pathStructure import create_sheet_path, sheet_image_path, settings
from simulator import plc_simulator
from PySide6.QtCore import QObject
from multiprocessing import Process, Queue, Value
import database_utils
from backend import date_funcs
from math import ceil
import threading


def read_image(cameras, qimage, qinfo, sheet_id, nframe, start_cam, stop_cam, s, d, stop):
    connected_cameras = cameras.get_connected_cameras_by_id()
    for camera_id in range(s, d + 1):
        if start_cam.value < camera_id <= stop_cam.value or start_cam.value + 12 < camera_id <= stop_cam.value + 12:
            if str(camera_id) in list(connected_cameras.keys()):
                connected_cameras[str(camera_id)].start_grabbing()
            if stop.value:
                return
    while True:
        if s == 1:
            nframe.value += 1
        for camera_id in range(s, d + 1):
            if start_cam.value < camera_id <= stop_cam.value or start_cam.value + 12 < camera_id <= stop_cam.value + 12:
                if str(camera_id) in list(connected_cameras.keys()):
                    img = connected_cameras[str(camera_id)].getPictures()
                    qimage.put(img)
                    qinfo.put((str(sheet_id.value), str(camera_id), str(nframe.value)))
                else:
                    img = np.zeros((1920, 1200))
                    qimage.put(img)
                    qinfo.put((str(sheet_id.value), str(camera_id), str(nframe.value)))
            if stop.value:
                return
        if stop.value:
            return


def write_image(qimage, qinfo, main_path, image_format, stop):
    while True:
        if stop.value:
            return
        if qimage.empty() or qinfo.empty():
            continue
        img = qimage.get()
        info = qinfo.get()

        if info[1] <= 12:
            side = 'TOP'
        else:
            side = 'BOTTOM'
        path = sheet_image_path(main_path, info[0], side, info[1], info[2],
                                image_format)
        cv2.imwrite(path, img)


class ImageManager(QObject):
    def __init__(self, user, ui, cameras):
        super().__init__()
        self.user = user
        self.ui = ui
        self.cameras = cameras
        self.plc_thread = None
        self.n_read_process = 4
        self.n_write_process = 2
        self.read_process = []
        self.write_process = []
        self.qinfo = None
        self.qimage = None
        self.db = database_utils.dataBaseUtils()
        self.sheet_id = Value('i', 0)
        self.coil_dict = None
        self.image_format = '.png'
        self.nframe = Value('i', 0)
        self.total_frames = 0
        self.start_cam = Value('i', 0)
        self.stop_cam = Value('i', 12)
        self.camera_width = 40
        self.main_path = self.db.get_parent_path()
        self.stop_capture = Value('i', 0)

    def set_user(self, user):
        self.user = user

    def set_stop_capture(self):
        self.stop_capture.value = 1

    def create_queues(self):
        self.qimage = Queue()
        self.qinfo = Queue()

    def create_read_processes(self):
        step = int(24 / self.n_read_process)
        for i in range(self.n_read_process):
            self.read_process.append(Process(target=read_image, args=(self.cameras, self.qimage, self.qinfo,
                                                                      self.sheet_id, self.nframe, self.start_cam,
                                                                      self.stop_cam, (i * step) + 1, (i + 1) * step, self.stop_capture)))

    def start_read_process(self):
        for p in self.read_process:
            p.start()

    def create_write_processes(self):
        for i in range(self.n_write_process):
            self.write_process.append(
                Process(target=write_image, args=(self.qimage, self.qinfo, self.main_path, self.image_format,
                                                  self.stop_capture)))

    def start_write_process(self):
        for p in self.write_process:
            p.start()

    def read_from_plc(self):
        with open('plc.txt', 'r', encoding='Utf-8') as plc:
            coil_dict = eval(plc.read())
        sheet_id_new = coil_dict['sheet_id']
        if sheet_id_new != self.sheet_id:
            self.sheet_id = sheet_id_new
            self.total_frames = self.nframe
            self.nframe = 1
            self.stop_cam = ceil(coil_dict['width'] / self.camera_width)
            create_sheet_path(self.main_path, self.sheet_id)
            if self.coil_dict:
                self.update_database()
            self.coil_dict = coil_dict
        if self.stop_capture.value:
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

    def join_all(self):
        for p in self.read_process:
            p.join()
        for p in self.write_process:
            p.join()

    def start(self):
        self.create_queues()
        self.create_read_processes()
        self.create_write_processes()
        plc_simulator()
        self.read_from_plc()
        self.start_read_process()
        self.start_write_process()
        self.join_all()

import cv2
from backend.pathStructure import create_sheet_path, sheet_image_path, settings
from simulator import cameras_simulator, plc_simulator, PATH
from PySide6.QtGui import QImage, QPixmap
import os
from multiprocessing import Process, Queue


class live_manager:
    def __init__(self, path, ui=None, cameras=None):
        self.stop = False
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.n_camera = [1, 2, 13, 14]
        self.n_frame = [1] * 24
        self.coil_number = 0
        self.grab = ['False'] * 24
        self.ui = ui
        self.path = path
        self.n_process = 2
        self.qimgs = Queue()
        self.qinfo = Queue()
        self.s_processes = []
        self.n_camera_live = 1

    def create_save_processes(self):
        for i in range(self.n_process):
            p = Process(target=save_camera_images, args=(self.qimgs, self.qinfo))
            self.s_processes.append(p)
            p.start()

    def read_coil_number(self):
        with open('plc.txt', encoding='Utf-8') as f:
            plc = f.read().strip()
        if plc == '':
            return False
        coil_number_new = int(plc)
        if coil_number_new != self.coil_number:
            self.n_frame = [1] * 24
            self.coil_number = coil_number_new
            create_sheet_path(self.path, self.coil_number)
        return True

    def read_grab(self, ncamera):
        with open('grab' + str(ncamera) + '.txt', encoding='Utf-8') as f:
            grab_new = f.read().strip()
        if grab_new == '':
            return False
        if grab_new == 'True' and self.grab[int(ncamera) - 1] == 'True':
            return False
        self.grab[int(ncamera) - 1] = grab_new
        return True

    def join_processes(self):
        for i in range(self.n_process):
            self.qimgs.put(None)
            self.qinfo.put(None)
        for i in range(self.n_process):
            self.s_processes[i].join()

    def read_camera_images(self):
        plc_simulator()
        cameras_simulator(self.n_camera)
        self.create_save_processes()

        while 1:
            if self.stop:
                self.join_processes()
                break

            if not self.read_coil_number():
                continue

            for i in self.n_camera:
                if not self.read_grab(i):
                    continue
                if self.grab[int(i) - 1] == 'True':
                    img = cv2.imread(os.path.join(PATH, str(i) + '.png'), 0)
                    if img is None:
                        continue
                    if i <= 12:
                        c = int(i)
                        side = 'UP'
                    else:
                        c = i - 12
                        side = 'BOTTOM'

                    path = sheet_image_path(self.path, self.coil_number, side, str(c), self.n_frame[int(i) - 1],
                                            '.png')

                    self.qimgs.put(img)
                    self.qinfo.put(path)

                    self.n_frame[int(i) - 1] += 1

                    if self.n_camera_live == i:
                        self.live(img)

    def live(self, img):
        fs = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_Grayscale8)
        self.ui.live1.setPixmap(QPixmap.fromImage(fs))


def save_camera_images(imgs, info):
    while True:
        if imgs.empty() or info.empty():
            continue
        img = imgs.get()
        path = info.get()
        if img is None or path is None:
            return
        cv2.imwrite(path, img)

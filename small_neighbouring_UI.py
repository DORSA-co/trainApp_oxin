import time

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from backend.mouse import Mouse
from utils import Utils
import os

ui, _ = loadUiType("UI/small_neighbour_imgs.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class small_neighbouring(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

    def __init__(self, parent):
        super(small_neighbouring, self).__init__(parent=parent)
        self.setupUi(self)
        self.installEventFilter(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.win_set_geometry()
        self.center()
        self._old_pos = None
        self.maxFlag = False
        self.mouse = Mouse()

        self.imgs = []
        self.anns = []
        self.ann = None
        self.img = None
        self.original_img = None

        # btn connector

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def win_set_geometry(self, left=10, top=10, width=288, height=180):
        self.setGeometry(left, top, width, height)

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        # print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)

    def set_imgs(self, imgs):
        self.imgs = imgs

    def set_img(self, img, index):
        self.imgs[index] = img

    def get_original_img(self):
        return self.original_img

    def get_img(self):
        return self.img

    def set_annts(self, anns):
        self.anns = anns

    def set_annt(self, annt, index):
        self.anns[index] = annt

    def get_annt(self):
        return self.ann

    def set_image_in_label(self, annotation=True):
        # print(self.imgs[3].dtype, self.imgs[8].dtype, self.imgs[2].dtype)
        image_u = cv2.hconcat([self.imgs[0], self.imgs[1], self.imgs[2]])
        image_c = cv2.hconcat([self.imgs[3], self.imgs[8], self.imgs[4]])
        image_d = cv2.hconcat([self.imgs[5], self.imgs[6], self.imgs[7]])
        self.original_img = cv2.vconcat([image_u, image_c, image_d])
        self.img = self.original_img

        if annotation:
            annotation_u = cv2.hconcat([self.anns[0], self.anns[1], self.anns[2]])
            annotation_c = cv2.hconcat([self.anns[3], self.anns[8], self.anns[4]])
            annotation_d = cv2.hconcat([self.anns[5], self.anns[6], self.anns[7]])
            self.ann = cv2.vconcat([annotation_u, annotation_c, annotation_d])
            self.img = Utils.add_layer_to_img(self.img, self.ann, opacity=0.4, compress=0.5)

        self.image.setPixmap(QPixmap.fromImage(
            QImage(self.img, self.img.shape[1], self.img.shape[0], self.img.strides[0],
                   QImage.Format_BGR888)))


# api = labeling_api.labeling_API(win)
import cv2

if __name__ == "__main__":
    img = cv2.imread('/home/reyhane/oxin_image_grabber/995/BOTTOM/1/5.png')
    imgs = []
    for i in range(9):
        imgs.append(img)
    app = QApplication()
    win = small_neighbouring(None)
    win.set_imgs(imgs)
    win.set_image_in_label(False)
    win.show()
    sys.exit(app.exec())

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6 import QtCore as sQtCore
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

import os
import texts

import subprocess
sys.path.append('../oxin_help')

ui, _ = loadUiType(os.path.join(os.path.dirname(os.path.abspath(__file__)), "UI/neighbour_imgs.ui"))
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class neighbouring(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self, img, annotated_image=None, has_annotation=False, lang='en'):
        super(neighbouring, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        title = "SENSE-Image Enlargement"
        self.setWindowTitle(title)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.img = img
        self.annotated_image = annotated_image
        self.n_image.setPixmap(QPixmap.fromImage(QImage(self.img, self.img.shape[1], self.img.shape[0], self.img.strides[0], QImage.Format_BGR888)))
        # annotated image
        if has_annotation:
            self.annot_checkbox.setEnabled(True)
        else:
            self.msg_label.setText(self.annotated_image)
        self.activate_()
        self.win_set_geometry()
        self.center()
        self._old_pos = None

        self.scale = 1
        self.position = [0, 0]
        self.pressed = None

        # btn connector
        self.annot_checkbox.stateChanged.connect(self.set_annotations)
        self.eq_hist.stateChanged.connect(self.equalize_img)
        self.n_image.mousePressEvent = self.mousePressImage()
        self.n_image.mouseReleaseEvent = self.mouseReleaseImage()
        self.n_image.mouseMoveEvent = self.mouseMoveImage()

        self.language = lang
        self.annot_checkbox.setText(texts.Titles['show_labels'][lang])
        self.label_303.setText(texts.Titles['brightness'][lang])
        self.label_305.setText(texts.Titles['contrast'][lang])


        self.org_image = self.img
        self.org_image_annt = self.annotated_image

        #Update br of image
        self.btightness_slider.valueChanged.connect(self.update_image_brightess)
        self.contrast_slider.valueChanged.connect(self.update_image_brightess)
        
        self.equalize_img()

        self.help_process = None

    def mousePressEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

    def mousePressImage(self):
        def func(event):
            if self.n_image.hasScaledContents():
                self.scale = 1
                self.position = [0, 0]
            if self.scale != 1:
                self.pressed = event.x(), event.y()
                self.anchor = self.position
        return func

    def mouseReleaseImage(self):
        def func(event):
            if self.n_image.hasScaledContents():
                self.scale = 1
                self.position = [0, 0]
            self.pressed = None
        return func

    def mouseMoveImage(self):
        def func(event):
            if self.n_image.hasScaledContents():
                self.scale = 1
                self.position = [0, 0]
            x, y = event.x(), event.y()
            if self.pressed:
                dx, dy = x - self.pressed[0], y - self.pressed[1]
                self.position = self.anchor[0] - dx, self.anchor[1] - dy
                self.position = self.update_image(self.position)
        return func

    def wheelEvent(self, event):
        if self.n_image.hasScaledContents():
            self.scale = 1
            self.position = [0, 0]
            self.n_image.setScaledContents(False)
        if event.angleDelta().y() > 0:
            self.scale *= 1.25
        else:
            self.scale /= 1.25
            if self.scale < 1:
                self.scale = 1
                self.position = [0, 0]
        if self.annot_checkbox.isChecked():
            self.position = self.show_image_in_label(self.annotated_image, self.scale, (event.position().x(), event.position().y()))
        else:
            self.position = self.show_image_in_label(self.img, self.scale, (event.position().x(), event.position().y()))

    def show_image_in_label(self, img, scale=1, position=(0, 0)):
        self.fs = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
        if scale == 1:
            self.n_image.setScaledContents(True)
            self.n_image.setPixmap(QPixmap.fromImage(self.fs))
        else:
            self.fs = self.fs.scaled(self.n_image.size() * scale)
            # self.n_image.setPixmap(QPixmap.fromImage(self.fs).scaled(self.n_image.size() * scale))
            position = self.update_image(position)

        return position

    def update_image(self, position):
        pixmap = QPixmap(self.n_image.size())
        px, py = position
        px = px if (px <= self.fs.width() - self.n_image.width()) else (
                self.fs.width() - self.n_image.width())
        py = py if (py <= self.fs.height() - self.n_image.height()) else (
                self.fs.height() - self.n_image.height())
        px = px if (px >= 0) else 0
        py = py if (py >= 0) else 0
        position = (px, py)

        painter = QPainter()
        painter.begin(pixmap)
        painter.drawImage(QPoint(0, 0), self.fs,
                          QRect(position[0], position[1], self.n_image.width(),
                                self.n_image.height()))
        painter.end()

        self.n_image.setPixmap(pixmap)

        return position

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)
        self.helpButton.clicked.connect(self.show_help)

    def win_set_geometry(self, left=100, top=600, width=800, height=600):
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()
    
    def maxmize_minimize(self):
        if self.annot_checkbox.isChecked():
            self.position = self.show_image_in_label(self.annotated_image)
        else:
            self.position = self.show_image_in_label(self.img)
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def show_help(self):
        if self.help_process is not None and self.help_process.poll() is None:
            self.help_process.terminate()
        text = texts.Titles['image_enlargement'][self.language]
        self.help_process = subprocess.Popen(
                        ['/bin/python3', '../oxin_help/help_UI.py',
                        self.language,
                        text
                        ]
                    )

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        ##print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)

    def set_annotations(self):
        self.n_image.setScaledContents(True)
        self.scale = 1
        if self.annot_checkbox.isChecked():
            self.n_image.setPixmap(QPixmap.fromImage(QImage(self.annotated_image,
                                                            self.annotated_image.shape[1],
                                                            self.annotated_image.shape[0],
                                                            self.annotated_image.strides[0],
                                                            QImage.Format_BGR888)))
        
        else:
            self.n_image.setPixmap(QPixmap.fromImage(QImage(self.img,
                                                            self.img.shape[1],
                                                            self.img.shape[0],
                                                            self.img.strides[0],
                                                            QImage.Format_BGR888)))





    def update_image_brightess(self):
        br = self.btightness_slider.value()
        cr = self.contrast_slider.value()
        self.img = cv2.convertScaleAbs(self.org_image, alpha=br, beta=cr)
        self.annotated_image = cv2.convertScaleAbs(self.org_image_annt, alpha=br, beta=cr)
        self.set_annotations()


    def equalize_img(self):


        if self.eq_hist.isChecked():

            self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
            self.img = cv2.equalizeHist(self.img)
            self.img = cv2.cvtColor(self.img,cv2.COLOR_GRAY2BGR)
            self.set_annotations()

        else:
            self.img = self.org_image
            self.set_annotations()
            pass

# api = labeling_api.labeling_API(win)
import cv2
if __name__ == "__main__":
    img = cv2.imread('/home/reyhane/Desktop/train/image/3.jpg')
    # img = cv2.resize(img, (1792, 1200))
    app = QApplication()
    win = neighbouring(img)
    win.show()
    sys.exit(app.exec())
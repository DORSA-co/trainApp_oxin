from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

ui, _ = loadUiType("UI/small_neighbour_imgs.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class small_neighbouring(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

    def __init__(self, imgs, parent):
        super(small_neighbouring, self).__init__(parent=parent)
        self.setupUi(self)
        self.installEventFilter(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.set_imgs(imgs)
        self.win_set_geometry()
        self.center()
        self._old_pos = None

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
        image_ul = imgs[0]
        self.image_up_left.setPixmap(QPixmap.fromImage(
            QImage(image_ul, image_ul.shape[1], image_ul.shape[0], image_ul.strides[0], QImage.Format_BGR888)))

        image_u = imgs[1]
        self.image_up.setPixmap(QPixmap.fromImage(
            QImage(image_u, image_u.shape[1], image_u.shape[0], image_u.strides[0], QImage.Format_BGR888)))

        image_ur = imgs[2]
        self.image_up_right.setPixmap(QPixmap.fromImage(
            QImage(image_ur, image_ur.shape[1], image_ur.shape[0], image_ur.strides[0], QImage.Format_BGR888)))

        image_l = imgs[3]
        self.image_left.setPixmap(QPixmap.fromImage(
            QImage(image_l, image_l.shape[1], image_l.shape[0], image_l.strides[0], QImage.Format_BGR888)))

        image_r = imgs[4]
        self.image_right.setPixmap(QPixmap.fromImage(
            QImage(image_r, image_r.shape[1], image_r.shape[0], image_r.strides[0], QImage.Format_BGR888)))

        image_bl = imgs[5]
        self.image_bottom_left.setPixmap(QPixmap.fromImage(
            QImage(image_bl, image_bl.shape[1], image_bl.shape[0], image_bl.strides[0], QImage.Format_BGR888)))

        image_b = imgs[6]
        self.image_bottom.setPixmap(QPixmap.fromImage(
            QImage(image_b, image_b.shape[1], image_b.shape[0], image_b.strides[0], QImage.Format_BGR888)))

        image_br = imgs[7]
        self.image_bottom_right.setPixmap(QPixmap.fromImage(
            QImage(image_br, image_br.shape[1], image_br.shape[0], image_br.strides[0], QImage.Format_BGR888)))

        image_c = imgs[8]
        self.image_center.setPixmap(QPixmap.fromImage(
            QImage(image_c, image_c.shape[1], image_c.shape[0], image_c.strides[0], QImage.Format_BGR888)))


# api = labeling_api.labeling_API(win)
import cv2

if __name__ == "__main__":
    img = cv2.imread('/home/reyhane/oxin_image_grabber/995/BOTTOM/1/1.png')
    imgs = []
    for i in range(9):
        imgs.append(img)
    app = QApplication()
    win = small_neighbouring(imgs)
    win.show()
    sys.exit(app.exec())
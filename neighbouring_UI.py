from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

ui, _ = loadUiType("UI/neighbour_imgs.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


class neighbouring(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self, img):
        super(neighbouring, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.n_image.setPixmap(QPixmap.fromImage(
            QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)))
        self.activate_()

        self.win_set_geometry()
        self._old_pos = None

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

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)

    def win_set_geometry(self, left=100, top=600, width=800, height=600):
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()


# api = labeling_api.labeling_API(win)
import cv2
if __name__ == "__main__":
    img = cv2.imread('/home/reyhane/oxin_image_grabber/995/BOTTOM/0/0.jpg')
    app = QApplication()
    win = neighbouring(img)
    win.show()
    sys.exit(app.exec())
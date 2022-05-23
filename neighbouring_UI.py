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

    def __init__(self, img, annotated_image=None, has_annotation=False):
        super(neighbouring, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
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

        # btn connector
        self.annot_checkbox.clicked.connect(self.set_annotations)


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
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    def win_set_geometry(self, left=100, top=600, width=800, height=600):
        self.setGeometry(left, top, width, height)

    def minimize(self):
        self.showMinimized()
    
    def maxmize_minimize(self):

        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().screen()
        center_loc = screen.geometry().center()
        #print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)


    def set_annotations(self):
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



# api = labeling_api.labeling_API(win)
import cv2
if __name__ == "__main__":
    img = cv2.imread('/home/reyhane/oxin_image_grabber/995/BOTTOM/0/0.jpg')
    app = QApplication()
    win = neighbouring(img)
    win.show()
    sys.exit(app.exec())
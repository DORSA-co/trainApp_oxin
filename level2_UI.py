import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

from PyQt5.QtWidgets import QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem,QColor,QFont
import cv2
import os

try:
    import texts
except:
    pass

ui, _ = loadUiType("UI/level2.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%



TRUE_COLOR = '#4E9A06'
FALSE_COLOR = '#A40000'


class levl2_UI(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self, lang='en'):
        super(levl2_UI, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        title = "Level2-test"
        self.setWindowTitle(title)

        self.activate_()
        self._old_pos = None

        self.set_style_sheet('dummy',False)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)

    def close_win(self):
        self.close()



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
        if not self.isMaximized():
            self.move(self.pos() + delta)




    def set_style_sheet(self,frame_name,color_status =True):
        
        if color_status:
            color_status=TRUE_COLOR
        else:
            color_status=FALSE_COLOR
        
        frame_name = eval('self.frame_{}'.format(frame_name))
        frame_name.setStyleSheet("background-color: {}".format(color_status))


    def set_time(self,label_name,data):
        label_name = eval('self.label_time_{}'.format(label_name))
        label_name.setText(str(data))


    



if __name__ == "__main__":
    app = QApplication()
    win = levl2_UI(lang='en')
    win.show()
    sys.exit(app.exec())
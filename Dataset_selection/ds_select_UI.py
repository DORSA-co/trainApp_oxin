
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6 import QtCore as sQtCore
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtGui import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import os
ui, _ = loadUiType("Dataset_selection/dataset_select.ui")


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class Ds_selection(QMainWindow, ui):
    global widgets
    widgets = ui

    def __init__(self):

        super(Ds_selection, self).__init__()


        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "SENSE-Dataset Selection"
        self.setWindowTitle(title)

        
        # SET LANGUAGE
        #//////////////////////////////////////////////
        # self.set_language()
        self.language = 'en'

        self._old_pos = None  
        self.selected_datasets = []    

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
 
    def activate_(self):
        self.cancel_btn.clicked.connect(self.close_win)
        self.ok_btn.clicked.connect(self.find_selected_datasets)

    def close_win(self):
        self.close()

    def find_selected_datasets(self):
        self.selected_datasets = []
        for i in range(self.table.rowCount()):
            if (self.table.item(i, 0).checkState() == Qt.Checked):
                self.selected_datasets.append(self.table.item(i, 2).text())
        self.close_win()

    def get_select_datasets(self):
        return self.selected_datasets

if __name__ == "__main__":
    app = QApplication()
    win = Ds_selection()
    win.show()
    sys.exit(app.exec())
    

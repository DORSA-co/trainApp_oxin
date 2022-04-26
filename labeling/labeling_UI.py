import enum
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
import pandas as pd

from PyQt5.QtGui import QPainter
from labeling import labeling_api
# import labeling_api
ui, _ = loadUiType("UI/labeling.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class labeling(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self):
        super(labeling, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
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
        self.cancel_btn.clicked.connect(self.close_win)
        self.save_btn.clicked.connect(self.minimize)
        # self.maxiButton.clicked.connect(self.maxmize_minimize)

    def win_set_geometry(self,left=100, top=600, width=250, height=130):

        self.setGeometry(left, top, width, height)

 
    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def set_combobox(self,defects_list):

        self.comboBox_defects.addItems(defects_list)

        
    def set_on_top(self):
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        # self.show()
        print('set_on_top')

    def updte_table(self,records):

      

        # self.clear_table()                                                  #cleare table

        self.tableWidget_defects.setRowCount(1)           #set row count

        self.hh_Labels=['name', 'defect_ID', 'is_defect', 'group','level']
        self.tableWidget_defects.setHorizontalHeaderLabels(self.hh_Labels)
        table_item = QTableWidgetItem(str(records))

        print('roeasdawd',records[self.hh_Labels[1]])

        for row in range(len(self.hh_Labels)):
            
            table_item = QTableWidgetItem(records[self.hh_Labels[row]])
            # table_item.setData(Qt.DisplayRole, record)
            self.tableWidget_defects.setItem(0,row,table_item)



        #     print('eror')


    def get_label_name(self):

        return self.comboBox_defects.currentText()


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName =='toggleButton':
            self.toggleMenu(True)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

















#api = labeling_api.labeling_API(win)



if __name__ == "__main__":
    app = QApplication()
    win = labeling()
    api = labeling_api.labeling_API(win)
    win.show()
    sys.exit(app.exec())
    
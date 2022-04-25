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

        self.comboBox_defects.currentTextChanged.connect(self.updte_table)
        

    


    def updte_table(self,records):

        try:

            self.clear_table()                                                  #cleare table

            self.listWidget_defect.setRowCount(len(records))           #set row count



            for row,record in enumerate(records):
                # for i in range(11):
                    # print(i)
                    record = '{} - {} - {}'.format(record[0],record[1],(record[2]))
                    table_item = QTableWidgetItem(str(record))
                    # if i ==0:
                    table_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                    table_item.setData(Qt.DisplayRole, record)
                    self.listWidget_defect.setItem(row,0,table_item)
                    print(table_item)
        except:

            print('eror')


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName =='toggleButton':
            self.toggleMenu(True)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')





















if __name__ == "__main__":
    app = QApplication()
    win = labeling()
    win.show()
    sys.exit(app.exec())
    
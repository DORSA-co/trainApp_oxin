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
#import database
from trainApp_loader import database
# from modules import UIFunctions
import api

from PyQt5.QtGui import QPainter

ui, _ = loadUiType("trainApp_loader\data_loader.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class UI_data_loader(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self):
        super(UI_data_loader, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.show_dataset()
        self.table_report_request()
        self.fun_par_path()
        self.load_btn.clicked.connect(self.load)
        self.tableWidget_dataset.clicked.connect(self.show_detail)
        self.selected=-1
        self.counter=-1
        


    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        # self.maxiButton.clicked.connect(self.maxmize_minimize)

 
    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def show_detail(self):
        row = self.tableWidget_dataset.currentIndex().row()
        print(row)


    def fun_par_path(self):
        self.par_path = 'G:/oxin_image_grabber'


    def load(self):
        cont=0
        self.selected_list=[]
        for i in range(self.tableWidget_dataset.rowCount()):    
            if self.tableWidget_dataset.item(i, 0).checkState() == QtCore.Qt.Checked:
                self.selected=i
                self.selected_list.append(i)
                cont+=1
        # if cont != 1:
        #     self.detail_dataset.setText('you must select 1 coil')
        # else:
        self.detail_dataset.setText('coil {} loaded'.format(self.records[self.selected][0]))
        self.next_coil()
        print('*'*50,self.selected_list)
        self.close()
    
    
    def next_coil(self):

            print("*"*50,self.counter,len(self.selected_list))
            if self.counter<len(self.selected_list):
                self.counter+=1
                self.selected=self.selected_list[self.counter]
                self.load_images()

            print('list end')
    def prev_coil(self):
        # try:
            print("*"*50,self.counter,len(self.selected_list))
            if self.counter>=0:
                self.counter-=1
                self.selected=self.selected_list[self.counter]
                self.load_images()
            # except:
            print('list end')


    def load_images(self):
        
        self.path=os.path.join(self.par_path,str(self.records[self.selected][0]))
        print('new_path',self.path)
        self.id=str(self.records[self.selected][0])
        self.heat_no=str(self.records[self.selected][1])
        self.psn=str(self.records[self.selected][2])
        self.pdln=str(self.records[self.selected][3])
        self.lenght=str(self.records[self.selected][4])
        self.details={'id':self.id,'heat_no':self.heat_no,'psn':self.psn,'pdln':self.pdln,'lenght':self.lenght}

        


    #LOAD DATASET --------------
    def show_dataset(self):
        self.hh_Labels=['ID','HEAT No.', 'Product Schedule Number', 'Product Drift Line Number','Height']
        self.tableWidget_dataset.setHorizontalHeaderLabels(self.hh_Labels)
        # self.class_list.setColumnWidth(0,90)
        # self.class_list.setColumnWidth(1,70)
        # self.class_list.setColumnWidth(2,300)
        # self.class_list.setColumnWidth(3,50)
        header = self.tableWidget_dataset.horizontalHeader()       
        header = self.tableWidget_dataset.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)



        # print(x,y)


    def table_report_request(self):
        
        # tedad=self.spinBox_tedad.text()
        self.records=database.report_last(10)
        # print(records)
        self.tableWidget_dataset.setRowCount(len(self.records))
        # for item in self.tableWidget.selectedItems():
        #     newitem = QtGui.QTableWidgetItem(str(0))
        #     self.tableWidget.setItem(item.row(), item.column(), newitem)
        for row,string in enumerate(self.records):
            for i in range(5):
              #  print(i)
          #  print (row,string)
                table_item = QTableWidgetItem(str(string))
                table_item.setData(Qt.DisplayRole, str(string[i]))
                if i==0:
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                self.tableWidget_dataset.setItem(row,i,table_item)


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName =='toggleButton':
            self.toggleMenu(True)
        



        




        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mouseMoveEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # print(self.ret_mouse())
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
























if __name__ == "__main__":
    app = QApplication()
    win = UI_data_loader()
    win.show()
    sys.exit(app.exec())
    
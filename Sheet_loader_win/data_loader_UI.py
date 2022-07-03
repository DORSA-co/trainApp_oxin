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
#import database
import database
# from modules import UIFunctions
import api

from PyQt5.QtGui import QPainter

ui, _ = loadUiType("Sheet_loader_win/data_loader.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class data_loader(QMainWindow, ui):
    
    global widgets
    widgets = ui
    x=0

    def __init__(self):
        super(data_loader, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()


        self.set_parent_path()

        self.show_dataset()



        self.load_btn.clicked.connect(self.load)
        self.tableWidget_dataset.clicked.connect(self.show_detail)
        self.selected=-1
        self.counter=-1
        
        
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
        # self.maxiButton.clicked.connect(self.maxmize_minimize)

 
    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()




    def show_sheets_info(self,sheets):
        
        self.tableWidget_dataset.setRowCount(len(sheets))


        for row,sheet in enumerate(sheets):
            for i,(feature, value) in enumerate( sheet.get_info_dict().items()):
                table_item = QTableWidgetItem(str(feature))
                table_item.setData(Qt.DisplayRole,str(value))

                if i==0:
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                self.tableWidget_dataset.setItem(row,i,table_item)

        return 0

        n_features=len(coils_info[0])

        for row,string in enumerate(coils_info):
            for i in range(n_features):

                table_item = QTableWidgetItem(str(string))
                table_item.setData(Qt.DisplayRole, str(string[i]))
                if i==0:
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                self.tableWidget_dataset.setItem(row,i,table_item)






    def show_detail(self):
        row = self.tableWidget_dataset.currentIndex().row()
        print(row)


    def set_parent_path(self,path='D:/oxin_image_grabber'):
           # api.set_parent_path()
         self.par_path=path
        

    def get_parent_path(self):

        return self.par_path


    def load(self):
        cont=0
        self.selected_list=[]
        for i in range(self.tableWidget_dataset.rowCount()):    
            if self.tableWidget_dataset.item(i, 0).checkState() == QtCore.Qt.Checked:
                self.selected=i
                self.selected_list.append(self.tableWidget_dataset.item(i, 0).text())
                cont+=1
        # if cont != 1:
        #     self.detail_dataset.setText('you must select 1 coil')
        # else:
        #self.detail_dataset.setText('coil {} loaded'.format(self.records[self.selected][0]))

        return self.selected_list
    
    



    def get_selected_sheetid(self):
        return self.selected_list

    def load_images(self):
        
        self.path=os.path.join(self.par_path,str(self.records[self.selected][0]))
        print('new_path',self.path)
        self.coil_number=str(self.records[self.selected][0])
        self.heat_no=str(self.records[self.selected][1])
        self.psn=str(self.records[self.selected][2])
        self.pdln=str(self.records[self.selected][3])
        self.lenght=str(self.records[self.selected][4])
        self.details={'id':self.coil_number,'heat_no':self.heat_no,'psn':self.psn,'pdln':self.pdln,'lenght':self.lenght}

        


    #LOAD DATBASE --------------
    def show_dataset(self):
        self.hh_Labels=['ID','HEAT No.', 'Product Schedule Number', 'Product Drift Line Number','Height']
        self.tableWidget_dataset.setHorizontalHeaderLabels(self.hh_Labels)

        header = self.tableWidget_dataset.horizontalHeader()       
        header = self.tableWidget_dataset.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)



        # print(x,y)



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
    win = data_loader()
    win.show()
    sys.exit(app.exec())
    
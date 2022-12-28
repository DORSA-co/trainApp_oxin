import enum
import os
from select import select
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
# from pyqt5_plugins import *
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
import texts

from PyQt5.QtGui import QPainter

try:
    import database_utils
except:
    pass

ui, _ = loadUiType("Sheet_loader_win/data_loader.ui")
# ui, _ = loadUiType("UI/data_loader.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

class data_loader(QMainWindow, ui):
    
    global widgets
    widgets = ui
    x=0

    def __init__(self, main_ui_obj):
        super(data_loader, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()

        self.main_ui_obj = main_ui_obj

        self.language = 'en'

        self.set_parent_path()

        self.show_dataset()

        self.load_btn.clicked.connect(self.load)
        self.tableWidget_dataset.clicked.connect(self.show_detail)
        self.open_folder_image.clicked.connect(self.open_folder_images)
       
        self.btn_id_search.clicked.connect(self.search_id)
        self.btn_heat_search.clicked.connect(self.search_heat)
        self.btn_pdln_search.clicked.connect(self.search_pdln)
        self.btn_psn_search.clicked.connect(self.search_psn)
        
        self.selected=-1
        self.counter=-1
        
        self.tables=[self.list_show_id,self.list_heat_number,self.list_ps_number,self.list_pdl_number]

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
        if not self.isMaximized():
            self.move(self.pos() + delta)

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def maxmize_minimize(self):
        # self.show_image_in_label()
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def set_language(self, lang='en'):
        self.language = lang

    def clear_tables(self):
        for table_name in self.tables:
            table_name.clear()

    def show_sheets_info(self, sheets, full=True):
        if full:
            self.load_sheets = sheets
        self.tableWidget_dataset.setRowCount(len(sheets))

        self.clear_tables()                  # clear tables
        self.detail_dataset.setText('')

        for row,sheet in enumerate(sheets):
            print('****', sheet.get_info_dict())
            for i,(feature, value) in enumerate( sheet.get_info_dict().items()):
                table_item = QTableWidgetItem(str(feature))
                table_item.setData(Qt.DisplayRole,str(value))
                print('value',value)
                if i==0:
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                self.tableWidget_dataset.setItem(row,i,table_item)
            self.list_show_id.insertItem(row, str(sheet.sheet_id))   # add id in listwidget
            self.list_heat_number.insertItem(row, str(sheet.heat_number))   # add id in listwidget
            self.list_ps_number.insertItem(row, str(sheet.ps_number))   # add id in listwidget
            self.list_pdl_number.insertItem(row, str(sheet.pdl_number))   # add id in listwidget

        self.table_sheets = sheets

    def show_detail(self):
        text = ''
        for i in range(self.tableWidget_dataset.rowCount()):    
            if self.tableWidget_dataset.item(i, 0).checkState() == QtCore.Qt.Checked:
                text += texts.MESSEGES['sheet_details'][self.language].format(self.table_sheets[i].get_id(), self.table_sheets[i].get_time_string(), self.table_sheets[i].get_date_string(), self.table_sheets[i].get_user(), self.table_sheets[i].get_nframe(),self.table_sheets[i].get_cameras())
                text += '\n'
        self.detail_dataset.setText(text)
                
    def set_parent_path(self, path='D:/oxin_image_grabber'):
           # api.set_parent_path()
        self.db = database_utils.dataBaseUtils(ui_obj=self.main_ui_obj)


        self.par_path = self.db.get_parent_path()

    def get_parent_path(self):

        return self.par_path

    def load(self):
        self.selected_list=[]
        for i in range(self.tableWidget_dataset.rowCount()):    
            if self.tableWidget_dataset.item(i, 0).checkState() == QtCore.Qt.Checked:
                self.selected=i
                self.selected_list.append(self.tableWidget_dataset.item(i, 0).text())
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

    def open_folder_images(self):
        select=self.load()
        if len(select) != 1:
            self.set_warning(texts.WARNINGS['SELECT_SHEET'][self.language], level=2)
            return
        print('select',select,str(select[0]))
        path1= os.path.join(self.par_path,str(select[0]))
        print('path',path1)
        # import os
        try:
            if os.path.exists(path1): 
                os.system('nautilus {}'.format(path1))
            else : 
                print('Path Not Exist  {}'.format(str(path1)))
                self.set_warning(texts.ERRORS['path_not_exist'][self.language], level=3)
        except:
            print('Cant open folder')
            self.set_warning(texts.ERRORS['open_folder_failed'][self.language], level=3)

    #LOAD DATBASE --------------
    def show_dataset(self):
        self.hh_Labels=['ID', 'HEAT Number', 'Length', 'Width', 'Product Schedule Number', 'Product Drift Line Number', 'Thickness']
        self.hh_Labels_fa=['شناسه', 'شماره سفارش', 'طول', 'عرض', 'شماره سفارش', 'شماره سفارش', 'ضخامت']
        if self.language=='en':
            self.tableWidget_dataset.setHorizontalHeaderLabels(self.hh_Labels)
        if self.language=='fa':
            self.tableWidget_dataset.setHorizontalHeaderLabels(self.hh_Labels_fa)

        header = self.tableWidget_dataset.horizontalHeader()       
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def search_id(self):
        print('asd')
        itemsTextList =  [str(self.list_show_id.item(i).text()) for i in range(self.list_show_id.count())]
        print(itemsTextList)
        if self.line_search_id.text() in itemsTextList:
            print('exist')
            sheets = []
            for sheet in self.load_sheets:
                if sheet.get_id() == self.line_search_id.text():
                    sheets.append(sheet)
            self.show_sheets_info(sheets)
            self.set_warning(texts.MESSEGES['search_success'][self.language], level=1)
        else:
            self.set_warning(texts.WARNINGS['UNAV_ID'][self.language], level=2)

    def search_heat(self):
        print('asd')
        itemsTextList =  [str(self.list_heat_number.item(i).text()) for i in range(self.list_heat_number.count())]
        print(itemsTextList)
        if self.line_search_heat.text() in itemsTextList:
            print('exist')
            sheets = []
            for sheet in self.load_sheets:
                if sheet.get_heatnumber() == self.line_search_heat.text():
                    sheets.append(sheet)
            self.show_sheets_info(sheets)
            self.set_warning(texts.MESSEGES['search_success'][self.language], level=1)
        else:
            self.set_warning(texts.WARNINGS['UNAV_HEAT'][self.language], level=2)

    def search_psn(self):
        print('asd')
        itemsTextList =  [str(self.list_ps_number.item(i).text()) for i in range(self.list_ps_number.count())]
        print(itemsTextList)
        if self.line_search_psn.text() in itemsTextList:
            print('exist')
            sheets = []
            for sheet in self.load_sheets:
                print(sheet.get_psnumber())
                if sheet.get_psnumber() == self.line_search_psn.text():
                    sheets.append(sheet)
            self.show_sheets_info(sheets)
            self.set_warning(texts.MESSEGES['search_success'][self.language], level=1)
        else:
            self.set_warning(texts.WARNINGS['UNAV_PSN'][self.language], level=2)

    def search_pdln(self):
        print('asd')
        itemsTextList =  [str(self.list_pdl_number.item(i).text()) for i in range(self.list_pdl_number.count())]
        print(itemsTextList)
        if self.line_search_pdln.text() in itemsTextList:
            print('exist')
            sheets = []
            for sheet in self.load_sheets:
                if sheet.get_pdlnumber() == self.line_search_pdln.text():
                    sheets.append(sheet)
            self.show_sheets_info(sheets)
            self.set_warning(texts.MESSEGES['search_success'][self.language], level=1)
        else:
            self.set_warning(texts.WARNINGS['UNAV_PDLN'][self.language], level=2)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName =='toggleButton':
            self.toggleMenu(True)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def set_warning(self, text, name='warning', level=1):
        """Show warning with time delay 2 second , all labels for show warning has been set here"""

        waring_labels = {
            "warning": self.warning
        }
        # print('set_warning')
        if text != None:

            if level == 1:
                waring_labels[name].setText(" " + text + " ")
                waring_labels[name].setStyleSheet(
                    "background-color:#20a740;border-radius:2px;color:white"
                )

            if level == 2:
                waring_labels[name].setText(texts.WARNINGS['WARNING'][self.language] + text)
                waring_labels[name].setStyleSheet(
                    "background-color:#FDFFA9;border-radius:2px;color:black"
                )

            if level >= 3:
                waring_labels[name].setText(texts.ERRORS['ERROR'][self.language] + text)
                waring_labels[name].setStyleSheet(
                    "background-color:#D9534F;border-radius:2px;color:black"
                )
            QTimer.singleShot(2000, lambda: self.set_warning(None, name))

        else:
            waring_labels[name].setText("")
            waring_labels[name].setStyleSheet("")






















if __name__ == "__main__":
    app = QApplication()
    win = data_loader()
    win.show()
    sys.exit(app.exec())
    
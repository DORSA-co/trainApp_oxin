from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
import sqlite3
from sqlite3 import Error

from PySide6.QtCore import *

from PySide6.QtWidgets import *


# def set_stack_widget(self):
#     # self.stackedWidget_defect.setCurrentWidget(self.page_yes)
#     self.stackedWidget.setCurrentWidget(self.page_software_setting)


class setting_window():

    def __init__(self) :
        
        pass
    def language(self):
        x=['English','Persian(فارسی)','Russian']
        self.comboBox_10.addItems(x)
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from language')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    
        self.comboBox_23.setCurrentText(str(rec[0][0]))

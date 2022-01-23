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
from app_settings import Settings
from backend import data_grabber
import detect_lenguage
import setting
import api
from trainApp_loader.data_loader import UI_data_loader
from PIL import ImageQt
import numpy as np

# from modules import UIFunctions

import cv2
import time

from PyQt5.QtGui import QPainter

ui, _ = loadUiType("oxin.ui")
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x=0

    def __init__(self):
        super(UI_main_window, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.toggleButton.clicked.connect(self.buttonClick)


        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "SABA - trainer"
        description = "PyDracula APP - Theme with colors based on Dracula for Python."
        # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)
        self.test()
        
        # SET LANGUAGE
        #//////////////////////////////////////////////
        # self.set_language()

        # self.toggleButton.clicked.connect(self.toggleMenu(True))



        # CONNECTED WINDOWS
        #//////////////////////////////////////////////
        self.win=UI_data_loader()





        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            self.theme(themeFile, True)

            # SET HACKS
            self.setThemeHack()


        #/////////Setting
        self.btn_software_setting.clicked.connect(self.buttonClick)
        
        
        self.x,self.y,self.status,self.widget_name=-1,-1,'',''
        # #left bar click
        self.Data_auquzation_btn.clicked.connect(self.buttonClick)
        self.label_btn.clicked.connect(self.buttonClick)
        self.tuning_btn.clicked.connect(self.buttonClick)
        self.pbt_btn.clicked.connect(self.buttonClick)
        
        # extra left bar
        # #---------------
        self.Binary_btn.clicked.connect(self.buttonClick)
        self.Localization_btn.clicked.connect(self.buttonClick)
        self.Classification_btn.clicked.connect(self.buttonClick)
        # self.stackedWidget.setCurrentWidget(self.page_live)

        # binary page
        self.binary_list.clicked.connect(self.buttonClick)
        self.binary_training.clicked.connect(self.buttonClick)
        self.binary_history.clicked.connect(self.buttonClick)
        # localization page
        self.localization_Statistic.clicked.connect(self.buttonClick)
        self.localization_training.clicked.connect(self.buttonClick)
        self.localization_history.clicked.connect(self.buttonClick)
        # classification page
        self.classification_class_list.clicked.connect(self.buttonClick)
        self.classification_add_new_class.clicked.connect(self.buttonClick)
        self.classification_training.clicked.connect(self.buttonClick)       
        self.classification_history.clicked.connect(self.buttonClick)     

        self.yes_defect.clicked.connect(self.buttonClick) 
        self.no_defect.clicked.connect(self.buttonClick) 
       # login btn
        self.login_btn.clicked.connect(self.buttonClick) 
        self.setting_btn.clicked.connect(self.buttonClick) 

        # labeling

        self.polygon_btn.clicked.connect(self.buttonClick) 
        self.bounding_btn.clicked.connect(self.buttonClick) 
        # QPixmap pixmapTarget = QPixmap(":/icons/images/icons/2png);
        # pixmapTarget = pixmapTarget.scaled(size-5, size-5, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        # ui->label_image_power->setPixmap(pixmapTarget );
        self.classification_class_list_table()


        #data aquization page
        self.load_coil_btn.clicked.connect(self.buttonClick)
        self.label_btn_2.clicked.connect(self.buttonClick)
        self.next_coil_btn.clicked.connect(self.buttonClick)
        self.prev_coil_btn.clicked.connect(self.buttonClick)

        

        
        
        
        
        


    def ret_mouse(self):
        x,y,widget_name,status = self.x,self.y,self.widget_name,self.status
        self.x,self.y,self.widget_name,self.status = -1,-1,'',''
        return (x,y),widget_name,status



    #///////////////////// LANGUAGE
    def set_language(self):
        print(detect_lenguage.language())
        if detect_lenguage.language()=='Persian(فارسی)':
            print('salam')
            detect_lenguage.main_window(self)
    
    
    def set_img_sheet(self,img,side):
        if side=="up":
            image = QImage(img,img.shape[1], img.shape[0],img.strides[0], QImage.Format_BGR888 )
            self.up_side_technical.setPixmap(QPixmap.fromImage(image))
        if side=="down":
            image = QImage(img,img.shape[1], img.shape[0],img.strides[0], QImage.Format_BGR888 )
            self.down_side_technical.setPixmap(QPixmap.fromImage(image))

    def set_crop_image(self,img):

        image = QImage(img,img.shape[1], img.shape[0],img.strides[0], QImage.Format_BGR888 )
        self.crop_image_up.setPixmap(QPixmap.fromImage(image))
        # cv2.waitKey(200)


    #/////////////////// end


    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                print('OPEN')
                self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t2.png);")
                widthExtended = maxExtend
                print(widthExtended)
            else:
                self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t1.png);")
                print('Close')
                widthExtended = standard
                print(widthExtended)

            # ANIMATION
            self.animation = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
 
    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def hi(self):
        print('asdw')
        # GET WIDTH
        width = self.extraLeftBox.width()
        widthRightBox = 0
        maxExtend = Settings.LEFT_BOX_WIDTH
        color = Settings.BTN_LEFT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
        style = self.toggleLeftBox.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            # SELECT BTN
            self.toggleLeftBox.setStyleSheet(style + color)
            if widthRightBox != 0:
                style = self.settingsTopBtn.styleSheet()
                # self.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            # RESET BTN
            self.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        self.start_box_animation(width, widthRightBox, "left")

 
    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 120
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       
        print('ok')
        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
        print('ok',left_width)
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        # self.group.addAnimation(self.right_box)
        self.group.start()

        


 
    # TOGGLE Yes_defect
    # /////////////////////////////////////////////////////////////// 
    def def_yes_defect(self):
        self.stackedWidget_defect.setCurrentWidget(self.page_yes)
        self.stackedWidget_defect.setMaximumHeight(166666)
        x=self.stackedWidget_defect.height()
        if x <70:
            print('x',x)
            self.left_box = QPropertyAnimation(self.stackedWidget_defect, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(60)
            self.left_box.setEndValue(400)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart) 
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()       
    
 
 
    def def_no_defect(self):
        self.stackedWidget_defect.setCurrentWidget(self.page_no)
        self.stackedWidget_defect.setMaximumHeight(60)
        x=self.stackedWidget_defect.height()
        print('height',x)
        # if x ==400:
        self.left_box = QPropertyAnimation(self.stackedWidget_defect, b"maximumHeight")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(400)
        self.left_box.setEndValue(60)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart) 
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        # self.group.addAnimation(self.right_box)
        self.group.start()    
        print('no ani')   

 
    # TOGGLE LOGIN & setting
    # ///////////////////////////////////////////////////////////////

    def show_login(self):
        width=self.frame_login.width()
        print('width',width)
        if width==0:
            self.left_box = QPropertyAnimation(self.frame_login, b"maximumWidth")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(width)
            self.left_box.setEndValue(600)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)  
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            print('open')
            # self.group.addAnimation(self.right_box)
            self.group.start()       
        else :
            self.left_box = QPropertyAnimation(self.frame_login, b"maximumWidth")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(width)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            print('close')
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()

    def setting_win(self):
        height=self.frame_settin2.height()
        # self.stackedWidget_defect.setCurrentWidget(self.page_no)
        # self.stackedWidget_defect.setMaximumHeight(60)
        # x=self.stackedWidget_defect.height()
        print('height',height)
        if height ==0:
            self.left_box = QPropertyAnimation(self.frame_settin2, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(0)
            self.left_box.setEndValue(40)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart) 
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()    
            print('no ani')
        elif height ==40:
            self.left_box = QPropertyAnimation(self.frame_settin2, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(40)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart) 
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()    
            print('no ani')           
        

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.styleSheet.setStyleSheet(str)


    def setThemeHack(self):
        print('asdaw')
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.pushButton.setStyleSheet("background-color: #6272a4;")
        self.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.comboBox.setStyleSheet("background-color: #6272a4;")
        self.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.leftMenuFrame.setStyleSheet("color: #ff79c6;")
        print('asdaw')

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

 
    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()
        sys.exit()

    def maxmize_minimize(self):
        
        if self.isMaximized():
            self.showNormal()
            # self.sheet_view_down=data_grabber.sheetOverView(h=129,w=1084,nh=12,nw=30)
        else:
            self.showMaximized()

    def left_bar_clear(self):
            self.Data_auquzation_btn.setStyleSheet("background-image: url(:/icons/images/icons/graber.png);")
            self.label_btn.setStyleSheet("background-image: url(:/icons/images/icons/label.png);")
            self.tuning_btn.setStyleSheet("background-image: url(:/icons/images/icons/tuning.png);")
            self.pbt_btn.setStyleSheet("background-image: url(:/icons/images/icons/pbt.png);")
            # self.page_aboutus_btn.setStyleSheet("QPushButton {background-color: rgb(100,100,100);;	color: rgb(0,0,0);	border: none;	text-align: left;padding-left: 10px;}QPushButton:hover {background-color:  rgb(197 , 195,196)};QPushButton:pressed {background-color: rgb(197 , 195,196);}")
              

    def test(self):
        input_image = cv2.imread('1.jpg')
        self.input_image=input_image
        image = QImage(input_image,input_image.shape[1], input_image.shape[0],input_image.strides[0], QImage.Format_BGR888 )
        self.image.setPixmap(QPixmap.fromImage(image))
        input_image = cv2.imread('2.jpg')
        image = QImage(input_image,input_image.shape[1], input_image.shape[0],input_image.strides[0], QImage.Format_BGR888 )
        self.n_image.setPixmap(QPixmap.fromImage(image))
        input_image = cv2.imread('3.jpg')
        image = QImage(input_image,input_image.shape[1], input_image.shape[0],input_image.strides[0], QImage.Format_BGR888 )
        self.p_image.setPixmap(QPixmap.fromImage(image))
        print(image)


    def classification_class_list_table(self):
        self.hh_Labels=['No', 'Date', 'Name', 'Short name','ID','Is Defect','Group','Level','Color','Number','Percentage']
        self.class_list.setHorizontalHeaderLabels(self.hh_Labels)
        # self.class_list.setColumnWidth(0,90)
        # self.class_list.setColumnWidth(1,70)
        # self.class_list.setColumnWidth(2,300)
        # self.class_list.setColumnWidth(3,50)
        # self.class_list.setColumnWidth(4,50)
        # self.class_list.setColumnWidth(5,50)
        # self.class_list.setColumnWidth(6,50)
        # self.class_list.setColumnWidth(7,150)
        # self.class_list.setColumnWidth(8,280)
        header = self.class_list.horizontalHeader()       
        header = self.class_list.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)


    def table_classification_select_class(self):
        print('asd')


#--------- label page
    def bounding_box(self):
        print('bounding_box')
        self.image.setCursor(Qt.CrossCursor)


    def polygon(self):
        print('polygon')
        pixmap = QPixmap("images/icons8-cursor-24.png")
        cursor = QCursor(pixmap, 5,5)
        # QApplication.setOverrideCursor(cursor)
        self.image.setCursor(cursor)



    def data_loader_win(self):
        print('show loader win')
        self.win.show()



        # print(x,y)


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName =='toggleButton':
            self.toggleMenu(True)
        
        if btnName =='Data_auquzation_btn':
            self.left_bar_clear()
            self.Data_auquzation_btn.setStyleSheet("background-image: url(:/icons/images/icons/graber.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            self.stackedWidget.setCurrentWidget(self.page_data_auquzation)
        if btnName =='label_btn':
            self.left_bar_clear()
            self.label_btn.setStyleSheet("background-image: url(:/icons/images/icons/label.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            self.stackedWidget.setCurrentWidget(self.page_label)
        if btnName =='tuning_btn':
            self.left_bar_clear()
            self.tuning_btn.setStyleSheet("background-image: url(:/icons/images/icons/tuning.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            # self.stackedWidget.setCurrentWidget(self.page_tuning)
            self.hi()

        if btnName =='pbt_btn':
            self.left_bar_clear()
            self.pbt_btn.setStyleSheet("background-image: url(:/icons/images/icons/pbt.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            self.stackedWidget.setCurrentWidget(self.page_pbt)
        if btnName =='aboutus_btn':
            self.left_bar_clear()
            # self.page_aboutus_btn.setStyleSheet("QPushButton {background-color: rgb(197 , 195,196);	color: rgb(0,0,0);	border: none;	text-align: left;padding-left: 10px;}QPushButton:hover {background-color:  rgb(197 , 195,196)};QPushButton:pressed {background-color: rgb(197 , 195,196);}")
            self.stackedWidget.setCurrentWidget(self.page_aboutus)

        if btnName =='Binary_btn':
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            self.stackedWidget.setCurrentWidget(self.page_Binary)


        if btnName =='Localization_btn':
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            self.stackedWidget.setCurrentWidget(self.page_Localization)

        if btnName =='Classification_btn':
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            self.stackedWidget.setCurrentWidget(self.page_Classification)
        
        if btnName =='binary_list':
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_list)
        
        if btnName =='binary_training':
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_training)
        
        if btnName =='binary_history':
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_history)
        
        if btnName =='localization_Statistic':
            self.stackedWidget_localization.setCurrentWidget(self.page_localization_statics)
        
        if btnName =='localization_training':
            self.stackedWidget_localization.setCurrentWidget(self.page_localization_training)
        
        if btnName =='localization_history':
            self.stackedWidget_localization.setCurrentWidget(self.page_localization_history)
 
        if btnName =='classification_class_list':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_class_list)
        
        if btnName =='classification_add_new_class':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_add_new_class)
        
        if btnName =='classification_training':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_training)
       
        if btnName =='classification_history':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_history)
     
        if btnName =='yes_defect':
            self.def_yes_defect()

        if btnName =='no_defect':
            self.def_no_defect()

        if btnName =='login_btn':
            self.show_login()

        if btnName =='setting_btn':
            self.setting_win()

        if btnName =='polygon_btn':
            self.polygon()

        if btnName =='bounding_btn':
            self.bounding_box()

        if btnName =='btn_software_setting':
            print('asdqwdwqd')
            # self.bounding_box()
            self.stackedWidget.setCurrentWidget(self.page_software_setting)
            setting.language(self)
            # self.stackedWidget.setCurrentWidget(self.page_software_setting)

        if btnName =='load_coil_btn':
            # print('asdqwdwqd')
            self.data_loader_win()

        if btnName =='next_coil_btn':
            # print('asdqwdwqd')
            api.next_coil()

        if btnName =='prev_coil_btn':
            # print('asdqwdwqd')
            api.prev_coil()

        if btnName =='label_btn_2':
            self.stackedWidget.setCurrentWidget(self.page_label)
            image = ImageQt.fromqpixmap(self.crop_image_up.pixmap())
            image=np.ascontiguousarray(image)
            self.fs = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )           
            self.image.setPixmap(QPixmap.fromImage(self.fs)) 






        if self.extraLeftBox.width()!=0:
            self.hi()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mouseMoveEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        print(self.ret_mouse())
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
























if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    api = api.API(win)
    win.show()
    sys.exit(app.exec())
    
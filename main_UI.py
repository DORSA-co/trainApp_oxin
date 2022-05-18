import re
from cgitb import enable
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
import PySide6.QtGui as PG
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
import pandas as pd
from functools import partial

# from pytools import F

from FileDialog import FileDialog
from app_settings import Settings
from backend import data_grabber, chart_funcs , camera_connection
import detect_lenguage
import setting
import api
from Sheet_loader_win.data_loader_UI import data_loader
from labeling.labeling_UI import labeling
from neighbouring_UI import neighbouring
from labeling import labeling_api
from PIL import ImageQt
import numpy as np
import threading
# from modules import UIFunctions

import cv2
import time

from PyQt5.QtGui import QPainter

from consts.keyboards_keys import KEYS
from consts.pages_indexs import PAGES_IDX
import texts




ui, _ = loadUiType("UI/oxin.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

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
        # self.test()

        # SET LANGUAGE
        # //////////////////////////////////////////////
        # self.set_language()
        self.language = 'en'

        # SET FONT & SIZE
        # /////////////////////////////////////////////
        # self.label_6.setFont(QFont('Arial', 10))

        # self.toggleButton.clicked.connect(self.toggleMenu(True))

        # CONNECTED WINDOWS
        #//////////////////////////////////////////////
        self.load_sheets_win=data_loader()

        # self.labeling_win=labeling()
        # labeling_api.labeling_API(self.labeling_win)
        self.labeling_win=None



        # self.labeling_win=labeling()
        # labeling_api.labeling_API(self.labeling_win)
        self.labeling_win = None

        self.labeling_win = labeling()
        # labeling_api.labeling_API(self.labeling_win)

        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            self.theme(themeFile, True)

            # SET HACKS
            self.setThemeHack()

        self.label_dorsa_open(enable=True)
        # /////////Setting
        self.btn_software_setting.clicked.connect(self.buttonClick)

        self.x, self.y, self.status, self.widget_name = -1, -1, '', ''
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
        self.zoomIn_btn.clicked.connect(self.buttonClick)
        self.zoomOut_btn.clicked.connect(self.buttonClick)
        self.drag_btn.clicked.connect(self.buttonClick)
        # self.add_label.clicked.connect(self.buttonClick)
        self.add_label_btn.clicked.connect(self.buttonClick)

        # QPixmap pixmapTarget = QPixmap(":/icons/images/icons/2png);
        # pixmapTarget = pixmapTarget.scaled(size-5, size-5, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        # ui->label_image_power->setPixmap(pixmapTarget );
        self.classification_class_list_table()

        # data aquization page
        self.load_coil_btn.clicked.connect(self.buttonClick)

        self.next_coil_btn.clicked.connect(self.buttonClick)
        self.prev_coil_btn.clicked.connect(self.buttonClick)
        self.checkBox_select.clicked.connect(self.buttonClick)

        self.show_tools_btn.clicked.connect(self.buttonClick)

        self.keyboard_connections = {}
        self.label_type = 'mask'
        self.zoom_type = None

        self.img = cv2.imread('images/dorsa-logo.png')
        self.set_crop_image(self.img)



        self.set_combo_boxes()


        # Training_page

        self.init_training_page()
        self.b_add_ds.clicked.connect(self.buttonClick)
        self.b_add_cancel.clicked.connect(self.buttonClick)

        self._old_pos = None


        # charts ---------------------------------------------------------------------------------------------
        self.chart_names = ['loss','accuracy', 'recall', 'precision']
        # binary chart
        # accuracy
        chart_funcs.create_train_chart_on_ui(ui_obj=self, frame_obj=self.binary_chart_loss_frame, chart_postfix=self.chart_names[0],
                                                chart_title='Loss', legend_train='Train', legend_val='Validation',
                                                axisX_title='Epoch', axisY_title='Loss', checkbox_obj=self.binary_chart_checkbox, legend_visible=False, axisY_set_range=False)

        chart_funcs.create_train_chart_on_ui(ui_obj=self, frame_obj=self.binary_chart_acc_frame, chart_postfix=self.chart_names[1],
                                                chart_title='Accuracy', legend_train='Train', legend_val='Validation',
                                                axisX_title='Epoch', axisY_title='Accuracy', checkbox_obj=self.binary_chart_checkbox)
        # precission
        chart_funcs.create_train_chart_on_ui(ui_obj=self, frame_obj=self.binary_chart_prec_frame, chart_postfix=self.chart_names[2],
                                                chart_title='Precision', legend_train='Train', legend_val='Validation',
                                                axisX_title='Epoch', axisY_title='Precision', checkbox_obj=self.binary_chart_checkbox)
        # recall
        chart_funcs.create_train_chart_on_ui(ui_obj=self, frame_obj=self.binary_chart_recall_frame, chart_postfix=self.chart_names[3],
                                                chart_title='Recall', legend_train='Train', legend_val='Validation',
                                                axisX_title='Epoch', axisY_title='Recall', checkbox_obj=self.binary_chart_checkbox, axisX_visible=True)

        # ----------------------------------------------------------------------------------------------------



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

    def get_technical(self, name=True):
        if name:
            return {self.up_side_technical.objectName(): self.up_side_technical,
                    self.down_side_technical.objectName(): self.down_side_technical}

        else:
            return {'up': self.up_side_technical,
                    'down': self.down_side_technical}

    def get_technical_wgt_side(self, wgt_name):
        if wgt_name == self.down_side_technical.objectName():
            return 'down'

        elif wgt_name == self.up_side_technical.objectName():
            return 'up'

    def ret_mouse(self):
        x, y, widget_name, status = self.x, self.y, self.widget_name, self.status
        self.x, self.y, self.widget_name, self.status = -1, -1, '', ''
        return (x, y), widget_name, status

    # ///////////////////// LANGUAGE
    def set_language(self):
        print(detect_lenguage.language())
        if detect_lenguage.language() == 'Persian(فارسی)':
            detect_lenguage.main_window(self)

    def set_img_sheet(self, img, side):
        if side == "up" or side == self.up_side_technical.objectName():
            image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
            self.up_side_technical.setPixmap(QPixmap.fromImage(image))
        if side == "down" or side == self.down_side_technical.objectName():
            image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
            self.down_side_technical.setPixmap(QPixmap.fromImage(image))

    def set_crop_image(self, img):

        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
        self.crop_image.setPixmap(QPixmap.fromImage(image))
        # cv2.waitKey(200)

    def set_enabel(self, widget, status):
        widget.setDisabled(not (status))
        # /////////////////// end

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
                # print('OPEN')
                self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t2.png);")
                widthExtended = maxExtend
                # print(widthExtended)
            else:
                self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t1.png);")
                # print('Close')
                widthExtended = standard
                # print(widthExtended)

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
            # print('ok')
        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
        # print('ok',left_width)
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        # self.group.addAnimation(self.right_box)
        self.group.start()

    # Label Dorsa
    # ///////////////////////////////////////////////     
    def label_dorsa_open(self, enable):
        if enable:
            # GET WIDTH
            width = self.label_dorsa.width()
            maxExtend = 150
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                # print('OPEN')
                # self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t2.png);")
                widthExtended = maxExtend
                # print(widthExtended)
            else:
                # self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t1.png);")
                # print('Close')
                widthExtended = standard
                # print(widthExtended)

            # ANIMATION
            self.animation = QPropertyAnimation(self.label_dorsa, b"minimumWidth")
            self.animation.setDuration(1200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE Yes_defect
    # /////////////////////////////////////////////////////////////// 
    def def_yes_defect(self):
        self.stackedWidget_defect.setCurrentWidget(self.page_yes)
        self.stackedWidget_defect.setMaximumHeight(166666)
        x = self.stackedWidget_defect.height()
        if x < 70:
            # print('x',x)
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
        x = self.stackedWidget_defect.height()
        # print('height',x)
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
        # print('no ani')

    # TOGGLE LOGIN & setting
    # ///////////////////////////////////////////////////////////////

    def show_login(self):
        width = self.frame_login.width()
        # print('width',width)
        if width == 0:
            self.left_box = QPropertyAnimation(self.frame_login, b"maximumWidth")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(width)
            self.left_box.setEndValue(600)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # print('open')
            # self.group.addAnimation(self.right_box)
            self.group.start()
        else:
            self.left_box = QPropertyAnimation(self.frame_login, b"maximumWidth")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(width)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            # print('close')
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()

    def setting_win(self):
        height = self.frame_settin2.height()
        # self.stackedWidget_defect.setCurrentWidget(self.page_no)
        # self.stackedWidget_defect.setMaximumHeight(60)
        # x=self.stackedWidget_defect.height()
        # print('height',height)
        if height == 0:
            self.left_box = QPropertyAnimation(self.frame_settin2, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(0)
            self.left_box.setEndValue(40)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()
            # print('no ani')
        elif height == 40:
            self.left_box = QPropertyAnimation(self.frame_settin2, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(40)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            # self.group.addAnimation(self.right_box)
            self.group.start()
            # print('no ani')

    # frame tools   ////////////////////////////////////
    def show_frame_tools(self):
        height = self.frame_tools_technical.height()
        if height == 0:
            self.group = QParallelAnimationGroup()
            for f in ([b"minimumHeight", b"maximumHeight"]):
                left_box = QPropertyAnimation(self.frame_tools_technical, f)
                left_box.setDuration(Settings.TIME_ANIMATION)
                left_box.setStartValue(0)
                left_box.setEndValue(220)
                left_box.setEasingCurve(QEasingCurve.InOutQuart)

                self.group.addAnimation(left_box)

            rMyIcon = QPixmap("images\icons\cil-arrow-bottom.png")
            self.show_tools_btn.setIcon(QIcon(rMyIcon))

            self.group.start()

        elif height == 220:
            self.group = QParallelAnimationGroup()
            for f in ([b"minimumHeight", b"maximumHeight"]):
                left_box = QPropertyAnimation(self.frame_tools_technical, f)
                left_box.setDuration(Settings.TIME_ANIMATION)
                left_box.setStartValue(220)
                left_box.setEndValue(0)
                left_box.setEasingCurve(QEasingCurve.InOutQuart)

                self.group.addAnimation(left_box)

            rMyIcon = QPixmap("images\icons\cil-arrow-top.png")
            self.show_tools_btn.setIcon(QIcon(rMyIcon))

            self.group.start()

            # IMPORT THEMES FILES QSS/CSS

    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.styleSheet.setStyleSheet(str)

    def setThemeHack(self):
        # print('asdaw')
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
        self.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.comboBox.setStyleSheet("background-color: #6272a4;")
        self.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.leftMenuFrame.setStyleSheet("color: #ff79c6;")

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
        self.show_image_in_label()
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
        self.input_image = input_image
        image = QImage(input_image, input_image.shape[1], input_image.shape[0], input_image.strides[0],
                       QImage.Format_BGR888)
        self.image.setPixmap(QPixmap.fromImage(image))
        input_image = cv2.imread('2.jpg')
        image = QImage(input_image, input_image.shape[1], input_image.shape[0], input_image.strides[0],
                       QImage.Format_BGR888)
        self.n_image.setPixmap(QPixmap.fromImage(image))
        input_image = cv2.imread('3.jpg')
        image = QImage(input_image, input_image.shape[1], input_image.shape[0], input_image.strides[0],
                       QImage.Format_BGR888)
        self.p_image.setPixmap(QPixmap.fromImage(image))
        # print(image)

    def classification_class_list_table(self):
        self.hh_Labels = ['No', 'Date', 'Name', 'Short name', 'ID', 'Is Defect', 'Group', 'Level', 'Color', 'Number',
                          'Percentage']
        self.class_list.setHorizontalHeaderLabels(self.hh_Labels)

        header = self.class_list.horizontalHeader()
        header = self.class_list.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def get_label_type(self):
        return self.label_type

    def get_zoom_type(self):
        return self.zoom_type

    def get_size_label_image(self):

        return self.image.height(), self.image.width()

    # --------- aquization page
    # def show_coil_loaded(self,name):
    #     self.listWidget_logs.addItem('Sheet {} Selected'.format(name))

    # def add_selected_image(self,selected):

    # for i in range(len(selected)):

    #     self.listWidget_append_img_list.addItem(texts.MESSEGES['SELECT_IMAGE'][self.language].format(selected[i]))

    def add_selected_image(self, records):

        self.checkBox_select.setChecked(False)  # set check statet false

        self.clear_table()  # cleare table

        self.listWidget_append_img_list.setRowCount(len(records))  # set row count

        for row, record in enumerate(records):
            # for i in range(11):
            # print(i)
            record = '{} - {} - {}'.format(record[0], record[1], (record[2]))
            table_item = QTableWidgetItem(str(record))
            # if i ==0:
            table_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            table_item.setCheckState(Qt.CheckState.Unchecked)
            table_item.setData(Qt.DisplayRole, record)
            self.listWidget_append_img_list.setItem(row, 0, table_item)
            print(table_item)

    def get_selected_img(self):
        selected_list = []
        for i in range(self.listWidget_append_img_list.rowCount()):
            if self.listWidget_append_img_list.item(i, 0).checkState() == QtCore.Qt.Checked:
                if i >= 0:
                    selected_list.append(i)

        return selected_list

    def clear_table(self):

        for i in range(self.listWidget_append_img_list.rowCount()):
            self.listWidget_append_img_list.removeRow(0)

    def select_unselect_all(self):
        if self.checkBox_select.isChecked():
            for i in range(self.listWidget_append_img_list.rowCount()):
                self.listWidget_append_img_list.item(i, 0).setCheckState(Qt.CheckState.Checked)

        else:
            for i in range(self.listWidget_append_img_list.rowCount()):
                self.listWidget_append_img_list.item(i, 0).setCheckState(Qt.CheckState.Unchecked)

    def show_selected_side(self, name):
        if name == 'up_side_technical':
            self.show_side.setText('UP Side Technical')

        if name == 'down_side_technical':
            self.show_side.setText('DOWN Side Technical')

    # --------- label page
    def bounding_box(self):
        # print('bounding_box')
        self.image.setCursor(Qt.CrossCursor)
        self.zoom_type = None
        self.label_type = 'bbox'

        self.tabWidget_defect.setCurrentIndex(1)

    def polygon(self):
        # print('polygon')
        # pixmap = QPixmap("images/icons8-cursor-24.png")
        # cursor = QCursor(pixmap, 5,5)
        # # QApplication.setOverrideCursor(cursor)
        # self.image.setCursor(cursor)

        self.image.setCursor(Qt.ArrowCursor)
        self.zoom_type = None
        self.label_type = 'mask'

        self.tabWidget_defect.setCurrentIndex(0)

    def zoom_in(self):
        cursor = PG.QPixmap('/home/reyhane/PycharmProjects/trainApp_oxin2/images/zoom-in_cursor.png')
        cursor = cursor.scaled(25, 25, Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setCursor(PG.QCursor(cursor))

        self.zoom_type = 'zoom_in'

    def zoom_out(self):
        cursor = PG.QPixmap('/home/reyhane/PycharmProjects/trainApp_oxin2/images/zoom-out_cursor.png')
        cursor = cursor.scaled(25, 25, Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setCursor(PG.QCursor(cursor))

        self.zoom_type = 'zoom_out'

    def drag_image(self):
        self.image.setCursor(Qt.OpenHandCursor)
        self.zoom_type = 'drag'

    def data_loader_win_show(self):
        self.label_type = 'mask'

        self.load_sheets_win.show()

        # print(x,y)

    def ret_create_labeling(self):
        self.labeling_win = labeling()
        return self.labeling_win
        # self.labeling_win_show()

    def show_labels(self, labels, label_type):

        LABEL_TABLE = {'mask': self.mask_table_widget, 'bbox': self.bbox_table_widget}

        print('labe', label_type)

        self.clear_table()  # cleare table

        LABEL_TABLE[label_type].setRowCount(len(labels))  # set row count

        for row in range(len(labels)):
            table_item = QTableWidgetItem(str(labels[row][0]))
            LABEL_TABLE[label_type].setItem(row, 0, table_item)

        self.labeling_win.show()

    def show_neighbouring(self, img):
        self.n = neighbouring(img)
        self.n.show()

    def show_sheet_details(self, details):

        text = '  id: ' + str(details['sheet_id']) + ' || heat_number: ' + str(
            details['heat_number']) + ' || width: ' + str(details['width']) + ' || lenght: ' + str(details['lenght'])

        self.details_label.setText(text)

    def set_warning(self, text, name, level=1):
        waring_labels = {
            'data_auquzation': self.warning_data_page,
            'label': self.warning_label_page,
            'train': self.warning_train_page,
            'camera_connection':self.camera_connection_msg
        }
        # print('set_warning')
        if text != None:
    
            if level == 1:
                waring_labels[name].setText(' ' + text + ' ')
                waring_labels[name].setStyleSheet('background-color:#20a740;border-radius:10px;color:white')

            if level == 2:
                waring_labels[name].setText(' Warning: ' + text)
                waring_labels[name].setStyleSheet('background-color:#FDFFA9;border-radius:2px;color:black')

            if level == 3:
                waring_labels[name].setText(' EROR : ' + text)
                waring_labels[name].setStyleSheet('background-color:#D9534F;border-radius:2px;color:black')

            threading.Timer(2, self.set_warning, args=(None, name)).start()




        else:
            waring_labels[name].setText('')
            waring_labels[name].setStyleSheet('')

    def show_question(self, title, message):
        msg = QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            return True
        if msg == QMessageBox.No:
            return False

    def show_current_position(self, pt):
        self.current_pos_x.setText(str(pt[0]))
        self.current_pos_y.setText(str(pt[1]))

    def show_label_page(self):
        self.left_bar_clear()
        self.label_btn.setStyleSheet(
            "background-image: url(:/icons/images/icons/label.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
        self.stackedWidget.setCurrentWidget(self.page_label)

    def show_image_in_label(self, img=None, scale=1, position=(0, 0)):
        if img is None:
            img = api.get_image()
            if img is None:
                return
        self.next_img_label_btn.setEnabled(True)
        self.prev_img_label_btn.setEnabled(True)
        self.zoomIn_btn.setEnabled(True)
        self.zoomOut_btn.setEnabled(True)
        self.drag_btn.setEnabled(True)
        self.polygon_btn.setEnabled(True)
        self.bounding_btn.setEnabled(True)
        self.delete_btn.setEnabled(True)
        self.heatmap_btn.setEnabled(True)
        self.fs = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
        if scale == 1:
            self.image.setScaledContents(True)
            self.image.setPixmap(QPixmap.fromImage(self.fs))
        else:
            self.fs = self.fs.scaled(self.image.size() * scale)
            # self.image.setPixmap(QPixmap.fromImage(self.fs).scaled(self.image.size() * scale))
            position = self.update_image(position)

        return position

    def show_image_in_neighbour_labels(self, imgs):
        image_ul = imgs[0]
        self.image_up_left.setPixmap(QPixmap.fromImage(
            QImage(image_ul, image_ul.shape[1], image_ul.shape[0], image_ul.strides[0], QImage.Format_BGR888)))

        image_u = imgs[1]
        self.image_up.setPixmap(QPixmap.fromImage(
            QImage(image_u, image_u.shape[1], image_u.shape[0], image_u.strides[0], QImage.Format_BGR888)))

        image_ur = imgs[2]
        self.image_up_right.setPixmap(QPixmap.fromImage(
            QImage(image_ur, image_ur.shape[1], image_ur.shape[0], image_ur.strides[0], QImage.Format_BGR888)))

        image_l = imgs[3]
        self.image_left.setPixmap(QPixmap.fromImage(
            QImage(image_l, image_l.shape[1], image_l.shape[0], image_l.strides[0], QImage.Format_BGR888)))

        image_r = imgs[4]
        self.image_right.setPixmap(QPixmap.fromImage(
            QImage(image_r, image_r.shape[1], image_r.shape[0], image_r.strides[0], QImage.Format_BGR888)))

        image_bl = imgs[5]
        self.image_bottom_left.setPixmap(QPixmap.fromImage(
            QImage(image_bl, image_bl.shape[1], image_bl.shape[0], image_bl.strides[0], QImage.Format_BGR888)))

        image_b = imgs[6]
        self.image_bottom.setPixmap(QPixmap.fromImage(
            QImage(image_b, image_b.shape[1], image_b.shape[0], image_b.strides[0], QImage.Format_BGR888)))

        image_br = imgs[7]
        self.image_bottom_right.setPixmap(QPixmap.fromImage(
            QImage(image_br, image_br.shape[1], image_br.shape[0], image_br.strides[0], QImage.Format_BGR888)))

    def update_image(self, position):
        pixmap = QPixmap(self.image.size())
        px, py = position
        px = px if (px <= self.fs.width() - self.image.width()) else (
                self.fs.width() - self.image.width())
        py = py if (py <= self.fs.height() - self.image.height()) else (
                self.fs.height() - self.image.height())
        px = px if (px >= 0) else 0
        py = py if (py >= 0) else 0
        position = (px, py)

        painter = QPainter()
        painter.begin(pixmap)
        painter.drawImage(QPoint(0, 0), self.fs,
                          QRect(position[0], position[1], self.image.width(),
                                self.image.height()))
        painter.end()

        self.image.setPixmap(pixmap)

        return position

    ######## Training Page

    def init_training_page(self):

        b_algorithms = ['Xbc', 'Rbe']  # Must change
        self.b_algorithms.addItems(b_algorithms)
        self.set_default_parms()

        # self.b_algorithms.setCurrentText(str(records[0][0]))   #Must change

    def set_default_parms(self):

        b_parms = {'algorithm_name': 'Xbc', 'input_type': True, 'epochs': '2', 'batch_size': '8',
                   'learning_rate': '1e-3', 'tuning_epochs': '1', 'validation_split': '20'}

        self.b_algorithms.setCurrentText(b_parms['algorithm_name'])

        self.input_type_resize.setChecked(not b_parms['input_type'])
        self.input_type_split.setChecked(b_parms['input_type'])

        self.b_epochs.setText(b_parms['epochs'])
        self.b_batch.setText(b_parms['batch_size'])
        self.b_lr.setText(b_parms['learning_rate'])
        self.b_te.setText(b_parms['tuning_epochs'])
        self.b_vs.setText(b_parms['validation_split'])

        l_parms = {'batch_size': '64',
                   'image_path': 'asdsa'}  # Must change

        self.l_batch.setText(l_parms['batch_size'])

    def set_default_db_parms(self, binary_path, split_size):
        self.input_size1.setValue(split_size[0])
        self.input_size2.setValue(split_size[1])
        self.b_dp.setPlainText('1. ' + binary_path)

    def get_binary_parms(self):
        binary_algorithm_name = self.b_algorithms.currentText()
        binary_input_size = tuple((self.input_size1.value(), self.input_size2.value()))
        binary_input_type = self.input_type_split.isChecked()
        binary_epoch = int(float(self.b_epochs.text()))
        binary_batch = int(float(self.b_batch.text()))
        binary_lr = float(self.b_lr.text())
        binary_te = int(float(self.b_te.text()))
        binary_vs = float(self.b_vs.text()) / 100
        if binary_vs > 0.5: binary_vs = 0.5
        text = self.b_dp.toPlainText()
        pattern = r'[0-9]+. '
        binary_dp = [s.rstrip() for s in re.split(pattern, text)[1:]]

        return (
            binary_algorithm_name, binary_input_size, binary_input_type, binary_epoch, binary_batch, binary_lr,
            binary_te,
            binary_vs, binary_dp)

    def add_binary_dataset(self):
        height = self.b_add_ds_frame.height()

        if height == 0:
            self.left_box = QPropertyAnimation(self.b_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(0)
            self.left_box.setEndValue(67)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    def cancel_add_binary_ds(self):
        height = self.b_add_ds_frame.height()
        if height == 67:
            self.left_box = QPropertyAnimation(self.b_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(100)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()
            self.b_add_ds_lineedit.setText('')

    def get_localization_parms(self):
        localization_algorithm_name = self.l_algorithms.currentText()
        localization_epoch = self.l_ecpochs.text()
        localization_batch = self.l_batch.text()
        localization_lr = self.l_lr.text()
        localization_te = self.l_te.text()
        localization_vs = self.l_vs.text()
        localization_ip = self.l_ip.text()
        localization_lp = self.l_lp.text()

        return (localization_algorithm_name, localization_epoch, localization_batch, localization_lr, localization_te,
                localization_vs, localization_ip, localization_lp)



    # Dta aquization page add live cameras              Milad

    def set_combo_boxes(self):
    
        strings = [str(x) for x in range(1,25)]
        strings.append('All')
        self.comboBox_cam_select.addItems(strings)
        self.comboBox_cam_select.setCurrentIndex(24)

        # x=['Small','Medium','Large']
        # self.block_image_proccessing={'Small':100,'Medium':200,'Large':300}
        # self.comboBox_block_size.addItems(x)
        # self.comboBox_block_size.currentTextChanged.connect(self.combo_image_preccess)

    def update_combo_box(self,combo_name,index):
        combo_name.setCurrentIndex(index)
    def set_list_combo_boxes(self,combo_name,items):
        combo_name.clear()
        combo_name.addItems(items)  
    def get_camera_parms(self):

        cam_num=self.comboBox_cam_select.currentText()


        return cam_num






    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'toggleButton':
            self.toggleMenu(True)

        if btnName == 'Data_auquzation_btn':
            self.left_bar_clear()
            self.Data_auquzation_btn.setStyleSheet(
                "background-image: url(:/icons/images/icons/graber.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            self.stackedWidget.setCurrentWidget(self.page_data_auquzation)
        if btnName == 'label_btn' or btnName == 'label_btn_SI':
            print('asdasdasd')
            self.left_bar_clear()
            self.label_btn.setStyleSheet(
                "background-image: url(:/icons/images/icons/label.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            self.stackedWidget.setCurrentWidget(self.page_label)
        if btnName == 'tuning_btn':
            self.left_bar_clear()
            self.tuning_btn.setStyleSheet(
                "background-image: url(:/icons/images/icons/tuning.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            # self.stackedWidget.setCurrentWidget(self.page_tuning)
            self.hi()

        if btnName == 'pbt_btn':
            self.left_bar_clear()
            self.pbt_btn.setStyleSheet(
                "background-image: url(:/icons/images/icons/pbt.png);background-color: rgb(212, 212, 212);color:rgp(0,0,0);")
            self.stackedWidget.setCurrentWidget(self.page_pbt)
        if btnName == 'aboutus_btn':
            self.left_bar_clear()
            # self.page_aboutus_btn.setStyleSheet("QPushButton {background-color: rgb(197 , 195,196);	color: rgb(0,0,0);	border: none;	text-align: left;padding-left: 10px;}QPushButton:hover {background-color:  rgb(197 , 195,196)};QPushButton:pressed {background-color: rgb(197 , 195,196);}")
            self.stackedWidget.setCurrentWidget(self.page_aboutus)

        if btnName == 'Binary_btn':
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            self.stackedWidget.setCurrentWidget(self.page_Binary)

        if btnName == 'Localization_btn':
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            self.stackedWidget.setCurrentWidget(self.page_Localization)

        if btnName == 'Classification_btn':
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            self.stackedWidget.setCurrentWidget(self.page_Classification)

        if btnName == 'binary_list':
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_list)

        if btnName == 'binary_training':
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_training)

        if btnName == 'binary_history':
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_history)

        if btnName == 'localization_Statistic':
            self.stackedWidget_localization.setCurrentWidget(self.page_localization_statics)

        if btnName == 'localization_training':
            self.stackedWidget_localization.setCurrentWidget(self.page_localization_training)

        if btnName == 'localization_history':
            self.stackedWidget_localization.setCurrentWidget(self.page_localization_history)

        if btnName == 'classification_class_list':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_class_list)

        if btnName == 'classification_add_new_class':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_add_new_class)

        if btnName == 'classification_training':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_training)

        if btnName == 'classification_history':
            self.stackedWidget_classification.setCurrentWidget(self.page_classification_history)

        if btnName == 'yes_defect':
            self.def_yes_defect()

        if btnName == 'no_defect':
            self.def_no_defect()

        if btnName == 'login_btn':
            self.show_login()

        if btnName == 'setting_btn':
            self.setting_win()

        if btnName == 'polygon_btn':
            self.polygon()

        if btnName == 'bounding_btn':
            self.bounding_box()

        if btnName == 'zoomIn_btn':
            self.zoom_in()

        if btnName == 'zoomOut_btn':
            self.zoom_out()

        if btnName == 'drag_btn':
            self.drag_image()

        if btnName == 'add_label_btn':
            api.add_remove_label()

        if btnName == 'btn_software_setting':
            # self.bounding_box()
            self.stackedWidget.setCurrentWidget(self.page_software_setting)
            setting.language(self)
            # self.stackedWidget.setCurrentWidget(self.page_software_setting)

        if btnName == 'load_coil_btn':
            # print('asdqwdwqd')
            self.data_loader_win_show()

        if btnName == 'checkBox_select':
            # print('asdqwdwqd')

            self.select_unselect_all()

        if btnName == "show_tools_btn":
            self.show_frame_tools()
        if btnName == 'label_btn_2':
            self.stackedWidget.setCurrentWidget(self.page_label)
            image = ImageQt.fromqpixmap(self.crop_image.pixmap())
            image = np.ascontiguousarray(image)
            self.fs = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_BGR888)
            self.image.setPixmap(QPixmap.fromImage(self.fs))

        if btnName == 'b_add_ds':
            self.add_binary_dataset()

        if btnName == 'b_add_cancel':
            self.cancel_add_binary_ds()

        if self.extraLeftBox.width() != 0:
            self.hi()

        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    # def mouseMoveEvent(self, event):
    #     # SET DRAG POS WINDOW
    #     self.dragPos = event.globalPos()
    #     self.x_pos=event.x()
    #     print(self.ret_mouse())
    #     # PRINT MOUSE EVENTS
    #     if event.buttons() == Qt.LeftButton:
    #         print('Mouse click: LEFT CLICK')
    #     if event.buttons() == Qt.RightButton:
    #         print('Mouse click: RIGHT CLICK')
    #     return event.x()

    def connet_keyboard(self, keys, functions, page_name):
        for key in keys:
            self.keyboard_connections[key] = (page_name, functions)

    def do_keyboard(self, key):
        connections = self.keyboard_connections.get(key)
        if connections is None:
            return -1
        else:
            page_name, funcs = connections
            if page_name == PAGES_IDX.get(self.stackedWidget.currentIndex()) or page_name == None:
                for func in funcs:
                    func(key)
                return 1
            return -1

    def keyPressEvent(self, event):
        self.do_keyboard(KEYS.get(event.key()))
        return KEYS.get(event.key())

    def show_image_info_lable_page(self, sheet, pos):
        self.plabel_coil_num_txt.setText(str(sheet.get_id()))
        self.plabel_date_txt.setText(str(sheet.get_date_string()))
        self.plabel_cam_txt.setText(str(pos[-1][0]))

    def show_image_info_lable_page(self, sheet, pos):
        self.plabel_coil_num_txt.setText(str(sheet.get_id()))
        self.plabel_date_txt.setText(str(sheet.get_date_string()))
        self.plabel_cam_txt.setText(str(pos[-1][0]))

    # def get_label_type(self):
    #     if self.tabWidget_defect.currentTabText() =='Mask':
    #         return 'mask'

    #     elif self.tabWidget_defect.currentTabText() == 'Bounding Box':
    #         return 'bbox'

    def set_image_label(self,label_name, img):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = sQImage(img.data, w, h, bytes_per_line, sQImage.Format_RGB888)


        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))


    def set_img_btn_camera(self,cam_num,status=True):

        if status==True:
            # print('avtive')
            img_top = 'images/camtop_actived.png'
            img_btm = 'images/cambtm_actived.png'

        elif status=='Disconnect':
            img_top = 'images/camtop.png'
            img_btm = 'images/cambtm.png'

        else:
            img_top = 'images/camtop_deactive.png'
            img_btm = 'images/cambtm_deactive.png'
        if int(cam_num)<=12:

            btn_name=eval('self.camera%s_btn_2'%cam_num)
            btn_name.setIcon(QIcon(img_top))
        
        else :

            btn_name=eval('self.camera%s_btn_2'%cam_num)
            btn_name.setIcon(QIcon(img_btm))





if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    api = api.API(win)
    win.show()
    sys.exit(app.exec())

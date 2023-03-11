import os
import psutil
import PyQt5

# qt_path= os.path.dirname(PyQt5.__file__)
# os.environ['QT_PLUGIN_PATH'] = os.path.join(qt_path, "Qt/plugins")

import re
from cgitb import enable
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from pyqt5_plugins import *

from PySide6.QtCharts import *
from PySide6.QtCore import *
import PySide6.QtGui as PG
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
from PySide6.QtWidgets import QMessageBox as sQMessageBox
from PySide6.QtGui import QPixmap as sQPixmap
from PySide6.QtGui import QIcon as sQIcon
from PySide6.QtGui import QIntValidator as sQIntValidator
from PySide6 import QtCore as sQtCore
from PySide6.QtCore import QSize as sQSize
import pandas as pd
from functools import partial

from FileDialog import FileDialog
from app_settings import Settings
from backend import (
    data_grabber,
    storage_funcs,
    chart_funcs,
    camera_connection,
    colors_pallete,
    notification_popup,
)
import detect_lenguage
import setting
import api
from Sheet_loader_win.data_loader_UI import data_loader
from labeling.labeling_UI import labeling
from help_UI import help
from neighbouring_UI import neighbouring
from small_neighbouring_UI import small_neighbouring
from labeling import labeling_api
from PIL import ImageQt
import numpy as np
import threading

# from modules import UIFunctions
# import resource
import resources_rc
import cv2
import time

from PyQt5.QtGui import QPainter

from consts.keyboards_keys import KEYS
from consts.pages_indexs import PAGES_IDX
import texts, texts_codes
from logging_modules import logging_funcs, show_logs_UI
from login_win.login_UI import UI_login_window

from Dataset_selection.ds_select_UI import Ds_selection

# from login_win.login_api import

from train_api import ALGORITHM_NAMES
from train_api import ALGORITHM_NAMES

ui, _ = loadUiType("UI/oxin.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


DEBUG_UI = False
SHAMSI_DATE = False


class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

    def __init__(self):
        """
        create init variables
        """

        super(UI_main_window, self).__init__()

        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.statusBar().setMaximumHeight(5)

        self.stackedWidget.setCurrentWidget(self.page_data_auquzation)

        self.mask_table_widget.horizontalHeader().setVisible(True)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.toggleButton.clicked.connect(self.buttonClick)
        # self.btn_technical_move.clicked.connect(self.buttonClick)
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
        self.language = "en"
        self.log_mainfolderpath = "./app_logs"

        # logger object
        self.logger = logging_funcs.app_logger(
            name="saba_train-app_logger",
            log_mainfolderpath=self.log_mainfolderpath,
            console_log=True,
        )
        self.logger.create_new_log(message=texts.MESSEGES["UI_CREATED"]["en"], code=texts_codes.SubTypes['UI_CREATED'])

        # load notification module
        self.notif_manager = notification_popup.Notification_manager(ui_obj=self)
        self.notif_manager.clear_directory()
        # timer to update plc params and check plc is connected
        self.timer_notification = sQtCore.QTimer()
        self.timer_notification.timeout.connect(self.check_nofification_status)
        self.timer_notification.start(2000)

        # SET FONT & SIZE
        # /////////////////////////////////////////////
        # self.label_6.setFont(QFont('Arial', 10))

        # self.toggleButton.clicked.connect(self.toggleMenu(True))

        # CONNECTED WINDOWS
        # //////////////////////////////////////////////
        self.load_sheets_win = data_loader(main_ui_obj=self)

        self.labeling_win = None
        self.login_window = UI_login_window()
        self.help_win = help(lang=self.language)

        self.suggested_defects_btn.setIcon(QIcon("UI/images/suggest.png"))

        self.label_dorsa_open(enable=True)
        # /////////Setting
        self.btn_software_setting.clicked.connect(self.buttonClick)

        self.x, self.y, self.status, self.widget_name = -1, -1, "", ""
        # #left bar click
        self.Data_auquzation_btn.clicked.connect(self.buttonClick)
        self.label_btn.clicked.connect(self.buttonClick)
        self.tuning_btn.clicked.connect(self.buttonClick)
        self.pbt_btn.clicked.connect(self.buttonClick)
        self.log_btn.clicked.connect(self.buttonClick)

        # extra left bar
        # #---------------
        self.Binary_btn.clicked.connect(self.buttonClick)
        self.Localization_btn.clicked.connect(self.buttonClick)
        self.Classification_btn.clicked.connect(self.buttonClick)
        self.Yolo_btn.clicked.connect(self.buttonClick)
        # self.stackedWidget.setCurrentWidget(self.page_live)

        # binary page
        self.binary_list.clicked.connect(self.buttonClick)
        self.binary_training.clicked.connect(self.buttonClick)
        self.binary_history.clicked.connect(self.buttonClick)
        # localization page
        self.localization_training.clicked.connect(self.buttonClick)
        self.localization_history.clicked.connect(self.buttonClick)
        # yolo page
        self.yolo_training.clicked.connect(self.buttonClick)
        self.yolo_history.clicked.connect(self.buttonClick)

        # classification page
        self.classification_class_list.clicked.connect(self.buttonClick)
        # self.classification_add_new_class.clicked.connect(self.buttonClick)
        self.classification_training.clicked.connect(self.buttonClick)
        self.classification_history.clicked.connect(self.buttonClick)

        self.yes_defect.toggled.connect(self.buttonClick)
        self.no_defect.toggled.connect(self.buttonClick)
        # login btn
        self.login_btn.clicked.connect(self.buttonClick)
        self.setting_btn.clicked.connect(self.buttonClick)

        # cameras settings info
        self.selelcted_cameras = [False] * 24

        # labeling
        self.polygon_btn.clicked.connect(self.buttonClick)
        self.zoomIn_btn.clicked.connect(self.buttonClick)
        self.zoomOut_btn.clicked.connect(self.buttonClick)
        self.drag_btn.clicked.connect(self.buttonClick)
        self.label_show_help_btn.clicked.connect(self.buttonClick)
        # self.add_label.clicked.connect(self.buttonClick)
        # self.add_label_btn.clicked.connect(self.buttonClick)

        # QPixmap pixmapTarget = QPixmap(":/icons/images/icons/2png);
        # pixmapTarget = pixmapTarget.scaled(size-5, size-5, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        # ui->label_image_power->setPixmap(pixmapTarget );
        # self.classification_class_list_table()

        # data aquization page
        self.load_coil_btn.clicked.connect(self.buttonClick)

        self.next_coil_btn.clicked.connect(self.buttonClick)
        self.prev_coil_btn.clicked.connect(self.buttonClick)
        self.checkBox_select.clicked.connect(self.buttonClick)
        self.checkBox_all_imgs_SI.stateChanged.connect(self.buttonClick)
        self.checkBox_all_camera_SI.stateChanged.connect(self.buttonClick)
        self.checkBox_all_frame_SI.stateChanged.connect(self.buttonClick)

        # self.show_tools_btn.clicked.connect(self.buttonClick)

        self.keyboard_connections = {}
        self.label_type = "mask"
        self.zoom_type = None

        self.img = cv2.imread("images/dorsa-logo.png")
        self.set_crop_image(self.img)

        img = cv2.imread("UI/images/male-placeholder.jpg")
        self.set_image_label(self.user_label, img)

        self.set_combo_boxes()

        # Training_page
        self.init_training_page()
        self.validate_binary_train_params()
        self.validate_localization_train_params()
        self.validate_yolo_train_params()
        self.b_add_ds.clicked.connect(self.buttonClick)
        self.b_add_cancel.clicked.connect(self.buttonClick)
        self.binary_reset.clicked.connect(self.reset_binary_default_params)
        self.l_algorithms.currentTextChanged.connect(self.buttonClick)
        self.l_add_ds.clicked.connect(self.buttonClick)
        self.l_add_cancel.clicked.connect(self.buttonClick)
        self.localization_reset.clicked.connect(self.reset_localization_default_params)
        self.y_add_ds.clicked.connect(self.buttonClick)
        self.y_add_cancel.clicked.connect(self.buttonClick)
        self.yolo_reset.clicked.connect(self.reset_yolo_default_params)

        # user page

        self.create_new_database.clicked.connect(self.buttonClick)
        self.all_databases.clicked.connect(self.buttonClick)
        self.my_databases_2.clicked.connect(self.buttonClick)
        self.my_databases_3.clicked.connect(self.buttonClick)
        self.btn_user_profile.clicked.connect(self.buttonClick)
        self.toolButton_select_directory.clicked.connect(self.buttonClick)
        # self.set_col_all_datasets()
        # self.set_col_user_datasets()

        self._old_pos = None
        self.sn = small_neighbouring(self.image)
        self.sn.win_set_geometry(0, 0)

        # pbt page

        self.pipeline_pbt_btn.clicked.connect(self.buttonClick)

        self.BTN_apply_of_binary_classifaction_in_PBT_page.setEnabled(False)
        self.load_dataset_pbt_btn.clicked.connect(self.buttonClick)
        self.history_pbt_btn.clicked.connect(self.buttonClick)
        # charts ---------------------------------------------------------------------------------------------
        self.chart_names = ["loss", "accuracy", "recall", "precision"]
        # binary chart
        # loss
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.binary_chart_loss_frame,
            chart_postfix=self.chart_names[0],
            chart_title="Loss",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.binary_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Loss",
            checkbox_obj=self.binary_chart_checkbox,
            legend_visible=False,
            axisY_set_range=False,
        )
        # accuracy
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.binary_chart_acc_frame,
            chart_postfix=self.chart_names[1],
            chart_title="Accuracy",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.binary_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Accuracy",
            checkbox_obj=self.binary_chart_checkbox,
        )
        # recall
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.binary_chart_recall_frame,
            chart_postfix=self.chart_names[2],
            chart_title="Recall",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.binary_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Recall",
            checkbox_obj=self.binary_chart_checkbox,
        )
        # precission
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.binary_chart_prec_frame,
            chart_postfix=self.chart_names[3],
            chart_title="Precission",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.binary_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Precission",
            checkbox_obj=self.binary_chart_checkbox,
            axisX_visible=True,
        )

        # -------------------------------------------------------------------------------------
        # localization chart
        self.loc_chart_names = [
            "loc_loss",
            "loc_accuracy",
            "loc_iou",
            "loc_fscore",
        ]
        # loss
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.localization_chart_loss_frame,
            chart_postfix=self.loc_chart_names[0],
            chart_title="Loss",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.localization_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Loss",
            checkbox_obj=self.localization_chart_checkbox,
            legend_visible=False,
            axisY_set_range=False,
        )
        # accuracy
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.localization_chart_acc_frame,
            chart_postfix=self.loc_chart_names[1],
            chart_title="Accuracy",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.localization_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Accuracy",
            checkbox_obj=self.localization_chart_checkbox,
        )
        # precission
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.localization_chart_iou_frame,
            chart_postfix=self.loc_chart_names[2],
            chart_title="IOU",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.localization_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="IOU",
            checkbox_obj=self.localization_chart_checkbox,
        )
        # recall
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.localization_chart_fscore_frame,
            chart_postfix=self.loc_chart_names[3],
            chart_title="FScore",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.localization_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="FScore",
            checkbox_obj=self.localization_chart_checkbox,
            axisX_visible=True,
        )

        # -------------------------------------------------------------------------------------------------------
        # classification chart
        self.cls_chart_names = [
            "loss_cls",
            "accuracy_cls",
            "recall_cls",
            "precision_cls",
        ]
        # loss
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.cls_chart_loss_frame,
            chart_postfix=self.cls_chart_names[0],
            chart_title="Loss",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.cls_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Loss",
            checkbox_obj=self.cls_chart_checkbox,
            legend_visible=False,
            axisY_set_range=False,
        )
        # accuracy
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.cls_chart_acc_frame,
            chart_postfix=self.cls_chart_names[1],
            chart_title="Accuracy",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.cls_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Accuracy",
            checkbox_obj=self.cls_chart_checkbox,
        )
        # recall
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.cls_chart_recall_frame,
            chart_postfix=self.cls_chart_names[2],
            chart_title="Recall",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.cls_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Recall",
            checkbox_obj=self.cls_chart_checkbox,
        )
        # precision
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.cls_chart_prec_frame,
            chart_postfix=self.cls_chart_names[3],
            chart_title="Precision",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.cls_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Precision",
            checkbox_obj=self.cls_chart_checkbox,
            axisX_visible=True,
        )
        # -------------------------------------------------------------------------------------------------------
        # yolo chart
        self.yolo_chart_names = [
            "box_loss_yolo",
            "obj_loss_yolo",
            "cls_loss_yolo",
            "recall_yolo",
            "precision_yolo",
            "mAP_yolo",
        ]
        # loss
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.yolo_chart_boxloss_frame,
            chart_postfix=self.yolo_chart_names[0],
            chart_title="Box Loss",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.yolo_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Box Loss",
            checkbox_obj=self.yolo_chart_checkbox,
            legend_visible=False,
            axisY_set_range=False,
            axisX_visible=True,
        )
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.yolo_chart_objloss_frame,
            chart_postfix=self.yolo_chart_names[1],
            chart_title="Obj Loss",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.yolo_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Obj Loss",
            checkbox_obj=self.yolo_chart_checkbox,
            legend_visible=False,
            axisY_set_range=False,
            axisX_visible=True,
        )
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.yolo_chart_clsloss_frame,
            chart_postfix=self.yolo_chart_names[2],
            chart_title="Cls Loss",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.yolo_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Cls Loss",
            checkbox_obj=self.yolo_chart_checkbox,
            legend_visible=False,
            axisY_set_range=False,
            axisX_visible=True,
        )
        # recall
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.yolo_chart_recall_frame,
            chart_postfix=self.yolo_chart_names[3],
            chart_title="Recall",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.yolo_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Recall",
            checkbox_obj=self.yolo_chart_checkbox,
            axisX_visible=True,
        )
        # precision
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.yolo_chart_prec_frame,
            chart_postfix=self.yolo_chart_names[4],
            chart_title="Precision",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.yolo_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="Precision",
            checkbox_obj=self.yolo_chart_checkbox,
            axisX_visible=True,
        )
        # mAP
        chart_funcs.create_train_chart_on_ui(
            ui_obj=self,
            frame_obj=self.yolo_chart_mAP_frame,
            chart_postfix=self.yolo_chart_names[5],
            chart_title="mAP",
            legend_train="Train",
            legend_val="Validation",
            scroll_obj=self.yolo_chart_scrollbar,
            axisX_title="Epoch",
            axisY_title="mAP",
            checkbox_obj=self.yolo_chart_checkbox,
            axisX_visible=True,
        )
        # ------------------------------------------------------------------------------------------------------
        # storage
        chart_funcs.create_storage_barchart_on_ui(
            ui_obj=self, 
            frame_obj_storage=self.storage_chart_frame,
        )
        self.update_storage_chart()
        self.start_storage_timer()

        # -----------------------------------------------------------------------------------------------------
        # PLC check buttons
        self.PLC_items = [
            "ProjectorPulseTrig",
            "NCamera",
            "MemSoftwareStart",
            "MemDownLimitSwitchIn",
            "MemDownLimitSwitchOut",
            "MemDownProjectorOnOff1",
            "MemDownProjectorOnOff2",
            "MemDownProjectorOnOff3",
            "MemDownProjectorOnOff4",
            "MemDownProjectorOnOff5",
            "MemDownProjectorOnOff6",
            "MemDownValve",
            "DownTemperature",
            "DownHighThreshold",
            "DownLowThreshold",
            "MemUpLimitSwitchIn",
            "MemUpLimitSwitchOut",
            "MemUpProjectorOnOff1",
            "MemUpProjectorOnOff2",
            "MemUpProjectorOnOff3",
            "MemUpProjectorOnOff4",
            "MemUpProjectorOnOff5",
            "MemUpProjectorOnOff6",
            "MemUpValve",
            "UpTemperature",
            "UpHighThreshold",
            "UpLowThreshold",
            "MemDistanceSensor",
        ]
        # timer to update plc params and check plc is connected
        # self.timer_notification= QTimer()
        # self.timer_notification.timeout.connect(self.check_nofification_status)
        # self.timer_notification.start(2000)
        self.plc_status = False
        self.update_timer_plc = self.update_timer_plc_spinBox.value()
        self.update_wind_plc = self.update_wind_plc_spinBox.value()
        self.auto_wind = self.auto_wind_check.isChecked()
        self.auto_wind_intervals = self.update_auto_wind_plc_spinBox.value()
        self.wind_itr = 1
        self.frame_rate = self.frame_rate_spinBox.value()
        self.update_timer_live_frame = self.update_timer_live_frame_spinBox.value()
        self.manual_plc = self.manual_plc_check.isChecked()
        self.manual_camera = self.manual_cameras_check.isChecked()

        self.show_mesagges_thread_lock = (
            False  # flag to dont run another thread until one is available
        )

        # Cameras Connection
        self.checkBox_top.stateChanged.connect(self.buttonClick)
        self.checkBox_bottom.stateChanged.connect(self.buttonClick)
        self.checkBox_all.stateChanged.connect(self.buttonClick)
        for i in range(1, 25):
            if i < 10:
                btn_name = eval("self.camera0%s_btn" % i)
            else:
                btn_name = eval("self.camera%s_btn" % i)
            btn_name.clicked.connect(self.buttonClick)

        # self.start_wind_btn.clicked.connect(self.start_wind)

        # ----------------------------------------------------------------------------------------------------
        # change_language

        self.appearance_btn.clicked.connect(self.change_language_font)
        self.plc_btn.clicked.connect(self.change_plc_parms)
        self.cameras_btn.clicked.connect(self.change_cameras_parms)
        self.combo_change_language.currentTextChanged.connect(
            self.change_language_image
        )
        self.auto_wind_check.clicked.connect(self.change_wind_setting_status)

        # Clock timer

        self.clock_timer = QTimer(self)

        # adding action to timer
        self.clock_timer.timeout.connect(self.showTime)

        # update the timer every second
        # self.clock_timer.start(1000)

        # self.fontDB = QtGui.QFontDatabase()
        # self.fontDB.addApplicationFont("font/digital-7.ttf")
        # self.setFont(QtGui.QFont("Bariol", 18))

        self.show_labeling_help()

    def update_storage_chart(self):
        drives = storage_funcs.get_available_drives()
        if len(drives) > 0:
            drives = [drives[0]]
            drives.append('/')
            names = ['HDD', 'SSD']
            self.label_289.setMaximumHeight(16777215)
        else:
            drives = ['/']
            names = ['SSD']
            self.label_289.setMaximumHeight(7)
        storage_status = {}
        for d, n in zip(drives, names):
            status = storage_funcs.get_storage_status(d)
            storage_status[n] = status

        chart_funcs.update_storage_barchart(
            ui_obj=self,
            storage_status=storage_status
        )

    def start_storage_timer(self):
        self.storage_timer = sQtCore.QTimer()
        self.storage_timer.timeout.connect(self.update_storage_chart)
        # self.storage_timer.start(600000)
        self.storage_timer.start(10000)

    def showTime(self):

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        self.sec_label.setText(current_time.toString("ss"))
        self.min_label.setText(current_time.toString("mm"))
        self.h_label.setText(current_time.toString("hh"))

        # showing it to the label
        # self.sec_label.setText(label_time)

    def set_settings(self, 
                lang, 
                font,
                manual_plc,
                plc_update_time, 
                wind_duration, 
                automatic_wind, 
                auto_wind_intervals, 
                manual_cameras, 
                frame_rate, 
                live_update_time
            ):
        """set language

        Args:
            lang (string): input language from api
            font (string): input font from api

        Returns: None
        """
        self.combo_change_language.setCurrentText(
            texts.Titles[lang.lower()][self.language]
        )
        self.fontComboBox.setCurrentText(font)
        self.change_language_font()

        if manual_plc == 'True':
            self.manual_plc_check.setCheckState(Qt.CheckState.Checked)
        else:
            self.manual_plc_check.setCheckState(Qt.CheckState.Unchecked)
        self.update_timer_plc_spinBox.setValue(int(plc_update_time))
        self.update_wind_plc_spinBox.setValue(int(wind_duration))
        if automatic_wind == 'True':
            self.auto_wind_check.setCheckState(Qt.CheckState.Checked)
        else:
            self.auto_wind_check.setCheckState(Qt.CheckState.Unchecked)
        self.update_auto_wind_plc_spinBox.setValue(int(auto_wind_intervals))
        self.change_plc_parms()

        if manual_cameras == 'True':
            self.manual_cameras_check.setCheckState(Qt.CheckState.Checked)
        else:
            self.manual_cameras_check.setCheckState(Qt.CheckState.Unchecked)
        self.frame_rate_spinBox.setValue(int(frame_rate))
        self.update_timer_live_frame_spinBox.setValue(int(live_update_time))
        self.change_cameras_parms()

    def change_language_font(self):
        """Change language and font in ui and update image

        Returns: None

        """
        if (
            self.combo_change_language.currentText()
            == texts.Titles["english"][self.language]
        ):
            self.language = "en"
            api.language = "en"
            self.sn.language = "en"
            self.help_win.set_language(lang="en")
            self.load_sheets_win.set_language("en")
            img_path = "UI/images/english.png"

        else:
            self.language = "fa"
            api.language = "fa"
            self.sn.language = "fa"
            self.help_win.set_language(lang="fa")
            self.load_sheets_win.set_language("fa")
            img_path = "UI/images/persian.png"

        pixmap = QPixmap(img_path)
        self.label_language.setPixmap(pixmap)

        texts.set_title(self, self.language)
        texts.set_moving_title(self, self.language)
        self.set_combo_boxes()
        self.init_training_page()
        self.bgApp.setStyleSheet("font: %s;" % (self.fontComboBox.currentText()))
        QApplication.instance().setFont(self.fontComboBox.currentText())

        self.logger.create_new_log(message=texts.MESSEGES["setting_applied"]['en'].format(texts.Titles['language_font']['en']),
                                    code=texts_codes.SubTypes['language_font'])
        self.set_warning(
            texts.MESSEGES["setting_applied"][self.language].format(texts.Titles['language_font'][self.language]), 
            "setting", 
            texts_codes.SubTypes['language_font'],
            level=1
        )

    def change_language_image(self):
        """Update image of language in ui

        Returns: None

        """
        if (
            self.combo_change_language.currentText()
            == texts.Titles["english"][self.language]
        ):
            img_path = "UI/images/english.png"

        else:
            img_path = "UI/images/persian.png"

        pixmap = QPixmap(img_path)
        self.label_language.setPixmap(pixmap)

    def change_wind_setting_status(self):
        self.update_auto_wind_plc_spinBox.setEnabled(self.auto_wind_check.isChecked()) 

    def change_plc_parms(self):
        """Change plc timer params in ui

        Returns: None

        """
        self.update_timer_plc = self.update_timer_plc_spinBox.value()
        self.update_wind_plc = self.update_wind_plc_spinBox.value()
        self.auto_wind = self.auto_wind_check.isChecked()
        self.auto_wind_intervals = self.update_auto_wind_plc_spinBox.value()
        # try:
        #     api.start_auto_wind()
        # except:
        #     pass
        self.manual_plc = self.manual_plc_check.isChecked()
        self.logger.create_new_log(message=texts.MESSEGES["setting_applied"]['en'].format(texts.Titles['plc']['en']),
                                    code=texts_codes.SubTypes['plc'])
        self.set_warning(
            texts.MESSEGES["setting_applied"][self.language].format(texts.Titles['plc'][self.language]), 
            "setting", 
            texts_codes.SubTypes['plc'],
            level=1
        )

    def change_cameras_parms(self):
        """Change cameras params in ui

        Returns: None

        """
        self.frame_rate = self.frame_rate_spinBox.value()
        self.update_timer_live_frame = self.update_timer_live_frame_spinBox.value()
        self.manual_camera = self.manual_cameras_check.isChecked()
        self.logger.create_new_log(message=texts.MESSEGES["setting_applied"]['en'].format(texts.Titles['cameras']['en']),
                                    code=texts_codes.SubTypes['cameras'])
        self.set_warning(
            texts.MESSEGES["setting_applied"][self.language].format(texts.Titles['cameras'][self.language]), 
            "setting",
            texts_codes.SubTypes['cameras'],
            level=1
        )

    def create_alert_message(self, title, message):
        """
        create alert and message box

        Args:
            title (str): title of message box
            message (str): description of message box

        Returns: None
        """
        alert_window = sQMessageBox(sQMessageBox.Warning, title, message)
        alert_window.setStandardButtons(sQMessageBox.Ok)
        icon = sQIcon()
        icon.addPixmap(sQPixmap("images/alert.png"), sQIcon.Normal)
        alert_window.setWindowIcon(icon)
        alert_window.exec()
        self.logger.create_new_log(
            message="create new alert with message : {}".format(message),
            code=texts_codes.SubTypes['new_alert']
        )

    def mousePressEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): left or right click for drag window
        Returns: None
        """
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): release Event for update drag window
        Returns: None
        """
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): when click and move mouse for drag window
        Returns: None
        """

        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        if not self.isMaximized():
            self.move(self.pos() + delta)

    def get_technical(self, name=True):
        """
        get up side and down side objects in window

        Args:
            name (str): for get objects with sopecific name or not
        Returns: dict {'side':'widget object'}
        """
        if name:
            return {
                self.up_side_technical.objectName(): self.up_side_technical,
                self.down_side_technical.objectName(): self.down_side_technical,
            }

        else:
            return {"up": self.up_side_technical, "down": self.down_side_technical}

    def get_technical_wgt_side(self, wgt_name):
        """
        get name of objects top or bottom
        Args:
            wgt_name (obj): technical object
        Returns: side
        """
        if wgt_name == self.down_side_technical.objectName():
            return "down"

        elif wgt_name == self.up_side_technical.objectName():
            return "up"

    def ret_mouse(self):
        """
        ret mouse details
        Returns : mouse position (x,y) , widget name , status (drag,realese,left,right , ...)
        """
        x, y, widget_name, status = self.x, self.y, self.widget_name, self.status
        self.x, self.y, self.widget_name, self.status = -1, -1, "", ""
        return (x, y), widget_name, status

    def set_img_sheet(self, img, side):
        """
        update image in UI (technical side) with side

        Args:
            img (aray): new image
            side (str): up or down / Top or Bottom
        Returns: None
        """
        if side == "up" or side == self.up_side_technical.objectName():
            image = QImage(
                img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888
            )
            self.up_side_technical.setPixmap(QPixmap.fromImage(image))
        if side == "down" or side == self.down_side_technical.objectName():
            image = QImage(
                img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888
            )
            self.down_side_technical.setPixmap(QPixmap.fromImage(image))

    def set_crop_image(self, img):
        """
        update image in UI (full image) with side
        Args:
            img (aray): new image
        Returns: None
        """
        image = QImage(
            img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888
        )
        self.crop_image.setPixmap(QPixmap.fromImage(image))
        # cv2.waitKey(200)

    def set_enabel(self, widget, status):
        """enable or disable btns in UI

        Args:
            widget (widget): widget that want disable or eanble
            status (bool): True or Fasle
        """
        widget.setDisabled(not (status))
        # /////////////////// end

    def set_buttons_enable_or_disable(self, names, enable=True):
        """
        this function will enable or disble all the ui elements in the input list

        Inputs:
            names: ui elements (in list)
            enable: a boolean value determining wheather to enable/diable the elements
        """

        for name in names:
            name.setEnabled(enable)

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        """open/close left menu animation
        Args:
            enable (bool): open/close menu with animation or not
        """
        if enable:
            # GET WIDTH
            width = self.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                # #print('OPEN')
                self.toggleButton.setStyleSheet(
                    "background-image: url(:/icons/images/icons/t2.png);"
                )
                widthExtended = maxExtend
                # #print(widthExtended)
            else:
                self.toggleButton.setStyleSheet(
                    "background-image: url(:/icons/images/icons/t1.png);"
                )
                # #print('Close')
                widthExtended = standard
                # #print(widthExtended)

            # ANIMATION
            self.animation = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

        self.logger.create_new_log(message="Left menu open/close.", code=texts_codes.SubTypes['left_menu'])

    # Technical view Move
    # ///////////////////////////////////////////////////////////////

    def technical_move(self, enable):
        """open/close technicals window with animation

        Args:
            enable (bool): True or False
        """
        if enable:
            # GET WIDTH
            width = self.frame_413.width()
            maxExtend = 0
            standard = 600

            # SET MAX WIDTH
            if width != 0:
                # #print("OPEN")
                # self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t2.png);")
                self.set_btn_image(self.btn_technical_move, "UI/images/images/left.png")
                widthExtended = maxExtend
                # #print(widthExtended)
            else:
                # self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t1.png);")
                self.set_btn_image(
                    self.btn_technical_move, "UI/images/images/fast-forward.png"
                )

                # #print("Close")
                widthExtended = standard
                # #print(widthExtended)

            # ANIMATION
            # #print("width", width)
            self.animation = QPropertyAnimation(self.frame_413, b"maximumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            # self.animation = QPropertyAnimation(self.frame_413, b"minimumWidth")
            # self.animation.setDuration(Settings.TIME_ANIMATION)
            # self.animation.setStartValue(width)
            # self.animation.setEndValue(widthExtended)
            # self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            # self.animation.start()
            # #print("start")

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def extra_left_box_move(self):
        """open/close extra left box with animation

        Args:
            enable (bool): True or False
        """
        # GET WIDTH
        width = self.extraLeftBox.width()
        widthRightBox = 0
        maxExtend = Settings.LEFT_BOX_WIDTH
        color = Settings.BTN_LEFT_BOX_COLOR
        standard = 0

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            if widthRightBox != 0:
                style = self.settingsTopBtn.styleSheet()
                # self.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
        else:
            widthExtended = standard

        self.start_box_animation(width, widthRightBox, "left")
        self.logger.create_new_log(message="extra Left menu open/close.", code=texts_codes.SubTypes['extra_left_menu'])

    def start_box_animation(self, left_box_width, right_box_width, direction):
        """run move animation with inputs

        Args:
            left_box_width (int): size of that should be
            right_box_width (int): size of that should be
            direction : side left or right
        """
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
            # #print('ok')
        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
        # #print('ok',left_width)
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        # self.group.addAnimation(self.right_box)
        self.group.start()

    # Label Dorsa
    # ///////////////////////////////////////////////
    def label_show_help(self):
        h = self.label_show_help_frame.height()
        if h <= 1:
            self.minHeight = sQtCore.QPropertyAnimation(self.label_show_help_frame, b"minimumHeight")
            self.minHeight.setDuration(300)
            self.minHeight.setStartValue(h)
            self.minHeight.setEndValue(106)
            self.minHeight.setEasingCurve(sQtCore.QEasingCurve.InOutQuart)
            self.group = sQtCore.QParallelAnimationGroup()
            self.group.addAnimation(self.minHeight)

            self.maxHeight = sQtCore.QPropertyAnimation(self.label_show_help_frame, b"maximumHeight")
            self.maxHeight.setDuration(300)
            self.maxHeight.setStartValue(h)
            self.maxHeight.setEndValue(131)
            self.maxHeight.setEasingCurve(sQtCore.QEasingCurve.InOutQuart)
            self.group.addAnimation(self.maxHeight)
            self.group.start()

            icon_path = 'UI/images/bottom_arrow.png'
            self.label_show_help_btn.setIcon(sQPixmap.fromImage(sQImage(icon_path)))

        else:
            self.minHeight = sQtCore.QPropertyAnimation(self.label_show_help_frame, b"minimumHeight")
            self.minHeight.setDuration(300)
            self.minHeight.setStartValue(h)
            self.minHeight.setEndValue(1)
            self.minHeight.setEasingCurve(sQtCore.QEasingCurve.InOutQuart)
            self.group = sQtCore.QParallelAnimationGroup()
            self.group.addAnimation(self.minHeight)

            self.maxHeight = sQtCore.QPropertyAnimation(self.label_show_help_frame, b"maximumHeight")
            self.maxHeight.setDuration(300)
            self.maxHeight.setStartValue(h)
            self.maxHeight.setEndValue(1)
            self.maxHeight.setEasingCurve(sQtCore.QEasingCurve.InOutQuart)
            self.group.addAnimation(self.maxHeight)
            self.group.start()

            icon_path = 'UI/images/top_arrow.png'
            self.label_show_help_btn.setIcon(sQPixmap.fromImage(sQImage(icon_path)))

    def label_dorsa_open(self, enable):
        """open dorsa label when program started

        Args:
            enable (bool): True/False for animation or not
        """
        if enable:
            # GET WIDTH
            width = self.label_dorsa.width()
            maxExtend = 300
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                # #print('OPEN')
                # self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t2.png);")
                widthExtended = maxExtend
                # #print(widthExtended)
            else:
                # self.toggleButton.setStyleSheet("background-image: url(:/icons/images/icons/t1.png);")
                # #print('Close')
                widthExtended = standard
                # #print(widthExtended)

            # ANIMATION
            self.animation = QPropertyAnimation(self.label_dorsa, b"minimumWidth")
            self.animation.setDuration(1200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            self.logger.create_new_log(message="Dorsa label opened", code=texts_codes.SubTypes['dorsa_label'])

    # TOGGLE Yes_defect
    # ///////////////////////////////////////////////////////////////
    def def_yes_defect(self):
        """set stack widget page with click"""
        self.stackedWidget_defect.setCurrentWidget(self.page_yes)

    def def_no_defect(self):
        """set stack widget page with click"""
        self.stackedWidget_defect.setCurrentWidget(self.page_no)

    # TOGGLE LOGIN & setting
    # ///////////////////////////////////////////////////////////////

    def show_login(self):
        """show login window"""
        self.login_window.show()
        self.logger.create_new_log(message="open login window", code=texts_codes.SubTypes['show_login_window'])

    def setting_win(self):
        """open setting Frame with click"""

        height = self.frame_settin2.height()
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
            # #print('no ani')
        elif height == 40:
            self.left_box = QPropertyAnimation(self.frame_settin2, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(40)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    def activate_(self):
        """main butoons connect -- exit , minize , maximize, help --"""
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)
        self.helpButton.clicked.connect(self.show_help)

    def minimize(self):
        """Minimize winodw"""
        self.showMinimized()
        self.logger.create_new_log(message="minimize window", code=texts_codes.SubTypes['minimize_window'])

    def close_win(self):
        """Close window"""
        api.stop_capture_func()
        ret = api.check_image_saved()
        if ret:
            t = self.show_question(
                    texts.WARNINGS["question"][self.language],
                    texts.MESSEGES["exit_confirm"][self.language],
                )
            if not t:
                return
            else:
                self.logger.create_new_log(message="Close window", code=texts_codes.SubTypes['close_window'])
                self.close()
                sys.exit()

    def maxmize_minimize(self):
        """Maximize or Minimize window"""
        self.show_image_in_label()
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.logger.create_new_log(message="Maximize or Minimize window", code=texts_codes.SubTypes['maximize_minimize_window'])

    def show_help(self):
        help_image = None
        name = self.stackedWidget.currentWidget().objectName()
        if name == "page_software_setting":
            text = texts.HELPS["SETTINGS_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["SETTINGS_PAGE"][self.language])
        elif name == "page_data_auquzation":
            tab_name = self.tabWidget_2.currentWidget().objectName()
            if tab_name == "tab_5":
                text = texts.HELPS["LIVE_PAGE"][self.language]
                help_image = cv2.imread(texts.HELPS_ADDRESS["LIVE_PAGE"][self.language])
            elif tab_name == "tab_6":
                text = texts.HELPS["TECHNICAL_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["TECHNICAL_PAGE"][self.language]
                )
        elif name == "page_label":
            text = texts.HELPS["LABEL_PAGE"][self.language]
            help_image = cv2.imread(texts.HELPS_ADDRESS["LABEL_PAGE"][self.language])
        elif name == "page_user_profile":
            stack_name = self.stackedWidget_2.currentWidget().objectName()
            if stack_name == "page_create_db":
                text = texts.HELPS["PROFILE_CREATEDS_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["PROFILE_CREATEDS_PAGE"][self.language]
                )
            elif stack_name == "page_all_db":
                text = texts.HELPS["PROFILE_ALLDS_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["PROFILE_ALLDS_PAGE"][self.language]
                )
            elif stack_name == "page_my_db":
                text = texts.HELPS["PROFILE_MYDS_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["PROFILE_MYDS_PAGE"][self.language]
                )
            elif stack_name == "page_my_pipelines":
                text = texts.HELPS["PROFILE_MYPIP_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["PROFILE_MYPIP_PAGE"][self.language]
                )
        elif name == "page_pbt":
            pass
            # tab_name = self.stackedWidget_pbt.currentWidget().objectName()
            # if tab_name == "page_pipeline":
            #     text = texts.HELPS["PBT_PIPLINE_PAGE"][self.language]
            #     help_image = cv2.imread(
            #         texts.HELPS_ADDRESS["PBT_PIPLINE_PAGE"][self.language]
            #     )
            # elif tab_name == "page_load_dataset":
            #     text = texts.HELPS["PBT_LOADDATASET_PAGE"][self.language]
            #     help_image = cv2.imread(
            #         texts.HELPS_ADDRESS["PBT_LOADDATASET_PAGE"][self.language]
            #     )
            # elif tab_name == "page_history":
            #     text = texts.HELPS["PBT_HISTORY_PAGE"][self.language]
            #     help_image = cv2.imread(
            #         texts.HELPS_ADDRESS["PBT_HISTORY_PAGE"][self.language]
            #     )
        elif name == "page_Binary":
            stack_name = self.stackedWidget_binary.currentWidget().objectName()
            if stack_name == "page_binary_list":
                text = texts.HELPS["BINARYLIST_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["BINARYLIST_PAGE"][self.language]
                )
            if stack_name == "page_binary_training":
                text = texts.HELPS["BINARY_TRAINING_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["BINARY_TRAINING_PAGE"][self.language]
                )
            if stack_name == "page_binary_history":
                text = texts.HELPS["BINARY_HISTORY_PAGE"][self.language]
                help_image = cv2.imread(
                    texts.HELPS_ADDRESS["BINARY_HISTORY_PAGE"][self.language]
                )
        elif name == "page_Localization":
            pass
            # stack_name = self.stackedWidget_localization.currentWidget().objectName()
            # if stack_name == "page_localization_training":
            #     text = texts.HELPS["LOC_TRAINING_PAGE"][self.language]
            #     help_image = cv2.imread(
            #         texts.HELPS_ADDRESS["LOC_TRAINING_PAGE"][self.language]
            #     )
            # elif stack_name == "page_localization_history":
            #     text = texts.HELPS["LOC_HISTORY_PAGE"][self.language]
            #     help_image = cv2.imread(
            #         texts.HELPS_ADDRESS["LOC_HISTORY_PAGE"][self.language]
            #     )
        elif name == "page_Classification":
            stack_name = self.stackedWidget_classification.currentWidget().objectName()
            if stack_name == "page_classification_class_list":
                pass
            elif stack_name == "page_classification_training":
                pass
            elif stack_name == "page_classification_history":
                pass
        elif name == "page_software_setting":
            pass
        if help_image is not None:
            self.help_win.textEdit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.help_win.textEdit.setText(text)
            image = QImage(
                help_image,
                help_image.shape[1],
                help_image.shape[0],
                help_image.strides[0],
                QImage.Format_BGR888,
            )
            self.help_win.label.setPixmap(QPixmap.fromImage(image))
            self.help_win.show()

    def left_bar_clear(self):
        """change left bar image with base color (white)"""
        self.Data_auquzation_btn.setStyleSheet(
            "background-image: url(./images/icons/graber.png);"
        )
        self.label_btn.setStyleSheet("background-image: url(./images/icons/label.png);")
        self.tuning_btn.setStyleSheet(
            "background-image: url(./images/icons/tuning.png);"
        )
        self.pbt_btn.setStyleSheet("background-image: url(./images/icons/PBT.png);")

    def get_label_type(self):
        return self.label_type

    def get_zoom_type(self):
        return self.zoom_type

    def get_size_label_image(self):
        """
        Return : return size (width,height) of main image in Label Page UI
        """
        return self.image.height(), self.image.width()

    def add_selected_image(self, records):
        """Fill the table of selected Images in Data aquization page

        Args:
            records (list): list of selected images
        """

        self.checkBox_select.setChecked(False)  # set check statet false

        # self.clear_table()  # cleare table

        self.listWidget_append_img_list.setRowCount(len(records))  # set row count

        for row, record in enumerate(records):
            # for i in range(11):
            # #print(i)
            record = "{} - {} - {}".format(record[0], record[1], (record[2]))
            
            table_item = QTableWidgetItem(str(record))
            # if i ==0:
            table_item.setFlags(
                Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled
            )
            table_item.setCheckState(Qt.CheckState.Unchecked)
            table_item.setData(Qt.DisplayRole, record)
            self.listWidget_append_img_list.setItem(row, 0, table_item)
            # #print(table_item)

    def get_selected_img(self):
        """Return the table of selected Images in Data aquization page

        Return : Selected Images
        """
        selected_list = []
        for i in range(self.listWidget_append_img_list.rowCount()):
            if (
                self.listWidget_append_img_list.item(i, 0).checkState()
                == sQtCore.Qt.Checked
            ):
                if i >= 0:
                    selected_list.append(i)
        self.logger.create_new_log(message="get selected images in UI", code=texts_codes.SubTypes['get_selected_images'])
        return selected_list

    def clear_table(self):
        """Clear table of selected Images in Data aquization page"""
        for i in range(self.listWidget_append_img_list.rowCount()):
            self.listWidget_append_img_list.removeRow(0)

    def select_unselect_all(self):
        """Select/Unselect all images in table Data aquization page"""
        if self.checkBox_select.isChecked():
            for i in range(self.listWidget_append_img_list.rowCount()):
                self.listWidget_append_img_list.item(i, 0).setCheckState(
                    Qt.CheckState.Checked
                )

        else:
            for i in range(self.listWidget_append_img_list.rowCount()):
                self.listWidget_append_img_list.item(i, 0).setCheckState(
                    Qt.CheckState.Unchecked
                )

    def able_enable_filters(self):
        """When sheet load or some times widgets has been Enableed or Dsable"""
        if self.checkBox_all_imgs_SI.isChecked():
            self.comboBox_side_SI.setEnabled(False)
            self.comboBox_ncamera_SI.setEnabled(False)
            self.checkBox_all_camera_SI.setEnabled(False)
            self.comboBox_nframe_SI.setEnabled(False)
            self.checkBox_all_frame_SI.setEnabled(False)

            self.comboBox_side_SI.setCurrentIndex(-1)
            self.comboBox_ncamera_SI.setCurrentIndex(-1)
            self.comboBox_nframe_SI.setCurrentIndex(-1)
        else:
            self.comboBox_side_SI.setEnabled(True)
            self.comboBox_ncamera_SI.setEnabled(True)
            self.checkBox_all_camera_SI.setEnabled(True)
            self.comboBox_nframe_SI.setEnabled(True)
            self.checkBox_all_frame_SI.setEnabled(True)

    def able_enable_camera_filter(self):
        """When sheet load or some times camera widgets has been Enableed or Dsable"""
        if self.checkBox_all_camera_SI.isChecked():
            self.comboBox_ncamera_SI.setEnabled(False)
        else:
            self.comboBox_ncamera_SI.setEnabled(True)

    def able_enable_frame_filter(self):
        """When sheet load or some times widgets about frame has been Enableed or Dsable"""
        if self.checkBox_all_frame_SI.isChecked():
            self.comboBox_nframe_SI.setEnabled(False)
        else:
            self.comboBox_nframe_SI.setEnabled(True)

    def polygon(self):
        """Change mouse shape and label type and run polygan functions"""

        self.image.setCursor(Qt.ArrowCursor)
        self.zoom_type = None
        self.label_type = "mask"

        api.load_image_to_label_page()

    def zoom_in(self):
        """change mouse shape and zoom in mode"""
        cursor = PG.QPixmap("images/zoom-in_cursor.png")
        cursor = cursor.scaled(25, 25, Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setCursor(PG.QCursor(cursor))
        self.zoom_type = "zoom_in"

    def zoom_out(self):
        """change mouse shape and zoom out mode"""
        cursor = PG.QPixmap("images/zoom-out_cursor.png")
        cursor = cursor.scaled(25, 25, Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setCursor(PG.QCursor(cursor))
        self.zoom_type = "zoom_out"

    def drag_image(self):
        """change mouse shape and drage mode"""
        self.image.setCursor(Qt.OpenHandCursor)
        self.zoom_type = "drag"

    def data_loader_win_show(self):
        """open Dataloader window"""
        self.label_type = "mask"
        self.load_sheets_win.show()
        self.logger.create_new_log(message="Open Dataloader Window", code=texts_codes.SubTypes['dataloader_window'])  # LOG

    def ret_create_login(self):
        """Create Object Login Window and set Title Page language
        Return : login object
        """
        self.login_window = UI_login_window()
        texts.set_title_login(self, self.language)

        self.logger.create_new_log(message="create login object", code=texts_codes.SubTypes['create_login_window'])  # LOG
        return self.login_window

    def create_ds_selection_dialog(self):
        self.select_ds_dialog = Ds_selection()
        texts.set_title_ds_selection(self, self.language)

        self.logger.create_new_log(message="create dataset selection object", code=texts_codes.SubTypes['create_ds_selection_window'])  # LOG
        return self.select_ds_dialog

    def ret_create_labeling(self):
        """Create Object Labeling and set Title Page language
        Return : labeling object
        """
        if self.labeling_win:
            self.labeling_win.close()
        self.labeling_win = labeling()  # LOG
        texts.set_title_labeling(self, self.language)
        return self.labeling_win

    def show_labels(self, labels, labels_name, label_type, selected_list):
        """Show Labels in Table Defects With Details (in every update teble has been clear)
        Args:
            labels (list): list of ares labels
            labels_name(list[str]) : Name of labels
            labels_type(list[str]) : Type of labels
        """
        LABEL_TABLE = {"mask": self.mask_table_widget}
        # self.clear_table()  # clear table
        self.mask_table_widget.horizontalHeader().setVisible(True)
        LABEL_TABLE[label_type].setHorizontalHeaderLabels(
            ["Defect ID", "Defect Name", "Size"]
        )
        LABEL_TABLE[label_type].setRowCount(len(labels))  # set row count

        for row in range(len(labels)):
            table_item = QTableWidgetItem(str(labels[row][0]))
            if row in selected_list:
                table_item.setCheckState(Qt.CheckState.Checked)
            else:
                table_item.setCheckState(Qt.CheckState.Unchecked)
            LABEL_TABLE[label_type].setItem(row, 0, table_item)

            table_item = QTableWidgetItem(str(labels_name[row]))
            LABEL_TABLE[label_type].setItem(row, 1, table_item)

            s = cv2.contourArea(labels[row][1])
            table_item = QTableWidgetItem(str(s))
            LABEL_TABLE[label_type].setItem(row, 2, table_item)

    def show_neighbouring(self, img, annt):
        """show neighbouring of image this func run multi for all neighbours
        Args:
            img (array) : neighbour image
        """
        if self.checkBox_show_neighbours_labels.isChecked():
            self.n = neighbouring(img, annt, True, self.language)
            self.n.annot_checkbox.setChecked(True)
        else:
            self.n = neighbouring(img, has_annotation=False, lang=self.language)
        self.n.show()

    def maximize_labeling_help_images(self, n):
        path = 'images/labeling_helps'
        help_images = sorted(os.listdir(path))
        img = cv2.imread(os.path.join(path, help_images[n-1]))
        self.n_help = neighbouring(img, annotated_image=texts.ERRORS["annotation_not_exist"][self.language], lang=self.language)
        self.n_help.show()

    def show_small_neighbouring(self):
        """Show neighbours Window"""
        self.sn.win_set_geometry(0, 0)
        self.sn.show()

    def update_neighbour_images(self, imgs, anns):
        """Update neighbours Window
        Args:
            imgs (list) : neighbour image
            anns (list) : list of annotations of image
        """
        if self.sn:
            self.sn.set_imgs(imgs)
            self.sn.set_annts(anns)
            self.sn.set_image_in_label(self.checkBox_show_neighbours_labels.isChecked())

    def update_center_image(self, img, ann):
        if self.sn:
            self.sn.set_img(img, 8)
            self.sn.set_annt(ann, 8)
            self.sn.set_image_in_label(self.checkBox_show_neighbours_labels.isChecked())

    def update_neighbour_labels(self, flag):
        if self.sn:
            self.sn.set_image_in_label(flag)

    def close_small_neighbouring(self):
        """Close neighbour window"""
        self.sn.close()

    def show_sheet_details(self, details, tab_live=False):
        """Show Sheet Details in Data aquzation page With incoming details
        Args:
        details (list): list of sheet details
        """
        try:
            if tab_live:
                self.set_label(self.label_sheet_id, str(details["sheet_id"]))
            else:
                self.set_label(self.label_sheet_id_2, str(details["sheet_id"]))
        except Exception as e:
            self.set_label(self.label_sheet_id_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        try:
            if tab_live:
                self.set_label(self.label_heat_number, str(details["heat_number"]))
            else:
                self.set_label(self.label_heat_number_2, str(details["heat_number"]))
        except Exception as e:
            self.set_label(self.label_heat_number_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        try:
            if tab_live:
                self.set_label(self.label_ps_number, str(details["ps_number"]))
            else:
                self.set_label(self.label_ps_number_2, str(details["ps_number"]))
        except Exception as e:
            self.set_label(self.label_ps_number_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        try:
            if tab_live:
                self.set_label(self.label_pdl_number, str(details["pdl_number"]))
            else:
                self.set_label(self.label_pdl_number_2, str(details["pdl_number"]))
        except Exception as e:
            self.set_label(self.label_pdl_number_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        try:
            if tab_live:
                self.set_label(self.label_length, str(details["length"]))
            else:
                self.set_label(self.label_length_2, str(details["length"]))
        except Exception as e:
            self.set_label(self.label_length_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        try:
            if tab_live:
                self.set_label(self.label_width, str(details["width"]))
            else:
                self.set_label(self.label_width_2, str(details["width"]))
        except Exception as e:
            self.set_label(self.label_width_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        try:
            if tab_live:
                self.set_label(self.label_thickness, str(details["thickness"]))
            else:
                self.set_label(self.label_thickness_2, str(details["thickness"]))
        except Exception as e:
            self.set_label(self.label_thickness_2, "-")
            self.logger.create_new_log(
                message="set sheet detail Error", code=texts_codes.SubTypes['set_sheet_detail_error'], level=5
            )
        self.logger.create_new_log(message="Set sheet details", code=texts_codes.SubTypes['set_sheet_detail'])

    def set_warning(self, text, name, code=None, level=1):
        """Show warning with time delay 2 second , all labels for show warning has been set here"""

        waring_labels = {
            "data_auquzation": self.warning_data_page,
            "label": self.warning_label_page,
            "train": self.warning_train_page,
            "l_train": self.l_warning_train_page,
            "y_train": self.y_warning_train_page,
            "camera_connection": self.camera_connection_msg,
            "binarylist": self.warning_binarylist_page,
            "setting_eror": self.setting_eror,
            "app_erors": self.label_app_erors,
            "classification_model_history": self.cls_tabel_label,
            "classlist_msg_label": self.classlist_msg_label,
            "binary_model_history": self.binary_tabel_label,
            "localization_model_history": self.localization_tabel_label,
            "yolo_model_history": self.yolo_tabel_label,
            "setting": self.setting_msg_label,
            "profile": self.profile_msg_label,
        }
        if text != None:
            if code:
                text = '(' + code + ')' + text
            if level == 1:
                waring_labels[name].setText(" " + text + " ")
                waring_labels[name].setStyleSheet(
                    "background-color:#20a740;border-radius:2px;color:white"
                )

            if level == 2:
                waring_labels[name].setText(
                    texts.WARNINGS["WARNING"][self.language] + text
                )
                waring_labels[name].setStyleSheet(
                    "background-color:#FDFFA9;border-radius:2px;color:black"
                )

            if level >= 3:
                waring_labels[name].setText(texts.ERRORS["ERROR"][self.language] + text)
                waring_labels[name].setStyleSheet(
                    "background-color:#D9534F;border-radius:2px;color:black"
                )
            QTimer.singleShot(3000, lambda: self.set_warning(None, name))
            # self.logger.create_new_log(
            #     message="waring_labels {} Error {}".format(name, text),
            #     level=2,
            # )

        else:
            waring_labels[name].setText("")
            waring_labels[name].setStyleSheet("")
    
    def show_question(self, title, message):
        """Show question window with specefic message
        Args:
            title (str) : set Title of window
            message (str) : set message of window
        Return (bool) : True/False
        """
        messageBox = sQMessageBox(self)
        messageBox.setWindowTitle(title)
        messageBox.setIcon(sQMessageBox.Question)
        messageBox.setInformativeText(message)
        
        buttonoptionA = messageBox.addButton(texts.Titles['yes'][self.language], sQMessageBox.YesRole)    
        buttonoptionB = messageBox.addButton(texts.Titles['no'][self.language], sQMessageBox.NoRole)  
        messageBox.setDefaultButton(buttonoptionB)
        
        messageBox.exec_()

        if messageBox.clickedButton() == buttonoptionA:
            return True
        elif messageBox.clickedButton() == buttonoptionB:
            return False

    def show_current_position(self, pt):
        """Update current position with incoming postion
        Args:
            pt (tuple): x,y position of current move
        """
        self.current_pos_x.setText(str(pt[0]))
        self.current_pos_y.setText(str(pt[1]))

    def show_label_page(self):
        self.left_bar_clear()
        self.label_btn.setStyleSheet(
            "background-image: url(./images/icons/label.png);background-color: rgb(170, 170, 212);color:rgp(0,0,0);"
        )
        self.stackedWidget.setCurrentWidget(self.page_label)

    def show_image_in_label(self, img=None, scale=1, position=(0, 0)):
        """show image in main image label_page with incoming scale and position and enable left buttons
        Args:
            scale (int): zoom level
            position : offset of image after zoom
        """
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
        self.suggested_defects_btn.setEnabled(True)
        self.delete_btn.setEnabled(True)
        self.heatmap_btn.setEnabled(True)
        self.checkBox_show_neighbours.setEnabled(True)
        self.checkBox_show_neighbours_labels.setEnabled(True)
        # self.yes_defect.setEnabled(True)
        # self.no_defect.setEnabled(True)
        self.save_dataset_btn.setEnabled(True)
        self.save_all_dataset_btn.setEnabled(True)
        self.fs = QImage(
            img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888
        )
        if scale == 1:
            self.image.setScaledContents(True)
            self.image.setPixmap(QPixmap.fromImage(self.fs))
        else:
            self.fs = self.fs.scaled(self.image.size() * scale)
            # self.image.setPixmap(QPixmap.fromImage(self.fs).scaled(self.image.size() * scale))
            position = self.update_image(position)

        return position

    def update_image(self, position):
        """uodate image with position if scale in show_image_in_label is not == 1

        :param position: incoming mouse pisition
        :type position: tuple
        :return: end draw position
        :rtype: tuple
        """
        pixmap = QPixmap(self.image.size())
        px, py = position
        px = (
            px
            if (px <= self.fs.width() - self.image.width())
            else (self.fs.width() - self.image.width())
        )
        py = (
            py
            if (py <= self.fs.height() - self.image.height())
            else (self.fs.height() - self.image.height())
        )
        px = px if (px >= 0) else 0
        py = py if (py >= 0) else 0
        position = (px, py)

        painter = QPainter()
        painter.begin(pixmap)
        painter.drawImage(
            QPoint(0, 0),
            self.fs,
            QRect(position[0], position[1], self.image.width(), self.image.height()),
        )
        painter.end()

        self.image.setPixmap(pixmap)

        return position

    ######## Training Page

    def init_training_page(self):
        """set init parms for training page such as comboboxes"""
        self.b_algorithms.clear()
        self.l_algorithms.clear()
        self.y_algorithms.clear()
        self.classification_algo_combo.clear()
        self.binary_name_filter_combo.clear()
        self.localization_name_filter_combo.clear()
        self.yolo_name_filter_combo.clear()
        self.cls_name_filter_combo.clear()

        b_algorithms = ALGORITHM_NAMES['binary']
        l_algorithms = ALGORITHM_NAMES['localization']
        class_algorithms = ALGORITHM_NAMES['classification']
        yolo_algorithms = ALGORITHM_NAMES['yolo']
        y_algorithms = ALGORITHM_NAMES['yolo']
        self.b_algorithms.addItems(b_algorithms)
        self.l_algorithms.addItems(l_algorithms)
        self.y_algorithms.addItems(y_algorithms)
        self.classification_algo_combo.addItems(class_algorithms)
        self.binary_name_filter_combo.addItem(texts.Titles["all"][self.language])
        self.binary_name_filter_combo.addItems(b_algorithms)
        self.localization_name_filter_combo.addItem(texts.Titles["all"][self.language])
        self.localization_name_filter_combo.addItems(l_algorithms)
        self.yolo_name_filter_combo.addItem(texts.Titles["all"][self.language])
        self.yolo_name_filter_combo.addItems(y_algorithms)
        self.cls_name_filter_combo.addItem(texts.Titles["all"][self.language])
        self.cls_name_filter_combo.addItems(class_algorithms)
        self.set_default_parms()

        # self.b_algorithms.setCurrentText(str(records[0][0]))   #Must change

    def validate_binary_train_params(self):
        reg_ex1 = sQtCore.QRegularExpression("[1-9][0-9]+")
        input_validator = PG.QRegularExpressionValidator(reg_ex1, self.b_epochs)
        self.b_epochs.setValidator(input_validator)
        
        input_validator = PG.QRegularExpressionValidator(reg_ex1, self.b_batch)
        self.b_batch.setValidator(input_validator)

        reg_ex2 = sQtCore.QRegularExpression("[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")
        input_validator = PG.QRegularExpressionValidator(reg_ex2, self.b_lr)
        self.b_lr.setValidator(input_validator)

        reg_ex3 = sQtCore.QRegularExpression("[0-9][0-9]+")
        input_validator = PG.QRegularExpressionValidator(reg_ex3, self.b_te)
        self.b_te.setValidator(input_validator)

        reg_ex4 = sQtCore.QRegularExpression("^([1-9]\d?|100)$")
        input_validator = PG.QRegularExpressionValidator(reg_ex4, self.b_vs)
        self.b_vs.setValidator(input_validator)

    def validate_localization_train_params(self):
        reg_ex1 = sQtCore.QRegularExpression("[1-9][0-9]+")
        input_validator = PG.QRegularExpressionValidator(reg_ex1, self.l_epochs)
        self.l_epochs.setValidator(input_validator)
        
        input_validator = PG.QRegularExpressionValidator(reg_ex1, self.l_batch)
        self.l_batch.setValidator(input_validator)

        reg_ex2 = sQtCore.QRegularExpression("[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")
        input_validator = PG.QRegularExpressionValidator(reg_ex2, self.l_lr)
        self.l_lr.setValidator(input_validator)

        reg_ex3 = sQtCore.QRegularExpression("^([1-9]\d?|100)$")
        input_validator = PG.QRegularExpressionValidator(reg_ex3, self.l_vs)
        self.l_vs.setValidator(input_validator)

    def validate_yolo_train_params(self):
        reg_ex1 = sQtCore.QRegularExpression("[1-9][0-9]+")
        input_validator = PG.QRegularExpressionValidator(reg_ex1, self.y_epochs)
        self.y_epochs.setValidator(input_validator)
        
        input_validator = PG.QRegularExpressionValidator(reg_ex1, self.y_batch)
        self.y_batch.setValidator(input_validator)

        # reg_ex2 = sQtCore.QRegularExpression("[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")
        # input_validator = PG.QRegularExpressionValidator(reg_ex2, self.y_lr)
        # self.y_lr.setValidator(input_validator)

        reg_ex3 = sQtCore.QRegularExpression("^([1-9]\d?|100)$")
        input_validator = PG.QRegularExpressionValidator(reg_ex3, self.y_vs)
        self.y_vs.setValidator(input_validator)

    def localization_algorithm_changed(self):
        text = self.l_algorithms.currentText()
        flag = text[-2:] == 'pr'
        self.l_select_prep.setEnabled(flag)
        self.l_prep.setEnabled(flag)

    def set_default_parms(self):
        """set default parms for sub training pages , that show in UI , every parms"""
        b_parms = {
            "algorithm_name": "Xbc",
            "input_type": True,
            "epochs": "20",
            "batch_size": "8",
            "learning_rate": "1e-3",
            "tuning_epochs": "1",
            "validation_split": "20",
        }

        l_parms = {
            "algorithm_name": "Ulnim",
            "input_type": True,
            "epochs": "20",
            "batch_size": "8",
            "learning_rate": "1e-3",
            "validation_split": "20",
        }

        classification_params = {
            "algorithm_name": "Xcc",
            "epochs": "2",
            "batch_size": "8",
            "learning_rate": "1e-3",
            "tuning_epochs": "1",
            "validation_split": "20",
        }
        
        y_parms = {
            "algorithm_name": "5n",
            "input_type": True,
            "epochs": "20",
            "batch_size": "8",
            # "learning_rate": "1e-3",
            "validation_split": "20",
        }

        self.b_algorithms.setCurrentText(b_parms["algorithm_name"])

        self.input_type_resize.setChecked(not b_parms["input_type"])
        self.input_type_split.setChecked(b_parms["input_type"])

        self.b_epochs.setText(b_parms["epochs"])
        self.b_batch.setText(b_parms["batch_size"])
        self.b_lr.setText(b_parms["learning_rate"])
        self.b_te.setText(b_parms["tuning_epochs"])
        self.b_vs.setText(b_parms["validation_split"])
        self.input_size1.setValue(256)

        # localization model params
        self.l_algorithms.setCurrentText(l_parms["algorithm_name"])

        self.l_input_type_resize.setChecked(not l_parms["input_type"])
        self.l_input_type_split.setChecked(l_parms["input_type"])

        self.l_epochs.setText(l_parms["epochs"])
        self.l_batch.setText(l_parms["batch_size"])
        self.l_lr.setText(l_parms["learning_rate"])
        self.l_vs.setText(l_parms["validation_split"])
        self.l_input_size1.setValue(256)

        # classification model params
        self.class_epoch_lineedit.setText(classification_params["epochs"])
        self.class_batch_lineedit.setText(classification_params["batch_size"])
        self.class_lr_lineedit.setText(classification_params["learning_rate"])
        self.class_tepoch_lineedit.setText(classification_params["tuning_epochs"])
        self.class_split_lineedit.setText(classification_params["validation_split"])

        # yolo model params
        self.y_algorithms.setCurrentText(y_parms["algorithm_name"])

        self.y_input_type_resize.setChecked(not y_parms["input_type"])
        self.y_input_type_split.setChecked(y_parms["input_type"])

        self.y_epochs.setText(y_parms["epochs"])
        self.y_batch.setText(y_parms["batch_size"])
        # self.y_lr.setText(l_parms["learning_rate"])
        self.y_vs.setText(y_parms["validation_split"])
        self.y_input_size1.setValue(256)

        self.logger.create_new_log(message="Set training default params", code=texts_codes.SubTypes['set_training_default_params'])

    def reset_binary_default_params(self):
        """set default parms for binary training pages , that show in UI , every parms"""
        b_parms = {
            "algorithm_name": "Xbc",
            "input_type": True,
            "epochs": "20",
            "batch_size": "8",
            "learning_rate": "1e-3",
            "tuning_epochs": "1",
            "validation_split": "20",
            "proc": "CPU"
            }

        self.b_algorithms.setCurrentText(b_parms["algorithm_name"])

        self.input_type_resize.setChecked(not b_parms["input_type"])
        self.input_type_split.setChecked(b_parms["input_type"])

        self.b_epochs.setText(b_parms["epochs"])
        self.b_batch.setText(b_parms["batch_size"])
        self.b_lr.setText(b_parms["learning_rate"])
        self.b_te.setText(b_parms["tuning_epochs"])
        self.b_vs.setText(b_parms["validation_split"])
        self.input_size1.setValue(256)
        self.b_gpu.setCurrentText(b_parms["proc"])

        self.logger.create_new_log(message="Reset binary training params", code=texts_codes.SubTypes['reset_binary_training_params'])
   
    def reset_localization_default_params(self):
        """set default parms for localization training pages , that show in UI , every parms"""
        l_parms = {
            "algorithm_name": "Ulnim",
            "input_type": True,
            "epochs": "20",
            "batch_size": "8",
            "learning_rate": "1e-3",
            "validation_split": "20",
            "proc": "CPU"
        }

        # localization model params
        self.l_algorithms.setCurrentText(l_parms["algorithm_name"])

        self.l_input_type_resize.setChecked(not l_parms["input_type"])
        self.l_input_type_split.setChecked(l_parms["input_type"])

        self.l_epochs.setText(l_parms["epochs"])
        self.l_batch.setText(l_parms["batch_size"])
        self.l_lr.setText(l_parms["learning_rate"])
        self.l_vs.setText(l_parms["validation_split"])
        self.l_input_size1.setValue(256)
        self.l_gpu.setCurrentText(l_parms["proc"])

        self.logger.create_new_log(message="Reset localization training params", code=texts_codes.SubTypes['reset_localization_training_params'])

    def reset_classification_default_params(self):
        """set default parms for classification training pages , that show in UI , every parms"""
        classification_params = {
            "algorithm_name": "Xcc",
            "epochs": "2",
            "batch_size": "8",
            "learning_rate": "1e-3",
            "tuning_epochs": "1",
            "validation_split": "20",
            "proc": "CPU"
        }

        # classification model params
        self.class_epoch_lineedit.setText(classification_params["epochs"])
        self.class_batch_lineedit.setText(classification_params["batch_size"])
        self.class_lr_lineedit.setText(classification_params["learning_rate"])
        self.class_tepoch_lineedit.setText(classification_params["tuning_epochs"])
        self.class_split_lineedit.setText(classification_params["validation_split"])
        # self.c_gpu.setCurrentText(classification_params["proc"])

        self.logger.create_new_log(message="Reset classification training params", code=texts_codes.SubTypes['reset_classification_training_default_params'])
   
    def reset_yolo_default_params(self):
        """set default parms for yolo training pages , that show in UI , every parms"""
        y_parms = {
            "algorithm_name": "5n",
            "input_type": True,
            "epochs": "20",
            "batch_size": "8",
            # "learning_rate": "1e-3",
            "validation_split": "20",
            "proc": "CPU" 
        }

        # yolo model params
        self.y_algorithms.setCurrentText(y_parms["algorithm_name"])

        self.y_input_type_resize.setChecked(not y_parms["input_type"])
        self.y_input_type_split.setChecked(y_parms["input_type"])

        self.y_epochs.setText(y_parms["epochs"])
        self.y_batch.setText(y_parms["batch_size"])
        # self.y_lr.setText(l_parms["learning_rate"])
        self.y_vs.setText(y_parms["validation_split"])
        self.y_input_size1.setValue(256)
        self.y_gpu.setCurrentText(y_parms["proc"])

        self.logger.create_new_log(message="Reset yolo training params", code=texts_codes.SubTypes['reset_yolo_training_params'])

    def set_b_default_db_parms(self, binary_path):
        """Add default dataset to binary pathes for train"""
        self.b_dp.clear()
        self.b_dp.setPlainText("1. " + binary_path)

    def set_l_default_db_parms(self, localization_path):
        """Add default dataset to localization pathes for train"""
        self.l_dp.clear()
        self.l_dp.setPlainText("1. " + localization_path)

    def set_y_default_db_parms(self, yolo_path):
        """Add default dataset to yolo pathes for train"""
        self.y_dp.clear()
        self.y_dp.setPlainText("1. " + yolo_path)

    def get_binary_parms(self):
        """Get Selected parms that User Selected In Train Binary UI
        :return: all parms in Binary Train UI / in except return []
        :rtype: tuple of Parms
        """
        try:
            binary_algorithm_name = self.b_algorithms.currentText()
            binary_input_size = tuple(
                (self.input_size1.value(), self.input_size1.value())
            )
            binary_input_type = self.input_type_split.isChecked()
            binary_epoch = int(float(self.b_epochs.text()))
            binary_batch = int(float(self.b_batch.text()))
            binary_lr = float(self.b_lr.text())
            binary_te = int(float(self.b_te.text()))
            binary_vs = float(self.b_vs.text()) / 100
            if binary_vs > 0.5:
                binary_vs = 0.5
            str = self.b_gpu.currentText().split(' ')
            binary_gpu = int(str[1]) if str[0]=='GPU' else -1
            text = self.b_dp.toPlainText()
            if text == '':
                self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
                )
                self.set_warning(
                    texts.WARNINGS["parameters_error"][self.language],
                    "train",
                    texts_codes.SubTypes['parameters_error'],
                    level=2,
                )
                return []
            pattern = r"[0-9]+. "
            binary_dp = [s.rstrip() for s in re.split(pattern, text)[1:]]

            return (
                binary_algorithm_name,
                binary_input_size,
                binary_input_type,
                binary_epoch,
                binary_batch,
                binary_lr,
                binary_te,
                binary_vs,
                binary_gpu,
                binary_dp,
            )

        except:
            self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
            )
            self.set_warning(
                texts.WARNINGS["parameters_error"][self.language],
                "train",
                texts_codes.SubTypes['parameters_error'],
                level=2,
            )
            return []

    def get_localization_parms(self):
        """Get Selected parms that User Selected In Train Localization UI
        :return: all parms in Localization Train UI / in except return []
        :rtype: tuple of Parms
        """
        try:
            localization_algorithm_name = self.l_algorithms.currentText()
            localization_pretrain_path = self.l_prep.toPlainText()
            if localization_algorithm_name[-2:] == 'pr' and localization_pretrain_path == '':
                self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
                )
                self.set_warning(
                    texts.WARNINGS["parameters_error"][self.language],
                    "l_train",
                    texts_codes.SubTypes['parameters_error'],
                    level=2,
                )
                return []
            localization_input_size = tuple(
                (self.l_input_size1.value(), self.l_input_size1.value())
            )
            localization_input_type = self.l_input_type_split.isChecked()
            localization_epoch = int(float(self.l_epochs.text()))
            localization_batch = int(float(self.l_batch.text()))
            localization_lr = float(self.l_lr.text())
            localization_vs = float(self.l_vs.text()) / 100
            if localization_vs > 0.5:
                localization_vs = 0.5
            str = self.l_gpu.currentText().split(' ')
            localization_gpu = int(str[1]) if str[0]=='GPU' else -1
            text = self.l_dp.toPlainText()
            if text == '':
                self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
                )
                self.set_warning(
                    texts.WARNINGS["parameters_error"][self.language],
                    "l_train",
                    texts_codes.SubTypes['parameters_error'],
                    level=2,
                )
                return []
            pattern = r"[0-9]+. "
            localization_dp = [s.rstrip() for s in re.split(pattern, text)[1:]]

            return (
                localization_algorithm_name,
                localization_pretrain_path,
                localization_input_size,
                localization_input_type,
                localization_epoch,
                localization_batch,
                localization_lr,
                localization_vs,
                localization_gpu,
                localization_dp,
            )

        except:
            self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
            )
            self.set_warning(
                texts.WARNINGS["parameters_error"][self.language],
                "l_train",
                texts_codes.SubTypes['parameters_error'],
                level=2,
            )
            return []

    def get_classification_parms(self):
        """Get Selected parms that User Selected In Train Classification  UI
        :return: all parms in Classification Train UI
        :rtype: tuple of Parms
        """

        try:
            classification_algorithm_name = self.classification_algo_combo.currentText()
            classification_epoch = int(float(self.class_epoch_lineedit.text()))
            classification_batch = int(float(self.class_batch_lineedit.text()))
            classification_lr = float(self.class_lr_lineedit.text())
            classification_te = int(float(self.class_tepoch_lineedit.text()))
            classification_vs = float(self.class_split_lineedit.text()) / 100

        except:
            self.logger.create_new_log(
                message=texts.WARNINGS["training_params_invalid"]["en"],
                code=texts_codes.SubTypes['parameters_error'],
                level=5
            )
            return []

        if classification_vs > 0.5:
            classification_vs = 0.5

        return (
            classification_algorithm_name,
            classification_epoch,
            classification_batch,
            classification_lr,
            classification_te,
            classification_vs,
        )

    def get_yolo_parms(self):
        """Get Selected parms that User Selected In Train Yolo UI
        :return: all parms in Yolo Train UI / in except return []
        :rtype: tuple of Parms
        """
        try:
            yolo_algorithm_name = self.y_algorithms.currentText()
            yolo_input_size = tuple(
                (self.y_input_size1.value(), self.y_input_size1.value())
            )
            yolo_input_type = self.y_input_type_split.isChecked()
            yolo_epoch = int(float(self.y_epochs.text()))
            yolo_batch = int(float(self.y_batch.text()))
            # yolo_lr = float(self.y_lr.text())
            yolo_vs = float(self.y_vs.text()) / 100
            if yolo_vs > 0.5:
                yolo_vs = 0.5
            str = self.y_gpu.currentText().split(' ')
            yolo_gpu = int(str[1]) if str[0]=='GPU' else -1
            text = self.y_dp.toPlainText()
            if text == '':
                self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
                )
                self.set_warning(
                    texts.WARNINGS["parameters_error"][self.language],
                    "y_train",
                    texts_codes.SubTypes['parameters_error'],
                    level=2,
                )
                return []
            pattern = r"[0-9]+. "
            yolo_dp = [s.rstrip() for s in re.split(pattern, text)[1:]]

            return (
                yolo_algorithm_name,
                # yolo_pretrain_path,
                yolo_input_size,
                yolo_input_type,
                yolo_epoch,
                yolo_batch,
                # yolo_lr,
                yolo_vs,
                yolo_gpu,
                yolo_dp,
            )

        except:
            self.logger.create_new_log(
                message=texts.WARNINGS["parameters_error"]['en'], 
                code=texts_codes.SubTypes['parameters_error'],
                level=5
            )
            self.set_warning(
                texts.WARNINGS["parameters_error"][self.language],
                "y_train",
                texts_codes.SubTypes['parameters_error'],
                level=2,
            )
            return []

    def add_binary_dataset(self):
        """animation Add dataset into train binary UI"""

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
        """animation close page add dataset into train binary UI"""
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
            self.b_add_ds_lineedit.setText("")

    def add_localization_dataset(self):
        """animation Add dataset into train binary UI"""

        height = self.l_add_ds_frame.height()
        if height == 0:
            self.left_box = QPropertyAnimation(self.l_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(0)
            self.left_box.setEndValue(67)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    def cancel_add_localization_ds(self):
        """animation close page add dataset into train binary UI"""
        height = self.l_add_ds_frame.height()
        if height == 67:
            self.left_box = QPropertyAnimation(self.l_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(100)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()
            self.l_add_ds_lineedit.setText("")

    def add_yolo_dataset(self):
        """animation Add dataset into train binary UI"""

        height = self.y_add_ds_frame.height()
        if height == 0:
            self.left_box = QPropertyAnimation(self.y_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(0)
            self.left_box.setEndValue(67)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    def cancel_add_yolo_ds(self):
        """animation close page add dataset into train binary UI"""
        height = self.y_add_ds_frame.height()
        if height == 67:
            self.left_box = QPropertyAnimation(self.y_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(100)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()
            self.y_add_ds_lineedit.setText("")

    def set_side_combobox(self):
        """set combobox Items in data aquization page for select sides"""
        self.comboBox_side_SI.clear()
        self.comboBox_side_SI.addItems(["TOP", "BOTTOM", "BOTH"])
        self.comboBox_side_SI.setCurrentIndex(-1)

    def set_camera_combobox(self, min, max):
        """set combobox Items in data aquization page for select cameras with range min , max"""

        self.comboBox_ncamera_SI.clear()
        i = 0
        for x in range(min, max+1):
            self.comboBox_ncamera_SI.addItem(str(x))
            self.comboBox_ncamera_SI.setItemChecked(i, False)
            i += 1
        self.comboBox_ncamera_SI.setCurrentIndex(-1)

    def set_frame_combobox(self, max):
        """set combobox Items in data aquization page for frames with max size"""
        self.comboBox_nframe_SI.clear()
        i = 0
        for x in range(1, max+1):
            self.comboBox_nframe_SI.addItem(str(x))
            self.comboBox_nframe_SI.setItemChecked(i, False)
            i += 1
        self.comboBox_nframe_SI.setCurrentIndex(-1)

    # Dta aquization page add live cameras              Milad

    def set_combo_boxes(self):
        """set some combo boxes in settings page"""
        string = [
            texts.Titles["english"][self.language],
            texts.Titles["persian"][self.language],
        ]
        self.combo_change_language.clear()
        self.combo_change_language.addItems(string)
        if self.language == "fa":
            self.combo_change_language.setCurrentText(texts.Titles["persian"]["fa"])

    def update_combo_box(self, combo_name, index):
        """Global function for set index Combo boxes

        :param combo_name: considered combobox
        :type combo_name: widget
        :param index: index that should be
        :type index: int
        """
        combo_name.setCurrentIndex(index)

    def set_list_combo_boxes(self, combo_name, items):
        """Global function refresh content of Combo boxes"""
        combo_name.clear()
        combo_name.addItems(items)

    def get_create_dataset_parms(self):
        """get parms for create dataset in user page

        :return: parms of create date set
        :rtype: dictionary
        """
        try:
            user_name = self.user_name_3.text()
            user_id = self.user_id.text()
            dataset_name = self.lineEdit_name_dataset.text()
            path = self.lineEdit_path_dataset.text()
            date = self.today_date.text()

            if not date:
                self.set_warning(
                    texts.ERRORS["date_empty"][self.language],
                    "profile",
                    texts_codes.SubTypes['ds_params_error'],
                    level=2,
                )
                return {}
                
            if not user_name:
                self.set_warning(
                    texts.ERRORS["creator_user_name_empty"][self.language],
                    "profile",
                    texts_codes.SubTypes['ds_params_error'],
                    level=2,
                )
                return {}

            if not dataset_name:
                self.set_warning(
                    texts.ERRORS["dataset_name_empty"][self.language],
                    "profile",
                    texts_codes.SubTypes['ds_params_error'],
                    level=2,
                )
                return {}

            if not path:
                self.set_warning(
                    texts.ERRORS["location_empty"][self.language],
                    "profile",
                    texts_codes.SubTypes['ds_params_error'],
                    level=2,
                )
                return {}

            return {
                "user_name": user_name,
                "user_id": user_id,
                "dataset_name": dataset_name,
                "path": path,
                "date": date,
            }

        except:
            self.logger.create_new_log(
                message="Except in get create dataset parms from UI", 
                code=texts_codes.SubTypes['ds_params_error'],
                level=5
            )
            return []

    def open_file_dialog(self):
        """open and set path dataset created"""
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_path_dataset.setText(file)

    def clear_table_name(self, name):
        """cleare table with name

        :param name: widget of table that want to be clear
        :type name: widget
        """
        for i in range(name.rowCount()):
            name.removeRow(0)

    def show_all_datasets(self, records):
        """show datasets in User page

        :param records: dictionary of dataset
        """
        self.all_ds_id.setText(str(records[0]))
        self.all_ds_name.setText(str(records[1]))
        self.all_ds_owner_user.setText(str(records[2]))
        self.all_ds_path.setText(str(records[3]))

    def show_user_datasets(self, records):
        """show user own of dataset in User page
        :type records: dictionary
        """
        self.my_ds_id.setText(str(records[0]))
        self.my_ds_name.setText(str(records[1]))
        self.my_ds_owner_user.setText(str(records[2]))
        self.my_ds_path.setText(str(records[3]))

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "toggleButton":
            self.toggleMenu(True)

        if btnName == "btn_technical_move":
            self.technical_move(True)

        if btnName == "Data_auquzation_btn":
            self.left_bar_clear()
            self.Data_auquzation_btn.setStyleSheet(
                "background-image: url(./images/icons/graber.png);background-color: rgb(170, 170, 212);color:rgp(0,0,0);"
            )
            self.stackedWidget.setCurrentWidget(self.page_data_auquzation)

        if btnName == "label_btn" or btnName == "label_btn_SI":
            self.left_bar_clear()
            self.label_btn.setStyleSheet(
                "background-image: url(./images/icons/label.png);background-color: rgb(170, 170, 212);color:rgp(0,0,0);"
            )
            self.stackedWidget.setCurrentWidget(self.page_label)

        if btnName == "checkBox_top":
            if self.checkBox_top.isChecked():
                for i in range(1, 13):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setEnabled(False)
            else:
                for i in range(1, 13):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setEnabled(True)
            self.select_unselect_camera(
                top_flag=True, status=self.checkBox_top.isChecked()
            )

        if btnName == "checkBox_bottom":
            if self.checkBox_bottom.isChecked():
                for i in range(13, 25):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setEnabled(False)
            else:
                for i in range(13, 25):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setEnabled(True)
            self.select_unselect_camera(
                bottom_flag=True, status=self.checkBox_bottom.isChecked()
            )

        if btnName == "checkBox_all":
            if self.checkBox_all.isChecked():
                self.checkBox_top.setCheckState(Qt.CheckState.Unchecked)
                self.checkBox_top.setEnabled(False)
                self.checkBox_bottom.setCheckState(Qt.CheckState.Unchecked)
                self.checkBox_bottom.setEnabled(False)
                for i in range(1, 25):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setEnabled(False)
            else:
                self.checkBox_top.setEnabled(True)
                self.checkBox_bottom.setEnabled(True)
                for i in range(1, 25):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setEnabled(True)
            self.select_unselect_camera(
                all_flag=True, status=self.checkBox_all.isChecked()
            )

        if btnName[:6] == "camera" and btnName[8:] == "_btn":
            self.select_unselect_camera(
                cam_number=int(btnName[6:8]),
                status=not (self.selelcted_cameras[int(btnName[6:8]) - 1]),
            )

        if btnName == "tuning_btn":
            self.left_bar_clear()
            self.tuning_btn.setStyleSheet(
                "background-image: url(./images/icons/tuning.png);background-color: rgb(170, 170, 212);color:rgp(0,0,0);"
            )
            # self.stackedWidget.setCurrentWidget(self.page_tuning)
            self.extra_left_box_move()

        if btnName == "pbt_btn":
            self.left_bar_clear()
            self.pbt_btn.setStyleSheet(
                "background-image: url(./images/icons/PBT.png);background-color: rgb(170, 170, 212);color:rgp(0,0,0);"
            )
            # self.stackedWidget.setCurrentWidget(self.page_pbt)
        
        if btnName == 'log_btn':
            self.show_log_win = show_logs_UI.show_logs(lang=self.language)
            texts.set_show_log(self, self.language)
            self.show_log_win.show()

        if btnName == "aboutus_btn":
            self.left_bar_clear()
            # self.page_aboutus_btn.setStyleSheet("QPushButton {background-color: rgb(197 , 195,196);	color: rgb(0,0,0);	border: none;	text-align: left;padding-left: 10px;}QPushButton:hover {background-color:  rgb(197 , 195,196)};QPushButton:pressed {background-color: rgb(197 , 195,196);}")
            self.stackedWidget.setCurrentWidget(self.page_aboutus)

        if btnName == "Binary_btn":
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            # self.stackedWidget.setCurrentWidget(self.page_Binary)

        if btnName == "Localization_btn":
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            # self.stackedWidget.setCurrentWidget(self.page_Localization)

        if btnName == "Classification_btn":
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            # self.stackedWidget.setCurrentWidget(self.page_Classification)

        if btnName == "yolo_btn":
            self.start_box_animation(self.extraLeftBox.width(), 0, "left")
            # self.stackedWidget.setCurrentWidget(self.page_Classification)

        if btnName == "binary_list":
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_list)
            self.binary_list.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.binary_training.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
            self.binary_history.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
        if btnName == "binary_training":
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_training)
            self.binary_training.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.binary_list.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
            self.binary_history.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "binary_history":
            self.stackedWidget_binary.setCurrentWidget(self.page_binary_history)
            self.binary_history.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.binary_list.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
            self.binary_training.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "localization_training":
            self.stackedWidget_localization.setCurrentWidget(
                self.page_localization_training
            )
            self.localization_training.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.localization_history.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "localization_history":
            self.stackedWidget_localization.setCurrentWidget(
                self.page_localization_history
            )
            self.localization_history.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.localization_training.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "yolo_training":
            self.stackedWidget_yolo.setCurrentWidget(
                self.page_yolo_training
            )
            self.yolo_training.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.yolo_history.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "yolo_history":
            self.stackedWidget_yolo.setCurrentWidget(
                self.page_yolo_history
            )
            self.yolo_history.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.yolo_training.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "classification_class_list":
            self.stackedWidget_classification.setCurrentWidget(
                self.page_classification_class_list
            )
            self.classification_class_list.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.classification_training.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
            self.classification_history.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "classification_add_new_class":
            self.stackedWidget_classification.setCurrentWidget(
                self.page_classification_add_new_class
            )

        if btnName == "classification_training":
            self.stackedWidget_classification.setCurrentWidget(
                self.page_classification_training
            )
            self.classification_training.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.classification_class_list.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
            self.classification_history.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "classification_history":
            self.stackedWidget_classification.setCurrentWidget(
                self.page_classification_history
            )
            self.classification_history.setStyleSheet(
                "QPushButton { background-color: rgb(170 ,170, 170); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(197 ,195, 196);}"
            )
            self.classification_training.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )
            self.classification_class_list.setStyleSheet(
                "QPushButton { background-color: rgb(100, 100, 100); color: rgb(0,0,0); border: none;} \
                                            QPushButton:hover {background-color:  rgb(150 ,150, 150);}"
            )

        if btnName == "label_show_help_btn":
            self.label_show_help()

        if btnName == "yes_defect":
            self.def_yes_defect()

        if btnName == "no_defect":
            self.def_no_defect()

        if btnName == "login_btn":
            pass
            # #print("click")
            # self.show_login()

        if btnName == "setting_btn":
            self.setting_win()

        if btnName == "polygon_btn":
            self.polygon()

        if btnName == "zoomIn_btn":
            self.zoom_in()

        if btnName == "zoomOut_btn":
            self.zoom_out()

        if btnName == "drag_btn":
            self.drag_image()

        if btnName == "btn_software_setting":
            # self.bounding_box()
            self.stackedWidget.setCurrentWidget(self.page_software_setting)
            # setting.language(self)
            # self.stackedWidget.setCurrentWidget(self.page_software_setting)

        if btnName == "load_coil_btn":
            # #print('asdqwdwqd')
            self.data_loader_win_show()

        if btnName == "checkBox_select":
            # #print('asdqwdwqd')

            self.select_unselect_all()

        if btnName == "checkBox_all_imgs_SI":
            self.able_enable_filters()

        if btnName == "checkBox_all_camera_SI":
            self.able_enable_camera_filter()

        if btnName == "checkBox_all_frame_SI":
            self.able_enable_frame_filter()

        # if btnName == "show_tools_btn":
        #     self.show_frame_tools()
        if btnName == "label_btn_2":
            self.stackedWidget.setCurrentWidget(self.page_label)
            image = ImageQt.fromqpixmap(self.crop_image.pixmap())
            image = np.ascontiguousarray(image)
            self.fs = QImage(
                image,
                image.shape[1],
                image.shape[0],
                image.strides[0],
                QImage.Format_BGR888,
            )
            self.image.setPixmap(QPixmap.fromImage(self.fs))

        if btnName == "b_add_ds":
            self.add_binary_dataset()

        if btnName == "b_add_cancel":
            self.cancel_add_binary_ds()

        if btnName == 'l_algorithms':
            self.localization_algorithm_changed()

        if btnName == "l_add_ds":
            self.add_localization_dataset()

        if btnName == "l_add_cancel":
            self.cancel_add_localization_ds()

        if btnName == "y_add_ds":
            self.add_yolo_dataset()

        if btnName == "y_add_cancel":
            self.cancel_add_yolo_ds()

        if self.extraLeftBox.width() != 0:
            self.extra_left_box_move()

        if btnName == "create_new_database":
            self.stackedWidget_2.setCurrentWidget(self.page_create_db)
            chart_funcs.clear_userprofile_barchart(self)
            self.create_new_database.setStyleSheet(
                "color:white;background-color: rgb(212, 212, 212);"
            )
            self.all_databases.setStyleSheet("color:white;")
            self.my_databases_2.setStyleSheet("color:white;")
            self.my_databases_3.setStyleSheet("color:white;")

        if btnName == "all_databases":
            self.stackedWidget_2.setCurrentWidget(self.page_all_db)
            self.create_new_database.setStyleSheet("color:white;")
            self.all_databases.setStyleSheet(
                "color:white;background-color: rgb(212, 212, 212);"
            )
            self.my_databases_2.setStyleSheet("color:white;")
            self.my_databases_3.setStyleSheet("color:white;")

        if btnName == "my_databases_2":
            self.stackedWidget_2.setCurrentWidget(self.page_my_db)
            self.create_new_database.setStyleSheet("color:white;")
            self.all_databases.setStyleSheet("color:white;")
            self.my_databases_2.setStyleSheet(
                "color:white;background-color: rgb(212, 212, 212);"
            )
            self.my_databases_3.setStyleSheet("color:white;")

        if btnName == "my_databases_3":
            self.stackedWidget_2.setCurrentWidget(self.page_my_pipelines)
            chart_funcs.clear_userprofile_barchart(self)
            self.create_new_database.setStyleSheet("color:white;")
            self.all_databases.setStyleSheet("color:white;")
            self.my_databases_2.setStyleSheet("color:white;")
            self.my_databases_3.setStyleSheet(
                "color:white;background-color: rgb(212, 212, 212);"
            )

        if btnName == "toolButton_select_directory":
            self.open_file_dialog()

        if btnName == "pipeline_pbt_btn":
            self.stackedWidget_pbt.setCurrentWidget(self.page_pipeline)
            self.refresh_pipline_tabs_in_PBT()
        if btnName == "load_dataset_pbt_btn":
            self.stackedWidget_pbt.setCurrentWidget(self.page_load_dataset)
            self.set_active_color(wich_tab=1)
        if btnName == "history_pbt_btn":
            self.stackedWidget_pbt.setCurrentWidget(self.page_history)
            self.set_active_color(wich_tab=2)

    def select_unselect_camera(
        self,
        cam_number=-1,
        top_flag=False,
        bottom_flag=False,
        all_flag=False,
        status=True,
    ):
        """This function is used to change camera icons after select or unselect them.

        :param cam_number: Camera number clicked on it, defaults to -1
        :type cam_number: int, optional
        :param top_flag: Flag that determine all top cameras are selected or not, defaults to False
        :type top_flag: bool, optional
        :param bottom_flag: Flag that determine all bottom cameras are selected or not, defaults to False
        :type bottom_flag: bool, optional
        :param all_flag: Flag that determine all cameras are selected or not, defaults to False
        :type all_flag: bool, optional
        :param status: Flag that determine camera(s) are selected or unselected, defaults to True
        :type status: bool, optional
        """
        if all_flag:
            if status:
                self.selelcted_cameras = [True] * 24
                for i in range(1, 25):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setStyleSheet(
                        "background:Transparent; border-color:Transparent; background-color: #a3aeb5; border-radius: 10px;"
                    )
            else:
                self.selelcted_cameras = [False] * 24
                for i in range(1, 25):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setStyleSheet(
                        "background:Transparent; border-color:Transparent;"
                    )

        elif top_flag:
            if status:
                self.selelcted_cameras[:12] = [True] * 12
                for i in range(1, 13):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setStyleSheet(
                        "background:Transparent; border-color:Transparent; background-color: #a3aeb5; border-radius: 10px;"
                    )
            else:
                self.selelcted_cameras[:12] = [False] * 12
                for i in range(1, 13):
                    if i < 10:
                        btn_name = eval("self.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setStyleSheet(
                        "background:Transparent; border-color:Transparent;"
                    )

        elif bottom_flag:
            if status:
                self.selelcted_cameras[12:] = [True] * 12
                for i in range(13, 25):
                    btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setStyleSheet(
                        "background:Transparent; border-color:Transparent; background-color: #a3aeb5; border-radius: 10px;"
                    )
            else:
                self.selelcted_cameras[12:] = [False] * 12
                for i in range(13, 25):
                    btn_name = eval("self.camera%s_btn" % i)
                    btn_name.setStyleSheet(
                        "background:Transparent; border-color:Transparent;"
                    )

        else:
            if cam_number < 10:
                btn_name = eval("self.camera0%s_btn" % cam_number)
            else:
                btn_name = eval("self.camera%s_btn" % cam_number)
            if status:
                self.selelcted_cameras[cam_number - 1] = True
                btn_name.setStyleSheet(
                    "background:Transparent; border-color:Transparent; background-color: #a3aeb5; border-radius: 10px;"
                )
            else:
                self.selelcted_cameras[cam_number - 1] = False
                btn_name.setStyleSheet(
                    "background:Transparent; border-color:Transparent;"
                )

    def set_img_btn_camera(self, cam_num, status="True"):
        """set image in connection cameras active/deactive with number"""
        if status == "True":
            img_top = "UI/images/camtop_actived.png"
            img_btm = "UI/images/cambtm_actived.png"

        elif status == "Disconnect":
            img_top = "UI/images/camtop.png"
            img_btm = "UI/images/cambtm.png"

        else:
            img_top = "UI/images/camtop_deactive.png"
            img_btm = "UI/images/cambtm_deactive.png"

        if int(cam_num) <= 12:
            if int(cam_num) < 10:
                btn_name = eval("self.camera0%s_btn" % cam_num)
            else:
                btn_name = eval("self.camera%s_btn" % cam_num)
            ico = sQIcon()
            ico.addFile(img_top, sQSize(30,30), sQIcon.Disabled, sQIcon.Off)
            btn_name.setIcon(ico)

        else:
            btn_name = eval("self.camera%s_btn" % cam_num)
            ico = sQIcon()
            ico.addFile(img_btm, sQSize(30,30), sQIcon.Disabled, sQIcon.Off)
            btn_name.setIcon(ico)

    def get_selected_cameras(self):
        return self.selelcted_cameras

    def change_plc_status(self, status=True):
        if status == "connect":
            self.plc_status_label.setStyleSheet(
                "background: rgb(50, 200, 50); border-radius: 15px; border: 3px solid #434c5d;"
            )
        elif status == "disconnect":
            self.plc_status_label.setStyleSheet(
                "background: red; border-radius: 15px; border: 3px solid #434c5d;"
            )
        elif status == "retry":
            self.plc_status_label.setStyleSheet(
                "background: yellow; border-radius: 15px; border: 3px solid #434c5d;"
            )

    def set_active_color(
        self,
        wich_tab,
    ):
        tabs = [self.pipeline_pbt_btn, self.load_dataset_pbt_btn, self.history_pbt_btn]
        tabs[wich_tab].setStyleSheet("background-color: rgb(200,200,200)")
        for i, _ in enumerate(tabs):
            if i != wich_tab:
                tabs[i].setStyleSheet("background-color: rgb(100,100,100)")

    def refresh_pipline_tabs_in_PBT(self):

        self.cbBox_of_binary_model_in_PBT_page.clear()
        self.cbBox_of_binary_model_in_PBT_page.addItem("All")
        self.cbBox_of_binary_model_in_PBT_page.addItems(ALGORITHM_NAMES["binary"])
        self.cbBox_of_localization_model_in_PBT_page.clear()
        self.cbBox_of_localization_model_in_PBT_page.addItem("All")
        self.cbBox_of_localization_model_in_PBT_page.addItems(
            ALGORITHM_NAMES["localization"]
        )

        self.cbBox_of_yolo_model_in_PBT_page.clear()
        self.cbBox_of_yolo_model_in_PBT_page.addItem("All")
        self.cbBox_of_yolo_model_in_PBT_page.addItems(
            ALGORITHM_NAMES["yolo"]
        )


        self.cbBox_of_multiClassification_model_in_PBT_page.clear()
        self.cbBox_of_multiClassification_model_in_PBT_page.addItem("All")
        self.cbBox_of_multiClassification_model_in_PBT_page.addItems(
            ALGORITHM_NAMES["classification"]
        )
        self.set_active_color(wich_tab=0)
        self.pipline_name.setText("")
        self.pipline_name.setPlaceholderText(
            texts.Titles["example_of_pipline_name"][self.language]
        )
        self.pipline_name_status.setText(
            texts.Titles["warn_of_valid_pipline_name"][self.language]
        )
        self.LBL_of_selected_binary_classifaction_model_in_PBT_page.setText("")
        self.LBL_of_selected_multiClassification_model_in_PBT_page.setText("")
        self.LBL_of_selected_localization_model_in_PBT_page.setText("")
        self.LBL_of_selected_binary_yolo_model_in_PBT_page.setText("")

    def connet_keyboard(self, keys, functions, page_name):
        """Connect keys into specefic function in a page"""
        for key in keys:
            self.keyboard_connections[key] = (page_name, functions)

    def do_keyboard(self, key):
        """run function with input key"""
        connections = self.keyboard_connections.get(key)
        if connections is None:
            return -1
        else:
            page_name, funcs = connections
            if (
                page_name == PAGES_IDX.get(self.stackedWidget.currentIndex())
                or page_name == None
            ):
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
        self.plabel_frame_txt.setText(str(pos[-1][1]))

    def show_image_btn(self, label_name, img_path):
        """set pixmap btn icon with input image path"""
        label_name.setIcon(sQPixmap.fromImage(sQImage(img_path)))

    def set_qlineedit_validator(self):
        """set validator for input line edits in binary train page"""
        self.onlyInt = sQIntValidator()
        self.binary_epoch_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_epoch_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_tepoch_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_tepoch_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_batch_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_batch_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_split_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_split_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_loss_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_loss_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_acc_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_acc_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_prec_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_prec_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_rec_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_rec_max_filter_lineedit.setValidator(self.onlyInt)
        self.binary_date_min_filter_lineedit.setValidator(self.onlyInt)
        self.binary_date_max_filter_lineedit.setValidator(self.onlyInt)

    def show_mesagges(self, label_name, text="", level=0, clearable=True, prefix=True):
        """
        this function is used to show input message in input label, also there is a message level determining the color of label, and a timer to clear meesage after a while

        Inputs:
            label_name: label element name to show the message in
            text: input message to show (in string)
            level: level of the message (in int), its a value betweem [0, 2] determining the bakground color of message label
            clearable: a boolean value determining whater to clear the message after timeout or not
            prefix: a boolean value determinign wheater to show the message prefix or not

        Returns: None
        """

        if text != "" and not self.show_mesagges_thread_lock:
            if level == 0:
                label_name.setText(text)
                # label_name.setStyleSheet("color:{}".format(color))
            #
            if level == 1:
                if prefix:
                    label_name.setText(text)
                else:
                    label_name.setText(text)
                label_name.setStyleSheet(
                    "background-color: %s; color:white;"
                    % (colors_pallete.warning_yellow)
                )
            #
            if level >= 2:
                if prefix:
                    label_name.setText(text)
                else:
                    label_name.setText(text)
                label_name.setStyleSheet(
                    "background-color: %s; color:white;" % (colors_pallete.failed_red)
                )

            #
            if clearable and not self.show_mesagges_thread_lock:
                self.show_mesagges_thread_lock = True

                # timer to clear the message
                # #print("show_mesagges_thread_lock True")
                QTimer.singleShot(2000, lambda: self.show_mesagges(label_name))

        # clear the message after timeout

    # notification manager
    def check_nofification_status(self):
        self.notif_manager.pop_and_create_new_notif(font_size=10, font_style="Arial")

    def set_label(self, label_name, text):
        """set text in input llabel"""
        label_name.setText(text)

    def set_image_label(self, label_name, img):
        """set imnage in input label"""
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = sQImage(
            img.data, w, h, bytes_per_line, sQImage.Format_BGR888
        )
        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

    def set_btn_image(self, btn_name, path):
        btn_name.setIcon(QIcon(path))

    def set_widget_page(self, widget, page_name):
        """set widget page with page name"""
        widget.setCurrentWidget(page_name)

    # --------------------------------------------PLC---------------------------

    def get_plc_ip(self):
        """
        this function takes anf returns input PLC IP from ui

        Inputs: None

        Returns:
            PLC ip: (in string)
        """

        return self.plc_ip_line.text()

    def set_plc_ip(self, text):
        """
        this function will set input PLC IP from database to ui field

        Inputs:
            text: PLC ip (in string)

        Returns: None
        """
        self.plc_ip_line.setText(text)

    def set_status_plc(self, mode=False, auto=True, text=None):
        if auto:
            if not mode:

                self.plc_status_line.setText(texts.Titles["disconnect"][self.language])
                self.plc_warnings.setText(texts.Titles["disconnect"][self.language])
                self.plc_status = False
                self.plc_status_line.setStyleSheet("color : red")
                self.plc_warnings.setStyleSheet("color : red")

            else:
                self.plc_status_line.setText(texts.Titles["connect"][self.language])
                self.plc_warnings.setText(texts.Titles["connect"][self.language])
                self.plc_status = True
                self.plc_status_line.setStyleSheet("color : green")
                self.plc_warnings.setStyleSheet("color : green")
        else:
            self.plc_status_line.setText(text)
            self.plc_warnings.setText(text)
            self.plc_status_line.setStyleSheet("color : #FDFF09")
            self.plc_warnings.setStyleSheet("color : #FDFF09")

    def change_plc_check_status(self, mode=True):
        # x=self.detect_sensor_check_box.isChecked()

        self.detect_sensor_check_box.setChecked(bool(mode))
        if DEBUG_UI:
            print("asdwdw", mode)

    def update_plc_temp(self, temp_top=0, temp_down=0):
        self.label_up_temperature.setText(str(temp_top))
        self.label_down_temperature.setText(str(temp_down))

    def start_wind(self, end=False):
        if not end:
            self.wind_itr = self.update_wind_plc
            self.start_wind_btn.setEnabled(False)
            self.start_wind_btn.setText(
                texts.Titles["seconds"][self.language].format(self.wind_itr)
            )
            QTimer.singleShot(1000, lambda: self.start_wind(end=True))
        else:
            if self.wind_itr != 1:
                self.wind_itr -= 1
                if self.wind_itr != 1:
                    self.start_wind_btn.setText(
                        texts.Titles["seconds"][self.language].format(self.wind_itr)
                    )
                else:
                    self.start_wind_btn.setText(
                        texts.Titles["second"][self.language].format(self.wind_itr)
                    )
                QTimer.singleShot(1000, lambda: self.start_wind(end=True))
            else:
                self.start_wind_btn.setText(texts.Titles["start"][self.language])
                self.start_wind_btn.setEnabled(True)
                api.set_wind(False)

    def clear_binary_filters_fields(self, wich_page='not PBT'):
        if wich_page != "PBT":
            self.binary_epoch_min_filter_lineedit.clear()
            self.binary_epoch_max_filter_lineedit.clear()
            self.binary_tepoch_min_filter_lineedit.clear()
            self.binary_tepoch_max_filter_lineedit.clear()
            self.binary_batch_min_filter_lineedit.clear()
            self.binary_batch_max_filter_lineedit.clear()
            self.binary_split_min_filter_lineedit.clear()
            self.binary_split_max_filter_lineedit.clear()
            self.binary_loss_min_filter_lineedit.clear()
            self.binary_loss_max_filter_lineedit.clear()
            self.binary_acc_min_filter_lineedit.clear()
            self.binary_acc_max_filter_lineedit.clear()
            self.binary_prec_min_filter_lineedit.clear()
            self.binary_prec_max_filter_lineedit.clear()
            self.binary_rec_min_filter_lineedit.clear()
            self.binary_rec_max_filter_lineedit.clear()
            self.binary_start_year_lineedit.clear()
            self.binary_start_month_lineedit.clear()
            self.binary_start_day_lineedit.clear()
            self.binary_end_year_lineedit.clear()
            self.binary_end_month_lineedit.clear()
            self.binary_end_day_lineedit.clear()

    def clear_localization_filters_fields(self):
        self.localization_epoch_min_filter_lineedit.clear()
        self.localization_epoch_max_filter_lineedit.clear()
        self.localization_batch_min_filter_lineedit.clear()
        self.localization_batch_max_filter_lineedit.clear()
        self.localization_split_min_filter_lineedit.clear()
        self.localization_split_max_filter_lineedit.clear()
        self.localization_loss_min_filter_lineedit.clear()
        self.localization_loss_max_filter_lineedit.clear()
        self.localization_acc_min_filter_lineedit.clear()
        self.localization_acc_max_filter_lineedit.clear()
        self.localization_iou_min_filter_lineedit_2.clear()
        self.localization_iou_max_filter_lineedit_2.clear()
        self.localization_fscore_min_filter_lineedit.clear()
        self.localization_fscore_max_filter_lineedit.clear()
        self.localization_start_year_lineedit.clear()
        self.localization_start_month_lineedit.clear()
        self.localization_start_day_lineedit.clear()
        self.localization_end_year_lineedit.clear()
        self.localization_end_month_lineedit.clear()
        self.localization_end_day_lineedit.clear()

    def clear_yolo_filters_fields(self):
        self.yolo_epoch_min_filter_lineedit.clear()
        self.yolo_epoch_max_filter_lineedit.clear()
        self.yolo_batch_min_filter_lineedit.clear()
        self.yolo_batch_max_filter_lineedit.clear()
        self.yolo_split_min_filter_lineedit.clear()
        self.yolo_split_max_filter_lineedit.clear()
        self.yolo_boxloss_min_filter_lineedit.clear()
        self.yolo_boxloss_max_filter_lineedit.clear()
        self.yolo_objloss_min_filter_lineedit.clear()
        self.yolo_objloss_max_filter_lineedit.clear()
        self.yolo_clsloss_min_filter_lineedit.clear()
        self.yolo_clsloss_max_filter_lineedit.clear()
        self.yolo_recall_min_filter_lineedit.clear()
        self.yolo_recall_max_filter_lineedit.clear()
        self.yolo_prec_min_filter_lineedit.clear()
        self.yolo_prec_max_filter_lineedit.clear()
        self.yolo_map_min_filter_lineedit.clear()
        self.yolo_map_max_filter_lineedit.clear()
        self.yolo_start_year_lineedit.clear()
        self.yolo_start_month_lineedit.clear()
        self.yolo_start_day_lineedit.clear()
        self.yolo_end_year_lineedit.clear()
        self.yolo_end_month_lineedit.clear()
        self.yolo_end_day_lineedit.clear()

    def show_labeling_help(self, n_helps=6):
        path = 'images/labeling_helps'
        help_images = sorted(os.listdir(path))
        for i in range(n_helps):
            img = cv2.imread(os.path.join(path, help_images[i]))
            image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
            exec('self.labeling_help_{}.setPixmap(QPixmap.fromImage(image))'.format(i+1))

if __name__ == "__main__":
    app = QApplication()
    win = UI_main_window()
    api = api.API(win)
    win.show()
    sys.exit(app.exec())

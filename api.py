# from logging import _Level
import ast
from email.mime import image
from ntpath import join
from operator import le
from pickletools import uint8
import re
from shutil import which
from stat import FILE_ATTRIBUTE_NORMAL
import sys
from ast import Try
from email import utils
from tkinter import NO, PIESLICE
from PySide6.QtCore import *
from PySide6.QtWidgets import QFileDialog
from cv2 import log

from PySide6 import QtGui
from PySide6.QtCharts import QPieSeries, QPieSlice, QChart, QChartView
from PySide6.QtCore import *
from PySide6.QtCore import QThread as sQThread
from PySide6.QtGui import QPen, QPainter
from PySide6.QtWidgets import QFileDialog
from matplotlib import pyplot as plt
from matplotlib.style import use
from pyautogui import PRIMARY

from Defect_detection_modules.SteelSurfaceInspection import SSI, CreateHeatmap
from app_settings import Settings
from backend import data_grabber, camera_connection
from backend.pipelines import (
    MODEL_ACCURACY,
    MODEL_DICE,
    MODEL_F1,
    MODEL_IOU,
    MODEL_LOSS,
    MODEL_PRECISION,
    MODEL_RECALL,
    Pipeline,
)
import backend.pipelines
from backend.mouse import Mouse
from backend.keyboard import Keyboard

# from backend import Label
import cv2
import threading
import time
from PIL import ImageQt
import numpy as np
import math
import os
from datetime import date, time, datetime
from PyQt5.QtWidgets import QListWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap, QImage

# from backend import add_remove_label
from PyQt5 import QtCore, QtWidgets
from Sheet_loader_win import get_data
from PySide6.QtCore import QThread
from functools import partial
from backend import (
    Label,
    chart_funcs,
    binary_model_funcs,
    binary_list_funcs,
    date_funcs,
    classification_model_funcs,
    classification_list_funcs,
    dataset,
    colors_pallete,
    plc_managment,
    level2_connection,
    localization_model_funcs,
    pathStructure
)

import database_utils
from utils import *
from utils.move_on_list import moveOnList, moveOnImagrList

import texts  # eror and warnings texts
import texts_codes
from utils import tempMemory, Utils

from backend.dataset import Dataset
from random_split import get_crops, get_crops_no_defect, get_crops_no_defect2
import train_api

from labeling.labeling_UI import labeling

from Dataset_selection.ds_select_UI import Ds_selection
from FileDialog import FileDialog

from labeling import labeling_api
from pynput.mouse import Button, Controller

from login_win.login_api import login_API
from camera_live_thread import ImageManager
from multiprocessing import Process
import dataset_utils
import image_processing_worker
import save_all_worker
import random

# _______JJ importing:
import random
import time
from PySide6.QtWidgets import QLabel as sQLabel, QProgressBar
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6.QtWidgets import QVBoxLayout
from Train_modules.models import xception_cnn, resnet_cnn
from Train_modules.models import unet, low_unet, resnet_unet
import matplotlib.pyplot as plt
from tensorflow.keras.metrics import Accuracy, Precision, Recall
from Train_modules.deep_utils import metrics
from backend import pipelines
import tensorflow as tf
from image_splitter import ImageCrops
import json
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from PySide6.QtCore import QObject, QThread, Signal

# _______JJ


WIDTH_TECHNICAL_SIDE = 49 * 12
HEIGHT_FRAME_SIZE = 51
NCAMERA = 12

TECHNICAL_WGT_NAME_TO_SIDE = {"up_side_technical", "top", "bottom"}

MAX_SHOW_IN_PAGE = 20

FRAME_RATE = 7


# down_side_technical     ,   up_side_technical
class API:
    def __init__(self, ui):
        self.ui = ui
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.move_on_list = moveOnList()
        self.db = database_utils.dataBaseUtils(ui_obj=self.ui)
        self.create_classlist_pie_chart()
        self.create_label_color()
        self.create_default_ds()
        # self.mask_label_backend=Label.maskLbl(self.ui.get_size_label_image(), LABEL_COLOR)
        self.label_bakcend = {
            "mask": Label.maskLbl((1200, 1920), self.LABEL_COLOR),
        }
        self.label_bakcend_neighbours = {
            "mask": Label.maskLbl((1200, 1920), self.LABEL_COLOR),
        }

        # Label.bbox_lbl()
        self.label_memory = tempMemory.manageLabel()
        self.image_save_status = {}
        # self.technical_backend = {'top': data_grabber()}
        self.thechnicals_backend = {}
        # self.ui.crop_image.mouseDoubleClickEvent = self.fit_image
        self.t = 0
        self.scale = 1
        self.position = [0, 0]
        self.pressed = None
        self.current_technical_side = ""
        self.selected_images_for_label = tempMemory.manageSelectedImage()
        self.finish_draw = 0
        self.language = self.ui.language
        self.img = None
        self.n_imgs = []
        self.n_anns = []
        self.selected_defects = []
        # iterator for binary-model history tabel
        self.bmodel_tabel_itr = 1
        # iterator for localization-model history tabel
        self.lmodel_tabel_itr = 1
        self.bmodel_count = 0
        self.lmodel_count = 0
        self.filter_mode = False
        self.lfilter_mode = False
        self.flag_all_camera = False
        self.start_capture_flag = False
        self.ready_capture_flag = False
        self.live_type = 0

        # binarylist dataset parms
        self.dataset_params = {}

        self.logged_in = False
        # Create labeling window
        # -------------------------------------

        # self.labaling_UI=labeling_UI.labeling()
        # self.labeling_win=labeling()
        self.mouse_controll = Controller()

        self.get_defects()

        # self.defects_name,self.defects_info=self.db.get_defects()

        # -------------------------------------
        # connet buttons to correspondings functions in API               ////////////////////
        self.button_connector()
        self.comboBox_connector()
        self.QTableWidget_connector()
        self.checkbox_connector()
        self.perfect_show = True
        self.defect_show = True
        # connet mouse event to correspondings functions in API
        self.mouse_connector()
        # connet keyboard event to correspondings functions in API
        self.keyboard_connector()
        # -------------------------------------

        self.load_settings()

        # connect to camera connection
        self.cameras = camera_connection.connect_manage_cameras()
        self.i = 0
        self.j = 0

        # connecting camera

        self.index_num = 0

        # binary model start-up funcs
        self.refresh_binary_models_table(get_count=True)

        # create binarylist sliders on UI
        # perfect
        self.binarylist_sliders_check = []
        self.binarylist_sliders_check.append(
            binary_list_funcs.create_image_slider_on_ui(
                ui_obj=self.ui,
                db_obj=self.db,
                frame_obj=self.ui.binary_list_perfect_frame,
                prefix=binary_list_funcs.widjet_prefixes["perfect"],
            )
        )
        # defect
        self.binarylist_sliders_check.append(
            binary_list_funcs.create_image_slider_on_ui(
                ui_obj=self.ui,
                db_obj=self.db,
                frame_obj=self.ui.binary_list_defect_frame,
                prefix=binary_list_funcs.widjet_prefixes["defect"],
            )
        )
        # validate
        if False in self.binarylist_sliders_check:
            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"][self.ui.language],
                level=3,
            )

        # binarylist image object
        self.binary_image_list = moveOnImagrList(
            sub_directory="", step=binary_list_funcs.n_images_per_row
        )

        # ________________________________________________________________
        # localization model start-up funcs
        self.refresh_localization_models_table(get_count=True)

        # ________________________________________________________________
        # create classlist slider on UI
        self.classification_image_list_name = "classlist"
        self.classlist_slider_check = []
        self.classlist_slider_check.append(
            binary_list_funcs.create_image_slider_on_ui(
                ui_obj=self.ui,
                db_obj=self.db,
                frame_obj=self.ui.class_list_slider_frame,
                prefix=self.classification_image_list_name,
                image_per_row=binary_list_funcs.n_images_per_row_classlist,
            )
        )
        # validate
        if False in self.classlist_slider_check:
            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"][self.ui.language],
                level=3,
            )

        # classlist image object
        self.classification_image_list = moveOnImagrList(
            sub_directory="", step=binary_list_funcs.n_images_per_row_classlist
        )

        # _____________________________________________________________________
        self.ImageManager = ImageManager(self.login_user_name, self.ui, self.cameras)

        # _________________________________________
        # create binarylist sliders on UI

        self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedWidth(0)
        self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedHeight(0)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(0)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(0)
        self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedWidth(0)
        self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedHeight(0)
        self.raw_and_evaluated_Imagw_sliders_check = []
        self.raw_and_evaluated_Imagw_sliders_check.append(
            binary_list_funcs.set_image_on_loadDataSetSlider_in_PBT(
                ui_obj=self.ui,
                db_obj=self.db,
                frame_obj=self.ui.original_image_list_frame,
                prefix="original",
            )
        )
        # evaluated image
        self.raw_and_evaluated_Imagw_sliders_check.append(
            binary_list_funcs.set_image_on_loadDataSetSlider_in_PBT(
                ui_obj=self.ui,
                db_obj=self.db,
                frame_obj=self.ui.evaluated_image_list_frame,
                prefix="evaluated",
            )
        )

        self.original_and_evaluated_image_in_PBT = moveOnImagrList(
            sub_directory="", step=binary_list_funcs.n_images_per_row
        )
        # _________________________________________

        # PLC
        self.retry_connecting_plc = 0
        self.set_plc_ip_to_ui()
        self.connect_plc()
        self.load_plc_parms()  # should be commecnt in finbal version
        self.ui.start_wind_btn.clicked.connect(lambda: self.set_wind(True))
        self.start_auto_wind()
        # self.update_plc_parms()
        self.plc_timer = QTimer()
        self.plc_timer.timeout.connect(self.update_sensor_and_temp)
        self.plc_update = QTimer()
        self.plc_update.timeout.connect(self.update_plc_values)
        self.slab_detect = False
        self.language = self.ui.language
        self.last_sensor = False
        self.sensor = False
        self.init_check_plc()

        # Level2 connection
        self.l2_connection = level2_connection.connection_level2()

        # PBT

        self.current_b_model = None
        self.current_l_model = None
        self.current_c_model = None
        self.add_piplines_in_combobox()
        self.add_dataset_in_combobox()

        # ImageProcessing
        self.sheet_imgprocessing_mem = {}
        self.finished_threads = 0
        self.l = self.db.get_image_processing_params()

        #notif manager 

        self.show_save_notif=False

        self.runing_b_model=False
        self.runing_l_model=False

        # DEBUG_FUNCTIONS
        # -------------------------------------
        # self.__debug_load_sheet__(["996", "997"])
        # self.__debug_select_random__()
        # self.__debug_select_for_label()
        self.__debug__login__()

    def __debug_load_sheet__(self, ids):
        self.move_on_list.add(ids, "sheets_id")
        self.selected_images_for_label.clear()
        self.load_sheet()

    def __debug_select_random__(
        self,
    ):
        for id in range(self.move_on_list.get_count("sheets_id")):
            self.next_sheet()
            for side in ["up", "down"]:
                for _ in range(np.random.randint(0, 5)):
                    cam = np.random.randint(
                        self.sheet.get_cameras()[0], self.sheet.get_cameras()[1] + 1
                    )
                    frame = np.random.randint(0, self.sheet.get_nframe() + 1)
                    self.selected_images_for_label.add(
                        self.move_on_list.get_current("sheets_id"), side, (cam, frame)
                    )
                    self.thechnicals_backend[side].update_selected(
                        self.selected_images_for_label.get_sheet_side_selections(
                            self.move_on_list.get_current("sheets_id"), side
                        )
                    )
        self.refresh_thechnical(fp=1)
        self.ui.add_selected_image(
            self.selected_images_for_label.get_all_selections_list()
        )

    def __debug_select_for_label(self):
        self.ui.checkBox_select.setChecked(True)
        self.ui.select_unselect_all()
        self.label_selected_img()

    def __debug__login__(self):
        self.auto_login()
        # self.

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    def create_default_ds(self):
        parms = self.db.get_dataset()
        parms = {
            "user_name": parms["user_own"],
            "user_id": parms["id"],
            "dataset_name": parms["name"],
            "path": parms["path"],
            "max_size": "15 Gb",
            "date": "3-3-1401",
        }
        self.ds = Dataset(parms["path"])
        self.ds_json = dataset_utils.dataset_json(main_ui_obj=self.ui)
        self.ds_json.create_json_dataset(parms)
        binary_count = self.ds_json.get_binary_count(
            os.path.join(parms["path"], parms["dataset_name"] + ".json")
        )
        self.ui.set_b_default_db_parms(self.ds.binary_path)
        self.ui.set_l_default_db_parms(self.ds.localization_path)
        chart_funcs.update_label_piechart(self.ui, binary_count)

    # _____________________________________________________________________JJ ZONE BEGINE

    def show_summery_of_selected_model_in_lineEdit_in_PBT_page(self, row, column):
        """this function called,when the user select ,rows from tabel in UI(IN PBT PAGE)
        and,pass number of selected row as input to the function

        Parameters
        ----------
        row : int
            row number of item
        column : int
            column number of item
        """

        # create string as summery of model(or algorithm)
        model_summery_that_show = "algorithm:{},that tarin in date:{},with dataset:{},and the weights is here {}".format(
            self.bmodels_list[row]["algo_name"],
            self.bmodels_list[row]["date_"],
            self.bmodels_list[row]["dataset_pathes"],
            self.bmodels_list[row]["weights_path"],
        )

        temp = self.bmodels_list[row]["input_size"]
        input_size = tuple(map(int, temp[1:-1].split(",")))

        self.current_bmodel = self.bmodels_list[row]
        if self.bmodels_list[row]["algo_name"] in train_api.ALGORITHM_NAMES["binary"]:
            # set the  summery at the lineEdit ,that under the table
            self.ui.LBL_of_selected_binary_classifaction_model_in_PBT_page.setText(
                model_summery_that_show
            )

            self.algo_name_binary_model = self.bmodels_list[row]["algo_name"]
            self.input_size_binary_model = input_size
            self.weight_path_binary_model = self.bmodels_list[row]["weights_path"]

            self.current_b_model = self.bmodels_list[row]

        elif (
            self.bmodels_list[row]["algo_name"]
            in train_api.ALGORITHM_NAMES["classification"]
        ):
            # set the  summery at the lineEdit ,that under the table
            self.ui.LBL_of_selected_multiClassification_model_in_PBT_page.setText(
                model_summery_that_show
            )

            self.algo_name_classification_model = self.bmodels_list[row]["algo_name"]
            self.input_size_classification_model = input_size
            self.weight_path_classification_model = self.bmodels_list[row][
                "weights_path"
            ]

            self.current_c_model = self.bmodels_list[row]

        elif (
            self.bmodels_list[row]["algo_name"]
            in train_api.ALGORITHM_NAMES["localization"]
        ):
            # set the  summery at the lineEdit ,that under the table
            self.ui.LBL_of_selected_localization_model_in_PBT_page.setText(
                model_summery_that_show
            )

            self.algo_name_localization_model = self.bmodels_list[row]["algo_name"]
            self.input_size_localization_model = input_size
            self.weight_path_localization_model = self.bmodels_list[row]["weights_path"]

            self.current_l_model = self.bmodels_list[row]

        self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setEnabled(True)

    def apply_selected_model_after_push_applyBTN_in_PBT_page(self):
        """the function connect to 'BTN_apply_of_binary_classifaction_in_PBT_page',
        and if the user set models,by clicking the buttom ,load dataset page loaded
        """
        if self.check_name_pipline():
            if self.ui.show_question(
                texts.WARNINGS["WARNING"][self.language],
                texts.WARNINGS["Create_pipline"][self.language]
                + self.ui.pipline_name.text()
                + ")",
            ):
                if self.create_and_add_pipline():
                    self.ui.stackedWidget_pbt.setCurrentWidget(
                        self.ui.page_load_dataset
                    )
                    self.ui.load_dataset_pbt_btn.setStyleSheet(
                        "background-color: rgb(200,200,200)"
                    )
                    self.ui.history_pbt_btn.setStyleSheet(
                        "background-color: rgb(100,100,100)"
                    )
                    self.ui.pipeline_pbt_btn.setStyleSheet(
                        "background-color: rgb(100,100,100)"
                    )
                    self.refresh_datasets_table(PBT_page=True)
                    self.add_piplines_in_combobox(
                        piplinename=self.ui.pipline_name.text()
                    )
                    self.refresh_loadDataset_tabs_in_PBT()
                else:
                    self.ui.pipline_name_status.setText(
                        texts.ERRORS["pipline_eror"][self.language]
                    )

        else:
            pass
            # #print("name not valid")

    def check_name_pipline(self):

        pipline_name = self.ui.pipline_name.text()
        if pipline_name == "":
            self.ui.pipline_name_status.setText(
                texts.ERRORS["empty_name"][self.language]
            )
            return False

        db_pipline_names = self.db.get_pipline_names()

        if pipline_name in db_pipline_names:
            self.ui.pipline_name_status.setText(
                texts.ERRORS["repeat_name"][self.language]
            )
            return False
        if pipline_name not in db_pipline_names:
            return True
        return False

    def add_dataset_in_combobox(self):

        res, self.datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
        if not res:
            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["database_get_datasets_failed"][self.ui.language],
                level=3,
            )

        self.PBT_option_list = dataset.set_datasets_on_ui(
            ui_obj=self.ui,
            datasets_list=self.datasets_list,
            current_user=self.login_user_name,
            default_dataset=self.default_dataset_user,
            is_binarylist=False,
            PBT_page=True,
        )

    def create_and_add_pipline(self):

        try:
            # #print(self.current_b_model)
            # data = pipline_name,user_name,pipline path if save , binary_weight path , local weight path , class weight path
            data = (
                self.ui.pipline_name.text(),
                self.login_user_name,
                "Null",
                self.current_b_model["weights_path"],
                self.current_l_model["weights_path"],
                self.current_c_model["weights_path"],
            )  # path pipline null
            ret = self.db.add_pipline(data)
            # #print('ret',ret)
            return ret

        except:
            #     self.ui.pipline_name_status.setText(texts.ERRORS['repeat_name'][self.language])
            return False

    def add_piplines_in_combobox(self, piplinename=-1):

        db_pipline_names = self.db.get_pipline_names()
        self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.clear()
        self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.addItems(db_pipline_names)
        if piplinename != -1:
            inx = self.db_pipline_names.index(piplinename)
            self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.setCurrentIndex(inx)

    def load_image_btn_in_PBT_page(self):
        path = QFileDialog.getExistingDirectory(self.ui, "Choose Directory", "")
        self.ui.lineEdit_of_path_displayment_in_PBT_page.setText(path)
        self.customized_datasets = [{"path": path}]

    def set_perfect_defect_checkBox_dataset(self, state, perfectOrdefect):

        if perfectOrdefect == "perfect":
            self.perfect_show = state
        elif perfectOrdefect == "defect":
            self.defect_show = state

    def checkbox_connector(self):
        self.ui.chbox_prefectdata_in_PBT_page.stateChanged.connect(
            partial(
                lambda x: self.set_perfect_defect_checkBox_dataset(
                    state=self.ui.chbox_prefectdata_in_PBT_page.isChecked(),
                    perfectOrdefect="perfect",
                )
            )
        )
        self.ui.chbox_defectdata_in_PBT_page.stateChanged.connect(
            partial(
                lambda x: self.set_perfect_defect_checkBox_dataset(
                    state=self.ui.chbox_defectdata_in_PBT_page.isChecked(),
                    perfectOrdefect="defect",
                )
            )
        )

    def QTableWidget_connector(self):
        """by calling this function, the qtablewidget of UI connect to corresponding function.
        this function call in __init__ function
        """
        # qtablewidget in PBT page that,indicate all information of  binary classification DL model,from SQL
        self.ui.table_of_binary_classifaction_in_PBT_page.cellClicked.connect(
            partial(self.show_summery_of_selected_model_in_lineEdit_in_PBT_page)
        )

    def comboBox_connector(self):
        """by calling this function, the comboBox of UI connect to corresponding function.
        this function call in __init__ function
        """

        # comboBox in PBT page that ,indicate binary classification algorithm
        self.ui.cbBox_of_binary_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(filter_mode=True, wich_page="PBT")
        )

        self.ui.cbBox_of_multiClassification_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(
                filter_mode=True, wich_page="PBT", model_type="classification"
            )
        )

        self.ui.cbBox_of_localiztion_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(
                filter_mode=True, wich_page="PBT", model_type="localization"
            )
        )

        self.ui.comboBox_ncamera_SI.currentTextChanged.connect(
            partial(self.set_ncamera_label)
        )
        self.ui.comboBox_nframe_SI.currentTextChanged.connect(
            partial(self.set_nframe_label)
        )

    def load_table_with_btn(self, obj_name):
        algo_name = obj_name.split("_")[1]
        combo_name = eval(
            "self.ui.{}".format("cbBox_of_" + algo_name + "_model_in_PBT_page")
        )
        index = combo_name.currentIndex()

        if index != 0:
            combo_name.setCurrentIndex(0)
            combo_name.setCurrentIndex(index)
        else:
            combo_name.setCurrentIndex(1)
            combo_name.setCurrentIndex(index)

    def refresh_loadDataset_tabs_in_PBT(self):
        # labale updating
        self.ui.LBL_of_data_is_ready_in_PBT_page.setText("")
        self.ui.LBL_of_pipline_is_ready_in_PBT_page.setText("")
        self.ui.LBL_of_data_is_ready_in_PBT_page_2.setText("")
        self.ui.LBL_of_evalution_of_binary_model_in_PBT_page.setText("")
        self.ui.LBL_of_evalution_of_classification_model_in_PBT_page.setText("")
        # progressbar updating
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(0)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(0)
        # combobox updating
        self.ui.cbBox_of_dataset_in_PBT_page_load_dataset.clear()
        self.ui.cbBox_of_dataset_in_PBT_page_load_dataset.addItems(self.PBT_option_list)
        self.add_piplines_in_combobox()
        # checkbox updating
        self.ui.chbox_prefectdata_in_PBT_page.setChecked(True)
        self.ui.chbox_defectdata_in_PBT_page.setChecked(True)
        # lineEdit updating
        self.ui.lineEdit_of_path_displayment_in_PBT_page.setText("")

        # slider updating
        # ???????

    # _____________________________________________________________________JJ ZONE END

    def button_connector(self):
        """this function is used to connet UI buttons to their functionality"""
        # ______________JJ Zone start
        self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.clicked.connect(
            partial(self.apply_selected_model_after_push_applyBTN_in_PBT_page)
        )
        self.ui.pbt_btn.clicked.connect(
            lambda: self.refresh_binary_models_table_onevent(wich_page="PBT")
        )
        self.ui.pipeline_pbt_btn.clicked.connect(
            lambda: self.refresh_binary_models_table_onevent(wich_page="PBT")
        )
        self.ui.BTN_of_goToNextpage_in_PBT_page.clicked.connect(
            partial(
                lambda: self.binary_model_tabel_nextorprev(next=True, wich_page="PBT")
            )
        )
        self.ui.BTN_of_goToPreviouspage_in_PBT_page.clicked.connect(
            partial(
                lambda: self.binary_model_tabel_nextorprev(next=False, wich_page="PBT")
            )
        )
        self.ui.BTN_set_directory_image_in_PBT_page.clicked.connect(
            self.load_image_btn_in_PBT_page
        )
        self.ui.BTN_refreshing_pipline_page_in_PBT.clicked.connect(
            lambda: self.refresh_binary_models_table_onevent(wich_page="PBT")
        )
        self.ui.load_dataset_pbt_btn.clicked.connect(
            self.refresh_loadDataset_tabs_in_PBT
        )
        # ______________ JJ

        self.ui.load_sheets_win.load_btn.clicked.connect(partial(self.load_sheets))
        self.ui.load_sheets_win.btn_refresh.clicked.connect(
            partial(self.show_sheet_loader)
        )
        self.ui.add_btn_SI.clicked.connect(partial(self.append_select_img))
        self.ui.add_filter_btn_SI.clicked.connect(partial(self.append_filter_img))
        self.ui.select_filter_btn_SI.clicked.connect(partial(self.select_filter_img))

        self.ui.remove_btn_SI.clicked.connect(partial(self.remove_select_img))
        self.ui.load_coil_btn.clicked.connect(partial(self.show_sheet_loader))
        self.ui.next_coil_btn.clicked.connect(partial(self.next_sheet))
        self.ui.prev_coil_btn.clicked.connect(partial(self.prev_sheet))
        self.ui.label_btn_SI.clicked.connect(partial(self.label_selected_img))

        self.ui.next_img_label_btn.clicked.connect(partial(self.next_label_img))
        self.ui.prev_img_label_btn.clicked.connect(partial(self.prev_label_img))
        self.ui.binary_train.clicked.connect(partial(self.set_b_parms))
        self.ui.localization_train.clicked.connect(partial(self.set_l_parms))
        self.ui.save_dataset_btn.clicked.connect(partial(self.save_train_ds))
        self.ui.save_all_dataset_btn.clicked.connect(partial(self.save_all_train_ds))
        self.ui.heatmap_btn.clicked.connect(partial(self.create_Heatmap))
        self.ui.suggested_defects_btn.clicked.connect(partial(self.image_processing_suggest))
        self.ui.checkBox_show_neighbours.stateChanged.connect(
            partial(self.show_neighbours)
        )
        self.ui.checkBox_show_neighbours_labels.stateChanged.connect(
            partial(self.show_neighbours_labels)
        )
        self.ui.delete_btn.clicked.connect(self.delete_all_labels)
        self.ui.mask_table_widget.clicked.connect(self.select_defect)

        # trainig
        self.ui.b_select_dp.clicked.connect(partial(self.select_binary_dataset))
        self.ui.b_delete_ds.clicked.connect(partial(self.delete_binary_dataset))
        self.ui.b_add_ok.clicked.connect(partial(self.ok_add_binary_ds))

        self.ui.l_select_prep.clicked.connect(partial(self.select_localization_pretrain_path))
        self.ui.l_select_dp.clicked.connect(partial(self.select_localization_dataset))
        self.ui.l_delete_ds.clicked.connect(partial(self.delete_localization_dataset))
        self.ui.l_add_ok.clicked.connect(partial(self.ok_add_localization_ds))

        # login
        self.login_user_name = "root"
        self.default_dataset_user = "default_dataset"  # ///////////////////
        self.ui.login_btn.clicked.connect(partial(self.show_login))
        self.ui.btn_user_profile.clicked.connect(partial(self.set_profile_page))
        self.ui.create_database_btn.clicked.connect(partial(self.create_dataset))
        self.ui.all_databases.clicked.connect(partial(self.set_databases))
        self.ui.my_databases_2.clicked.connect(partial(self.set_user_databases))
        self.ui.set_default_database_btn.clicked.connect(
            partial(self.set_default_dataset)
        )
        # self.ui.split_dataset.clicked.connect(partial(self.split_binary_dataset))

        # labeling

        # self.labaling_UI.save_btn.clicked.connect(partial(self.set_label))
        # self.ui.no_defect.toggled.connect(self.change_image_save_status)
        # self.ui.yes_defect.toggled.connect(self.change_image_save_status)

        # data aquization
        self.ui.connect_camera_btn.clicked.connect(partial(self.connect_camera))
        self.ui.disconnect_camera_btn.clicked.connect(partial(self.disconnect_camera))

        self.ui.start_capture_btn.clicked.connect(partial(self.start_capture_func))
        self.ui.stop_capture_btn.clicked.connect(partial(self.stop_capture_func))
        self.ui.checkBox_save_images.stateChanged.connect(partial(self.save_images))
        self.ui.comboBox_connected_cams.currentTextChanged.connect(
            partial(self.change_live_camera)
        )
        self.ui.live_tabWidget.currentChanged.connect(partial(self.change_live_type))
        self.ui.checkBox_suggested_defects.stateChanged.connect(partial(self.load_suggestions))

        # binary-model history
        self.ui.binary_tabel_prev.clicked.connect(
            partial(lambda: self.binary_model_tabel_nextorprev(next=False))
        )
        self.ui.binary_tabel_next.clicked.connect(
            partial(lambda: self.binary_model_tabel_nextorprev(next=True))
        )
        self.ui.Binary_btn.clicked.connect(
            partial(lambda: self.refresh_datasets_table(is_binarylist=True))
        )
        self.ui.Binary_btn.clicked.connect(
            partial(self.refresh_binary_models_table_onevent)
        )
        self.ui.binary_history.clicked.connect(
            partial(self.refresh_binary_models_table_onevent)
        )
        self.ui.binary_table_refresh_btn.clicked.connect(
            partial(self.refresh_binary_models_table_onevent)
        )
        self.ui.binary_filter_btn.clicked.connect(
            partial(lambda: self.refresh_binary_models_table(filter_mode=True))
        )
        self.ui.binary_clearfilter_btn.clicked.connect(partial(self.clear_filters))

        # binary-list
        # self.ui.binary_list.clicked.connect(
        #     partial(lambda: self.refresh_datasets_table(is_binarylist=True))
        # )
        # self.ui.binary_list_dataset_btn.clicked.connect(partial(lambda: self.select_binary_dataset(page='binarylist')))
        self.ui.binary_list_show_btn.clicked.connect(
            partial(self.load_binary_images_list)
        )
        self.ui.binary_list_perfect_prev_btn.clicked.connect(
            partial(lambda: self.update_binary_images_on_ui(prevornext="prev"))
        )
        self.ui.binary_list_perfect_next_btn.clicked.connect(
            partial(lambda: self.update_binary_images_on_ui(prevornext="next"))
        )
        self.ui.binary_list_defect_prev_btn.clicked.connect(
            partial(
                lambda: self.update_binary_images_on_ui(defect=True, prevornext="prev")
            )
        )
        self.ui.binary_list_defect_next_btn.clicked.connect(
            partial(
                lambda: self.update_binary_images_on_ui(defect=True, prevornext="next")
            )
        )

        # localization-model history
        self.ui.localization_tabel_prev.clicked.connect(
            partial(lambda: self.localization_model_tabel_nextorprev(next=False))
        )
        self.ui.localization_tabel_next.clicked.connect(
            partial(lambda: self.localization_model_tabel_nextorprev(next=True))
        )
        self.ui.Localization_btn.clicked.connect(
            partial(self.refresh_localization_models_table_onevent)
        )
        self.ui.localization_history.clicked.connect(
            partial(self.refresh_localization_models_table_onevent)
        )
        self.ui.localization_table_refresh_btn.clicked.connect(
            partial(self.refresh_localization_models_table_onevent)
        )
        self.ui.localization_filter_btn.clicked.connect(
            partial(lambda: self.refresh_localization_models_table(filter_mode=True))
        )
        self.ui.localization_clearfilter_btn.clicked.connect(
            partial(self.clear_localization_filters)
        )

        # ______________________________________________JJ ZONE START
        self.ui.BTN_load_in_PBT_page.clicked.connect(
            self.load_binary_images_list_in_PBT_load_dataset_page
        )
        self.ui.BTN_load_image_in_PBT_page.clicked.connect(
            self.pre_load_binary_images_list_in_PBT_load_dataset_page
        )
        self.ui.BTN_evaluate_image_in_PBT_page_2.clicked.connect(
            self.evaluate_model_on_selected_model
        )
        self.ui.BTN_set_pipline_in_PBT_page.clicked.connect(self.set_pipline)

        self.ui.BTN_prev_original_image_in_PBT_page.clicked.connect(
            partial(
                lambda: self.update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
                    prevornext="prev", predict_eval=self.pred_each_path
                )
            )
        )
        self.ui.BTN_next_original_image_in_PBT_page.clicked.connect(
            partial(
                lambda: self.update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
                    prevornext="next", predict_eval=self.pred_each_path
                )
            )
        )
        self.ui.BTN_refresh_loadDataset_tab_in_PBT.clicked.connect(
            self.refresh_loadDataset_tabs_in_PBT
        )
        # ______________________________________________JJ ZONE STOP

        # classification page
        self.ui.Classification_btn.clicked.connect(partial(self.refresh_classes_table))
        self.ui.classification_history.clicked.connect(
            partial(self.refresh_classes_table)
        )
        self.ui.classification_class_list.clicked.connect(
            partial(self.refresh_classes_table)
        )
        self.ui.classification_training.clicked.connect(
            partial(self.refresh_classes_table)
        )
        self.ui.Classification_btn.clicked.connect(partial(self.refresh_datasets_table))
        self.ui.classification_class_list.clicked.connect(
            partial(self.refresh_datasets_table)
        )
        self.ui.classlist_show_related_img_btn.clicked.connect(
            partial(self.show_class_related_images)
        )
        self.ui.classlist_prev_btn.clicked.connect(
            partial(lambda: self.update_classlist_images_on_ui(prevornext="prev"))
        )
        self.ui.classlist_next_btn.clicked.connect(
            partial(lambda: self.update_classlist_images_on_ui(prevornext="next"))
        )
        # train model
        self.ui.class_check_train_btn.clicked.connect(
            partial(self.check_classification_train_params)
        )
        # cls history
        self.ui.Classification_btn.clicked.connect(
            partial(self.refresh_cls_models_table_onevent)
        )
        self.ui.classification_history.clicked.connect(
            partial(self.refresh_cls_models_table_onevent)
        )
        self.ui.cls_table_refresh_btn.clicked.connect(
            partial(self.refresh_cls_models_table_onevent)
        )
        self.ui.cls_filter_btn.clicked.connect(
            partial(lambda: self.refresh_cls_models_table(filter_mode=True))
        )
        self.ui.cls_tabel_prev.clicked.connect(
            partial(lambda: self.cls_model_tabel_nextorprev(next=False))
        )
        self.ui.cls_tabel_next.clicked.connect(
            partial(lambda: self.cls_model_tabel_nextorprev(next=True))
        )
        self.ui.cls_clearfilter_btn.clicked.connect(partial(self.clear_filters_cls))

        self.ui.Binary_btn.clicked.connect(
            partial(lambda: self.user_access_pages(self.ui.Binary_btn.objectName()))
        )
        self.ui.Localization_btn.clicked.connect(
            partial(
                lambda: self.user_access_pages(self.ui.Localization_btn.objectName())
            )
        )
        self.ui.Classification_btn.clicked.connect(
            partial(
                lambda: self.user_access_pages(self.ui.Classification_btn.objectName())
            )
        )
        self.ui.pbt_btn.clicked.connect(
            partial(lambda: self.user_access_pages(self.ui.pbt_btn.objectName()))
        )

        # Settings
        # Language
        self.ui.appearance_btn.clicked.connect(self.set_language_font)
        self.itr = 0
        # PLC
        self.ui.plc_btn.clicked.connect(self.set_plc_parms)
        # Camera
        self.ui.cameras_btn.clicked.connect(self.set_camera_parms)

        # pbt
        self.ui.my_databases_3.clicked.connect(self.update_combo_piplines)
        self.ui.remove_pipline.clicked.connect(self.remove_pipline)
        self.ui.show_details_pipline.clicked.connect(self.show_pipline_details_func)
        self.ui.toolButton_binary.clicked.connect(
            lambda: self.load_table_with_btn(self.ui.toolButton_binary.objectName())
        )
        self.ui.toolButton_localiztion.clicked.connect(
            lambda: self.load_table_with_btn(
                self.ui.toolButton_localiztion.objectName()
            )
        )
        self.ui.toolButton_multiClassification.clicked.connect(
            lambda: self.load_table_with_btn(
                self.ui.toolButton_multiClassification.objectName()
            )
        )
        self.ui.history_pbt_btn.clicked.connect(self.laod_bpt_jsons)
        self.ui.pipline_tabel_next_PBT.clicked.connect(self.next_page_pipline_history)
        self.ui.pipline_tabel_prev_PBT.clicked.connect(self.prev_page_pipline_history)
        self.ui.BTN_search_and_filter_in_PBT.clicked.connect(self.json_filter_btn)
        self.ui.BTN_clear_filter_in_PBT.clicked.connect(self.json_clear_filter_btn)

        # plc
        self.ui.connect_plc_btn.clicked.connect(self.connect_plc)
        self.ui.disconnect_plc_btn.clicked.connect(self.disconnect_plc)

        self.ui.line_thickness_slider.valueChanged.connect(self.change_label_line_thickness)
        self.ui.point_thickness_slider.valueChanged.connect(self.change_label_point_thickness)

    def change_label_line_thickness(self):
        x = self.ui.line_thickness_slider.value()
        self.label_bakcend["mask"].change_line_thickness(x)
        
    def change_label_point_thickness(self):
        x = self.ui.point_thickness_slider.value()
        self.label_bakcend["mask"].change_radius(x)

    def user_access_pages(self, btn_name):

        dic = {
            "Binary_btn": self.ui.page_Binary,
            "Localization_btn": self.ui.page_Localization,
            "Classification_btn": self.ui.page_Classification,
            "pbt_btn": self.ui.page_pbt,
        }
        if self.logged_in:
            eval(
                'self.ui.set_widget_page(self.ui.stackedWidget,dic["{}"])'.format(
                    btn_name
                )
            )
            # eval(self.stackedWidget.setCurrentWidget(self.page_Binary))

        else:
            self.ui.set_warning(
                texts.WARNINGS["LOGIN_FIRST"][self.language], "app_erors", level=2
            )

    def mouse_connector(self):
        for _, technical_widget in self.ui.get_technical().items():
            self.mouse.connet(technical_widget, self.update_technical_pointer_mouse)

        self.mouse.connect_all(self.ui.image, self.label_image_mouse)
        self.mouse.connet_dbclick(self.ui.image, self.label_classify)

        self.mouse.connet_dbclick(self.ui.crop_image, self.fit_image)
        self.mouse.connet_dbclick(self.ui.sn, self.maximize_neighbours)

        self.mouse.connet_dbclick(self.ui.labeling_help_1, self.maximize_labeling_helps)
        self.mouse.connet_dbclick(self.ui.labeling_help_2, self.maximize_labeling_helps)
        self.mouse.connet_dbclick(self.ui.labeling_help_3, self.maximize_labeling_helps)
        self.mouse.connet_dbclick(self.ui.labeling_help_4, self.maximize_labeling_helps)
        self.mouse.connet_dbclick(self.ui.labeling_help_5, self.maximize_labeling_helps)
        self.mouse.connet_dbclick(self.ui.labeling_help_6, self.maximize_labeling_helps)

    def keyboard_connector(self):
        self.keyboard.connet(
            self.ui,
            ["left", "right", "up", "down"],
            [self.update_technical_pointer_keyboard],
            "Technical View",
        )

    def change_image_save_status(self):
        sheet, pos, img_path = self.move_on_list.get_current(
            "selected_imgs_for_label"
        )
        self.image_save_status[img_path] = False

    # ----------------------------------------------------------------------------------------
    # get id of sheets that user select in load_sheet_win and load first one
    # ----------------------------------------------------------------------------------------
    def load_sheets(self):
        sheets_id = self.ui.load_sheets_win.get_selected_sheetid()
        if not sheets_id:
            self.ui.load_sheets_win.close()
            self.ui.set_warning(
                texts.WARNINGS["NO_SHEET"][self.language], "data_auquzation", level=2
            )
            return
        self.move_on_list.add(sheets_id, "sheets_id")
        for sheet_id in sheets_id:
            if sheet_id not in self.sheet_imgprocessing_mem.keys():
                self.sheet_imgprocessing_mem[sheet_id] = False
        self.selected_images_for_label.clear()
        self.ui.clear_table()
        self.ui.load_sheets_win.close()
        self.load_sheet()

        # ----------------------------------------------------------------------------------------

    # load sheet by its id in software
    # ----------------------------------------------------------------------------------------
    def load_sheet(self):
        selceted_sheets_id = self.move_on_list.get_current(
            "sheets_id"
        )  # get current value on list that corespond to "coils_id" name
        self.sheet = self.db.load_sheet(
            selceted_sheets_id
        )  # load inference of Sheet class from database by sheet id
        self.build_sheet_technical(self.sheet)  # build technical sheet
        if self.ui.checkBox_suggested_defects.isChecked():
            self.load_suggestions()
        self.ui.show_sheet_details(
            self.sheet.get_info_dict()
        )  # show sheet details in UI.details_label
        self.load_filter_params()
        self.ui.set_enabel(self.ui.checkBox_suggested_defects, True)

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def load_filter_params(self):
        self.ui.set_enabel(self.ui.checkBox_all_imgs_SI, True)
        self.ui.set_enabel(self.ui.checkBox_all_frame_SI, True)
        self.ui.set_enabel(self.ui.checkBox_all_camera_SI, True)
        self.ui.set_side_combobox()
        self.ui.set_camera_combobox(
            min=self.sheet.cameras[0], max=self.sheet.cameras[1]
        )
        self.ui.set_frame_combobox(max=self.sheet.nframe)
        self.ui.checkBox_all_imgs_SI.setChecked(True)

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def finish_th(self):
        self.finished_threads += 1
        if self.finished_threads == self.n_threads:
            self.finished_threads = 0
            self.sheet_imgprocessing_mem[self.sheet.get_id()] = True
            for side, _ in self.ui.get_technical(name=False).items():
                self.thechnicals_backend[side].reset_real_imgs()
                self.thechnicals_backend[side].set_show_bboxes()
                self.thechnicals_backend[side].update_defect()
                selecteds = self.selected_images_for_label.get_sheet_side_selections(
                        str(self.sheet.get_id()), side
                    )

                self.thechnicals_backend[side].update_selected(selecteds)
                self.thechnicals_backend[side].update_real_imgs()
                self.current_technical_side = side
                self.refresh_thechnical(fp=1)  

                self.ui.set_enabel(self.ui.load_coil_btn, True)
                self.ui.set_enabel(self.ui.next_coil_btn, True)
                self.ui.set_enabel(self.ui.prev_coil_btn, True)
                self.ui.set_enabel(self.ui.checkBox_suggested_defects, True)
    
    def load_suggestions(self, state=0):
        if self.ui.checkBox_suggested_defects.isChecked():
            self.ui.suggested_defects_progressBar.setValue(0)
            self.ui.suggested_defects_progressBar.setMaximum(self.sheet.get_cameras()[1]*2*self.sheet.get_nframe())
            l = self.db.get_image_processing_params()
            if l != self.l:
                for key in self.sheet_imgprocessing_mem.keys():
                    self.sheet_imgprocessing_mem[key] = False
            jsons_path = os.path.join(self.sheet.get_main_path()+'_imgProcessing', self.sheet.get_id())
            if not os.path.exists(jsons_path):
                self.sheet_imgprocessing_mem[self.sheet.get_id()] = False
            if not self.sheet_imgprocessing_mem[self.sheet.get_id()]:
                self.ui.set_enabel(self.ui.load_coil_btn, False)
                self.ui.set_enabel(self.ui.next_coil_btn, False)
                self.ui.set_enabel(self.ui.prev_coil_btn, False)
                self.ui.set_enabel(self.ui.checkBox_suggested_defects, False)

                self.n_threads = 4
                step = 3

                self.threads = []
                self.workers = []
                for i in range(self.n_threads):
                    self.threads.append(sQThread())
                    # Step 3: Create a worker object
                    self.workers.append(image_processing_worker.image_processing_worker())
                    self.workers[-1].assign_parameters(
                        n_cameras=((i*step)+1, (i+1)*step),
                        n_frames=(1, self.sheet.get_nframe()), 
                        main_path=self.sheet.get_main_path(), 
                        res_main_path=self.sheet.get_main_path()+'_imgProcessing',
                        sheet_id=self.sheet.get_id(), 
                        active_cameras = self.sheet.get_cameras(),
                        img_format=self.sheet.get_image_format(),
                        img_shape = data_grabber.IMAGE_SHAPE,
                        api_obj=self,
                        ui_obj=self.ui,
                        db_obj=self.db
                    )
                    # Step 4: Move worker to the thread
                    self.workers[-1].moveToThread(self.threads[-1])
                    # Step 5: Connect signals and slots
                    self.threads[-1].started.connect(self.workers[-1].run_algorithm)
                    self.workers[-1].finished.connect(self.threads[-1].quit)
                    self.workers[-1].finished.connect(
                        self.finish_th
                    )
                    self.workers[-1].finished.connect(self.workers[-1].deleteLater)
                    self.threads[-1].finished.connect(self.threads[-1].deleteLater)
                    self.workers[-1].update_progressbar.connect(self.update_suggestion_progressbar)
                    # Step 6: Start the thread
                    self.threads[-1].start()

            else:
                for side, _ in self.ui.get_technical(name=False).items():
                    self.thechnicals_backend[side].reset_real_imgs()
                    self.thechnicals_backend[side].set_show_bboxes()
                    self.thechnicals_backend[side].update_defect()
                    selecteds = self.selected_images_for_label.get_sheet_side_selections(
                            str(self.sheet.get_id()), side
                        )

                    self.thechnicals_backend[side].update_selected(selecteds)
                    self.thechnicals_backend[side].update_real_imgs()
                    self.current_technical_side = side
                    self.refresh_thechnical(fp=1)
        else:
            self.build_sheet_technical(self.sheet)

    def update_suggestion_progressbar(self):
        self.ui.suggested_defects_progressBar.setValue(self.ui.suggested_defects_progressBar.value() + 1)

    def build_sheet_technical(self, sheet):
        try:
            self.thechnicals_backend = {}
            for side, _ in self.ui.get_technical(name=False).items():
                self.thechnicals_backend[side] = data_grabber.sheetOverView(
                    sheet,
                    side,  # side of sheet that is UO
                    (HEIGHT_FRAME_SIZE * sheet.get_nframe(), WIDTH_TECHNICAL_SIDE),
                    (self.sheet.get_nframe(), NCAMERA),
                    # sheet.get_grade_shape(),
                    actives_camera=sheet.get_cameras(),
                    oriation=data_grabber.VERTICAL,
                )

                selecteds = self.selected_images_for_label.get_sheet_side_selections(
                    str(self.sheet.get_id()), side
                )

                self.thechnicals_backend[side].update_selected(selecteds)
                self.current_technical_side = side
                self.refresh_thechnical(fp=1)  #

        except:
            pass
            # #print("Error!: load_sheet() in API")

    # ----------------------------------------------------------------------------------------
    # when next next_coil_btn clicked this function move on next coil id and load it
    # ----------------------------------------------------------------------------------------
    def next_sheet(self):
        if self.move_on_list.check("sheets_id"):
            self.move_on_list.next_on_list(
                "sheets_id"
            )  # move previous on list that corespond to "coils_id" name
            self.load_sheet()  # laod current coil id

        else:
            self.ui.set_warning(
                texts.WARNINGS["NO_SHEET"][self.language], "data_auquzation", level=2
            )

    # ----------------------------------------------------------------------------------------
    # when next next_coil_btn clicked this function move on privous coil id and load it
    # ----------------------------------------------------------------------------------------
    def prev_sheet(self):
        if self.move_on_list.check("sheets_id"):
            self.move_on_list.prev_on_list(
                "sheets_id"
            )  # move next on list that corespond to "coils_id" name
            self.load_sheet()  # laod current coil id
        else:
            self.ui.set_warning(
                texts.WARNINGS["NO_SHEET"][self.language], "data_auquzation", level=2
            )

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def update_sheet_img(self, name):
        img = self.thechnicals_backend[name].get_sheet_img()
        self.ui.set_img_sheet(img, name)

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def show_pointer_position(self):
        x, y = self.thechnicals_backend[
            self.current_technical_side
        ].get_pos()  # get mouse position normilized between [0,1]
        x *= self.sheet.get_width()
        y *= self.sheet.get_length()
        y = np.round(y, 1)
        x = np.round(x, 1)
        self.ui.show_current_position((x, y))

    def update_technical_pointer_keyboard(self, key):
        self.thechnicals_backend[self.current_technical_side].update_pointer_keyboard(
            key
        )
        self.refresh_thechnical(fp=1)
        self.show_pointer_position()

    def update_technical_pointer_mouse(self, widget_name):
        if len(self.thechnicals_backend) == 0:
            self.ui.set_warning(
                texts.WARNINGS["NO_SHEET"][self.language], "data_auquzation", level=2
            )

        else:
            self.current_technical_side = self.ui.get_technical_wgt_side(widget_name)
            pt = (
                self.mouse.get_relative_position()
            )  # get mouse position (x,y) that x,y are in [0,1] range
            self.thechnicals_backend[self.current_technical_side].update_pointer(
                pt
            )  # update corespond backend mouse position
            self.refresh_thechnical(fp=5)
            self.show_pointer_position()

    def refresh_thechnical(self, fp):
        if self.t % fp == 0:
            self.t = 1

            self.thechnicals_backend[
                self.current_technical_side
            ].update_sheet_img()  # update technical image
            img = self.thechnicals_backend[
                self.current_technical_side
            ].get_real_img()  # get image of sheet corespond to mouse position
            self.ui.set_crop_image(img)  # show image in UI
            self.update_sheet_img(self.current_technical_side)
            # self.ui.show_selected_side(self.current_technical_side)

        else:
            self.t += 1

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def fit_image(self, widget_name):
        self.thechnicals_backend[self.current_technical_side].fit(
            self.mouse.get_relative_position()
        )
        self.refresh_thechnical(1)
        real_img = self.thechnicals_backend[self.current_technical_side].get_real_img()
        self.ui.set_crop_image(real_img)
        self.ui.set_enabel(self.ui.add_btn_SI, True)
        self.show_pointer_position()

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def show_sheet_loader(self):
        try:
            sheets = self.db.report_last_sheets(9999)
            self.ui.load_sheets_win.show_sheets_info(sheets)
            self.ui.load_sheets_win.reset_search_lines()
            self.ui.data_loader_win_show()
            self.ui.load_sheets_win.set_warning(
                texts.MESSEGES["refresh_success"][self.language], level=1
            )
        except:
            self.ui.load_sheets_win.set_warning(
                texts.ERRORS["refresh_failed"][self.language], level=3
            )

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def append_filter_img(self):
        side = []
        cameras = []
        frames = []
        try:
            sheet_id = self.sheet.get_id()
        except:
            self.ui.set_warning(
                texts.WARNINGS["NO_SHEET"][self.language], "data_auquzation", level=2
            )
            return

        if self.ui.checkBox_all_imgs_SI.isChecked():
            side = ["up", "down"]
            cameras = list(range(self.sheet.cameras[0], int(self.sheet.cameras[1])+1))
            frames = list(range(1, self.sheet.nframe+1))
        else:
            s = self.ui.comboBox_side_SI.currentText()
            if s == "TOP":
                side = ["up"]
            elif s == "BOTTOM":
                side = ["down"]
            elif s == "BOTH":
                side = ["up", "down"]
            if self.ui.checkBox_all_camera_SI.isChecked():
                cameras = list(range(self.sheet.cameras[0], int(self.sheet.cameras[1]+1)))
            else:
                cameras = self.ui.comboBox_ncamera_SI.getValue()
                cameras = list(map(int, cameras))
            if self.ui.checkBox_all_frame_SI.isChecked():
                frames = list(range(1, self.sheet.nframe+1))
            else:
                frames = self.ui.comboBox_nframe_SI.getValue()
                frames = list(map(int, frames))

        if not side:
            self.ui.set_warning(
                texts.WARNINGS["SIDE_EMPTY"][self.language], "data_auquzation", level=2
            )
            return
        if not cameras:
            self.ui.set_warning(
                texts.WARNINGS["CAMERA_EMPTY"][self.language],
                "data_auquzation",
                level=2,
            )
            return
        if not frames:
            self.ui.set_warning(
                texts.WARNINGS["FRAME_EMPTY"][self.language], "data_auquzation", level=2
            )
            return

        for s in side:
            for c in cameras:
                    for f in frames:
                        self.selected_images_for_label.add(sheet_id, s, (c, f))
            self.ui.add_selected_image(
                self.selected_images_for_label.get_all_selections_list()
            )
            self.thechnicals_backend[s].update_selected(
                self.selected_images_for_label.get_sheet_side_selections(sheet_id, s)
            )
            self.current_technical_side = s
            self.refresh_thechnical(fp=1)
        self.ui.set_warning(
            texts.WARNINGS["APPEND_SUCCESSFULLY"][self.language],
            "data_auquzation",
            level=1,
        )

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def select_filter_img(self):
        side = []
        cameras = []
        frames = []
        try:
            sheet_id = self.sheet.get_id()
        except:
            self.ui.set_warning(
                texts.WARNINGS["NO_SHEET"][self.language], "data_auquzation", level=2
            )
            return

        if self.ui.checkBox_all_imgs_SI.isChecked():
            side = ["up", "down"]
            cameras = list(range(self.sheet.cameras[0], self.sheet.cameras[1]+1))
            frames = list(range(1, self.sheet.nframe+1))
        else:
            s = self.ui.comboBox_side_SI.currentText()
            if s == "TOP":
                side = ["up"]
            elif s == "BOTTOM":
                side = ["down"]
            elif s == "BOTH":
                side = ["up", "down"]
            if self.ui.checkBox_all_camera_SI.isChecked():
                cameras = list(range(self.sheet.cameras[0], self.sheet.cameras[1]+1))
            else:
                cameras = self.ui.comboBox_ncamera_SI.getValue()
                cameras = list(map(int, cameras))
            if self.ui.checkBox_all_frame_SI.isChecked():
                frames = list(range(1, self.sheet.nframe+1))
            else:
                frames = self.ui.comboBox_nframe_SI.getValue()
                frames = list(map(int, frames))

        if not side:
            self.ui.set_warning(
                texts.WARNINGS["SIDE_EMPTY"][self.language], "data_auquzation", level=2
            )
            return
        if not cameras:
            self.ui.set_warning(
                texts.WARNINGS["CAMERA_EMPTY"][self.language],
                "data_auquzation",
                level=2,
            )
            return
        if not frames:
            self.ui.set_warning(
                texts.WARNINGS["FRAME_EMPTY"][self.language], "data_auquzation", level=2
            )
            return

        for s in side:
            for c in cameras:
                for f in frames:
                    index = self.selected_images_for_label.get_index_by_value(
                        [sheet_id, s, (c, f)]
                    )
                    if index is not None:
                        self.ui.listWidget_append_img_list.item(index, 0).setCheckState(
                            Qt.CheckState.Checked
                        )

    def set_ncamera_label(self, text):
        self.ui.label_ncamera_SI.clear()
        s = ""
        for t in self.ui.comboBox_ncamera_SI.getValue():
            s += t
            s += ", "
        self.ui.label_ncamera_SI.setText(s[:-2])

    def set_nframe_label(self, text):
        self.ui.label_nframe_SI.clear()
        s = ""
        for t in self.ui.comboBox_nframe_SI.getValue():
            s += t
            s += ", "
        self.ui.label_nframe_SI.setText(s[:-2])

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def append_select_img(self):
        if self.current_technical_side == "":
            self.ui.set_warning(
                texts.WARNINGS["NO_CHOOSEN_IMG"][self.language],
                "data_auquzation",
                level=2,
            )
            return
        cam, frame = self.thechnicals_backend[
            self.current_technical_side
        ].get_current_img_position()
        # #print(cam,frame, '^'*20)
        if (frame < 0) or (cam < 0):
            self.ui.set_warning(
                texts.WARNINGS["NO_CHOOSEN_IMG"][self.language],
                "data_auquzation",
                level=2,
            )
        else:

            side = self.thechnicals_backend[self.current_technical_side].get_side()
            main_path = self.sheet.get_path()

            x = main_path.split('/')
            path = pathStructure.sheet_image_path(x[0], x[-1], side, cam, frame, '.png')

            if not os.path.exists(path):
                self.ui.set_warning(
                texts.WARNINGS["image_not_exist"][self.language],
                "data_auquzation",
                level=2,
                )
                return

            self.selected_images_for_label.add(
                self.move_on_list.get_current("sheets_id"),
                self.current_technical_side,
                (cam, frame),
            )

            self.thechnicals_backend[self.current_technical_side].update_selected(
                self.selected_images_for_label.get_sheet_side_selections(
                    self.move_on_list.get_current("sheets_id"),
                    self.current_technical_side,
                )
            )
            self.refresh_thechnical(fp=1)

            self.ui.add_selected_image(
                self.selected_images_for_label.get_all_selections_list()
            )
            self.ui.set_warning(
                texts.WARNINGS["APPEND_SUCCESSFULLY"][self.language],
                "data_auquzation",
                level=1,
            )

    def remove_select_img(self):

        selected_img_for_remove = self.ui.get_selected_img()
        if len(selected_img_for_remove):
            self.selected_images_for_label.remove_by_index(selected_img_for_remove)
            self.ui.add_selected_image(
                self.selected_images_for_label.get_all_selections_list()
            )
            self.ui.set_warning(
                texts.WARNINGS["REMOVE_SUCCESSFULLY"][self.language],
                "data_auquzation",
                level=1,
            )
            for s in ["up", "down"]:
                self.thechnicals_backend[s].update_selected(
                    self.selected_images_for_label.get_sheet_side_selections(
                        self.sheet.get_id(), s
                    )
                )
                self.current_technical_side = s
                self.refresh_thechnical(fp=1)
        else:
            self.ui.set_warning(
                texts.WARNINGS["NO_CHOOSEN_IMG"][self.language],
                "data_auquzation",
                level=2,
            )

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def label_selected_img(self):
        selected_imgs = self.selected_images_for_label.get_all_selections_list()
        selected_idxs = self.ui.get_selected_img()
        if len(selected_idxs) > 0:

            filtered_selected = Utils.get_selected_value(selected_imgs, selected_idxs)
            paths = self.db.get_path_sheet_image(filtered_selected)
            sheets = []
            for select_img in filtered_selected:
                sheets.append(self.db.load_sheet(select_img[0]))

            self.ds.save_to_temp(paths, sheets, filtered_selected)

            self.move_on_list.add(
                list(zip(sheets, filtered_selected, paths)), "selected_imgs_for_label"
            )
            label_type = self.ui.get_label_type()
            for sheet, selected_img_pos, img_path in zip(
                sheets, filtered_selected, paths
            ):
                if img_path not in self.label_memory.get_all()[label_type].keys():
                    label = self.ds.get_label_from_annotation(selected_img_pos)
                    f = []
                    for i in label:
                        f.append([i["class"], np.array(i["mask"]), i['line_thickness'], i['point_thickness']])
                    if f:
                        self.label_memory.add(img_path, f, label_type)
                
                self.image_save_status[img_path] = False

            self.ui.show_label_page()
            self.ui.show_small_neighbouring()
            self.load_image_to_label_page()
            self.ui.checkBox_show_neighbours.setCheckState(Qt.CheckState.Checked)
            self.ui.checkBox_show_neighbours_labels.setCheckState(Qt.CheckState.Checked)
        else:
            self.ui.set_warning(
                texts.WARNINGS["NO_CHOOSEN_IMG"][self.language],
                "data_auquzation",
                level=2,
            )

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def refresh_label_img(self, img, fp=5):
        if self.t % fp == 0:
            self.t = 1
            self.ui.show_image_in_label(img)

        else:
            self.t += 1

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def load_image_to_label_page(self, fast=False):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current(
            "selected_imgs_for_label"
        )

        label_type = self.ui.get_label_type()
        self.img = Utils.read_image(img_path, "color")
        self.load_label_from_memory(img_path)

        if not fast:
            label_img = self.label_bakcend[label_type].draw(self.selected_defects)
            self.img = Utils.add_layer_to_img(
                self.img, label_img, opacity=0.4, compress=0.5
            )
            self.ui.show_image_in_label(self.img)

        labels = self.label_bakcend[label_type].get()
        
        if not fast:
            labels_name = []
            for label in labels:
                labels_name.append(self.defects_name_dict[label[0]])
            self.ui.show_labels(labels, labels_name, label_type, self.selected_defects)

        if len(labels) > 0:
            self.ui.yes_defect.setChecked(True)
            self.ui.no_defect.setChecked(False)
        else:
            self.ui.yes_defect.setChecked(False)
            self.ui.no_defect.setChecked(True)

        # #print(self.label_bakcend[label_type].get())
        # #print(label, img_path)

        if not fast:
            self.load_neighbour_images(selected_img_pos)

            self.ui.show_image_info_lable_page(sheet, selected_img_pos)

            self.ui.image.setScaledContents(True)
            self.scale = 1
            self.position = [0, 0]

    def load_label_from_memory(self, img_path):
        for label_type in ["mask"]:
            label = self.label_memory.get_label(label_type, img_path)
            self.label_bakcend[label_type].load(label)

    def load_neighbour_images(self, selected_img_pos):
        c = selected_img_pos[-1][0]
        f = selected_img_pos[-1][1]
        neighbours = []
        n_up_left = [selected_img_pos[0], selected_img_pos[1], (c - 1, f - 1)]
        neighbours.append(n_up_left)
        n_up = [selected_img_pos[0], selected_img_pos[1], (c, f - 1)]
        neighbours.append(n_up)
        n_up_right = [selected_img_pos[0], selected_img_pos[1], (c + 1, f - 1)]
        neighbours.append(n_up_right)
        n_left = [selected_img_pos[0], selected_img_pos[1], (c - 1, f)]
        neighbours.append(n_left)
        n_right = [selected_img_pos[0], selected_img_pos[1], (c + 1, f)]
        neighbours.append(n_right)
        n_down_left = [selected_img_pos[0], selected_img_pos[1], (c - 1, f + 1)]
        neighbours.append(n_down_left)
        n_down = [selected_img_pos[0], selected_img_pos[1], (c, f + 1)]
        neighbours.append(n_down)
        n_down_right = [selected_img_pos[0], selected_img_pos[1], (c + 1, f + 1)]
        neighbours.append(n_down_right)
        n_center = [selected_img_pos[0], selected_img_pos[1], (c, f)]
        neighbours.append(n_center)

        paths = self.db.get_path_sheet_image(neighbours)

        self.n_imgs = []
        for path in paths:
            if os.path.exists(path):
                img = Utils.read_image(path, "color")
            else:
                img = np.zeros((1200, 1920, 3), dtype='uint8')
            self.n_imgs.append(img)

        self.load_neighbour_annotations(neighbours, paths)

        self.ui.update_neighbour_images(self.n_imgs, self.n_anns)

    def load_neighbour_annotations(self, neighbours, paths):
        # t = time.time()
        label_type = self.ui.get_label_type()
        self.n_anns = []
        for selected_img_pos, img_path in zip(neighbours, paths):
            if img_path not in self.label_memory.get_all()[label_type].keys():
                label = self.ds.get_label_from_annotation(selected_img_pos)
                f = []
                for i in label:
                    f.append([i["class"], np.array(i["mask"]), i["line_thickness"], i["point_thickness"]])
                if f:
                    self.label_memory.add(img_path, f, label_type)
            label = self.label_memory.get_label(label_type, img_path)
            self.label_bakcend_neighbours[label_type].load(label)
            label_img = self.label_bakcend_neighbours[label_type].draw(
                select_list=["All"]
            )
            self.n_anns.append(label_img)
        # #print(time.time() - t)

    def next_label_img(self):
        # print(')))))))))))):', self.image_save_status)
        _, _, img_path = self.move_on_list.get_current(
            "selected_imgs_for_label"
        )
        if not self.image_save_status[img_path]:
            t = self.ui.show_question(
                    texts.WARNINGS["question"][self.language],
                    texts.MESSEGES["changes_not_saved"][self.language],
                )
            if not t:
                return
            else:
                self.selected_defects = []
                self.move_on_list.next_on_list("selected_imgs_for_label")
                self.load_image_to_label_page()
        else:
            self.selected_defects = []
            self.move_on_list.next_on_list("selected_imgs_for_label")
            self.load_image_to_label_page()

    def prev_label_img(self):
        _, _, img_path = self.move_on_list.get_current(
            "selected_imgs_for_label"
        )
        if not self.image_save_status[img_path]:
            t = self.ui.show_question(
                    texts.WARNINGS["question"][self.language],
                    texts.MESSEGES["changes_not_saved"][self.language],
                )
            if not t:
                return
            else:
                self.selected_defects = []
                self.move_on_list.prev_on_list("selected_imgs_for_label")
                self.load_image_to_label_page()
        else:
            self.selected_defects = []
            self.move_on_list.prev_on_list("selected_imgs_for_label")
            self.load_image_to_label_page()

    def check_image_saved(self):
        try:
            l = self.move_on_list.get_list("selected_imgs_for_label")
        except:
            return True
        for _, _, img_path in l:
            if not self.image_save_status[img_path]:
                t = self.ui.show_question(
                        texts.WARNINGS["question"][self.language],
                        texts.MESSEGES["changes_not_saved"][self.language],
                    )
                if not t:
                    return False
                else:
                    return True
        
        return True
            

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------

    def create_label_color(self):
        self.LABEL_COLOR = {"black": (0, 0, 0)}
        defect_name, defect_info = self.get_defects()
        # #print(len(defect_info),defect_info)
        for i in range(len(defect_info)):
            # #print(defect_name[i], defect_info[i]["color"])
            hex_color = defect_info[i]["color"].lstrip("#")
            rgb_color = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
            rgb = (rgb_color[2], rgb_color[1], rgb_color[0])
            self.LABEL_COLOR.update({defect_info[i]["defect_ID"]: rgb})

    def get_labels_color(self):
        defect_name, defect_info = self.get_defects()
        # #print(len(defect_info),defect_info)
        colors = {}
        for i in range(len(defect_info)):
            hex_color = defect_info[i]["color"]
            colors.update({defect_info[i]["defect_ID"]: hex_color})
        return colors

    def label_image_mouse(self, wgt_name=""):

        label_type = self.ui.get_label_type()
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()

        if self.ui.get_zoom_type() is None:
            try:
                sheet, pos, img_path = self.move_on_list.get_current(
                    "selected_imgs_for_label"
                )
                img = Utils.read_image(img_path, "color")
                ret = self.label_bakcend[label_type].mouse_event(
                    mouse_status, mouse_button, mouse_pt
                )

                neighbour_flag = False

                if ret == "mask":
                    self.selected_defects = []
                    neighbour_flag = True

                elif ret == 'editing':
                    neighbour_flag = True

                if self.label_bakcend[label_type].is_drawing_finish():
                    self.label_bakcend[label_type].save("0")
                    neighbour_flag = True

                label_img = self.label_bakcend[label_type].draw(self.selected_defects)
                # self.ui.update_center_image(img, label_img)
                img = Utils.add_layer_to_img(img, label_img, opacity=0.4, compress=0.5)
                self.ui.show_image_in_label(img, self.scale, self.position)
                self.img = img

                labels = self.label_bakcend[label_type].get()
                self.label_memory.add(img_path, labels, label_type)
                labels_name = []
                for label in labels:
                    labels_name.append(self.defects_name_dict[label[0]])
                self.ui.show_labels(
                    labels, labels_name, label_type, self.selected_defects
                )

                if len(labels) > 0:
                    self.ui.yes_defect.setChecked(True)
                    self.ui.no_defect.setChecked(False)
                else:
                    self.ui.yes_defect.setChecked(False)
                    self.ui.no_defect.setChecked(True)
                    
                if neighbour_flag:
                    self.load_neighbour_images(pos)
                    self.image_save_status[img_path] = False
            except:
                self.ui.set_warning(
                    texts.WARNINGS["NO_IMAGE_LOADED"][self.language], "label", level=2
                )
                return

        elif self.ui.get_zoom_type() != "drag":
            if mouse_status == "mouse_press":
                if self.ui.image.hasScaledContents():
                    self.scale = 1
                    self.position = [0, 0]
                    self.ui.image.setScaledContents(False)

                if self.ui.get_zoom_type() == "zoom_in":
                    self.scale *= 1.25
                elif self.ui.get_zoom_type() == "zoom_out":
                    self.scale /= 1.25
                if self.scale < 1:
                    self.scale = 1
                    self.position = [0, 0]

                self.position = self.ui.show_image_in_label(
                    self.img, self.scale, self.mouse.get_position()
                )

                if self.ui.get_zoom_type() == "zoom_out" and self.scale == 1:
                    self.ui.polygon()

        elif self.ui.get_zoom_type() == "drag":
            if self.ui.image.hasScaledContents():
                self.scale = 1
                self.position = [0, 0]
            if mouse_status == "mouse_press":
                if self.scale != 1:
                    self.pressed = self.mouse.get_position()
                    self.anchor = self.position
                    self.ui.image.setCursor(Qt.ClosedHandCursor)

            if mouse_status == "mouse_move":
                x, y = self.mouse.get_position()
                if self.pressed:
                    self.ui.image.setCursor(Qt.ClosedHandCursor)
                    dx, dy = x - self.pressed[0], y - self.pressed[1]
                    self.position = self.anchor[0] - dx, self.anchor[1] - dy
                    self.position = self.ui.update_image(self.position)

            if mouse_status == "mouse_release":
                self.pressed = None
                self.ui.image.setCursor(Qt.OpenHandCursor)

    def delete_all_labels(self):
        t = self.ui.show_question(
                    texts.WARNINGS["question"][self.language],
                    texts.MESSEGES["sure_delete"][self.language],
                )
        if not t:
            return
        else:
            label_type = self.ui.get_label_type()
            sheet, pos, img_path = self.move_on_list.get_current("selected_imgs_for_label")
            img = Utils.read_image(img_path, "color")
            self.img = img
            self.label_bakcend[label_type].clear_labels()
            self.label_memory.remove_by_value(label_type, img_path)
            self.ui.show_image_in_label(img, self.scale, self.position)
            self.ui.show_labels([], [], label_type, [])
            self.load_neighbour_images(pos)
            self.image_save_status[img_path] = False

    def select_defect(self):
        # #print(self.ui.mask_table_widget.selectedIndexes())
        self.selected_defects = []
        for i in range(self.ui.mask_table_widget.rowCount()):
            if self.ui.mask_table_widget.item(i, 0).checkState() == QtCore.Qt.Checked:
                self.selected_defects.append(i)
        label_type = self.ui.get_label_type()
        sheet, pos, img_path = self.move_on_list.get_current("selected_imgs_for_label")
        img = Utils.read_image(img_path, "color")
        label_img = self.label_bakcend[label_type].draw(self.selected_defects)
        img = Utils.add_layer_to_img(img, label_img, opacity=0.4, compress=0.5)
        self.ui.show_image_in_label(img, self.scale, self.position)
        self.img = img

    def label_classify(self, wgt_name=""):
        if self.ui.get_zoom_type() is None:
            label_type = self.ui.get_label_type()
            if label_type == "mask":
                mouse_position = self.mouse.get_relative_position()
                self.label_bakcend[label_type].delete_point(mouse_position)
                self.show_labeling(mouse_position)

    def get_defects(self):
        self.defects_name, self.defects_info = self.db.get_defects()
        self.find_defect_name()

        return self.defects_name, self.defects_info

    def find_defect_name(self):
        self.defects_name_dict = {}
        for defect in self.defects_info:
            self.defects_name_dict[defect["defect_ID"]] = defect["name"]

    def show_labeling(self, mouse_position):
        label_type = self.ui.get_label_type()
        if self.label_bakcend[label_type].clicked_in_defect(mouse_position):
            current_mouse_position = self.mouse_controll.position
            sign_defect_table = self.db.ret_sign_defect_table()
            if sign_defect_table == 0:
                pass
                # #print("nochange")
            else:
                # #print("change")
                try:
                    self.defects_name, self.defects_info = self.db.get_defects()
                    self.find_defect_name()
                    self.db.update_sign_table("defects_info", "0")
                except:
                    pass
            # self.create_labeling()
            labeling_win = self.ui.ret_create_labeling()
            self.labeling_api = labeling_api.labeling_API(
                labeling_win, self.defects_name, self.defects_info
            )
            self.ui.labeling_win.win_set_geometry(
                left=current_mouse_position[0], top=current_mouse_position[1]
            )
            self.ui.labeling_win.save_btn.clicked.connect(partial(self.set_label))
            self.ui.labeling_win.cancel_btn.clicked.connect(
                partial(self.close_labeling)
            )
            self.ui.labeling_win.show()
            # #print("end show_labeling")

    def auto_login(self):
        # self.show_login()
        # self.login_window.user_name.setText('test')
        # self.login_window.password.setText('test')
        self.ui.show_image_btn(self.ui.login_btn, "images/logout.png")
        self.logged_in = True
        # self.ui.stackedWidget.setCurrentWidget(self.ui.page_user_profile)
        # self.set_parms_login_page(self.login_info)
        # self.ui.notif_manager.append_new_notif(
        #     message=texts.MESSEGES["user_logedin"][self.ui.language], level=1
        # )
        # self.set_databases()
        self.set_user_databases()
        self.set_default_dataset()

    # login ---------------------------------

    def show_login(self):

        if self.logged_in == False:

            login_window = self.ui.ret_create_login()
            self.login_api = login_API(login_window, main_ui_obj=self.ui)
            # self.login_api.button_connector()
            login_window.login_btn.clicked.connect(partial(self.check_login))
            self.ui.login_window.show()
        else:
            # #print("user_loged_in")
            self.show_message_logout()

    def show_message_logout(self):

        t = self.ui.show_question(
            texts.WARNINGS["question"][self.language],
            texts.WARNINGS["CONFIRM_LOGOUT"][self.language],
        )
        if not t:
            return
        else:
            self.log_out()

    def log_out(self):
        self.logged_in = False
        self.ui.show_image_btn(self.ui.login_btn, "images/icons/person.png")
        self.ui.user_name.setText("")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_label)
        self.ui.comboBox_user_datasets.clear()
        self.ui.comboBox_all_datasets.clear()

        self.login_user_name = "root"
        self.ImageManager.set_user("root")
        self.ui.logger.set_current_user("root")
        self.ui.notif_manager.append_new_notif(
            message=texts.MESSEGES["user_logedout"][self.ui.language], level=0
        )
        self.create_default_ds()
        chart_funcs.clear_userprofile_barchart(self.ui)

    def check_login(self):
        self.login_info = self.login_api.check_login()
        if self.login_info[0] == True:
            self.ui.user_name.setText(
                "{} : {}".format(
                    texts.Titles["user_name"][self.language],
                    self.login_info[1]["user_name"],
                )
            )
            self.ui.show_image_btn(self.ui.login_btn, "images/logout.png")
            self.logged_in = True
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_user_profile)
            self.set_parms_login_page(self.login_info)
            self.ui.notif_manager.append_new_notif(
                message=texts.MESSEGES["user_logedin"][self.ui.language], level=1
            )
            self.set_databases()
            self.set_user_databases()
            self.set_default_dataset()
            # #print("*" * 50)

    def set_parms_login_page(self, login_info):
        self.ui.user_name_2.setText(str(login_info[1]["user_name"]))
        self.ui.user_name_3.setText(str(login_info[1]["user_name"]))
        self.ui.date_created.setText(str(login_info[1]["date_created"]))
        self.ui.user_id.setText(str(login_info[1]["id"]))
        self.ui.role.setText(login_info[1]["role"])
        self.ui.default_dataset.setText(str(login_info[1]["default_dataset"]))
        self.ui.today_date.setText(str(date_funcs.get_date(folder_path=True)))
        self.login_user_name = str(login_info[1]["user_name"])
        self.ImageManager.set_user(self.login_user_name)
        self.ui.logger.set_current_user(self.login_user_name)
        self.ds_json.set_user_name_database(self.login_user_name)
        # #print('username:', self.login_user_name)

    def set_profile_page(self):
        if self.logged_in == True:
            self.ui.set_widget_page(self.ui.stackedWidget, self.ui.page_user_profile)
            self.update_table_all_datasets()
            self.update_user_datasts()

        else:
            self.ui.set_warning(
                texts.WARNINGS["LOGIN_FIRST"][self.language], "setting_eror", level=2
            )

    def set_databases(self):
        dataset_names = []
        self.datasets = self.db.get_all_datasets()
        for i in range(len(self.datasets)):
            dataset_names.append(self.datasets[i]["name"])
        # #print("dataset_names", dataset_names)
        self.ui.comboBox_all_datasets.clear()
        self.ui.comboBox_all_datasets.addItems(dataset_names)
        self.update_table_all_datasets()
        self.ui.comboBox_all_datasets.currentTextChanged.connect(
            self.update_table_all_datasets
        )

    def update_table_all_datasets(self):
        current = self.ui.comboBox_all_datasets.currentIndex()
        self.ui.show_all_datasets(list(self.datasets[current].values()))
        binary_count = self.ds_json.get_binary_count(
            os.path.join(
                self.datasets[current]["path"], self.datasets[current]["name"] + ".json"
            )
        )
        if self.ui.stackedWidget_2.currentIndex() != 0 and self.ui.stackedWidget_2.currentIndex() != 3:
            chart_funcs.update_userprofile_piechart(ui_obj=self.ui, binary_len=binary_count)
            classification_count = self.ds_json.get_classification_count(
                os.path.join(
                    self.datasets[current]["path"], self.datasets[current]["name"] + ".json"
                )
            )
            chart_funcs.update_userprofile_barchart(
                ui_obj=self.ui, classification_len=classification_count
            )

    def set_user_databases(self):
        dataset_names = []
        self.user_databases = self.db.get_user_databases(self.login_user_name)
        # #print("******************", self.user_databases)
        self.user_default_databases = self.db.get_default_dataset(self.login_user_name)
        for i in range(len(self.user_databases)):
            dataset_names.append(self.user_databases[i]["name"])
        # #print("dataset_names", dataset_names)
        self.ui.comboBox_user_datasets.clear()
        self.ui.comboBox_user_datasets.addItems(dataset_names)
        # self.ui.comboBox_default_dataset.addItems(dataset_names)
        self.update_user_datasts()
        self.ui.comboBox_user_datasets.currentTextChanged.connect(
            self.update_user_datasts
        )

    def update_user_datasts(self):
        current = self.ui.comboBox_user_datasets.currentIndex()
        # #print('asd',self.user_databases[current].values)
        self.ui.show_user_datasets(list(self.user_databases[current].values()))
        binary_count = self.ds_json.get_binary_count(
            os.path.join(
                self.user_databases[current]["path"],
                self.user_databases[current]["name"] + ".json",
            )
        )
        if self.ui.stackedWidget_2.currentIndex() != 0 and self.ui.stackedWidget_2.currentIndex() != 3:
            chart_funcs.update_userprofile_piechart(ui_obj=self.ui, binary_len=binary_count)
            classification_count = self.ds_json.get_classification_count(
                os.path.join(
                    self.user_databases[current]["path"],
                    self.user_databases[current]["name"] + ".json",
                )
            )
            chart_funcs.update_userprofile_barchart(
                ui_obj=self.ui, classification_len=classification_count
            )

    def set_default_dataset(self):
        try:
            current_index = self.ui.comboBox_user_datasets.currentIndex()
            self.current = self.user_databases[current_index]
            self.ds = Dataset(self.current["path"])
            self.db.update_dataset_default(self.current["id"], self.login_user_name)
            self.ui.default_dataset.setText(self.current["name"])
            binary_count = self.ds_json.get_binary_count(
                os.path.join(self.current["path"], self.current["name"] + ".json")
            )
            chart_funcs.update_label_piechart(self.ui, binary_count)
            self.ui.set_warning(
                texts.MESSEGES["SET_DATASET"][self.language], "profile", texts_codes.SubTypes['SET_DATASET'], level=1
            )
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes['SET_DATASET'], message=texts.MESSEGES["SET_DATASET"]["en"], level=1
            )
            self.ui.set_b_default_db_parms(self.ds.binary_path)
            self.ui.set_l_default_db_parms(self.ds.localization_path)
        except:
            self.ui.set_warning(
                texts.ERRORS["SET_DATASET_FAILED"][self.language], "profile", texts_codes.SubTypes['SET_DATASET_FAILED'], level=3
            )
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes['SET_DATASET_FAILED'], message=texts.ERRORS["SET_DATASET_FAILED"]["en"], level=5
            )

    # ---------------------------------------------------------------------///////////////////////////////////////////
    # dataset

    def create_dataset(self):

        t = self.ui.show_question(
            texts.WARNINGS["question"][self.language],
            texts.WARNINGS["CREATE_DATABASE"][self.language],
        )
        if not t:
            return
        else:
            parms = self.ui.get_create_dataset_parms()

            if not parms:
                return

            if os.path.exists(os.path.join(parms["path"], parms["dataset_name"])):
                self.ui.set_warning(
                    texts.WARNINGS["CREATE_DATASET_EXIST"][self.language],
                    "profile",
                    texts_codes.SubTypes['CREATE_DATASET_EXIST'],
                    level=2,
                )
                self.ui.logger.create_new_log(
                    message=texts.WARNINGS["CREATE_DATASET_EXIST"]["en"], code=texts_codes.SubTypes['CREATE_DATASET_EXIST'], level=2
                )
                return
            try:
                parms["path"] = os.path.join(parms["path"], parms["dataset_name"])
                Dataset(parms["path"])
                ds_json = dataset_utils.dataset_json(main_ui_obj=self.ui)
                ds_json.create_json_dataset(parms)
                data = parms["dataset_name"], self.login_user_name, parms["path"]
                self.db.add_dataset(data)

                self.ui.set_warning(
                    texts.MESSEGES["CREATE_DATASET"][self.language], "profile", texts_codes.SubTypes['CREATE_DATASET'], level=1
                )
                self.ui.logger.create_new_log(
                    message=texts.MESSEGES["CREATE_DATASET"]["en"], code=texts_codes.SubTypes['CREATE_DATASET'], level=1
                )
            except:
                self.ui.set_warning(
                    texts.ERRORS["CREATE_DATASET_FAILED"][self.language],
                    "profile",
                    texts_codes.SubTypes['CREATE_DATASET_FAILED'],
                    level=3,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["CREATE_DATASET_FAILED"]["en"], code=texts_codes.SubTypes['CREATE_DATASET_FAILED'], level=5
                )

    # ----------------------------------------------------------------------///////////////////////

    def set_label(self):
        mouse_position = self.mouse.get_relative_position()
        selected_label_name = self.labeling_api.ret_selcted_label()
        selected_label = self.db.get_defect_id(selected_label_name)

        sheet, pos, img_path = self.move_on_list.get_current("selected_imgs_for_label")
        label_type = self.ui.get_label_type()
        self.label_bakcend[label_type].update_label(str(selected_label), mouse_position)
        img = Utils.read_image(img_path, "color")
        label_img = self.label_bakcend[label_type].draw(self.selected_defects)
        # self.ui.update_center_image(img, label_img)
        img = Utils.add_layer_to_img(img, label_img, opacity=0.4, compress=0.5)
        self.ui.show_image_in_label(img, self.scale, self.position)
        self.img = img

        self.ui.labeling_win.close_win()
        self.ui.labeling_win = None

        # label_type_dict=['masks','bboxs']

        labels = self.label_bakcend[label_type].get()

        self.label_memory.add(img_path, labels, label_type)

        labels_name = []
        for label in labels:
            labels_name.append(self.defects_name_dict[label[0]])
        self.ui.show_labels(labels, labels_name, label_type, self.selected_defects)

        self.load_neighbour_images(pos)
        self.image_save_status[img_path] = False

    def close_labeling(self):
        self.ui.labeling_win = None

    def clear_cache_fun(self):
        dir = self.cache_path
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        self.ui.listWidget_logs.addItem("Cache Cleared")

    def show_current_pos(self, pt):
        if self.widget_name == "down_side_technical":
            x, y = self.obj_sheet_down.get_pos()

            self.ui.current_pos_x.setText(
                str(int(x * 280))
            )  # zarbar arz varagh ya arzesh pixel

            self.ui.current_pos_y.setText(
                str(round(y * self.length, 2))
            )  # zarbar arz varagh ya arzesh pixel
        if self.widget_name == "up_side_technical":
            x, y = self.obj_sheet_up.get_pos()

            self.ui.current_pos_x.setText(
                str(int(x * 280))
            )  # zarbar arz varagh ya arzesh pixel

            self.ui.current_pos_y.setText(
                str(round(y * self.length, 2))
            )  # zarbar arz varagh ya arzesh pixel

    # def get_parent_path(self):

    #     self.db.report_last("default_setting", "id", 30)
    #     parent_path = "G:/oxin_image_grabber"  # MUST CHANGED -----------------
    #     return parent_path

    def set_b_parms(self):
        if not self.runing_b_model:
            # #print('statrt training binary model')
            b_parms = self.ui.get_binary_parms()
            if not b_parms:
                return
            if b_parms[2]:
                self.split_binary_dataset(b_parms[-1], b_parms[1])
            # update chart axes given train data
            self.update_b_chart_axes(b_parms[3])

            self.bmodel_train_thread = sQThread()
            # Step 3: Create a worker object
            self.bmodel_train_worker = binary_model_funcs.Binary_model_train_worker()
            self.bmodel_train_worker.assign_parameters(
                b_parms=b_parms, api_obj=self, ui_obj=self.ui, db_obj=self.db
            )
            # Step 4: Move worker to the thread
            self.bmodel_train_worker.moveToThread(self.bmodel_train_thread)
            # Step 5: Connect signals and slots
            self.bmodel_train_thread.started.connect(self.bmodel_train_worker.train_model)
            self.bmodel_train_worker.finished.connect(self.bmodel_train_thread.quit)
            self.bmodel_train_worker.finished.connect(
                self.bmodel_train_worker.show_bmodel_train_result
            )
            self.bmodel_train_worker.finished.connect(self.bmodel_train_worker.deleteLater)
            self.bmodel_train_thread.finished.connect(self.bmodel_train_thread.deleteLater)

            self.bmodel_train_worker.warning.connect(self.ui.set_warning)
            self.bmodel_train_worker.update_charts.connect(self.assign_new_value_to_b_chart)

            # Step 6: Start the thread
            self.runing_b_model=True
            self.bmodel_train_thread.start()
            
            self.ui.binary_train.setEnabled(False)

            self.ui.binary_train_progressBar.setValue(0)
            self.ui.binary_train_progressBar.setMaximum(b_parms[3])

    def update_b_chart_axes(self, nepoch):
        # for chart_postfix in self.ui.chart_names:
        #     eval("self.ui.axisX_%s" % chart_postfix).setRange(1, max(nepoch, chart_funcs.axisX_range))
        #     if self.ui.binary_chart_checkbox.isChecked():
        #         eval("self.ui.axisX_%s" % chart_postfix).setTickCount(nepoch)
        #     else:
        #         eval("self.ui.axisX_%s" % chart_postfix).setTickCount(
        #             chart_funcs.axisX_range
        #         )
        chart_funcs.update_axisX_range(ui_obj=self.ui, nepoch=nepoch)
        chart_funcs.clear_series_date(
            ui_obj=self.ui, chart_postfixes=self.ui.chart_names
        )
        self.ui.binary_chart_checkbox.setEnabled(True)
        # self.ui.binary_chart_checkbox.setChecked(True)

    def assign_new_value_to_b_chart(self, last_epoch, logs):
        try:
            self.ui.binary_train_progressBar.setValue(self.ui.binary_train_progressBar.value() + 1)
            chart_funcs.update_chart(
                ui_obj=self.ui,
                chart_postfixes=self.ui.chart_names,
                last_epoch=last_epoch,
                logs=logs,
                scroll_obj=self.ui.binary_chart_scrollbar,
            )
            self.ui.logger.create_new_log(message=texts.MESSEGES['UPDATE_BCHART']['en'].format(last_epoch))
        except:
            self.ui.logger.create_new_log(message=texts.ERRORS['UPDATE_BCHART_FAILED']['en'].format(last_epoch), level=5)
            self.ui.set_warning(texts.ERRORS['UPDATE_BCHART_FAILED'][self.language].format(last_epoch), 'train', None, 3)

    def set_l_parms(self):
        if not self.runing_l_model:
            l_parms = self.ui.get_localization_parms()
            if not l_parms:
                return
            if l_parms[3]:
                self.split_localization_dataset(l_parms[-1], l_parms[2])
            # update chart axes given train data
            self.update_l_chart_axes(l_parms[4])

            self.lmodel_train_thread = sQThread()
            # Step 3: Create a worker object
            self.lmodel_train_worker = (
                localization_model_funcs.Localization_model_train_worker()
            )
            self.lmodel_train_worker.assign_parameters(
                l_parms=l_parms, api_obj=self, ui_obj=self.ui, db_obj=self.db
            )
            # Step 4: Move worker to the thread
            self.lmodel_train_worker.moveToThread(self.lmodel_train_thread)
            # Step 5: Connect signals and slots
            self.lmodel_train_thread.started.connect(self.lmodel_train_worker.train_model)
            self.lmodel_train_worker.finished.connect(self.lmodel_train_thread.quit)
            self.lmodel_train_worker.finished.connect(
                self.lmodel_train_worker.show_lmodel_train_result
            )
            self.lmodel_train_worker.finished.connect(self.lmodel_train_worker.deleteLater)
            self.lmodel_train_thread.finished.connect(self.lmodel_train_thread.deleteLater)

            self.lmodel_train_worker.warning.connect(self.ui.set_warning)
            self.lmodel_train_worker.update_charts.connect(self.assign_new_value_to_l_chart)

            # Step 6: Start the thread
            self.runing_l_model=True
            self.lmodel_train_thread.start()
                
            self.ui.localization_train.setEnabled(False)

            self.ui.localization_train_progressBar.setValue(0)
            self.ui.localization_train_progressBar.setMaximum(l_parms[4])

    def update_l_chart_axes(self, nepoch):
        # for chart_postfix in self.ui.loc_chart_names:
        #     eval("self.ui.axisX_%s" % chart_postfix).setRange(0, max(nepoch, chart_funcs.axisX_range))
        #     if self.ui.localization_chart_checkbox.isChecked():
        #         eval("self.ui.axisX_%s" % chart_postfix).setTickCount(nepoch)
        #     else:
        #         eval("self.ui.axisX_%s" % chart_postfix).setTickCount(
        #             chart_funcs.axisX_range
        #         )
        chart_funcs.update_axisX_range(ui_obj=self.ui, nepoch=nepoch)
        chart_funcs.clear_series_date(
            ui_obj=self.ui, chart_postfixes=self.ui.loc_chart_names
        )
        self.ui.localization_chart_checkbox.setEnabled(True)
        # self.ui.localization_chart_checkbox.setChecked(True)

    def assign_new_value_to_l_chart(self, last_epoch, logs):
        try:
            self.ui.localization_train_progressBar.setValue(self.ui.localization_train_progressBar.value() + 1)
            chart_funcs.update_chart(
                ui_obj=self.ui,
                chart_postfixes=self.ui.loc_chart_names,
                last_epoch=last_epoch,
                logs=logs,
                scroll_obj=self.ui.localization_chart_scrollbar,
                chart_type='localization',
            )
            self.ui.logger.create_new_log(message=texts.MESSEGES['UPDATE_LCHART']['en'].format(last_epoch))
        except:
            self.ui.logger.create_new_log(message=texts.ERRORS['UPDATE_LCHART_FAILED']['en'].format(last_epoch), level=5)
            self.ui.set_warning(texts.ERRORS['UPDATE_LCHART_FAILED'][self.ui.language].format(last_epoch), 'l_train', None, 3)

    def save_to_dataset(self):
        sheet, pos, img_path = self.move_on_list.get_current("selected_imgs_for_label")
        self.ds.save(
            img_path=img_path, pos=pos, sheet=sheet, masks=self.label_bakcend["mask"]
        )

    def save_train_ds(self):
        masks = self.label_bakcend["mask"].get()
        try:
            sheet, pos, img_path = self.move_on_list.get_current(
                "selected_imgs_for_label"
            )
        except:
            self.ui.set_warning(
                texts.WARNINGS["NO_IMAGE_LOADED"][self.language], "label", level=2
            )
            return

        saved_perfect = self.ds.check_saved_perfect(pos=pos)
        saved_defect = self.ds.check_saved_defect(pos=pos)
        if self.ui.no_defect.isChecked():
            if masks:
                self.ui.set_warning(
                    texts.WARNINGS["WRONGE_MASK"][self.language], "label", level=2
                )
                return
            if saved_defect:
                t = self.ui.show_question(
                    texts.WARNINGS["question"][self.language],
                    texts.WARNINGS["ALREADY_SAVED_DEFECT"][self.language],
                )
                if not t:
                    return
                else:
                    self.ds.delete_from_defect(pos)
                    self.ds_json.modify_defect(self.ds.defect_path)

            self.ds.save_to_perfect(img_path=img_path, pos=pos)
            self.ui.set_warning(
                texts.WARNINGS["IMAGE_SAVE_SUCCESSFULLY"][self.language],
                "label",
                level=1,
            )
            self.ds_json.modify_perfect(self.ds.perfect_path)
            self.image_save_status[img_path] = True

        elif self.ui.yes_defect.isChecked():
            if not masks:
                self.ui.set_warning(
                    texts.WARNINGS["WRONGE_MASK"][self.language], "label", level=2
                )
                return
            if saved_perfect:
                t = self.ui.show_question(
                    texts.WARNINGS["question"][self.language],
                    texts.WARNINGS["ALREADY_SAVED_PERFECT"][self.language],
                )
                if not t:
                    return
                else:
                    self.ds.delete_from_perfect(pos)
                    self.ds_json.modify_perfect(self.ds.perfect_path)

            mask = self.create_mask_from_mask(img_path)
            self.ds.save_to_defect(img_path=img_path, pos=pos, mask=mask)
            self.ui.set_warning(
                texts.WARNINGS["IMAGE_SAVE_SUCCESSFULLY"][self.language],
                "label",
                level=1,
            )
            self.ds_json.modify_defect(self.ds.defect_path)
            self.image_save_status[img_path] = True
        else:
            self.ui.set_warning(
                texts.WARNINGS["IMAGE_STATUS"][self.language], "label", level=2
            )
            return

        self.ds.save(img_path=img_path, pos=pos, sheet=sheet, masks=masks)
        labels = []
        for mask in masks:
            if mask[0] not in labels:
                labels.append(mask[0])

        image_name = self.ds.__file_name__(pos) + self.ds.format_image
        self.ds_json.add_update_classification(image_name, labels)
        binary_count = self.ds_json.get_binary_count(None)
        chart_funcs.update_label_piechart(self.ui, binary_count)

    def save_all_train_ds(self):
        count = self.move_on_list.get_count("selected_imgs_for_label")
        self.ui.save_all_progressBar.setValue(0)
        self.ui.save_all_progressBar.setMaximum(count)

        self.thread = sQThread()
        # Step 3: Create a worker object
        self.worker = save_all_worker.save_all_worker()
        self.worker.assign_parameters(
            api_obj=self,
            count = count
        )
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.warning.connect(self.ui.set_warning)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.save_all_finished)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.update_progressbar.connect(self.update_save_all_progressbar)
        self.worker.question.connect(self.save_all_show_question)
        # Step 6: Start the thread
        self.thread.start()

    def save_all_show_question(self, title, message):
        self.save_all_question = self.ui.show_question(title, message)

    def save_all_finished(self):
        binary_count = self.ds_json.get_binary_count(None)
        chart_funcs.update_label_piechart(self.ui, binary_count)
        self.ui.set_warning(
                texts.WARNINGS["IMAGES_SAVE_SUCCESSFULLY"][self.language],
                "label",
                level=1,
            )

    def update_save_all_progressbar(self):
        self.ui.save_all_progressBar.setValue(self.ui.save_all_progressBar.value() + 1)

    def split_binary_dataset(self, paths, size):
        for path in paths:
            if self.ds.check_binary_dataset(path):
                self.ds.create_split_folder(path)

                s_mask = os.path.join(path, self.ds.defect_mask_folder)
                s_defect = os.path.join(path, self.ds.defect_folder)
                d_defect = os.path.join(path, self.ds.defect_splitted_folder)
                imgs = os.listdir(s_defect)
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_defect, i), color="gray")
                    mask = Utils.read_image(os.path.join(s_mask, i), color="gray")
                    crops, _ = get_crops(img, mask, size)
                    self.ds.save_to_defect_splitted(
                        crops, d_defect, name=i.split(".")[0]
                    )

                s_perfect = os.path.join(path, self.ds.perfect_folder)
                d_perfect = os.path.join(path, self.ds.perfect_splitted_folder)
                imgs = os.listdir(s_perfect)
                if len(os.listdir(s_perfect)):
                    n_split = np.ceil(
                        (len(os.listdir(d_defect)) * 1.5) / (len(os.listdir(s_perfect)))
                    )
                else:
                    n_split = 0
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_perfect, i), color="color")
                    crops = get_crops_no_defect(img, n_split, size)
                    self.ds.save_to_perfect_splitted(crops, d_perfect, i.split(".")[0])
            else:
                self.ui.set_warning(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], "train", level=2
                )
                return

    def split_localization_dataset(self, paths, size):
        for path in paths:
            if self.ds.check_localization_dataset(path):
                self.ds.create_l_split_folder(path)

                s_label = os.path.join(path, self.ds.localization_folder_label)
                s_image = os.path.join(path, self.ds.localization_folder_image)
                d_label = os.path.join(path, self.ds.localization_folder_label_splitted)
                d_image = os.path.join(path, self.ds.localization_folder_image_splitted)
                imgs = os.listdir(s_image)
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_image, i), color="gray")
                    label = Utils.read_image(os.path.join(s_label, i), color="gray")
                    image_crops, label_crops = get_crops(img, label, size)
                    self.ds.save_localization_splits(
                        image_crops, label_crops, d_image, d_label, name=i.split(".")[0]
                    )
            else:
                self.ui.set_warning(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], "train", level=2
                )
                return

    def select_binary_dataset(self, page="train"):
        self.ui.create_ds_selection_dialog()

        datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)[1]
        self.ui.select_ds_dialog.table.setRowCount(len(datasets_list))
        for i, ds in enumerate(datasets_list):
            # set name
            table_item = sQTableWidgetItem(str(ds["name"]))
            table_item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.select_ds_dialog.table.setItem(i, 0, table_item)
            # set user_own
            table_item = sQTableWidgetItem(str(ds["user_own"]))
            self.ui.select_ds_dialog.table.setItem(i, 1, table_item)
            # set path
            table_item = sQTableWidgetItem(str(ds["path"]))
            self.ui.select_ds_dialog.table.setItem(i, 2, table_item)
        

        self.ui.select_ds_dialog.ok_btn.clicked.connect(lambda: self.ok_selected_binary_datasets(page))
        self.ui.select_ds_dialog.show()
    
    def ok_selected_binary_datasets(self, page="train"):
        selecteds = self.ui.select_ds_dialog.get_select_datasets()

        for selected in selecteds:
            dname = os.path.join(selected, 'binary')
            if not self.ds.check_binary_dataset(dname):
                self.ui.set_warning(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], page, level=2
                )
                continue
            #
            if page == "train":
                text = self.ui.b_dp.toPlainText()
                pattern = r"[0-9]+. "
                datasets = [
                    os.path.abspath(s.rstrip()) for s in re.split(pattern, text)[1:]
                ]

                if os.path.abspath(dname) in datasets:
                    self.ui.set_warning(
                        texts.WARNINGS["DATASET_EXIST"][self.language], page, level=2
                    )
                    continue

                n = len(datasets) + 1
                if text != "":
                    text += " \n"
                self.ui.b_dp.setPlainText(text + str(n) + ". " + dname)
            #
            elif page == "binarylist":
                self.ui.binarylist_dataset_lineedit.setText(dname)
                self.ui.binarylist_dataset_annot_lineedit.setText(dname)

    def delete_binary_dataset(self):
        ds_n = self.ui.b_ds_num.value() - 1
        text = self.ui.b_dp.toPlainText()
        pattern = r"[0-9]+. "
        datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]
        if ds_n >= len(datasets):
            self.ui.set_warning(
                texts.WARNINGS["DATASET_NUMBER"][self.language], "train", level=2
            )
            return
        datasets.pop(ds_n)
        text = ""
        for i in range(len(datasets)):
            text += str(i + 1) + ". " + datasets[i]
            if i != len(datasets) - 1:
                text += "\n"

        self.ui.b_dp.setPlainText(text)

    def ok_add_binary_ds(self):
        path = self.ui.b_add_ds_lineedit.text().lstrip()
        path = path.rstrip()
        if not os.path.exists(path):
            self.ui.set_warning(
                texts.WARNINGS["INVALID_DATASET"][self.language], "train", level=2
            )
            return
        elif not self.ds.check_binary_dataset(path):
            self.ui.set_warning(
                texts.WARNINGS["DATASET_FORMAT"][self.language], "train", level=2
            )
            return

        text = self.ui.b_dp.toPlainText()
        pattern = r"[0-9]+. "

        datasets = [os.path.abspath(s.rstrip()) for s in re.split(pattern, text)[1:]]

        if os.path.abspath(path) in datasets:
            self.ui.set_warning(
                texts.WARNINGS["DATASET_EXIST"][self.language], "train", level=2
            )
        else:
            n = len(datasets) + 1
            if text != "":
                text += " \n"
            self.ui.b_dp.setPlainText(text + str(n) + ". " + path)
        self.ui.b_add_ds_lineedit.setText("")

        height = self.ui.b_add_ds_frame.height()
        if height == 67:
            self.left_box = QPropertyAnimation(self.ui.b_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(100)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    def select_localization_pretrain_path(self):
        self.l_select_pre_dialog = QFileDialog()
        path = "./"
        filter = "h5(*.h5)"
        dname = QFileDialog.getOpenFileName(self.l_select_pre_dialog, 'open', path, filter)[0]

        if dname == "":
            return
        self.ui.l_prep.setText(dname)

    def select_localization_dataset(self, page="l_train"):
        self.ui.create_ds_selection_dialog()

        datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)[1]
        self.ui.select_ds_dialog.table.setRowCount(len(datasets_list))
        for i, ds in enumerate(datasets_list):
            # set name
            table_item = sQTableWidgetItem(str(ds["name"]))
            table_item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.select_ds_dialog.table.setItem(i, 0, table_item)
            # set user_own
            table_item = sQTableWidgetItem(str(ds["user_own"]))
            self.ui.select_ds_dialog.table.setItem(i, 1, table_item)
            # set path
            table_item = sQTableWidgetItem(str(ds["path"]))
            self.ui.select_ds_dialog.table.setItem(i, 2, table_item)
        

        self.ui.select_ds_dialog.ok_btn.clicked.connect(lambda: self.ok_selected_localization_datasets(page))
        self.ui.select_ds_dialog.show()

    def ok_selected_localization_datasets(self, page="l_train"):
        selecteds = self.ui.select_ds_dialog.get_select_datasets()

        for selected in selecteds:
            dname = os.path.join(selected, 'localization')
            if not self.ds.check_localization_dataset(dname):
                self.ui.set_warning(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], page, level=2
                )
                return
            #
            if page == "l_train":
                text = self.ui.l_dp.toPlainText()
                pattern = r"[0-9]+. "
                datasets = [
                    os.path.abspath(s.rstrip()) for s in re.split(pattern, text)[1:]
                ]

                if os.path.abspath(dname) in datasets:
                    self.ui.set_warning(
                        texts.WARNINGS["DATASET_EXIST"][self.language], page, level=2
                    )
                    return

                n = len(datasets) + 1
                if text != "":
                    text += " \n"
                self.ui.l_dp.setPlainText(text + str(n) + ". " + dname)
                #
            elif page == "binarylist":
                self.ui.binarylist_dataset_lineedit.setText(dname)
                self.ui.binarylist_dataset_annot_lineedit.setText(dname)

    def delete_localization_dataset(self):
        ds_n = self.ui.l_ds_num.value() - 1
        text = self.ui.l_dp.toPlainText()
        pattern = r"[0-9]+. "
        datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]
        if ds_n >= len(datasets):
            self.ui.set_warning(
                texts.WARNINGS["DATASET_NUMBER"][self.language], "l_train", level=2
            )
            return
        datasets.pop(ds_n)
        text = ""
        for i in range(len(datasets)):
            text += str(i + 1) + ". " + datasets[i]
            if i != len(datasets) - 1:
                text += "\n"

        self.ui.l_dp.setPlainText(text)

    def ok_add_localization_ds(self):
        path = self.ui.l_add_ds_lineedit.text().lstrip()
        path = path.rstrip()
        if not os.path.exists(path):
            self.ui.set_warning(
                texts.WARNINGS["INVALID_DATASET"][self.language], "l_train", level=2
            )
            return
        elif not self.ds.check_localization_dataset(path):
            self.ui.set_warning(
                texts.WARNINGS["DATASET_FORMAT"][self.language], "l_train", level=2
            )
            return

        text = self.ui.l_dp.toPlainText()
        pattern = r"[0-9]+. "

        datasets = [os.path.abspath(s.rstrip()) for s in re.split(pattern, text)[1:]]

        if os.path.abspath(path) in datasets:
            self.ui.set_warning(
                texts.WARNINGS["DATASET_EXIST"][self.language], "l_train", level=2
            )
        else:
            n = len(datasets) + 1
            if text != "":
                text += " \n"
            self.ui.l_dp.setPlainText(text + str(n) + ". " + path)
        self.ui.l_add_ds_lineedit.setText("")

        height = self.ui.l_add_ds_frame.height()
        if height == 67:
            self.left_box = QPropertyAnimation(self.ui.l_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(100)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    def get_camera_config(self, id):
        """
        This function returns camera parameters from database

        :param id: Id of camera. a number in range [1, 24]
        :type id: int
        :return: Dictionary of camera parameters
        :rtype: dict
        """
        cam_parms = self.db.load_cam_params(id)
        return cam_parms

    # -------------------------------------------Camera conection and show ----------------------------------------

    def connect_camera(self):
        """
        This camera is used to connect selected cameras
        """
        selected_cameras = self.ui.get_selected_cameras()

        if not any(selected_cameras):
            self.ui.set_warning(
                texts.WARNINGS["no_camera_selected"][self.ui.language],
                "camera_connection",
                level=2
            )
            return

        if self.i == 0:
            self.i = np.where(selected_cameras)[0][0]
            self.ui.set_buttons_enable_or_disable(
                [self.ui.disconnect_camera_btn, self.ui.connect_camera_btn],
                enable=False,
            )
            self.ui.checkBox_top.setEnabled(False)
            self.ui.checkBox_bottom.setEnabled(False)
            self.ui.checkBox_all.setEnabled(False)
            for i in range(1, 25):
                if i < 10:
                    btn_name = eval("self.ui.camera0%s_btn" % i)
                else:
                    btn_name = eval("self.ui.camera%s_btn" % i)
                btn_name.setEnabled(False)

        if selected_cameras[self.i]:
            cam_num = self.i + 1
            cam_parms = self.get_camera_config(str(cam_num))
            ret = self.cameras.add_camera(str(cam_num), cam_parms)

            if ret == "True":
                self.ui.set_warning(
                    texts.MESSEGES["Camera_successful"][self.ui.language].format(cam_num),
                    "camera_connection",
                    level=1
                )
                self.ui.set_img_btn_camera(cam_num)

            else:
                if ret == "Camera Not Connected":
                    self.ui.set_warning(
                        texts.ERRORS["Camera_serial_error"][self.ui.language].format(
                            cam_num
                        ),
                        "camera_connection",
                        level=3
                    )
                else:
                    self.ui.set_warning(
                        texts.ERRORS["control_config_error"][self.ui.language].format(
                            cam_num
                        ),
                        "camera_connection",
                        level=3
                    )

                self.ui.set_img_btn_camera(cam_num, status="False")

        while 1:
            self.i += 1
            if self.i == len(selected_cameras):
                self.i = 0
                self.ui.set_buttons_enable_or_disable(
                    [self.ui.disconnect_camera_btn, self.ui.connect_camera_btn],
                    enable=True,
                )
                self.ui.checkBox_top.setEnabled(True)
                self.ui.checkBox_bottom.setEnabled(True)
                self.ui.checkBox_all.setEnabled(True)
                for i in range(1, 25):
                    if i < 10:
                        btn_name = eval("self.ui.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.ui.camera%s_btn" % i)
                    btn_name.setEnabled(True)
                self.set_available_cameras()
                return
            if selected_cameras[self.i]:
                QTimer.singleShot(3000, self.connect_camera)
                return

    def disconnect_camera(self):
        """
        This camera is used to disconnect selected cameras
        """
        selected_cameras = self.ui.get_selected_cameras()

        if not any(selected_cameras):
            self.ui.set_warning(
                texts.WARNINGS["no_camera_selected"][self.ui.language],
                "camera_connection",
                level=2
            )
            return

        if self.j == 0:
            self.j = np.where(selected_cameras)[0][0]
            self.ui.set_buttons_enable_or_disable(
                [self.ui.connect_camera_btn, self.ui.disconnect_camera_btn],
                enable=False,
            )
            self.ui.checkBox_top.setEnabled(False)
            self.ui.checkBox_bottom.setEnabled(False)
            self.ui.checkBox_all.setEnabled(False)
            for i in range(1, 25):
                if i < 10:
                    btn_name = eval("self.ui.camera0%s_btn" % i)
                else:
                    btn_name = eval("self.ui.camera%s_btn" % i)
                btn_name.setEnabled(False)

        if selected_cameras[self.j]:
            cam_num = self.j + 1
            cam_parms = self.get_camera_config(str(cam_num))
            ret = self.cameras.disconnect_camera(
                cam_parms["serial_number"], str(cam_num)
            )

            if ret == "True":
                self.ui.set_warning(
                    texts.MESSEGES["Disconnect_camera_successful"][
                        self.ui.language
                    ].format(cam_num),
                    "camera_connection",
                    level=1
                )
                self.ui.set_img_btn_camera(cam_num, status="Disconnect")

            elif ret == "no_connection":
                self.ui.set_warning(
                    texts.ERRORS["no_connect"][self.ui.language].format(cam_num),
                    "camera_connection",
                    level=3
                )

            else:
                self.ui.set_warning(
                    texts.ERRORS["disconnect_error"][self.ui.language].format(cam_num),
                    "camera_connection",
                    level=3
                )

        while 1:
            self.j += 1
            if self.j == len(selected_cameras):
                self.j = 0
                self.ui.set_buttons_enable_or_disable(
                    [self.ui.connect_camera_btn, self.ui.disconnect_camera_btn],
                    enable=True,
                )
                self.ui.checkBox_top.setEnabled(True)
                self.ui.checkBox_bottom.setEnabled(True)
                self.ui.checkBox_all.setEnabled(True)
                for i in range(1, 25):
                    if i < 10:
                        btn_name = eval("self.ui.camera0%s_btn" % i)
                    else:
                        btn_name = eval("self.ui.camera%s_btn" % i)
                    btn_name.setEnabled(True)
                return
            if selected_cameras[self.j]:
                QTimer.singleShot(3000, self.disconnect_camera)
                return

    def set_available_cameras(self):
        connected_cameras = self.cameras.get_connected_cameras_by_id()
        sn_available = list(connected_cameras.keys())
        sn_available = [str(i) for i in range(1, 25)]
        self.ui.comboBox_connected_cams.clear()
        self.ui.comboBox_connected_cams.addItems(sn_available)

    def start_capture_func(self, disable_ui=True):
        if disable_ui:
            self.ui.set_enabel(self.ui.connect_camera_btn, False)
            self.ui.set_enabel(self.ui.disconnect_camera_btn, False)
            self.ui.set_enabel(self.ui.start_capture_btn, False)
            self.ui.set_enabel(self.ui.stop_capture_btn, True)
            self.ImageManager = ImageManager(
                self.login_user_name, self.ui, self.cameras
            )
            self.live_timer = QTimer(self.ui)
            self.live_timer.timeout.connect(self.ImageManager.show_live)
            self.grab_timer = QTimer(self.ui)
            self.grab_timer.timeout.connect(self.grab_image)
            self.ImageManager.first_check_finished.connect(self.start_capture_timers)
            self.ImageManager.second_check_finished.connect(self.stop_capture_timers)
            self.start_capture_flag = True
            self.ready_capture_flag = True
        
        if self.sensor and not disable_ui:
            self.start_capture_flag = True
            self.ImageManager.set_live_type(self.live_type)
            self.ImageManager.set_save_flag(self.ui.checkBox_save_images.isChecked())
            self.ImageManager.set_manual_flag(self.ui.manual_camera)
            self.ui.set_enabel(self.ui.stop_capture_btn, False)
            QTimer().singleShot(1000, self.ImageManager.start_sheet_checking)
            QTimer().singleShot(1000, lambda: self.ui.set_enabel(self.ui.stop_capture_btn, True))

            self.init_check_plc()

    def stop_capture_func(self, disable_ui=True):
        if disable_ui:
            self.ui.set_enabel(self.ui.connect_camera_btn, True)
            self.ui.set_enabel(self.ui.disconnect_camera_btn, True)
            self.ui.set_enabel(self.ui.start_capture_btn, True)
            self.ui.set_enabel(self.ui.stop_capture_btn, False)
            self.ready_capture_flag = False
            self.ImageManager.stop()
            try:
                self.stop_capture_timers()
            except:
                pass

        if self.start_capture_flag:
            self.ImageManager.stop()
            try:
                self.stop_capture_timers()
            except:
                pass
            # self.camera_thread.quit()
            # self.camera_thread.wait()
            self.start_capture_flag = False
            self.set_start_software_plc(False)

    def start_capture_timers(self):
        self.ImageManager.stop_sheet_checking()
        try:
            _, _, speed, _ = self.l2_connection.get_full_info()  # get data from level2
        except:
            pass
        if speed > 0:
            self.ImageManager.start()
        self.live_timer.start(self.ui.update_timer_live_frame)
        self.grab_timer.start(int(1000/self.ui.frame_rate))

    def stop_capture_timers(self):
        self.ImageManager.stop()
        self.live_timer.stop()
        self.grab_timer.stop()

    def grab_image(self):
        try:
            _, _, speed, _ = self.l2_connection.get_full_info()  # get data from level2
        except:
            pass
        if speed > 0:
            self.ImageManager.stop()
            self.ImageManager.start()

    def change_live_camera(self, text):
        try:
            self.ImageManager.set_n_camera_live(int(text))
        except:
            pass

    def change_live_type(self, index):
        self.live_type = index
        self.ImageManager.set_live_type(index)

    def save_images(self, state):
        if state == 2:
            self.ImageManager.set_save_flag(1)
        elif state == 0:
            self.ImageManager.set_save_flag(0)

    # _________________________________________________________________________________________________
    # binary-model history page functions

    # binary-model history page functions
    def refresh_binary_models_table_onevent(self, wich_page="not PBT"):
        self.bmodel_tabel_itr = 1
        if wich_page == "PBT":
            self.ui.lineEdit_of_pageNumber_displayment_in_PBT_page.setText(
                str(self.bmodel_tabel_itr)
            )
            self.ui.refresh_pipline_tabs_in_PBT()
        else:
            self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))

        self.refresh_binary_models_table(get_count=True, wich_page=wich_page)
        self.refresh_binary_models_table(wich_page=wich_page)
        self.ui.clear_binary_filters_fields(wich_page=wich_page)
        self.filter_mode = False
        self.ui.set_warning(
            texts.MESSEGES["REFRESH_TABLE"][self.language],
            "binary_model_history",
            level=1,
        )

    def refresh_binary_models_table(
        self,
        nextorprev=False,
        get_count=False,
        filter_mode=False,
        wich_page="not PBT",
        model_type="binary",
    ):
        """this function is used to refresh/update binary models table on UI

        :param nextorprev: boolean determining if get next/prev page of records on table, defaults to False
        :type nextorprev: bool, optional
        :param get_count: boolean determining whether to get count of records in table in database, defaults to False
        :type get_count: bool, optional
        :param filter_mode: boolean determining if in table filter mode, defaults to False
        :type filter_mode: bool, optional
        :return:
            get_count==True: None
            get_count==False: boolean determining if done
        :rtype: _type_
        """
        if model_type == "binary":
            model_type_ = "binary_models"
        elif model_type == "classification":
            model_type_ = "classification_models"
        elif model_type == "localization":
            model_type_ = "localiztion_models"
        else:
            model_type_ = ""

        if get_count:
            res, self.bmodel_count = binary_model_funcs.get_binary_models_from_db(
                db_obj=self.db, count=get_count, model_type=model_type_
            )
            self.bmodel_count = self.bmodel_count[0]["count(*)"]

            # validation
            if not res:
                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["database_get_bmodels_failed"][
                        self.ui.language
                    ],
                    level=3,
                )
            #
            self.binary_model_tabel_nextorprev(check=True, wich_page=wich_page)
            return

        # load filterd models
        if filter_mode:
            # reset table page number to first (1)
            self.bmodel_tabel_itr = 1
            if wich_page == "PBT":
                self.ui.lineEdit_of_pageNumber_displayment_in_PBT_page.setText(
                    str(self.bmodel_tabel_itr)
                )
            else:
                self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))

            res = self.filter_binary_models(
                filter_signal=True,
                count=True,
                wich_page=wich_page,
                model_type=model_type,
            )

            if res[0]:
                self.bmodel_count = res[1][0]["count(*)"]
                self.binary_model_tabel_nextorprev(check=True, wich_page=wich_page)

                res = self.filter_binary_models(
                    filter_signal=True, wich_page=wich_page, model_type=model_type
                )

                if res[0]:
                    bmodels_list = res[1]
                else:
                    self.refresh_binary_models_table(
                        get_count=True, wich_page=wich_page, model_type=model_type
                    )
                    res, bmodels_list = binary_model_funcs.get_binary_models_from_db(
                        db_obj=self.db, model_type=model_type_
                    )
                    if not res:
                        self.ui.notif_manager.append_new_notif(
                            message=texts.ERRORS["database_get_bmodels_failed"][
                                self.ui.language
                            ],
                            level=3,
                        )

            else:
                self.refresh_binary_models_table(
                    get_count=True, wich_page=wich_page, model_type=model_type
                )
                res, bmodels_list = binary_model_funcs.get_binary_models_from_db(
                    db_obj=self.db, model_type=model_type_
                )
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_bmodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )

        else:
            if not nextorprev:
                res, bmodels_list = binary_model_funcs.get_binary_models_from_db(
                    db_obj=self.db, model_type=model_type_
                )
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_bmodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )

            else:
                if not self.filter_mode:
                    res, bmodels_list = binary_model_funcs.get_binary_models_from_db(
                        db_obj=self.db,
                        limit_size=binary_model_funcs.binary_table_nrows,
                        offset=(self.bmodel_tabel_itr - 1)
                        * binary_model_funcs.binary_table_nrows,
                        model_type=model_type_,
                    )
                    if not res:
                        self.ui.notif_manager.append_new_notif(
                            message=texts.ERRORS["database_get_bmodels_failed"][
                                self.ui.language
                            ],
                            level=3,
                        )

                else:
                    res = self.filter_binary_models(
                        limit_size=binary_model_funcs.binary_table_nrows,
                        offset=(self.bmodel_tabel_itr - 1)
                        * binary_model_funcs.binary_table_nrows,
                        wich_page=wich_page,
                        model_type=model_type,
                    )
                    bmodels_list = res[1]

        if len(bmodels_list) == 0 and nextorprev:
            return False

        # set returned models to UI table
        else:
            if wich_page == "PBT":
                binary_model_funcs.set_bmodels_on_ui_tabel_edited_version(
                    ui_obj=self.ui, bmodels_list=bmodels_list, model_type=model_type
                )
            else:
                binary_model_funcs.set_bmodels_on_ui_tabel(
                    ui_obj=self.ui, bmodels_list=bmodels_list
                )
            self.bmodels_list = bmodels_list
            return True

    # next and prev buttons for binary models table functionality
    def binary_model_tabel_nextorprev(
        self, next=True, check=False, wich_page="not PBT"
    ):
        """this function is used to get next/prev page for binary models table

        :param next: boolean determining whether to get next page, defaults to True
        :type next: bool, optional
        :param check: _description_, defaults to False
        :type check: bool, optional
        """
        if check:
            page_max = int(
                math.ceil(self.bmodel_count / binary_model_funcs.binary_table_nrows)
            )
            if self.bmodel_tabel_itr >= page_max:
                if wich_page == "PBT":
                    self.ui.BTN_of_goToNextpage_in_PBT_page.setEnabled(False)
                else:
                    self.ui.binary_tabel_next.setEnabled(False)
            else:
                if wich_page == "PBT":
                    self.ui.BTN_of_goToNextpage_in_PBT_page.setEnabled(True)
                else:
                    self.ui.binary_tabel_next.setEnabled(True)
            #
            if self.bmodel_tabel_itr > 1:
                if wich_page == "PBT":
                    self.ui.BTN_of_goToPreviouspage_in_PBT_page.setEnabled(True)
                else:
                    self.ui.binary_tabel_prev.setEnabled(True)
            else:
                if wich_page == "PBT":
                    self.ui.BTN_of_goToPreviouspage_in_PBT_page.setEnabled(False)
                else:
                    self.ui.binary_tabel_prev.setEnabled(False)

            return
        #
        if next:
            self.bmodel_tabel_itr += 1

        elif self.bmodel_tabel_itr > 1:
            self.bmodel_tabel_itr -= 1
        #
        res = self.refresh_binary_models_table(nextorprev=True, wich_page=wich_page)
        self.binary_model_tabel_nextorprev(check=True, wich_page=wich_page)
        if wich_page == "PBT":
            self.ui.lineEdit_of_pageNumber_displayment_in_PBT_page.setText(
                str(self.bmodel_tabel_itr)
            )
        else:
            self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))

    # filter function for binary models
    def filter_binary_models(
        self,
        limit_size=binary_model_funcs.binary_table_nrows,
        offset=0,
        filter_signal=False,
        count=False,
        wich_page="not PBT",
        model_type="binary",
    ):
        """this function is used to filter binary models given filter params on UI

        :param limit_size: n table rows in database to return, defaults to binary_model_funcs.binary_table_nrows
        :type limit_size: int, optional
        :param offset: starting row index in table to return n next rows, defaults to 0
        :type offset: int, optional
        :param filter_signal: boolean determining wheter to get/update filter params from UI, defaults to False
        :type filter_signal: bool, optional
        :param count: boolean determinig whether to get count of results, defaults to False
        :type count: bool, optional
        :return:
            result: boolean determining id done
            filtered_binary_models: list of dicts
        :rtype: _type_
        """

        if filter_signal:
            self.filter_params = (
                binary_model_funcs.get_binary_model_filter_info_from_ui(
                    ui_obj=self.ui, wich_page=wich_page, model_type=model_type
                )
            )
        #
        res = binary_model_funcs.get_filtered_binary_models_from_db(
            ui_obj=self.ui,
            db_obj=self.db,
            filter_params=self.filter_params,
            limit_size=limit_size,
            offset=offset,
            count=count,
            model_type=model_type,
        )

        if res[0] == "error":
            self.filter_mode = False
            return False, res[1]

        if res[0] == "all":
            self.filter_mode = False
            return False, res[1]

        else:
            self.filter_mode = True
            self.ui.set_warning(
                texts.MESSEGES["FILTERED_RESAULTS_SUCCUSSFULL"][self.language],
                "binary_model_history",
                level=1,
            )
            return True, res[1]

    # clear filters for binary models
    def clear_filters(self):
        """this function is used tp clear filters for binary models list"""

        self.filter_mode = False  # diactive filter mode
        # reset table page number
        self.bmodel_tabel_itr = 1
        self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))
        #
        self.refresh_binary_models_table(get_count=True)
        self.refresh_binary_models_table()
        self.ui.clear_binary_filters_fields()
        self.ui.set_warning(
            texts.MESSEGES["FILTERED_RESAULTS_CLEAR"][self.language],
            "binary_model_history",
            level=1,
        )

        # ____________JJ ZONE START

    def pre_load_binary_images_list_in_PBT_load_dataset_page(self):
        if self.ui.lineEdit_of_path_displayment_in_PBT_page.text() != "":
            self.ui.LBL_of_data_is_ready_in_PBT_page_2.setText("")
            self.load_binary_images_list_in_PBT_load_dataset_page(
                use_customized_flag=True
            )
        else:
            self.ui.LBL_of_data_is_ready_in_PBT_page_2.setText(
                texts.ERRORS["data_not_ready"][self.language]
            )

    def load_binary_images_list_in_PBT_load_dataset_page(
        self, use_customized_flag=False
    ):

        self.ui.LBL_of_data_is_ready_in_PBT_page_2.setText("")
        if (
            self.raw_and_evaluated_Imagw_sliders_check[0]
            and self.raw_and_evaluated_Imagw_sliders_check[1]
        ):
            if use_customized_flag:
                selected_datasets = self.customized_datasets
                text = "Customized"
            else:
                text = self.ui.cbBox_of_dataset_in_PBT_page_load_dataset.currentText()
                selected_datasets = (
                    dataset.get_selected_datasets_for_PBT_loadDataSet_page(
                        text, self.datasets_list
                    )
                )

            if len(selected_datasets) == 0:
                self.ui.set_warning(
                    texts.WARNINGS["SELECT_NO_DATASET"][self.language],
                    "binarylist",
                    level=2,
                )
                return

            (
                perfect_check,
                perfect_image_pathes,
                defect_check,
                defect_image_pathes,
                defect_annot_pathes,
                binary_count,
            ) = binary_list_funcs.get_binarylist_image_pathes_list(
                ds_obj=self.ds, dataset_pathes=selected_datasets
            )

            if not perfect_check and not defect_check:
                self.ui.set_warning(
                    texts.MESSEGES["NO_IMAGE_AVAILABLE_IN_DATASET"][self.language],
                    "binarylist",
                    level=2,
                )
            else:
                # msg
                self.ui.set_warning(
                    texts.MESSEGES["LOAD_IMAGES_DATASETS"][self.language],
                    "binarylist",
                    level=1,
                )

            if perfect_check or defect_check:
                if self.perfect_show and self.defect_show:
                    self.path_list = perfect_image_pathes + defect_image_pathes
                elif self.perfect_show and not (self.defect_show):
                    self.path_list = perfect_image_pathes
                elif not (self.perfect_show) and self.defect_show:
                    self.path_list = defect_image_pathes
                else:
                    self.path_list = []

                random.shuffle(self.path_list)

                self.original_and_evaluated_image_in_PBT.add(
                    mylist=self.path_list,
                    name="original",
                )
                self.original_image_list_next_func = (
                    self.original_and_evaluated_image_in_PBT.build_next_func(
                        name="original"
                    )
                )
                self.original_image_list_prev_func = (
                    self.original_and_evaluated_image_in_PBT.build_prev_func(
                        name="original"
                    )
                )
                # show message that data is ready
                self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedWidth(175)
                self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedHeight(83)
                data_report = "\n {} dataset has: \n {} perfect images \n {} defect images \n {} total images".format(
                    text,
                    len(perfect_image_pathes),
                    len(defect_image_pathes),
                    len(self.path_list),
                )
                if use_customized_flag:
                    self.ui.LBL_of_data_is_ready_in_PBT_page.setText(
                        texts.MESSEGES["Customized Data is ready"][self.language],
                        +data_report,
                    )
                else:

                    self.ui.LBL_of_data_is_ready_in_PBT_page.setText(
                        texts.MESSEGES["Data_Is_Ready"][self.language] + data_report
                    )
            else:
                self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedWidth(175)
                self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedHeight(16)
                if use_customized_flag:
                    self.ui.LBL_of_data_is_ready_in_PBT_page.setText(
                        texts.MESSEGES["Customized Data is not ready"][self.language]
                    )
                else:
                    self.ui.LBL_of_data_is_ready_in_PBT_page.setText(
                        texts.MESSEGES["Data_Is_Not_Ready"][self.language]
                    )

        else:
            self.ui.set_warning(
                texts.ERORS["BUILD_BINARYLIST_SLIDER_ERROR"][self.language],
                "binarylist",
                level=3,
            )

    def set_pred_each_path(self, value, summaries):

        self.ui.LBL_of_evalution_of_binary_model_in_PBT_page.setText(summaries[0])
        self.ui.LBL_of_evalution_of_classification_model_in_PBT_page.setText(
            summaries[1]
        )

        # hide labels of task of evalution
        # self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedWidth(0)
        # self.ui.LBL_of_data_is_ready_in_PBT_page.setFixedHeight(0)
        # self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedWidth(0)
        # self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedHeight(0)

        # after finishing progress,the progressBar will hide
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(0)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(0)

        self.ui.BTN_next_original_image_in_PBT_page.setEnabled(True)
        self.ui.BTN_prev_original_image_in_PBT_page.setEnabled(True)

        # update slider
        self.pred_each_path = value
        self.update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
            predict_eval=self.pred_each_path
        )

    def set_signal_from_evaluate_thread(self, percentage):
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(percentage)

    def evaluate_model_on_selected_model(self):
        # ______________________pre task start:
        # self.load_binary_images_list_in_PBT_load_dataset_page()
        # self.set_pipline()
        # ______________________pre task end.

        # _______________creat PIPLINE OBJ
        dataset_path = os.path.dirname(os.path.dirname(self.path_list[0]))
        pipline_name = self.pipline_OBJ.get(key=pipelines.PIPELINE_NAME)

        """temporary"""
        pipline_name = "JACK"

        self.ds.creat_folder_structure_of_wrong_predict_images(
            pipline_name=pipline_name
        )
        self.path_of_mask_prediction_with_current_pipline = os.path.join(
            dataset_path, "pred_of_" + pipline_name
        )
        self.ds.__creat_path__(self.path_of_mask_prediction_with_current_pipline)
        # code....
        # _______________creat PIPLINE OBJ

        # display progressBar of progress of evaluating  dataset
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(0)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(150)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(23)

        # Threading___________________
        self.evaluation_thread = QThread()
        self.evaluation = evaluation_worker()
        self.evaluation.set_params(
            paths=self.path_list,
            binary_model=self.b_model,
            classification_model=self.c_model,
            ds=self.ds,
            split_size=self.split_size,
            classes_num=self.classes_num,
            path_of_mask_prediction_with_current_pipline=self.path_of_mask_prediction_with_current_pipline,
            pipline_OBJ=self.pipline_OBJ,
        )

        self.evaluation.moveToThread(self.evaluation_thread)
        self.evaluation_thread.started.connect(self.evaluation.evaluate)
        self.evaluation.finished.connect(self.evaluation_thread.quit)
        self.evaluation.finished.connect(self.evaluation.deleteLater)
        self.evaluation_thread.finished.connect(self.evaluation_thread.deleteLater)
        self.evaluation.progress.connect(self.set_pred_each_path)
        self.evaluation.pgb_bar_signal.connect(self.set_signal_from_evaluate_thread)
        self.evaluation_thread.start()

        self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(False)
        self.evaluation_thread.finished.connect(
            lambda: self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(True)
        )

    # ______________________________________________________________________________________________________________________

    def set_pipline_of_model(self, id):
        if id == 1:
            self.b_model = self.ModelsCreation.b_model
            self.split_size = self.b_model.layers[0].output_shape[0][1:-1]
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(50)
        elif id == 2:
            self.l_model = self.ModelsCreation.l_model
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(70)
        elif id == 3:
            self.c_model = self.ModelsCreation.c_model
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(95)
        elif id == 4:
            self.pipline_OBJ = self.ModelsCreation.pipline_OBJ
            self.classes_num = self.ModelsCreation.classes_num
            # self.split_size=self.ModelsCreation.split_size
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(100)

            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(0)
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(0)

            self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedWidth(150)
            self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedHeight(16)
            self.ui.LBL_of_pipline_is_ready_in_PBT_page.setText(
                texts.MESSEGES["Pipline_Is_Ready"][self.language].format(
                    self.pipline_OBJ.get(key=pipelines.PIPELINE_NAME)
                )
            )
        else:
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(0)
            self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(0)
            self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedWidth(150)
            self.ui.LBL_of_pipline_is_ready_in_PBT_page.setFixedHeight(16)
            self.ui.LBL_of_pipline_is_ready_in_PBT_page.setText(
                texts.MESSEGES["Pipline_Is_Not_Ready"][self.language]
            )

    def set_pipline(self):

        # ______________________pre task start:
        self.load_binary_images_list_in_PBT_load_dataset_page()
        # ______________________pre task end.

        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setValue(0)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedWidth(151)
        self.ui.pgbar_of_pipiline_ready_in_PBT_page.setFixedHeight(23)

        # CREAT PIPLINE OBJ:
        pipline_name = self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.currentText()
        # """temporary"""
        # pipline_name='asdwd'
        # """temporary"""

        # Threading___________________
        self.ModelsCreation_thread = QThread()
        self.ModelsCreation = ModelsCreation_worker()
        self.ModelsCreation.set_params(
            login_user_name=self.login_user_name,
            db=self.db,
            language=self.language,
            pipline_name=pipline_name,
        )

        self.ModelsCreation.moveToThread(self.ModelsCreation_thread)
        self.ModelsCreation_thread.started.connect(self.ModelsCreation.set_pipline)
        self.ModelsCreation.finished.connect(self.ModelsCreation_thread.quit)
        self.ModelsCreation.finished.connect(self.ModelsCreation.deleteLater)
        self.ModelsCreation_thread.finished.connect(
            self.ModelsCreation_thread.deleteLater
        )

        self.ModelsCreation.model_creation_signal.connect(self.set_pipline_of_model)
        self.ModelsCreation_thread.start()

        self.ui.BTN_set_pipline_in_PBT_page.setEnabled(False)
        self.ModelsCreation_thread.finished.connect(
            lambda: self.ui.BTN_set_pipline_in_PBT_page.setEnabled(True)
        )

    # ____________JJ ZONE STOP
    # _________________________________________________________________________________________________
    # _________________________________________________________________________________________________
    # binary-list page functions
    # load binary images list
    def load_binary_images_list(self):
        """this function is used to show datasets images on binarylist page"""

        if self.binarylist_sliders_check[0] and self.binarylist_sliders_check[1]:
            # get selected datasets from ui
            res, datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
            if not res:
                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["database_get_datasets_failed"][
                        self.ui.language
                    ],
                    level=3,
                )

            selected_datasets = dataset.get_selected_datasets(
                ui_obj=self.ui, datasets_list=datasets_list, is_binarylist=True
            )

            if len(selected_datasets) == 0:
                self.ui.set_warning(
                    texts.WARNINGS["SELECT_NO_DATASET"][self.language],
                    "binarylist",
                    level=2,
                )
                return

            # get image/annots list related to defect
            # get image pathes
            (
                perfect_check,
                perfect_image_pathes,
                defect_check,
                defect_image_pathes,
                defect_annot_pathes,
                binary_count,
            ) = binary_list_funcs.get_binarylist_image_pathes_list(
                ds_obj=self.ds, dataset_pathes=selected_datasets
            )
            # validation
            if not perfect_check and not defect_check:
                self.ui.set_warning(
                    texts.MESSEGES["NO_IMAGE_AVAILABLE_IN_DATASET"][self.language],
                    "binarylist",
                    level=2,
                )
            else:
                # msg
                self.ui.set_warning(
                    texts.MESSEGES["LOAD_IMAGES_DATASETS"][self.language],
                    "binarylist",
                    level=1,
                )

            # create list object
            # perfect dir
            if perfect_check:
                self.binary_image_list.add(
                    mylist=perfect_image_pathes,
                    name=binary_list_funcs.image_list_object_names["perfect"],
                )
                # create next and prev funcs
                self.perfect_image_list_next_func = (
                    self.binary_image_list.build_next_func(
                        name=binary_list_funcs.image_list_object_names["perfect"]
                    )
                )
                self.perfect_image_list_prev_func = (
                    self.binary_image_list.build_prev_func(
                        name=binary_list_funcs.image_list_object_names["perfect"]
                    )
                )

                # connect next and prev buttons to funcs
                self.ui.binary_list_perfect_prev_btn.setEnabled(True)
                self.ui.binary_list_perfect_next_btn.setEnabled(True)
                self.update_binary_images_on_ui()

            else:
                self.binary_image_list.add(
                    mylist=perfect_image_pathes,
                    name=binary_list_funcs.image_list_object_names["perfect"],
                )
                # create next and prev funcs
                self.perfect_image_list_next_func = (
                    self.binary_image_list.build_next_func(
                        name=binary_list_funcs.image_list_object_names["perfect"]
                    )
                )
                self.perfect_image_list_prev_func = (
                    self.binary_image_list.build_prev_func(
                        name=binary_list_funcs.image_list_object_names["perfect"]
                    )
                )

                # connect next and prev buttons to funcs
                self.ui.binary_list_perfect_prev_btn.setEnabled(False)
                self.ui.binary_list_perfect_next_btn.setEnabled(False)
                self.update_binary_images_on_ui()

            # defect
            if defect_check:
                self.binary_image_list.add(
                    mylist=defect_image_pathes,
                    mylist_annots=defect_annot_pathes,
                    name=binary_list_funcs.image_list_object_names["defect"],
                )
                # create next and prev funcs
                self.defect_image_list_next_func = (
                    self.binary_image_list.build_next_func(
                        name=binary_list_funcs.image_list_object_names["defect"]
                    )
                )
                self.defect_image_list_prev_func = (
                    self.binary_image_list.build_prev_func(
                        name=binary_list_funcs.image_list_object_names["defect"]
                    )
                )
                # connect next and prev buttons to funcs
                self.ui.binary_list_defect_prev_btn.setEnabled(True)
                self.ui.binary_list_defect_next_btn.setEnabled(True)
                self.update_binary_images_on_ui(defect=True)

            else:
                self.binary_image_list.add(
                    mylist=defect_image_pathes,
                    mylist_annots=defect_annot_pathes,
                    name=binary_list_funcs.image_list_object_names["defect"],
                )
                # create next and prev funcs
                self.defect_image_list_next_func = (
                    self.binary_image_list.build_next_func(
                        name=binary_list_funcs.image_list_object_names["defect"]
                    )
                )
                self.defect_image_list_prev_func = (
                    self.binary_image_list.build_prev_func(
                        name=binary_list_funcs.image_list_object_names["defect"]
                    )
                )
                # connect next and prev buttons to funcs
                self.ui.binary_list_defect_prev_btn.setEnabled(False)
                self.ui.binary_list_defect_next_btn.setEnabled(False)
                self.update_binary_images_on_ui(defect=True)

            # update pie chart
            chart_funcs.update_binarylist_piechart(
                ui_obj=self.ui, binary_len=binary_count
            )
            chart_funcs.update_binarylist_barchart(
                ui_obj=self.ui, binary_len=binary_count
            )

        # error in building image sliders
        else:
            self.ui.set_warning(
                texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"][self.language],
                "binarylist",
                texts_codes.SubTypes['BUILD_BINARYLIST_SLIDER_ERROR'],
                level=3,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"]["en"], code=texts_codes.SubTypes['BUILD_BINARYLIST_SLIDER_ERROR'], level=4
            )

    # update slider images
    def update_binary_images_on_ui(self, defect=False, prevornext="False"):
        """this function is used to set/update dataset images on binarylist page sliders

        :param defect: boolean determining whether to set defect images, defaults to False
        :type defect: bool, optional
        :param prevornext: boolean determining whether to get next/prev images for slider, defaults to 'False'
        :type prevornext: str, optional
        """

        try:
            # next or prev on list
            if prevornext == "next":
                if not defect:
                    self.perfect_image_list_next_func()
                else:
                    self.defect_image_list_next_func()

            # prev
            elif prevornext == "prev":
                if not defect:
                    self.perfect_image_list_prev_func()
                else:
                    self.defect_image_list_prev_func()

            # get curent image list to set to UI
            if not defect:
                current_image_list = self.binary_image_list.get_n_current(
                    name=binary_list_funcs.image_list_object_names["perfect"]
                )
                current_annot_list = ["" for i in range(len(current_image_list))]

            else:
                (
                    current_image_list,
                    current_annot_list,
                ) = self.binary_image_list.get_n_current(
                    name=binary_list_funcs.image_list_object_names["defect"],
                    get_annots=True,
                )

            # set/update images on UI
            if not defect:
                res = binary_list_funcs.set_image_to_ui_slider_full_path(
                    ui_obj=self.ui,
                    image_path_list=current_image_list,
                    annot_path_list=current_annot_list,
                    prefix=binary_list_funcs.widjet_prefixes["perfect"],
                    image_per_row=binary_list_funcs.n_images_per_row,
                )
            else:
                res = binary_list_funcs.set_image_to_ui_slider_full_path(
                    ui_obj=self.ui,
                    image_path_list=current_image_list,
                    annot_path_list=current_annot_list,
                    prefix=binary_list_funcs.widjet_prefixes["defect"],
                    image_per_row=binary_list_funcs.n_images_per_row,
                )

            # validate
            if not res:
                self.ui.set_warning(
                    texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"][self.language],
                    "binarylist",
                    texts_codes.SubTypes['READ_BINARYLIST_IMAGES_ERROR'],
                    level=3,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"]["en"], code=texts_codes.SubTypes['READ_BINARYLIST_IMAGES_ERROR'], level=4
                )

        except Exception as e:
            self.ui.set_warning(
                texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"][self.language],
                "binarylist",
                texts_codes.SubTypes['READ_BINARYLIST_IMAGES_ERROR'],
                level=3,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"]["en"], code=texts_codes.SubTypes['READ_BINARYLIST_IMAGES_ERROR'], level=5
            )

    # ------------------------------------------------------------------------------------------------------------------------
    # localization-model history page functions
    def refresh_localization_models_table_onevent(self):
        """this function is used to refresh localization models table"""

        self.lmodel_tabel_itr = 1  # reset page number to first (1)
        self.ui.localization_tabel_page.setText(str(self.lmodel_tabel_itr))

        self.refresh_localization_models_table(get_count=True)
        self.refresh_localization_models_table()
        self.ui.clear_localization_filters_fields()
        self.lfilter_mode = False
        self.ui.set_warning(
            texts.MESSEGES["REFRESH_TABLE"][self.language],
            "localization_model_history",
            level=1,
        )

    def refresh_localization_models_table(
        self, nextorprev=False, get_count=False, filter_mode=False
    ):
        """this function is used to refresh/update localization models table on UI

        :param nextorprev: boolean determining if get next/prev page of records on table, defaults to False
        :type nextorprev: bool, optional
        :param get_count: boolean determining whether to get count of records in table in database, defaults to False
        :type get_count: bool, optional
        :param filter_mode: boolean determining if in table filter mode, defaults to False
        :type filter_mode: bool, optional
        :return:
            get_count==True: None
            get_count==False: boolean determining if done
        :rtype: _type_
        """

        if get_count:
            try:
                (
                    res,
                    self.lmodel_count,
                ) = localization_model_funcs.get_localization_models_from_db(
                    db_obj=self.db, count=get_count
                )
                self.lmodel_count = self.lmodel_count[0]["count(*)"]

                # validation
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_lmodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )
                #
                self.localization_model_tabel_nextorprev(check=True)
                return
            except:
                return
        # load filterd models
        if filter_mode:
            # reset table page number to first (1)
            self.lmodel_tabel_itr = 1
            self.ui.localization_tabel_page.setText(str(self.lmodel_tabel_itr))

            res = self.filter_localization_models(filter_signal=True, count=True)

            if res[0]:
                self.lmodel_count = res[1][0]["count(*)"]
                self.localization_model_tabel_nextorprev(check=True)

                res = self.filter_localization_models(filter_signal=True)

                if res[0]:
                    lmodels_list = res[1]
                else:
                    self.refresh_localization_models_table(get_count=True)
                    (
                        res,
                        lmodels_list,
                    ) = localization_model_funcs.get_localization_models_from_db(
                        db_obj=self.db
                    )
                    if not res:
                        self.ui.notif_manager.append_new_notif(
                            message=texts.ERRORS["database_get_lmodels_failed"][
                                self.ui.language
                            ],
                            level=3,
                        )

            else:
                self.refresh_localization_models_table(get_count=True)
                (
                    res,
                    lmodels_list,
                ) = localization_model_funcs.get_localization_models_from_db(
                    db_obj=self.db
                )
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_lmodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )

        else:
            if not nextorprev:
                (
                    res,
                    lmodels_list,
                ) = localization_model_funcs.get_localization_models_from_db(
                    db_obj=self.db
                )
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_lmodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )

            else:
                if not self.lfilter_mode:
                    (
                        res,
                        lmodels_list,
                    ) = localization_model_funcs.get_localization_models_from_db(
                        db_obj=self.db,
                        limit_size=localization_model_funcs.localization_table_nrows,
                        offset=(self.lmodel_tabel_itr - 1)
                        * localization_model_funcs.localization_table_nrows,
                    )
                    if not res:
                        self.ui.notif_manager.append_new_notif(
                            message=texts.ERRORS["database_get_lmodels_failed"][
                                self.ui.language
                            ],
                            level=3,
                        )

                else:
                    res = self.filter_localization_models(
                        limit_size=localization_model_funcs.localization_table_nrows,
                        offset=(self.lmodel_tabel_itr - 1)
                        * localization_model_funcs.localization_table_nrows,
                    )
                    lmodels_list = res[1]

        if len(lmodels_list) == 0 and nextorprev:
            return False

        # set returned models to UI table
        else:
            localization_model_funcs.set_lmodels_on_ui_tabel(
                ui_obj=self.ui, lmodels_list=lmodels_list
            )
            return True

    # next and prev buttons for localization models table functionality
    def localization_model_tabel_nextorprev(self, next=True, check=False):
        """this function is used to get next/prev page for localization models table

        :param next: boolean determining whether to get next page, defaults to True
        :type next: bool, optional
        :param check: _description_, defaults to False
        :type check: bool, optional
        """
        if check:
            page_max = int(
                math.ceil(
                    self.lmodel_count
                    / localization_model_funcs.localization_table_nrows
                )
            )

            if self.lmodel_tabel_itr >= page_max:
                self.ui.localization_tabel_next.setEnabled(False)
            else:
                self.ui.localization_tabel_next.setEnabled(True)
            #
            if self.lmodel_tabel_itr > 1:
                self.ui.localization_tabel_prev.setEnabled(True)
            else:
                self.ui.localization_tabel_prev.setEnabled(False)

            return

        #
        if next:
            self.lmodel_tabel_itr += 1

        elif self.lmodel_tabel_itr > 1:
            self.lmodel_tabel_itr -= 1

        #
        res = self.refresh_localization_models_table(nextorprev=True)
        self.localization_model_tabel_nextorprev(check=True)
        self.ui.localization_tabel_page.setText(str(self.lmodel_tabel_itr))

    # filter function for localization models
    def filter_localization_models(
        self,
        limit_size=localization_model_funcs.localization_table_nrows,
        offset=0,
        filter_signal=False,
        count=False,
    ):
        """this function is used to filter localization models given filter params on UI

        :param limit_size: n table rows in database to return, defaults to localization_model_funcs.localization_table_nrows
        :type limit_size: int, optional
        :param offset: starting row index in table to return n next rows, defaults to 0
        :type offset: int, optional
        :param filter_signal: boolean determining wheter to get/update filter params from UI, defaults to False
        :type filter_signal: bool, optional
        :param count: boolean determinig whether to get count of results, defaults to False
        :type count: bool, optional
        :return:
            result: boolean determining id done
            filtered_binary_models: list of dicts
        :rtype: _type_
        """

        if filter_signal:
            self.filter_params = (
                localization_model_funcs.get_localization_model_filter_info_from_ui(
                    ui_obj=self.ui
                )
            )
        #
        res = localization_model_funcs.get_filtered_localization_models_from_db(
            ui_obj=self.ui,
            db_obj=self.db,
            filter_params=self.filter_params,
            limit_size=limit_size,
            offset=offset,
            count=count,
        )

        if res[0] == "error":
            self.lfilter_mode = False
            return False, res[1]

        if res[0] == "all":
            self.lfilter_mode = False
            return False, res[1]

        else:
            self.lfilter_mode = True
            self.ui.set_warning(
                texts.MESSEGES["FILTERED_RESAULTS_SUCCUSSFULL"][self.language],
                "localization_model_history",
                level=1,
            )
            return True, res[1]

    # clear filters for localization models
    def clear_localization_filters(self):
        """this function is used tp clear filters for localization models list"""

        self.lfilter_mode = False  # diactive filter mode
        # reset table page number
        self.lmodel_tabel_itr = 1
        self.ui.localization_tabel_page.setText(str(self.lmodel_tabel_itr))
        #
        self.refresh_localization_models_table(get_count=True)
        self.refresh_localization_models_table()
        self.ui.clear_localization_filters_fields()
        self.ui.set_warning(
            texts.MESSEGES["FILTERED_RESAULTS_CLEAR"][self.language],
            "localization_model_history",
            level=1,
        )

    def update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
        self, prevornext="False", predict_eval=None
    ):
        # next or prev on list
        if prevornext == "next":
            self.original_image_list_next_func()
        # prev
        elif prevornext == "prev":
            self.original_image_list_prev_func()

        # get curent image list to set to UI
        current_image_list = self.original_and_evaluated_image_in_PBT.get_n_current(
            name="original"
        )
        current_mask_list = []  # temp
        res = binary_list_funcs.set_image_to_ui_slider_eidted_version(
            ui_obj=self.ui,
            sub_directory="xxx",
            annot_sub_direcotory="xxxx",
            image_path_list=current_image_list,
            mask_path_list=current_mask_list,
            predict_eval=predict_eval,
        )

        # # validate
        # if not res:
        #     self.ui.set_warning(
        #         texts.ERORS["READ_BINARYLIST_IMAGES_ERROR"][self.language],
        #         "binarylist",
        #         level=3,
        #     )

    # classification page
    # ------------------------------------------------------------------------------------------------------------------------
    # get defects from database and apply to defects table
    def refresh_classes_table(self):
        """this function is used to refresh defects tables in UI"""

        res, defects_list = classification_list_funcs.get_defects_from_db(
            db_obj=self.db
        )
        # validate
        if not res:
            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["database_get_defects_failed"][self.ui.language],
                level=3,
            )

        # translate defect group ids to names
        defects_list = classification_list_funcs.change_defect_group_id_to_name(
            db_obj=self.db, defects_list=defects_list
        )

        classification_list_funcs.set_defects_on_ui(
            ui_obj=self.ui, defects_list=defects_list
        )
        classification_list_funcs.set_defects_on_train_ui(
            ui_obj=self.ui, defects_list=defects_list
        )
        classification_model_funcs.set_defects_on_filter_ui(
            ui_obj=self.ui, defects_list=defects_list
        )

    # get datasets from database and apply to datasets table
    def refresh_datasets_table(self, is_binarylist=False, PBT_page=False):
        """this function is used to refresh datasets table in binary or classification list

        :param is_binarylist: boolean determining whether to refresh binarylist dataset table, defaults to False
        :type is_binarylist: bool, optional
        """

        # get dataset
        # read all datasets in table (must update)
        res, datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
        if not res:
            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["database_get_datasets_failed"][self.ui.language],
                level=3,
            )

        if PBT_page:
            self.PBT_option_list = dataset.set_datasets_on_ui(
                ui_obj=self.ui,
                datasets_list=datasets_list,
                current_user=self.login_user_name,
                default_dataset=self.default_dataset_user,
                is_binarylist=is_binarylist,
                PBT_page=True,
            )
            return
        # show on UI
        if not is_binarylist:
            # classlist
            dataset.set_datasets_on_ui(
                ui_obj=self.ui,
                datasets_list=datasets_list,
                current_user=self.login_user_name,
                default_dataset=self.default_dataset_user,
            )

        else:
            # binarylist
            dataset.set_datasets_on_ui(
                ui_obj=self.ui,
                datasets_list=datasets_list,
                current_user=self.login_user_name,
                default_dataset=self.default_dataset_user,
                is_binarylist=is_binarylist,
            )
            self.load_binary_images_list()

    # show class related images on UI
    def show_class_related_images(self):
        """this funcion is used to show class (defect) related images on ui classififcationlist slider"""

        # get selected defects from UI
        res, defects_list = classification_list_funcs.get_defects_from_db(
            db_obj=self.db
        )
        selected_defects = classification_list_funcs.get_selected_defects(
            ui_obj=self.ui
        )

        if len(selected_defects) > 1:
            self.ui.set_warning(
                texts.WARNINGS["SELECT_MORE_THAN_ONE_DEFECT_CLASS"][self.language],
                "classlist_msg_label",
                level=2,
            )

        elif len(selected_defects) == 0:
            self.ui.set_warning(
                texts.WARNINGS["SELECT_NO_DEFECT_CLASS"][self.language],
                "classlist_msg_label",
                level=2,
            )

        else:
            # get selected datasets from ui
            res, datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
            if not res:
                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["database_get_datasets_failed"][
                        self.ui.language
                    ],
                    level=3,
                )

            selected_datasets = dataset.get_selected_datasets(
                ui_obj=self.ui, datasets_list=datasets_list
            )
            if len(selected_datasets) == 0:
                self.ui.set_warning(
                    texts.WARNINGS["SELECT_NO_DATASET"][self.language],
                    "classlist_msg_label",
                    level=2,
                )
                return

            # get image/annots list related to defect
            (
                annotation_list,
                image_list,
                binary_count,
                classes_count,
            ) = classification_list_funcs.load_images_related_to_defect(
                ui_obj=self.ui,
                datasets_list=selected_datasets,
                defect_id=selected_defects[0],
            )

            # create list object
            self.classification_image_list.add(
                mylist=image_list,
                mylist_annots=annotation_list,
                name=self.classification_image_list_name,
            )
            # create next and prev funcs
            self.classification_image_list_next_func = (
                self.classification_image_list.build_next_func(
                    name=self.classification_image_list_name
                )
            )
            self.classification_image_list_prev_func = (
                self.classification_image_list.build_prev_func(
                    name=self.classification_image_list_name
                )
            )
            #
            self.update_classlist_images_on_ui()

            # no images available
            if len(annotation_list) == 0 and len(image_list) == 0:
                # msg
                self.ui.set_warning(
                    texts.MESSEGES["NO_IMAGE_AVAILABLE_WITH_DEFECT"][self.language],
                    "classlist_msg_label",
                    level=2,
                )
                # disable next/prev/buttons
                self.ui.classlist_prev_btn.setEnabled(False)
                self.ui.classlist_next_btn.setEnabled(False)

            else:
                # msg
                self.ui.set_warning(
                    texts.MESSEGES["LOAD_IMAGES_WITH_DEFECT"][self.language],
                    "classlist_msg_label",
                    texts_codes.SubTypes['LOAD_IMAGES_WITH_DEFECT'],
                    level=1,
                )
                self.ui.logger.create_new_log(
                    message=texts.MESSEGES["LOAD_IMAGES_WITH_DEFECT"]["en"], code=texts_codes.SubTypes['LOAD_IMAGES_WITH_DEFECT'], level=1
                )
                # disable next/prev/buttons
                self.ui.classlist_prev_btn.setEnabled(True)
                self.ui.classlist_next_btn.setEnabled(True)

            # update pie chart
            chart_funcs.update_classlist_piechart(
                ui_obj=self.ui,
                binary_len=binary_count,
                classes_len=classes_count,
                classes_list=defects_list,
            )

    # update slider images
    def update_classlist_images_on_ui(self, prevornext="False"):
        """this function is used to update classification images list on UI slider

        :param prevornext: boolean determining whether to get next/prev page, defaults to 'False'
        :type prevornext: str, optional
        """

        # next or prev on list
        if prevornext == "next":
            self.classification_image_list_next_func()
        # prev
        elif prevornext == "prev":
            self.classification_image_list_prev_func()

        # get curent image list to set to UI
        (
            current_image_list,
            current_annots_list,
        ) = self.classification_image_list.get_n_current(
            name=self.classification_image_list_name, get_annots=True
        )

        # set/update images on UI
        res = binary_list_funcs.set_image_to_ui_slider_full_path(
            ui_obj=self.ui,
            image_path_list=current_image_list,
            annot_path_list=current_annots_list,
            prefix=self.classification_image_list_name,
            image_per_row=binary_list_funcs.n_images_per_row_classlist,
        )

    # check classification params
    def check_classification_train_params(self):
        """this function is used to check/validate classification training parameters"""

        # get train params from UI
        cls_parms = self.ui.get_classification_parms()
        selected_defects = classification_list_funcs.get_selected_defects_for_train(
            ui_obj=self.ui
        )

        #
        if len(selected_defects) == 0:
            self.ui.show_mesagges(
                self.ui.classification_train_msg_label,
                texts.WARNINGS["no_defect_class_selected"][self.ui.language],
                color=colors_pallete.failed_red,
            )

        else:
            cls_parms += [selected_defects]

    # pie chart funcs
    def create_classlist_pie_chart(self):
        """this function is used to create needed piecharts on UI"""

        try:

            # classlist page
            chart_funcs.create_classlist_piechart_on_ui(
                ui_obj=self.ui,
                frame_obj_binary=self.ui.binary_chart_frame,
                frame_obj_classlist=self.ui.classlist_chart_frame,
            )

            # binarylist page
            chart_funcs.create_binarylist_piechart_on_ui(
                ui_obj=self.ui, frame_obj_binary=self.ui.binarylist_chart_frame
            )
            chart_funcs.create_binarylist_barchart_on_ui(
                ui_obj=self.ui, frame_obj_binary=self.ui.binarylist_chart_frame_2
            )

            # userprofile page
            chart_funcs.create_userprofile_piechart_on_ui(
                ui_obj=self.ui, frame_obj_binary=self.ui.binary_chart_frame_profile
            )
            chart_funcs.create_userprofile_barchart_on_ui(
                ui_obj=self.ui, frame_obj_binary=self.ui.classlist_chart_frame_profile
            )

            # labal page
            chart_funcs.create_label_piechart_on_ui(
                ui_obj=self.ui, frame_obj_binary=self.ui.binary_chart_frame_label
            )

        except Exception as e:
            self.ui.logger.create_new_log(
                message=texts.ERRORS["piechart_create_failed"]["en"], code=texts_codes.SubTypes['piechart_create_failed'], level=5
            )

    # _________________________________________________________________________________________________
    # classification-model history page functions
    def refresh_cls_models_table_onevent(self):
        """this function is used to refresh/reset classification model history table"""

        # reset table page to 1
        self.clsmodel_tabel_itr = 1
        self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))

        self.refresh_cls_models_table(get_count=True)
        self.refresh_cls_models_table()
        self.cls_filter_mode = False
        self.ui.set_warning(
            texts.MESSEGES["REFRESH_TABLE"][self.language],
            "classification_model_history",
            level=1,
        )

    def refresh_cls_models_table(
        self, nextorprev=False, get_count=False, filter_mode=False
    ):
        """this function is used to refresh/update classification models table, on next or prev page events or filtering mode

        :param nextorprev: boolean determining whether to get next/prev page, defaults to False
        :type nextorprev: bool, optional
        :param get_count: boolean determining whether to get count of table records in daabase, defaults to False
        :type get_count: bool, optional
        :param filter_mode: boolean determinnig whether to get filtering records from database, defaults to False
        :type filter_mode: bool, optional
        :return: _description_
        :rtype: _type_
        """

        if get_count:
            (
                ret,
                self.clsmodel_count,
            ) = classification_model_funcs.get_cls_models_from_db(
                ui_obj=self.ui, db_obj=self.db, count=get_count
            )
            self.clsmodel_count = self.clsmodel_count[0]["count(*)"]

            self.cls_model_tabel_nextorprev(check=True)
            return

        # load filterd models
        if filter_mode:
            # reset table to page 1
            self.clsmodel_tabel_itr = 1
            self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))

            res = self.filter_cls_models(filter_signal=True, count=True)

            if res[0]:
                self.clsmodel_count = res[1][0]["count(*)"]
                self.cls_model_tabel_nextorprev(check=True)

                res = self.filter_cls_models(filter_signal=True)
                if res[0]:
                    clsmodels_list = res[1]
                else:
                    self.refresh_cls_models_table(get_count=True)
                    (
                        ret,
                        clsmodels_list,
                    ) = classification_model_funcs.get_cls_models_from_db(
                        ui_obj=self.ui, db_obj=self.db
                    )

            else:
                self.refresh_cls_models_table(get_count=True)
                ret, clsmodels_list = classification_model_funcs.get_cls_models_from_db(
                    ui_obj=self.ui, db_obj=self.db
                )

        else:
            if not nextorprev:
                ret, clsmodels_list = classification_model_funcs.get_cls_models_from_db(
                    ui_obj=self.ui, db_obj=self.db
                )
            else:
                if not self.cls_filter_mode:
                    (
                        ret,
                        clsmodels_list,
                    ) = classification_model_funcs.get_cls_models_from_db(
                        ui_obj=self.ui,
                        db_obj=self.db,
                        limit_size=classification_model_funcs.cls_table_nrows,
                        offset=(self.clsmodel_tabel_itr - 1)
                        * classification_model_funcs.cls_table_nrows,
                    )
                else:
                    res = self.filter_cls_models(
                        limit_size=classification_model_funcs.cls_table_nrows,
                        offset=(self.clsmodel_tabel_itr - 1)
                        * classification_model_funcs.cls_table_nrows,
                    )
                    clsmodels_list = res[1]

        if len(clsmodels_list) == 0 and nextorprev:
            return False

        # set returned models to UI table
        else:
            classification_model_funcs.set_clsmodels_on_ui_tabel(
                ui_obj=self.ui, models_list=clsmodels_list
            )
            return True

    # next and prev buttons for binary models table functionality
    def cls_model_tabel_nextorprev(self, next=True, check=False):
        """this function is used to update classification models table to next or prev page

        :param next: boolean determining whether to get next or prev page, defaults to True
        :type next: bool, optional
        :param check: _description_, defaults to False
        :type check: bool, optional
        """
        if check:
            page_max = int(
                math.ceil(
                    self.clsmodel_count / classification_model_funcs.cls_table_nrows
                )
            )
            if self.clsmodel_tabel_itr >= page_max:
                self.ui.cls_tabel_next.setEnabled(False)
            else:
                self.ui.cls_tabel_next.setEnabled(True)
            #
            if self.clsmodel_tabel_itr > 1:
                self.ui.cls_tabel_prev.setEnabled(True)
            else:
                self.ui.cls_tabel_prev.setEnabled(False)

            return
        #
        if next:
            self.clsmodel_tabel_itr += 1

        elif self.clsmodel_tabel_itr > 1:
            self.clsmodel_tabel_itr -= 1
        #
        res = self.refresh_cls_models_table(nextorprev=True)
        self.cls_model_tabel_nextorprev(check=True)
        self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))

    # filter function for binary models
    def filter_cls_models(
        self,
        limit_size=classification_model_funcs.cls_table_nrows,
        offset=0,
        filter_signal=False,
        count=False,
    ):
        """this function is used to get filtered cls models given filtering params from UI

        :param limit_size: determining number of returning rows from database, defaults to classification_model_funcs.cls_table_nrows
        :type limit_size: int, optional
        :param offset: starting row index to return n next rows of table, defaults to 0
        :type offset: int, optional
        :param filter_signal: boolean determining whether to refresh/reset filter params from UI, defaults to False
        :type filter_signal: bool, optional
        :param count: boolean determining whether to get count of filtered rows, defaults to False
        :type count: bool, optional
        :return:
            result: boolean determining whether is done
            filtered_params:
        :rtype: _type_
        """

        if filter_signal:
            self.cls_filter_params = (
                classification_model_funcs.get_cls_model_filter_info_from_ui(
                    ui_obj=self.ui
                )
            )
        #
        res = classification_model_funcs.get_filtered_cls_models_from_db(
            ui_obj=self.ui,
            db_obj=self.db,
            filter_params=self.cls_filter_params,
            limit_size=limit_size,
            offset=offset,
            count=count,
        )

        if res[0] == "error":
            self.cls_filter_mode = False
            return False, res[1]

        if res[0] == "all":
            self.cls_filter_mode = False
            return False, res[1]

        else:
            self.cls_filter_mode = True
            self.ui.set_warning(
                texts.MESSEGES["FILTERED_RESAULTS_SUCCUSSFULL"][self.language],
                "classification_model_history",
                texts_codes.SubTypes['FILTERED_RESAULTS_SUCCUSSFULL'],
                level=1,
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["FILTERED_RESAULTS_SUCCUSSFULL"]["en"], code=texts_codes.SubTypes['FILTERED_RESAULTS_SUCCUSSFULL'], level=1
            )
            return True, res[1]

    # clear filters for binary models
    def clear_filters_cls(self):
        """this function is used to clear filters of classification models table"""

        self.cls_filter_mode = False

        # reset table page to 1
        self.clsmodel_tabel_itr = 1
        self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))

        self.refresh_cls_models_table(get_count=True)
        self.refresh_cls_models_table(get_count=True)
        self.refresh_cls_models_table()
        self.ui.set_warning(
            texts.MESSEGES["FILTERED_RESAULTS_CLEAR"][self.language],
            "classification_model_history",
            level=1,
        )

    # _____________________________________________________________________________________________________

    # _____________________________________________________________________________________________________

    def get_image(self):
        return self.img

    def create_mask_from_mask(self, img_path):
        labels = self.label_memory.get_label("mask", img_path)
        mask = np.zeros((self.img.shape[0], self.img.shape[1]))
        for lbl, cnt, line_thickness, point_thickness in labels:
            cv2.drawContours(mask, [cnt], 0, color=255, thickness=line_thickness)
            cv2.drawContours(mask, [cnt], 0, color=255, thickness=-1)
        return mask

    def create_Heatmap(self):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current(
            "selected_imgs_for_label"
        )
        img = Utils.read_image(img_path, "color")
        _, hm = SSI(img, heatmap=True)
        self.img = hm
        self.ui.set_image_label(self.ui.image, hm)
        self.ui.image.setScaledContents(True)
        self.scale = 1
        self.position = [0, 0]

    def image_processing_suggest(self):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current(
            "selected_imgs_for_label"
        )
        img = Utils.read_image(img_path, "color")
        res = SSI(img)
        self.img = res
        self.ui.set_image_label(self.ui.image, res)
        self.ui.image.setScaledContents(True)
        self.scale = 1
        self.position = [0, 0]

    def show_neighbours(self, state):
        if state == 2:
            self.ui.show_small_neighbouring()
        else:
            self.ui.close_small_neighbouring()

    def show_neighbours_labels(self, state):
        if state == 2:
            self.ui.update_neighbour_labels(True)
        else:
            self.ui.update_neighbour_labels(False)

    def maximize_neighbours(self, widget_name=""):
        if self.ui.sn:
            image = self.ui.sn.get_original_img()
            if image is not None:
                annt = self.ui.sn.get_img()
                self.ui.show_neighbouring(image, annt)

    def maximize_labeling_helps(self, widget_name=""):
        n = int(widget_name.split('_')[-1])
        self.ui.maximize_labeling_help_images(n)

    def load_settings(self):
        (
            lan, 
            font, 
            manual_plc,
            plc_update_time, 
            wind_duration, 
            automatic_wind, 
            auto_wind_intervals, 
            manual_cameras, 
            frame_rate, 
            live_update_time
        ) = self.db.load_settings()
        self.ui.set_settings(
            lan, 
            font, 
            manual_plc,
            plc_update_time, 
            wind_duration, 
            automatic_wind, 
            auto_wind_intervals, 
            manual_cameras, 
            frame_rate, 
            live_update_time
        )

    def set_language_font(self):
        lan = self.ui.combo_change_language.currentText()
        if lan == texts.Titles["persian"]["fa"] or lan == texts.Titles["persian"]["en"]:
            lan = texts.Titles["persian"]["en"]
        elif (
            lan == texts.Titles["english"]["fa"] or lan == texts.Titles["english"]["en"]
        ):
            lan = texts.Titles["english"]["en"]
        font = self.ui.fontComboBox.currentText()
        self.db.set_language_font(lan, font)

    def set_plc_parms(self):
        self.db.set_plc_params(self.ui.manual_plc,
                            self.ui.update_timer_plc,
                            self.ui.update_wind_plc,
                            self.ui.auto_wind,
                            self.ui.auto_wind_intervals        
                            )
        self.start_auto_wind()
        self.init_check_plc()

    def set_camera_parms(self):
        self.db.set_camera_params(self.ui.manual_camera,
                            self.ui.frame_rate,
                            self.ui.update_timer_live_frame,      
                            )

    # -----------------------------------------------------PLC setting -------------------------------------------------------

    def connect_plc(self):
        """
        this function is used to connect to plc

        Args: None

        Returns: None
        """

        # get plc ip
        ip = self.plc_ip
        # connect to plc
        self.my_plc = plc_managment.management(ip, ui_obj=self.ui)
        self.connection_status = self.my_plc.connection()
        # parms=self.db.load_plc_parms()
        # #print(parms)
        #
        if self.connection_status:
            self.retry_connecting_plc = 0
            self.ui.set_status_plc(mode=True)
            res = self.load_plc_parms()
            if not res:
                self.ui.set_warning(
                    texts.ERRORS['database_get_plc_params_failed'][self.ui.language], 
                    'camera_connection', 
                    texts_codes.SubTypes['database_get_plc_params_failed'], 
                    level=2)
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["database_get_plc_params_failed"]["en"],
                    code=texts_codes.SubTypes['database_get_plc_params_failed'],
                    level=3,
                )
                return
            else:
                # self.ui.show_mesagges(self.ui.plc_warnings, texts.MESSEGES['database_get_plc_params'][self.ui.language], level=0)

                self.ui.logger.create_new_log(
                    message=texts.MESSEGES["database_get_plc_params"]["en"], code=texts_codes.SubTypes['database_get_plc_params'], level=1
                )

            # self.ui.show_mesagges(self.ui.plc_warnings, texts.MESSEGES['plc_connection_apply'][self.ui.language], level=0)
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["plc_connection_apply"]["en"], code=texts_codes.SubTypes['plc_connection_apply'], level=1
            )
            self.plc_connection_status = True
            self.ui.disconnect_plc_btn.setEnabled(True)
            self.ui.connect_plc_btn.setEnabled(False)

        else:
            self.ui.set_status_plc(mode=False)
            # self.ui.show_mesagges(self.ui.plc_warnings, texts.ERRORS['plc_connection_apply_failed'][self.ui.language], level=2)
            self.ui.logger.create_new_log(
                message=texts.ERRORS["plc_connection_apply_failed"]["en"], code=texts_codes.SubTypes['plc_connection_apply_failed'], level=4
            )

            # self.connect_plc()
            if self.retry_connecting_plc < 10:
                self.retry_connecting_plc += 1
                QTimer().singleShot(1000,self.connect_plc)
                self.ui.set_status_plc(
                    auto=False,
                    text=texts.Titles["reconnect"][self.ui.language].format(
                        11 - self.retry_connecting_plc
                    ),
                )
            else:
                self.retry_connecting_plc = 0
                self.ui.set_status_plc(mode=False)
                self.ui.disconnect_plc_btn.setEnabled(False)
                self.ui.connect_plc_btn.setEnabled(True)

    def load_plc_parms(self):
        """
        this function is used to load plc params from database, and set to ui plc page

        Args: None

        Returns:
            resault: a boolean determining if params loaded from database
        """

        parms = self.db.load_plc_parms()

        if parms == None:
            return False
        self.pathes = parms
        self.dict_spec_pathes = plc_managment.set_pathes(self.pathes)

        self.up_high_threshold = self.my_plc.get_value(
            self.dict_spec_pathes["UpHighThreshold"]
        )
        self.up_low_threshold = self.my_plc.get_value(
            self.dict_spec_pathes["UpLowThreshold"]
        )
        self.down_high_threshold = self.my_plc.get_value(
            self.dict_spec_pathes["DownHighThreshold"]
        )
        self.down_low_threshold = self.my_plc.get_value(
            self.dict_spec_pathes["DownLowThreshold"]
        )
        # self.

        # #print('-'*50,self.up_high_threshold)
        # #print('88888888888888',self.dict_spec_pathes)

        # #print('parms',self.parms)
        return True

    def disconnect_plc(self, on_close=False, force_close=False):
        """
        this function is used to disconnect from plc

        Args:
            on_close (bool, optional): a boolean determining if function is called on app close. Defaults to False.
            force_close (bool, optional): a boolean determining to force close the plc (whenever plc is disconnected suddenly)
        """

        # force close the plc, this is for those times that plc is disconnecter by error
        if force_close:
            try:
                self.my_plc.disconnect()
            except:
                pass
            #
            self.timer_write_plc.stop()
            self.plc_connection_status = False
            del self.my_plc
            #
            # self.ui.show_mesagges(self.ui.plc_warnings, texts.ERRORS['plc_disconnected_by_error'][self.ui.language], level=2)
            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["plc_disconnected_by_error"][self.ui.language],
                level=3,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["plc_disconnected_by_error"]["en"], code=texts_codes.SubTypes['plc_disconnected_by_error'], level=4
            )
            #
            self.ui.disconnect_plc_btn.setEnabled(False)
            self.ui.connect_plc_btn.setEnabled(True)
            #
            # self.ui.plc_main_frame.setEnabled(False)

            return

        try:
            self.my_plc.disconnect()
            self.timer_write_plc.stop()
            self.plc_connection_status = False
            del self.my_plc
            #
            # self.ui.show_mesagges(self.ui.plc_warnings, texts.MESSEGES['plc_disconnected'][self.ui.language], level=0)
            self.ui.notif_manager.append_new_notif(
                message=texts.MESSEGES["plc_disconnected"][self.ui.language], level=1
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["plc_disconnected"]["en"], code=texts_codes.SubTypes['plc_disconnected'], level=1
            )
            #
            self.ui.disconnect_plc_btn.setEnabled(False)
            self.ui.connect_plc_btn.setEnabled(True)

        # failed to disconnect plc
        except:
            if not on_close:
                # self.ui.show_mesagges(self.ui.plc_warnings, texts.ERRORS['plc_disconnected_failed'][self.ui.language], level=2)
                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["plc_disconnected_failed"][self.ui.language],
                    level=3,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["plc_disconnected_failed"]["en"], code=texts_codes.SubTypes['plc_disconnected_failed'], level=3
                )

        #
        # self.ui.plc_main_frame.setEnabled(False)

    def set_plc_ip_to_ui(self):
        """
        this function is used to get plc ip from database and set to ui

        Args: None

        Returns: None
        """

        self.plc_ip = self.db.load_plc_ip()

        # failed to get ip from database
        if not self.plc_ip:
            self.ui.set_warning(
                    texts.ERRORS['database_get_plc_ip_failed'][self.ui.language], 
                    'camera_connection', 
                    texts_codes.SubTypes['database_get_plc_ip_failed'], 
                    level=2
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["database_get_plc_ip_failed"]["en"], code=texts_codes.SubTypes['database_get_plc_ip_failed'], level=4
            )
            return
        #
        else:
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["database_get_plc_ip"]["en"], code=texts_codes.SubTypes['database_get_plc_ip'], level=1
            )
            self.ui.set_plc_ip(self.plc_ip)

    def start_auto_wind(self):
        try:
            self.auto_wind_timer.stop()
        except:
            pass
        if self.ui.auto_wind:
            self.auto_wind_timer = QTimer()
            self.auto_wind_timer.timeout.connect(self.set_wind)
            auto_wind_timer = self.ui.update_wind_plc*1000 + self.ui.auto_wind_intervals
            self.auto_wind_timer.start(auto_wind_timer)

    def set_wind(self, mode=True):
        if self.ui.wind_itr == 1:
            ret = self.my_plc.set_value(self.dict_spec_pathes["MemUpValve"], str(mode))
            # if ret and mode:
            if mode:
                self.ui.start_wind()

    def set_start_software_plc(self, mode):
        # #print("software on plc ", str(mode))
        try:

            self.my_plc.set_value(self.dict_spec_pathes["MemSoftwareStart"], str(mode))

        except:
            pass

    def get_sensor_and_temp(self):
        try:
            self.sensor = self.my_plc.get_value(
                self.dict_spec_pathes["MemDistanceSensor"]
            )
            # #print(self.sensor[0])
            if self.sensor[0] == "-":
                if not self.ui.manual_plc:
                    # #print(";" * 50)
                    self.sensor = False
            else:
                self.sensor = bool(self.sensor[0])
        except:
            self.sensor = False

        try:
            self.top_temp = str(
                self.my_plc.get_value(self.dict_spec_pathes["UpTemperature"])[0]
            )
            self.bottom_temp = str(
                self.my_plc.get_value(self.dict_spec_pathes["DownTemperature"])[0]
            )
        except:
            self.top_temp = "0"
            self.bottom_temp = "0"

        if self.sensor:
            self.slab_detect = True
        else:
            self.slab_detect = False

        # threading.Thread(target=self.get_sensor_and_temp)

    def update_plc_values(self):
        threading.Thread(target=self.get_sensor_and_temp).start()
        # self.get_sensor_and_temp()

    def update_sensor_and_temp(self):
        # threading.Thread(target=self.get_sensor_and_temp).start()
        # self.get_sensor_and_temp()
        try:
            if (
                self.top_temp > self.up_high_threshold
                or self.bottom_temp > self.down_high_threshold
            ):
                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["overhead_temp"][self.ui.language], level=3
                )
        except:
            # #print('Except self.top_temp > self.up_high_threshold')
            pass
        #  self.up_high_threshold = self.my_plc.get_value(self.dict_spec_pathes["UpHighThreshold"])
        # self.up_low_threshold = self.my_plc.get_value(self.dict_spec_pathes["UpLowThreshold"])
        # self.down_high_threshold = self.my_plc.get_value(self.dict_spec_pathes["DownHighThreshold"])
        # self.down_low_threshold = self.my_plc.get_value(self.dict_spec_pathes["DownLowThreshold"])
        if self.ui.manual_plc:  # Manual change senssor   in final should be delete
            if self.itr <= 10:
                self.sensor = True
            else:
                self.sensor = False
                if self.itr >= 20:
                    self.itr = 0
            # #print(self.itr)
            self.itr += 1

        # if self.sensor:
        #     self.init_check_plc()
        # #print(self.sensor)
        if self.last_sensor != self.sensor:
            self.change_sensor_run()

        self.last_sensor = self.sensor

        self.ui.change_plc_check_status(mode=self.sensor)
        try:
            self.ui.update_plc_temp(self.top_temp, self.bottom_temp)
        except:
            pass

    def change_sensor_run(self):
        # #print(self.ready_capture_flag)
        if self.ready_capture_flag:
            if self.sensor:
                self.set_start_software_plc(True)
                try:
                    (
                        n_camera,
                        projectors,
                        speed,
                        details,
                    ) = self.l2_connection.get_full_info()  # get data from level2
                except:
                    self.stop_capture_func(disable_ui=True)
                    self.ui.create_alert_message(
                        title=texts.Titles["connection_failed"],
                        message=texts.MESSEGES["connection_failed"],
                    )

                self.ImageManager.update_sheet(n_camera, details)
                self.start_capture_func(disable_ui=False)
                self.ui.show_sheet_details(details, tab_live=True)
                self.my_plc.set_cams_and_prejector(n_camera, projectors)
                if self.show_save_notif:
                    self.ui.notif_manager.append_new_notif(
                        message=str(
                            texts.MESSEGES["start_captring"][self.ui.language]
                            + str(n_camera)
                            + " - "
                            + str(projectors)
                        ),
                        level=1,
                    )
            else:
                self.ImageManager.update_database()
                self.stop_capture_func(disable_ui=False)
                self.my_plc.set_cams_and_prejector(0, 0)
                if self.show_save_notif:
                    self.ui.notif_manager.append_new_notif(
                        message=str(texts.MESSEGES["save_sheet"][self.ui.language]), level=1
                    )

    def init_check_plc(self):
        # if self.start_capture_flag:
        try:
            self.plc_timer.stop()
            self.plc_update.stop()

        except:
            pass
        self.plc_timer.start(500)
        self.plc_update.start(self.ui.update_timer_plc)

    # Mypipline page------------------------------------------------

    def update_combo_piplines(self):
        db_pipline_names, spec_piplines = self.db.get_pipline_names(
            spec_name=self.login_user_name
        )
        self.ui.combo_all_pipline.clear()
        self.ui.combo_all_pipline.addItems(db_pipline_names)
        self.ui.combo_my_pipline.clear()
        self.ui.combo_my_pipline.addItems(spec_piplines)

    def remove_pipline(self):
        select_pipline = self.ui.combo_my_pipline.currentText()
        if select_pipline != "":
            if self.ui.show_question(
                texts.WARNINGS["WARNING"][self.language],
                texts.WARNINGS["Remove_pipline"][self.language] + select_pipline + ")",
            ):
                try:
                    res = self.db.remove_pipline(select_pipline)

                    if not res:
                        self.ui.set_warning(
                        texts.ERRORS["REMOVE_PIP_FAILED"][self.language],
                        "profile",
                        texts_codes.SubTypes['REMOVE_PIP_FAILED'],
                        level=3,
                        )
                        self.ui.logger.create_new_log(
                            message=texts.ERRORS["REMOVE_PIP_FAILED"]["en"], code=texts_codes.SubTypes['REMOVE_PIP_FAILED'], level=5
                        )

                    self.update_combo_piplines()
                    self.ui.set_warning(
                        texts.MESSEGES["REMOVE_PIP"][self.language], "profile", texts_codes.SubTypes['REMOVE_PIP'], level=1
                    )
                    self.ui.logger.create_new_log(
                        message=texts.MESSEGES["REMOVE_PIP"]["en"], code=texts_codes.SubTypes['REMOVE_PIP'], level=1
                    )
                except:
                    self.ui.set_warning(
                        texts.ERRORS["REMOVE_PIP_FAILED"][self.language],
                        "profile",
                        texts_codes.SubTypes['REMOVE_PIP_FAILED'],
                        level=3,
                    )
                    self.ui.logger.create_new_log(
                        message=texts.ERRORS["REMOVE_PIP_FAILED"]["en"], code=texts_codes.SubTypes['REMOVE_PIP_FAILED'], level=5
                    )

    # PBT Evaluate -----------------------------------------------

    def create_json_file(self, name):

        json_parent_path = self.db.get_json_parent_path()
        new_json = Pipeline(json_parent_path, name)

    def laod_bpt_jsons(self):

        self.filter_json_flag = False
        json_parent_path = self.db.get_json_parent_path()
        self.len_json, self.content_json = pipelines.load_all_json_files_by_date(
            json_parent_path
        )
        if self.len_json != 0:
            self.all_page_number = int(np.ceil(self.len_json / MAX_SHOW_IN_PAGE))
        else:
            self.all_page_number = 1

        self.page_number = 1
        self.json_clear_filter_btn()
        self.ui.lineEdit_in_history_of_pipline.setText(
            str(self.page_number) + "/" + str(self.all_page_number)
        )
        pipelines.set_piplines_on_ui_tabel(
            ui_obj=self.ui,
            values=self.content_json[
                ((self.page_number - 1) * MAX_SHOW_IN_PAGE) : (
                    self.page_number * MAX_SHOW_IN_PAGE
                )
            ],
        )
        pipelines.set_combox_of_pipline_history_page(self.ui, self.db)
        if self.len_json > 20:
            self.ui.pipline_tabel_next_PBT.setEnabled(True)

    def json_filter_btn(self):
        self.filter_json_flag = True
        self.filter_content_json = self.content_json.copy()
        filter_param = pipelines.get_pipline_info_from_ui(self.ui)
        pipelines.filter_piplines(
            all_content=self.filter_content_json, param_filter=filter_param
        )
        self.page_number = 1
        if len(self.filter_content_json) != 0:
            self.all_page_number = int(
                np.ceil(len(self.filter_content_json) / MAX_SHOW_IN_PAGE)
            )
        else:
            self.all_page_number = 1

        self.ui.lineEdit_in_history_of_pipline.setText(
            str(self.page_number) + "/" + str(self.all_page_number)
        )
        pipelines.set_piplines_on_ui_tabel(
            ui_obj=self.ui,
            values=self.filter_content_json[
                ((self.page_number - 1) * MAX_SHOW_IN_PAGE) : (
                    self.page_number * MAX_SHOW_IN_PAGE
                )
            ],
        )
        self.ui.pipline_tabel_prev_PBT.setEnabled(False)
        if len(self.filter_content_json) > 20:
            self.ui.pipline_tabel_next_PBT.setEnabled(True)
        else:
            self.ui.pipline_tabel_next_PBT.setEnabled(False)

    def json_clear_filter_btn(self):

        self.filter_json_flag = False

        pipelines.set_piplines_on_ui_tabel(
            ui_obj=self.ui,
            values=self.content_json[
                ((self.page_number - 1) * MAX_SHOW_IN_PAGE) : (
                    self.page_number * MAX_SHOW_IN_PAGE
                )
            ],
        )

        if self.len_json != 0:
            self.all_page_number = int(np.ceil(self.len_json / MAX_SHOW_IN_PAGE))
        else:
            self.all_page_number = 1
        self.page_number = 1
        self.ui.lineEdit_in_history_of_pipline.setText(
            str(self.page_number) + "/" + str(self.all_page_number)
        )

        if self.len_json > 20:
            self.ui.pipline_tabel_next_PBT.setEnabled(True)

        self.ui.cbBox_pipline_name_in_PBT_page.setCurrentIndex(0)
        self.ui.cbBox_binarry_model_in_PBT_page.setCurrentIndex(0)
        self.ui.cbBox_localization_model_in_PBT_page.setCurrentIndex(0)
        self.ui.cbBox_classification_model_in_PBT_page.setCurrentIndex(0)

        self.ui.binary_acc_min_filter_lineedit_3.setText("")
        self.ui.binary_acc_max_filter_lineedit_3.setText("")
        self.ui.binary_precision_min_filter_lineedit.setText("")
        self.ui.binary_precision_max_filter_lineedit.setText("")
        self.ui.binary_recall_min_filter_lineedit.setText("")
        self.ui.binary_recall_max_filter_lineedit.setText("")
        self.ui.binary_f1_min_filter_lineedit.setText("")
        self.ui.binary_f1_max_filter_lineedit.setText("")
        self.ui.localization_dice_min_filter_lineedit.setText("")
        self.ui.localization_dice_max_filter_lineedit.setText("")
        self.ui.localization_iou_min_filter_lineedit.setText("")
        self.ui.localization_iou_max_filter_lineedit.setText("")
        self.ui.classification_acc_min_filter_lineedit.setText("")
        self.ui.classification_acc_max_filter_lineedit.setText("")
        self.ui.classification_precision_min_filter_lineedit.setText("")
        self.ui.classification_precision_max_filter_lineedit.setText("")
        self.ui.classification_recall_min_filter_lineedit.setText("")
        self.ui.classification_recall_max_filter_lineedit.setText("")
        self.ui.classification_f1_min_filter_lineedit.setText("")
        self.ui.classification_f1_max_filter_lineedit.setText("")
        self.ui.pipline_year_lineedit.setText("")
        self.ui.pipline_month_lineedit.setText("")
        self.ui.pipline_day_lineedit.setText("")
        self.ui.pipline_hour_lineedit.setText("")
        self.ui.pipline_minut_lineedit.setText("")

    def next_page_pipline_history(self):

        if not self.filter_json_flag:
            self.filter_content_json = self.content_json

        if len(self.filter_content_json) != 0:
            self.all_page_number = int(
                np.ceil(len(self.filter_content_json) / MAX_SHOW_IN_PAGE)
            )
        else:
            self.all_page_number = 1

        self.page_number += 1
        self.ui.lineEdit_in_history_of_pipline.setText(
            str(self.page_number) + "/" + str(self.all_page_number)
        )
        pipelines.set_piplines_on_ui_tabel(
            ui_obj=self.ui,
            values=self.filter_content_json[
                ((self.page_number - 1) * MAX_SHOW_IN_PAGE) : (
                    self.page_number * MAX_SHOW_IN_PAGE
                )
            ],
        )
        if self.page_number > 1:
            self.ui.pipline_tabel_prev_PBT.setEnabled(True)
        if len(self.filter_content_json) < (self.page_number * MAX_SHOW_IN_PAGE):
            self.ui.pipline_tabel_next_PBT.setEnabled(False)

    def prev_page_pipline_history(self):
        if not self.filter_json_flag:
            self.filter_content_json = self.content_json

        if len(self.filter_content_json) != 0:
            self.all_page_number = int(
                np.ceil(len(self.filter_content_json) / MAX_SHOW_IN_PAGE)
            )
        else:
            self.all_page_number = 1

        self.page_number -= 1
        self.ui.lineEdit_in_history_of_pipline.setText(
            str(self.page_number) + "/" + str(self.all_page_number)
        )
        pipelines.set_piplines_on_ui_tabel(
            ui_obj=self.ui,
            values=self.filter_content_json[
                ((self.page_number - 1) * MAX_SHOW_IN_PAGE) : (
                    self.page_number * MAX_SHOW_IN_PAGE
                )
            ],
        )

        if self.page_number <= 1:
            self.ui.pipline_tabel_prev_PBT.setEnabled(False)
            self.ui.pipline_tabel_next_PBT.setEnabled(True)

        if (self.page_number * MAX_SHOW_IN_PAGE) > len(self.filter_content_json):
            self.ui.pipline_tabel_next_PBT.setEnabled(True)

    def show_pipline_details_func(self, flag=True, myflag=True):
        if flag:
            select_pipline = self.ui.combo_my_pipline.currentText()
            if select_pipline != "":
                self.ui.label_pipline_details.setText(
                    texts.WARNINGS["details_pipline"][self.language]
                )
                QTimer().singleShot(
                    5000, lambda: self.show_pipline_details_func(flag=False)
                )
        else:
            self.ui.label_pipline_details.setText("")


# ____________________________JJ ZONE
class evaluation_worker(QObject):

    # vars for handling thread
    finished = Signal()
    progress = Signal(dict, list)
    pgb_bar_signal = Signal(float)

    def set_params(
        self,
        paths,
        binary_model,
        classification_model,
        ds,
        split_size,
        classes_num,
        path_of_mask_prediction_with_current_pipline,
        pipline_OBJ,
        binary_thresh=0.5,
        classification_thresh=0.5,
    ):
        # var for handling evaluating
        self.paths = paths
        self.binary_thresh = binary_thresh
        self.classification_thresh = classification_thresh
        self.binary_model = binary_model
        self.classification_model = classification_model
        self.ds = ds
        self.split_size = split_size
        self.classes_num = classes_num
        self.path_of_mask_prediction_with_current_pipline = (
            path_of_mask_prediction_with_current_pipline
        )

        # will used:
        self.pipline_OBJ = pipline_OBJ

        self.pred_binary = []
        self.true_binary = []
        self.pred_classification = []
        self.true_classification = []
        self.pred_each_path = {}

    def evaluate(self):
        for i, path in enumerate(self.paths):

            file_name = os.path.basename(path)
            self.model_predicting(path=path, filename=file_name)

            # ckecking evaluting of model
            split_batch_size = self.pred_binary[-1].shape[0]
            true_flag = [1] in self.true_binary[-1 * split_batch_size :]
            pred_flag = [1] in self.pred_binary[-1]
            self.pred_each_path[path] = binary_list_funcs.WRONG_RIGHT_SYMBOL[
                (pred_flag == true_flag)
            ]
            # update progressbar
            percentage = 100 * (i + 1) / len(self.paths)
            self.pgb_bar_signal.emit(percentage)

        # convert true/pred to numpy array for calculating metrics
        # binary part
        pred_binary_matrix = np.concatenate(self.pred_binary)
        true_binary_matrix = np.array(self.true_binary)

        # binary metrics calculation:
        binary_acc = accuracy_score(
            y_true=true_binary_matrix, y_pred=pred_binary_matrix
        )
        binary_recall = recall_score(
            y_true=true_binary_matrix, y_pred=pred_binary_matrix
        )
        binary_precision = precision_score(
            y_true=true_binary_matrix, y_pred=pred_binary_matrix
        )
        binary_f1 = f1_score(y_true=true_binary_matrix, y_pred=pred_binary_matrix)

        # classification part
        classification_acc = -1.000
        classification_recall = -1.000
        classification_precision = -1.000
        classification_f1 = -1.000

        if len(self.pred_classification) != 0:
            pred_classification_matrix = np.concatenate(self.pred_classification)
            true_classification_matrix = np.concatenate(self.true_classification)

            # classification metrics calculation
            classification_acc = accuracy_score(
                y_true=true_classification_matrix, y_pred=pred_classification_matrix
            )
            classification_recall = recall_score(
                y_true=true_classification_matrix,
                y_pred=pred_classification_matrix,
                average="micro",
            )
            classification_precision = precision_score(
                y_true=true_classification_matrix,
                y_pred=pred_classification_matrix,
                average="micro",
            )
            classification_f1 = f1_score(
                y_true=true_classification_matrix,
                y_pred=pred_classification_matrix,
                average="micro",
            )

        # """UI SETTING"""
        # SHOW INFO IN UI
        binary_summary = "BINARY: \n accuracy:{:.3f} \n precision:{:.3f} \n recall;{:.3f} \n f1:{:.3f}".format(
            binary_acc, binary_precision, binary_recall, binary_f1
        )
        classification_summary = "CLASSIFICTION: \n accuracy:{:.3f} \n precision:{:.3f} \n recall;{:.3f} \n f1:{:.3f}".format(
            classification_acc,
            classification_precision,
            classification_recall,
            classification_f1,
        )
        summary_list = [binary_summary, classification_summary]

        """temporary"""  # shoul be function for setting this parameter!!!!!!!!!!!!!!!!! in future
        # binary part
        self.pipline_OBJ.set_binary_model(key=pipelines.MODEL_ACCURACY, value=-1)
        self.pipline_OBJ.set_binary_model(key=pipelines.MODEL_PRECISION, value=-1)
        self.pipline_OBJ.set_binary_model(key=pipelines.MODEL_RECALL, value=-1)
        self.pipline_OBJ.set_binary_model(key=pipelines.MODEL_F1, value=-1)
        self.pipline_OBJ.set_binary_model(key=pipelines.MODEL_LOSS, value=-1)

        """probably omit localiztion"""
        # localization part
        self.pipline_OBJ.set_localiztion_model(key=pipelines.MODEL_ACCURACY, value=-1)
        self.pipline_OBJ.set_localiztion_model(key=pipelines.MODEL_IOU, value=-1)
        self.pipline_OBJ.set_localiztion_model(key=pipelines.MODEL_DICE, value=-1)
        self.pipline_OBJ.set_localiztion_model(key=pipelines.MODEL_F1, value=-1)
        self.pipline_OBJ.set_localiztion_model(key=pipelines.MODEL_LOSS, value=-1)
        """probably omit localiztion"""

        # classification part
        self.pipline_OBJ.set_classification_model(
            key=pipelines.MODEL_ACCURACY, value=-1
        )
        self.pipline_OBJ.set_classification_model(
            key=pipelines.MODEL_PRECISION, value=-1
        )
        self.pipline_OBJ.set_classification_model(key=pipelines.MODEL_RECALL, value=-1)
        self.pipline_OBJ.set_classification_model(key=pipelines.MODEL_F1, value=-1)
        self.pipline_OBJ.set_classification_model(key=pipelines.MODEL_LOSS, value=-1)
        self.pipline_OBJ.set_classification_model(
            key=pipelines.MODEL_PERCLASSS_ACCURACY, value=-1
        )
        self.pipline_OBJ.set_classification_model(
            key=pipelines.MODEL_CONFUSION_MATRIX, value=-1
        )
        # """temporary"""

        # self.pipline_OBJ.save_json()

        self.progress.emit(self.pred_each_path, summary_list)
        self.finished.emit()

    def model_predicting(self, path, filename):
        img_ = cv2.imread(path)
        blocks_, _, _ = ImageCrops(img=img_, dim=self.split_size)
        w, h = blocks_.shape[0:2]
        blocks = np.reshape(
            blocks_, (w * h,) + self.split_size + (3,)
        )  # flatten all split (set them in a line)

        """set prediction part"""
        defects_inx, class_pred = self.set_grandpred(blocks=blocks)

        """set true part"""
        """process of setting true label/pred label/false positve/false negative for all three model"""
        if path.find(binary_list_funcs.PERFECT_PATH) != -1:

            if len(defects_inx) != 0:
                # calculate the column and row of single split
                # x=defects_inx/h
                # x=np.trunc(x).astype(np.uint8)
                # y=defects_inx-(h*x).astype(np.uint8)
                """temporary coment"""
                """save each split"""
                # self.write_fp_fn_in_dir(blocks[defects_inx],x,y,file_name,'fp')
                """save perfect image"""
                self.write_perfect_fp_fn_in_dir(file_name=filename, img=img_, flag="fp")

            # set true label
            if class_pred is not None:
                self.set_perfect_image_grandtrue(
                    w=w, h=h, classification_shape=class_pred.shape
                )
            else:
                self.set_perfect_image_grandtrue(
                    w=w, h=h, classification_shape=class_pred
                )
        else:
            if len(defects_inx) == 0:
                self.write_perfect_fp_fn_in_dir(file_name=filename, img=img_, flag="fn")

            mask_path = os.path.join(os.path.dirname(path), filename)
            mask_ = cv2.imread(mask_path, 0)
            mask_blocks_, rx, ry = ImageCrops(img=mask_, dim=self.split_size)
            json_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(path))),
                binary_list_funcs.ANNOTATION_PATH,
                filename[0:-3] + "json",
            )
            defects = self.indicate_defect_pixel(
                json_path=json_path,
                ratio_x=rx,
                ratio_y=ry,
                Length=mask_blocks_.shape[1] * self.split_size[1],
                width=mask_blocks_.shape[0] * self.split_size[0],
            )
            self.set_defect_image_grandtrue(
                img_blocks=blocks_,
                defects=defects,
                defects_inx=defects_inx,
                h=h,
                file_name=filename,
            )

    def set_grandpred(self, blocks):

        """set predicting label"""
        """set binary part"""
        # give all split of a image to binary model and threshold the model output
        pred = self.binary_model.predict(blocks)
        pred = (pred > self.binary_thresh).astype("int32")
        self.pred_binary.append(pred)  # set binary pred label of a single image
        defects_inx = np.where(pred[:, 0] == 1)[0]

        # mask_pred=None
        class_pred = None
        if len(defects_inx) != 0:
            """set classification part"""
            class_pred = self.classification_model.predict(blocks[defects_inx])
            class_pred = (class_pred > self.classification_thresh).astype("int32")

            self.pred_classification.append(class_pred)

        return defects_inx, class_pred

    def set_perfect_image_grandtrue(self, w, h, classification_shape):

        """set true label"""
        """process of setting true label/pred label/false positve/false negative for all three model"""

        """set binary part"""
        self.true_binary.extend(
            [[0]] * (w * h)
        )  # set binary true label of a single image

        # """set localiztion part"""
        # mask_true=np.zeros(localization_shape,dtype=np.uint8)
        # self.true_localization.append(mask_true)

        """set classification part"""

        if classification_shape is not None:
            true_label = np.zeros(classification_shape, dtype=np.uint8)
            self.true_classification.append(true_label)

    def set_defect_image_grandtrue(
        self, img_blocks, defects, defects_inx, h, file_name
    ):

        # self.true_localization.append(blocks[defects_inx])

        step = int(self.split_size[0])
        for i in range(img_blocks.shape[0]):
            for j in range(img_blocks.shape[1]):
                true_label = np.zeros((1, self.classes_num), dtype=np.uint8)
                binary_flag = False
                for key in defects:
                    flag = self.indicate_defect_split_class(
                        x1=j * step,
                        y1=i * step,
                        x2=(j + 1) * step,
                        y2=(i + 1) * step,
                        pixels=defects[key],
                        thresh=70,
                    )
                    if flag:
                        true_label[0, int(key.split("_")[0])] = 1
                        binary_flag = True

                if binary_flag:
                    self.true_binary.append([1])
                else:
                    self.true_binary.append([0])
                    # self.write_fp_fn_in_dir(img_blocks[i,j],i,j,file_name,'fn',mode='other')

                if ((i * h) + j) in defects_inx:
                    self.true_classification.append(true_label)

    def write_perfect_fp_fn_in_dir(self, file_name, img, flag):
        path_dic = {
            "fp": self.ds.pipline_wrong_result_fp_path,
            "fn": self.ds.pipline_wrong_result_fn_path,
        }
        img_path = os.path.join(path_dic[flag], file_name)
        cv2.imwrite(img_path, img)

    def write_fp_fn_in_dir(self, imgs, x, y, file_name, flag="other", mode="loop"):
        path_dic = {
            "fp": self.ds.pipline_wrong_result_fp_path,
            "fn": self.ds.pipline_wrong_result_fn_path,
            "other": self.path_of_mask_prediction_with_current_pipline,
        }
        if mode == "loop":
            fileNames = list(
                map(self.creat_split_name_file, x, y, [file_name] * (imgs.shape[0]))
            )
            for i, filename in enumerate(fileNames):
                dir = os.path.join(path_dic[flag], filename)
                cv2.imwrite(dir, imgs[i])
        else:
            fileName = self.creat_split_name_file(x, y, file_name)
            dir = os.path.join(path_dic[flag], fileName)
            cv2.imwrite(dir, imgs)

    def creat_split_name_file(
        self,
        x,
        y,
        file_name,
    ):
        fileName = "{f1}_{f2}_{f3}{f4}".format(
            f1=file_name[0:-4], f2=x, f3=y, f4=file_name[-4:]
        )
        return fileName

    def indicate_defect_pixel(self, json_path, ratio_x, ratio_y, Length, width):

        with open(json_path, "r") as f:
            json_info = json.load(f)
        f.close()

        defect_pixels = {}
        defects = json_info["obj_masks"]
        for i, defect in enumerate(defects):
            key = str(defect["class"]) + "_" + str(i)
            contour_angle = defect["mask"]
            angles = [
                (round(ratio_x * ele[0]), round(ratio_y * ele[1]))
                for ele in contour_angle
            ]
            defect_pixels[key] = self.get_all_pixel_contour(
                angles=angles, Length=Length, width=width
            )

        return defect_pixels

    def get_all_pixel_contour(self, angles, Length, width):

        mask = np.zeros((width, Length), dtype=np.uint8)

        for i in range(len(angles) - 1):
            mask = cv2.line(mask, angles[i], angles[i + 1], (255, 255, 255), 2)
        mask = cv2.line(mask, angles[i + 1], angles[0], (255, 255, 255), 2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros((width, Length), dtype=np.uint8)
        cv2.drawContours(mask, contours, 0, color=255, thickness=-1)
        all_pixel = np.where(mask == 255)
        all_pixel = list(zip(all_pixel[0], all_pixel[1]))

        return all_pixel

    def indicate_defect_split_class(self, x1, y1, x2, y2, pixels, thresh=30):

        counter = 0
        for px in pixels:
            if px[0] >= y1 and px[1] >= x1 and px[0] <= y2 and px[1] <= x2:
                counter += 1
                if counter > thresh:
                    return True
        return False

class ModelsCreation_worker(QObject):

    # vars for handling thread
    finished = Signal()
    model_creation_signal = Signal(int)

    def set_params(self, login_user_name, db, language, pipline_name):

        self.login_user_name = login_user_name
        self.db = db
        self.lang = language
        self.pipline_name = pipline_name

    def set_pipline(self):

        self.pipline_OBJ = pipelines.Pipeline(
            pipeline_root=binary_list_funcs.PIPLINES_PATH,
            pipeline_name=self.pipline_name,
        )
        self.pipline_OBJ.set(key=pipelines.OWNER, value=self.login_user_name)

        res, pipline_info = self.db.get_selected_pipline_record(value=self.pipline_name)

        if res:
            res, binary_model_info = self.db.get_model(
                self.db.binary_model, pipline_info[0]["binary_weight_path"]
            )
            if res:
                res, localiztion_model_info = self.db.get_model(
                    self.db.localiztion, pipline_info[0]["localization_weight_path"]
                )
            if res:
                res, classification_model_info = self.db.get_model(
                    self.db.classification,
                    pipline_info[0]["classification_weight_path"],
                )

            self.binary_input_size = binary_model_funcs.strInputSize_2_intInputSize(
                string=binary_model_info[0]["input_size"]
            )
            # set binary model parameter of pipline:
            self.pipline_OBJ.set_binary_model(
                key=pipelines.MODEL_ID, value=binary_model_info[0]["algo_name"]
            )
            self.pipline_OBJ.set_binary_model(
                key=pipelines.MODEL_WEIGHTS_PATH,
                value=binary_model_info[0][pipelines.MODEL_WEIGHTS_PATH],
            )

            self.localiztion_input_size = (
                binary_model_funcs.strInputSize_2_intInputSize(
                    string=localiztion_model_info[0]["input_size"]
                )
            )
            # set localiztion model parameter of pipline:
            self.pipline_OBJ.set_localiztion_model(
                key=pipelines.MODEL_ID, value=localiztion_model_info[0]["algo_name"]
            )
            self.pipline_OBJ.set_localiztion_model(
                key=pipelines.MODEL_WEIGHTS_PATH,
                value=localiztion_model_info[0][pipelines.MODEL_WEIGHTS_PATH],
            )

            self.classification_input_size = (
                binary_model_funcs.strInputSize_2_intInputSize(
                    string=classification_model_info[0]["input_size"]
                )
            )
            classes_num, classes = binary_model_funcs.strInputSize_2_intInputSize(
                string=classification_model_info[0]["classes"],
                use_for_other_parameter=True,
            )
            # set localiztion model parameter of pipline:
            self.pipline_OBJ.set_classification_model(
                key=pipelines.MODEL_ID, value=classification_model_info[0]["algo_name"]
            )
            self.pipline_OBJ.set_classification_model(
                key=pipelines.MODEL_WEIGHTS_PATH,
                value=classification_model_info[0][pipelines.MODEL_WEIGHTS_PATH],
            )
            self.pipline_OBJ.set_classification_model(
                key=pipelines.TARGET_CLASSES, value=classes
            )
            if res:
                try:
                    b_algo_name = (
                        binary_model_funcs.translate_binary_algorithm_id_to_name(
                            binary_model_info[0]["algo_name"]
                        )
                    )
                    l_algo_name = (
                        binary_model_funcs.translate_binary_algorithm_id_to_name(
                            localiztion_model_info[0]["algo_name"],
                            model_type="localization",
                        )
                    )
                    c_algo_name = (
                        binary_model_funcs.translate_binary_algorithm_id_to_name(
                            classification_model_info[0]["algo_name"],
                            model_type="classification",
                        )
                    )

                    self.b_model = binary_model_funcs.translate_model_algorithm_id_to_creator_function(
                        algo_id=b_algo_name, input_size=self.binary_input_size
                    )
                    self.model_creation_signal.emit(1)
                    self.l_model = binary_model_funcs.translate_model_algorithm_id_to_creator_function(
                        algo_id=l_algo_name, input_size=self.localiztion_input_size
                    )
                    self.model_creation_signal.emit(2)
                    self.classes_num = 5  # <------------------temporary
                    self.c_model = binary_model_funcs.translate_model_algorithm_id_to_creator_function(
                        algo_id=c_algo_name,
                        input_size=self.classification_input_size,
                        num_class=self.classes_num,
                        mode="categorical",
                    )
                    self.model_creation_signal.emit(3)
                except:
                    self.model_creation_signal.emit(5)
                    return

            self.model_creation_signal.emit(4)
            self.finished.emit()

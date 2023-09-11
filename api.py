# from logging import _Level
import copy
import ast
from email.mime import image
from importlib.resources import path
from ntpath import join
from operator import le
from pickletools import uint8
import re
from shutil import which
from stat import FILE_ATTRIBUTE_NORMAL
import sys
from ast import Try
import matplotlib

from PySide6.QtCore import *
from PySide6.QtWidgets import QFileDialog
from cv2 import log
from PySide6.QtCore import *
from PySide6.QtCore import QThread as sQThread
from PySide6.QtGui import QPen, QPainter
from matplotlib import pyplot as plt
from matplotlib.style import use

from Defect_detection_modules.SteelSurfaceInspection import SSI, CreateHeatmap
from app_settings import Settings
from backend import data_grabber, camera_connection
from backend.mouse import Mouse
from backend.keyboard import Keyboard
import cv2
import threading
import numpy as np
import math
import os
from PySide6.QtWidgets import QHeaderView as sQHeaderView
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
    yolo_model_funcs,
    pathStructure,
    FileManager
)
import database_utils
from utils1 import *
from utils1.move_on_list import moveOnList, moveOnImagrList
import texts  # eror and warnings texts
import texts_codes
from utils1 import tempMemory, Utils
from backend.dataset import Dataset
import train_api
from labeling import labeling_api
from pynput.mouse import Controller
from login_win.login_api import login_API
from camera_live_thread import ImageManager
import dataset_utils
import image_processing_worker
from technical_load_sheet_worker import technical_load_sheet_worker
import save_all_worker
import random
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem

from backend import pipelines
from backend.pipline_creation_module import ModelsCreation_worker
from backend.pipline_evaluation_module import Evaluation_worker
from backend.binary_list_funcs import PIPLINES_PATH
from backend.pipelines import Pipeline
import backend.pipelines

from PySide6.QtWidgets import QVBoxLayout
import matplotlib.pyplot as plt
# from tensorflow.keras.metrics import Accuracy, Precision, Recall
from Train_modules.deep_utils import metrics
from backend import pipelines
import tensorflow as tf
from image_splitter import ImageCrops
import json
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from PySide6.QtCore import QObject, QThread, Signal
import sys
sys.path.append('../oxin_storage_management')
from storage_main_UI import storage_management
from storage_api import storage_api
from storage_worker import storage_worker
import time
from level2_UI import levl2_UI
import getpass
import subprocess


WIDTH_TECHNICAL_SIDE = 49 * 12
HEIGHT_FRAME_SIZE = 51
NCAMERA = 12

TECHNICAL_WGT_NAME_TO_SIDE = {"up_side_technical", "top", "bottom"}

MAX_SHOW_IN_PAGE = 20

FRAME_RATE = 7


TRUE_COLOR = '#4E9A06'
FALSE_COLOR = '#A40000'



# down_side_technical     ,   up_side_technical
class API:
    def __init__(self, ui):
        self.ui = ui
        
        self.remove_pypylon_chache()

        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.move_on_list = moveOnList()
        self.db = database_utils.dataBaseUtils(ui_obj=self.ui)
        # self.config_database()
        self.create_classlist_pie_chart()
        self.create_label_color()
        self.create_default_ds()
        # self.mask_label_backend=Label.maskLbl(self.ui.get_size_label_image(), LABEL_COLOR)
        self.label_bakcend = {
            "mask": Label.maskLbl((1024, 1792), self.LABEL_COLOR),
        }
        self.label_bakcend_neighbours = {
            "mask": Label.maskLbl((1024, 1792), self.LABEL_COLOR),
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
        self.ymodel_tabel_itr = 1
        self.bmodel_count = 0
        self.lmodel_count = 0
        self.ymodel_count = 0
        self.filter_mode = False
        self.lfilter_mode = False
        self.yfilter_mode = False
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
        self.perfect_show = False
        # self.defect_show = True
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
        self.plc_connection_status = False
        self.set_plc_ip_to_ui()
        self.connect_plc()
        # self.load_plc_parms()  # should be commecnt in finbal version
        self.ui.start_wind_btn.clicked.connect(lambda: self.set_wind(True))
        self.wind_mode = False
        self.start_auto_wind()
        # self.update_plc_parms()
        self.plc_timer = QTimer()
        self.plc_timer.timeout.connect(self.update_sensor_and_temp)
        self.update_plc_values()

        self.slab_detect = False
        self.language = self.ui.language
        self.last_sensor = False
        self.sensor = False
        self.up_in = False
        self.up_out = False
        self.down_in = False
        self.down_out = False
        self.init_check_plc()
        self.create_level2_ui()

        self.my_plc.set_cams_and_prejector()


        # Level2 connection
        self.l2_connection = level2_connection.connection_level2(db_obj=self.db,close_ui=self.ui.flag_close_win,logger = self.ui.logger)
        
        # self.l2_connection.create_connection()
        # self.start_level2_thread()

        (
            self.n_camera,
            self.projectors,
            self.details,
        ) = self.l2_connection.get_dummy_info()
        self.get_info_flag = False

        self.ui.level2_btn.clicked.connect(self.show_level_ui)


        # PBT

        self.current_b_model = ""
        self.current_l_model = ""
        self.current_c_model = ""
        self.current_yolo_model = ""
        self.current_b_model_weights = ""
        self.current_l_model_weights = ""
        self.current_c_model_weights = ""
        self.current_yolo_model_weights = ""
        self.pipline_type = ""
        self.pipline_name = ""
        self.binary_model_flag = False
        self.segmentation_model_flag = False
        self.classification_model_flag = False
        self.yolo_model_flag = False
        self.pipline_is_ready = False
        self.data_is_ready = False
        self.add_piplines_in_combobox()
        self.add_dataset_in_combobox()

        # ImageProcessing
        self.sheet_imgprocessing_mem = {}

        # notif manager

        self.show_save_notif = False

        self.running_b_model = False
        self.running_l_model = False
        self.running_y_model = False


        self.ui.radioButton_use_yolo.setChecked(True)
        self.ui.radioButton_use_yolo.toggled.connect(
            lambda: self.set_pipline_mode("yolo")
        )
        self.ui.radioButton_use_unet.toggled.connect(
            lambda: self.set_pipline_mode("localization")
        )
        self.set_pipline_mode("yolo")
        self.load_plc_parms()


        # storage
        self.ssd_image_file_manager = None
        self.hdd_file_manager = None
        self.storage_win = None
        self.s_api = None
        self.storage_timer = None
        self.storage_start_process = None
        self.storage_show_process = None

        
        self.read_storage_paths_from_db()
        self.create_diskMemory_objs()
        # self.create_storage_window()
        self.start_storage_checking()
        

        # DEBUG_FUNCTIONS
        # -------------------------------------
        # self.__debug_load_sheet__(["996", "997"])
        # self.__debug_select_random__()
        # self.__debug_select_for_label()
        # self.__debug__login__()


        self.grab_time = 0
        self.stop_grab = False
        self.grab_main_thread = None



        # milad_pbt
        self.ui.pipline_name.textChanged.connect(self.check_name_pipline)


        # show level2 speed 
        self.show_speed_timer = QTimer()
        self.show_speed_timer.timeout.connect(self.show_speed)
        self.show_speed_timer.start(100)
        self.speed_mode = True

        #show level2 status
        self.show_l2_status = QTimer()
        self.show_l2_status.timeout.connect(self.show_status_level2)
        self.show_l2_status.start(1000)

        self.level2_win.reconnect_btn.clicked.connect(self.reconnect_level2)


        self.technical_scale = 1

        self.technical_threads = {}
        self.technical_workers = {}
        self.technical_thread_cnt = {}

        self.suggestion_threads = []
        self.suggestion_workers = []

        self.update_defect_threads = {}
        self.update_defect_workers = {}
        self.update_defect_thread_cnt = {}
        

        #milad
        self.baselines =None
    def create_level2_ui(self):
        self.level2_win = levl2_UI()
    def show_level_ui(self):
        self.level2_win.show()

    def reconnect_level2(self):
        self.l2_connection.close_ui=True
        self.ui.logger.create_new_log(
                        code=texts_codes.SubTypes['RESET_LEVEL2_GET_DATA'], message=texts.MESSEGES["RESET_LEVEL2_GET_DATA"]["en"], level=1
                    )
        threading.Timer(10,self.start_level2_thread).start()



    def start_level2_thread(self):
        self.l2_connection.reset_retry_values()
        self.l2_connection.close_ui=False
        self.level2_thread_data = threading.Thread(target=self.l2_connection.get_data)
        self.level2_thread_data.start()

        self.level2_thread_speed = threading.Thread(target=self.l2_connection.get_speed)
        self.level2_thread_speed.start()
    

        self.level2_thread_check_data = threading.Thread(target=self.l2_connection.get_check_data)
        self.level2_thread_check_data.start()


    def show_status_level2(self):
        t1 = QTime.currentTime().toString("hh:mm:ss")
        flag = True
        if self.l2_connection.last_speed !=False or int(self.l2_connection.last_speed)==0:
            self.set_ui_status_time('speed',True,t1)
        else:
            flag = False
            self.set_ui_status_time('speed',False,t1)

        #level2 data show status on ui

        if self.l2_connection.data:
            self.set_ui_status_time('level2',True,t1)
        else:
            flag = False
            self.set_ui_status_time('level2',False,t1)
            
        # level2 data dummy check on ui
        if self.l2_connection.check_data:
            self.set_ui_status_time('dummy',True,t1)
        else:
            # flag = False
            self.set_ui_status_time('dummy',False,t1)

        if flag:
            self.ui.level2_btn.setStyleSheet('QPushButton {background-color: #4E9A06;border-radius: 10px;border-color: beige;padding: 6px;color : white;}')
        else:
            self.ui.level2_btn.setStyleSheet('QPushButton {background-color: #A40000;border-radius: 10px;border-color: beige;padding: 6px;color : white;}')           
    def show_speed(self):
        # print(self.l2_connection.last_speed)


        if self.l2_connection.last_speed>0 and not self.speed_mode:
            self.ui.label_228.setStyleSheet("color : #1A5D1A")
            self.speed_mode = True
            self.ui.label_228.setText(str(self.l2_connection.last_speed))

        if self.l2_connection.last_speed<=0 and self.speed_mode:
            self.ui.label_228.setStyleSheet("color : #C51605")
            self.speed_mode = False
            self.ui.label_228.setText('{} 0.0 '.format(texts.Titles['stop'][self.language]))





    def set_ui_status_time(self,frame_name,status,time):

        self.level2_win.set_style_sheet(frame_name,status)
        self.level2_win.set_time(frame_name,time)







    def remove_pypylon_chache(self):
        try:
            path = os.getcwd()
            os.chdir('/dev/shm')
            listdir =os.listdir()
            for gen in listdir:
                if 'GenICam_XML' in gen:
                    os.system('rm {}'.format(gen))

            os.chdir(path)
        except:
            print('ERROR Try remove cache pypylon ')

    def read_storage_paths_from_db(self):
        res, storage_settings = self.db.load_storage_setting()
        if res:
            self.update_time = storage_settings['update_time']
            self.storage_upper_limit = storage_settings['storage_upper_limit']
            self.hdd_path = storage_settings['hdd_path']
            self.ssd_images_path = storage_settings['ssd_images_path']

    def create_diskMemory_objs(self):
        if not os.path.exists(self.hdd_path):
            os.makedirs(self.hdd_path, exist_ok=True)
        if not self.hdd_file_manager:
            self.hdd_file_manager = FileManager.diskMemory(path=self.hdd_path)

        if not os.path.exists(self.ssd_images_path):
            os.makedirs(self.ssd_images_path, exist_ok=True)
        if not self.ssd_image_file_manager:
            self.ssd_image_file_manager = FileManager.diskMemory(path=self.ssd_images_path)

    def create_storage_window(self):
        if not self.storage_win:
            self.storage_win = storage_management()
            self.storage_win.apply_settings_btn.clicked.connect(self.restart_storage_checking)
        if not self.s_api:
            self.s_api = storage_api(self.storage_win)

    def show_storage_window(self, start=False):
        # self.storage_win.set_language(self.language)
        # self.storage_win.show()
        # self.storage_win.show_main_page()
        try:
            if start:
                if not self.storage_start_process or self.storage_start_process.poll() != None:
                    if self.storage_show_process and self.storage_show_process.poll() == None:
                        self.storage_show_process.terminate()
                    self.storage_start_process = subprocess.Popen(
                        ['/bin/python3', '../oxin_storage_management/storage_main_UI.py', self.language, str(start)]
                        )
                    self.ui.logger.create_new_log(
                        code=texts_codes.SubTypes['Storage_opened'], message=texts.MESSEGES["Storage_opened"]["en"] + ' start={}'.format(start), level=1
                    )
            else:
                if not self.storage_show_process or self.storage_show_process.poll() != None:
                    if self.storage_start_process and self.storage_start_process.poll() == None:
                        return
                    self.storage_show_process = subprocess.Popen(
                        ['/bin/python3', '../oxin_storage_management/storage_main_UI.py', self.language, str(start)]
                        )
                    self.ui.logger.create_new_log(
                        code=texts_codes.SubTypes['Storage_opened'], message=texts.MESSEGES["Storage_opened"]["en"] + ' start={}'.format(start), level=1
                    )
        except:
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes['Storage_open_failed'], message=texts.MESSEGES["Storage_open_failed"]["en"], level=5
            )

    def check_storage(self):
        self.ssd_image_file_manager.refresh()
        self.hdd_file_manager.refresh()

        self.update_storage_charts()

        if self.ssd_image_file_manager:
            ssd_image_percent = self.ssd_image_file_manager.used.toPercent()
            print('ssd image percent: ', ssd_image_percent)

            if ssd_image_percent > self.storage_upper_limit:
                self.show_storage_window(start=True)
                # self.show_storage_window()
                # self.s_api.clear_filters()
                # self.s_api.start()
                
                    
    def update_storage_charts(self):
        self.ui.show_hdd_chart()
        self.update_hdd_chart()

        self.ui.show_ssd_chart()
        self.update_ssd_chart()

    def update_ssd_chart(self):
        storage_status = {'SSD': {'Used':self.ssd_image_file_manager.used.toGB(), 
                              'Free': self.ssd_image_file_manager.free.toGB()}, 
                    }
        chart_funcs.update_storage_barchart(
            ui_obj=self.ui,
            storage_type='SSD',
            storage_status=storage_status
        )

    def update_hdd_chart(self):
        storage_status = {'HDD': {'Used':self.hdd_file_manager.used.toGB(), 
                            'Free': self.hdd_file_manager.free.toGB()}
                    }
        chart_funcs.update_storage_barchart(
            ui_obj=self.ui,
            storage_type='HDD',
            storage_status=storage_status
        )

    def start_storage_checking(self):
        self.check_storage()
        if not self.storage_timer:
            self.storage_timer = QTimer()
            self.storage_timer.timeout.connect(self.check_storage)
        self.storage_timer.start(1000*60*self.update_time)

    def restart_storage_checking(self):
        self.storage_timer.stop()
        self.read_storage_paths_from_db()
        self.ssd_image_file_manager = None
        self.hdd_file_manager = None
        self.create_diskMemory_objs()
        self.start_storage_checking()

    def set_pipline_mode(self,key):
        """
        set_pipline_mode function for setting type of pipeline,that use yolo vs unet


        Parameters
        ----------
        key : str
           has 2 acceptable  values ,yolo and  localization
        """
        self.pipline_dict = {'yolo':[self.ui.page_yolo,self.ui.page_yolo_2],'localization':[self.ui.page_localization,self.ui.page_localization_2]}
        self.pipline_selected = key
        self.ui.stackedWidget_3.setCurrentWidget(self.pipline_dict[key][0])
        self.ui.stackedWidget_4.setCurrentWidget(self.pipline_dict[key][1])

        if key == "yolo":
            self.load_table_with_btn(self.ui.toolButton_yolo.objectName())
            # self.ui.cbBox_of_yolo_model_in_PBT_page.setCurrentIndex(0)
        elif key == "localization":
            self.load_table_with_btn(self.ui.toolButton_localization.objectName())
            self.load_table_with_btn(self.ui.toolButton_classification.objectName())
            # self.ui.cbBox_of_localization_model_in_PBT_page.setCurrentIndex(0)
            # self.ui.cbBox_of_classification_model_in_PBT_page.setCurrentIndex(0)
        self.load_table_with_btn(self.ui.toolButton_binary.objectName())
        # self.ui.cbBox_of_binary_model_in_PBT_page.setCurrentIndex(0)

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
        self.ui.set_b_default_db_parms(self.ds.dataset_path)
        self.ui.set_l_default_db_parms(self.ds.dataset_path)
        self.ui.set_y_default_db_parms(self.ds.dataset_path)
        chart_funcs.update_label_piechart(self.ui, binary_count)

    # _____________________________________________________________________JJ ZONE BEGINE

    def display_models_info_on_table_in_pbt(self, item):
        row = self.ui.table_of_binary_classifaction_in_PBT_page.indexFromItem(
            item
        ).row()
        if (
            self.ui.table_of_binary_classifaction_in_PBT_page.item(row, 0).checkState()
            == Qt.CheckState.Checked
        ):
            self.ui.table_of_binary_classifaction_in_PBT_page.item(
                row, 0
            ).setCheckState(Qt.CheckState.Unchecked)
            model_summery_that_show = ""
        else:
            self.ui.table_of_binary_classifaction_in_PBT_page.item(
                row, 0
            ).setCheckState(Qt.CheckState.Checked)
            # create string as summery of model(or algorithm)
            model_summery_that_show = "row {} selected,algorithm:{},that tarin in date:{},with dataset:{},and the weights is here {}".format(
                row + 1,
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
            self.ui.LBL_of_selected_binary_model_in_PBT_page.setText(
                model_summery_that_show
            )
            if model_summery_that_show != "":
                self.input_size_binary_model = input_size
                self.current_b_model = self.bmodels_list[row]
                self.current_b_model_weights = self.current_b_model["weights_path"]
            else:
                self.input_size_binary_model = ""
                self.current_b_model = ""
                self.current_b_model_weights = ""

        elif (
            self.bmodels_list[row]["algo_name"]
            in train_api.ALGORITHM_NAMES["classification"]
        ):
            # set the  summery at the lineEdit ,that under the table
            self.ui.LBL_of_selected_classification_model_in_PBT_page.setText(
                model_summery_that_show
            )
            if model_summery_that_show != "":
                self.input_size_classification_model = input_size
                self.current_c_model = self.bmodels_list[row]
                self.current_c_model_weights = self.current_c_model["weights_path"]
            else:
                self.input_size_classification_model = ""
                self.current_c_model = ""
                self.current_c_model_weights = ""

        elif (
            self.bmodels_list[row]["algo_name"]
            in train_api.ALGORITHM_NAMES["localization"]
        ):
            # set the  summery at the lineEdit ,that under the table
            self.ui.LBL_of_selected_localization_model_in_PBT_page.setText(
                model_summery_that_show
            )
            if model_summery_that_show != "":
                self.input_size_localization_model = input_size
                self.current_l_model = self.bmodels_list[row]
                self.current_l_model_weights = self.current_l_model["weights_path"]
            else:
                self.input_size_localization_model = ""
                self.current_l_model = ""
                self.current_l_model_weights = ""

        elif self.bmodels_list[row]["algo_name"] in train_api.ALGORITHM_NAMES["yolo"]:
            # set the  summery at the lineEdit ,that under the table
            self.ui.LBL_of_selected_yolo_model_in_PBT_page.setText(
                model_summery_that_show
            )
            if model_summery_that_show != "":
                self.input_size_yolo_model = input_size
                self.current_yolo_model = self.bmodels_list[row]
                self.current_yolo_model_weights = self.current_yolo_model[
                    "weights_path"
                ]
            else:
                self.input_size_yolo_model = ""
                self.current_yolo_model = ""
                self.current_yolo_model_weights = ""

        for i in range(self.ui.table_of_binary_classifaction_in_PBT_page.rowCount()):
            if self.ui.table_of_binary_classifaction_in_PBT_page.item(i, 0) != None:
                if (
                    i != row
                    and self.ui.table_of_binary_classifaction_in_PBT_page.item(
                        i, 0
                    ).checkState()
                    == Qt.CheckState.Checked
                ):
                    self.ui.table_of_binary_classifaction_in_PBT_page.item(
                        i, 0
                    ).setCheckState(Qt.CheckState.Unchecked)

        if self.current_b_model != "" and (
            self.current_yolo_model != "" or self.current_l_model != ""
        ):
            self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setEnabled(True)
            self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setFixedWidth(58)
            self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setFixedHeight(28)
            if self.current_yolo_model != "":
                if self.current_l_model != "":
                    self.pipline_type = "BSY"
                else:
                    self.pipline_type = "BY"
            elif self.current_c_model != "":
                self.pipline_type = "BSC"
            else:
                self.pipline_type = "BS"

        else:
            self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setEnabled(False)
            # self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setFixedWidth(0)
            # self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.setFixedHeight(0)

    def apply_selected_model_after_push_applyBTN_in_PBT_page(self):
        """the function connect to 'BTN_apply_of_binary_classifaction_in_PBT_page',
        and if the user set models,by clicking the buttom ,load dataset page loaded
        """
        if self.ui.pipline_name.text() != "":
            if self.check_name_pipline():
                classification_info = ""
                if self.current_l_model != "" and self.current_c_model == "":
                    classification_info = texts.WARNINGS["Have_Classification_model"][
                        self.language
                    ]

                if self.ui.show_question(
                    texts.WARNINGS["WARNING"][self.language],
                    texts.WARNINGS["Create_pipline"][self.language]
                    + self.ui.pipline_name.text()
                    + ")\n"
                    + classification_info,
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


    


    def check_name_pipline(self):

        print('asdw')

        pipline_name = self.ui.pipline_name.text()
        if pipline_name == "":
            self.ui.pipline_name_status.setText(
                texts.ERRORS["empty_name"][self.language]
            )

            self.ui.pipline_name_status.setStyleSheet(
                            "color: rgb(170, 0, 0);"
                        )

            return False

        db_pipline_names = self.db.get_pipline_names()

        if pipline_name in db_pipline_names:
            self.ui.pipline_name_status.setText(
                texts.ERRORS["repeat_name"][self.language]
            )
            self.ui.pipline_name_status.setStyleSheet(
                            "color: rgb(170, 0, 0);"
                        )

            return False
        else:
            self.ui.pipline_name_status.setText(
                texts.MESSEGES["valid_pipline"][self.language]
            )
            self.ui.pipline_name_status.setStyleSheet(
                            "color: rgb(0, 170, 0);"
                        )

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
            data = (
                self.ui.pipline_name.text(),
                self.login_user_name,
                self.current_b_model_weights,
                self.current_l_model_weights,
                self.current_c_model_weights,
                self.current_yolo_model_weights,
                self.pipline_type,
            )  # path pipline null
            ret = self.db.add_pipline(data)
            return ret

        except:
            # self.ui.pipline_name_status.setText(texts.ERRORS['repeat_name'][self.language])
            return False

    def add_piplines_in_combobox(self, piplinename=-1):
        """
        add_piplines_in_combobox add created pipline info to sql ,in pipline table

        check the name of piplie is new,if is new ,add pipline to sql table

        Parameters
        ----------
        piplinename:str
            name of pipline, by default -1
        """
        db_pipline_names = self.db.get_pipline_names()
        self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.clear()
        self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.addItems(db_pipline_names)
        # if piplinename != -1:
        #     inx = db_pipline_names.index(piplinename)
        #     self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.setCurrentIndex(inx)

    def load_image_btn_in_PBT_page(self):
        """
        load_image_btn_in_PBT_page concet to toolbuttom for gettinh path of cutomized dataset

        """
        path = QFileDialog.getExistingDirectory(self.ui, "Choose Directory", "")
        self.ui.lineEdit_of_path_displayment_in_PBT_page.setText(path)
        self.customized_datasets = [{"path": path}]

    def set_perfect_defect_checkBox_dataset(self, state):
        self.perfect_show = state

    def checkbox_connector(self):
        self.ui.chbox_prefectdata_in_PBT_page.stateChanged.connect(
            partial(
                lambda x: self.set_perfect_defect_checkBox_dataset(
                    state=self.ui.chbox_prefectdata_in_PBT_page.isChecked(),
                )
            )
        )

    def QTableWidget_connector(self):
        """by calling this function, the qtablewidget of UI connect to corresponding function.
        this function call in __init__ function
        """
        self.ui.table_of_binary_classifaction_in_PBT_page.itemClicked.connect(
            partial(self.display_models_info_on_table_in_pbt)
        )

    def comboBox_connector(self):
        """by calling this function, the comboBox of UI connect to corresponding function.
        this function call in __init__ function
        """

        # comboBox in PBT page that ,indicate binary classification algorithm
        self.ui.cbBox_of_binary_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(filter_mode=True, wich_page="PBT")
        )

        self.ui.cbBox_of_classification_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(
                filter_mode=True, wich_page="PBT", model_type="classification"
            )
        )

        self.ui.cbBox_of_localization_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(
                filter_mode=True, wich_page="PBT", model_type="localization"
            )
        )

        self.ui.cbBox_of_yolo_model_in_PBT_page.currentTextChanged.connect(
            lambda: self.refresh_binary_models_table(
                filter_mode=True, wich_page="PBT", model_type="yolo"
            )
        )

        self.ui.comboBox_ncamera_SI.currentTextChanged.connect(
            partial(self.set_ncamera_label)
        )
        self.ui.comboBox_nframe_SI.currentTextChanged.connect(
            partial(self.set_nframe_label)
        )

        self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.currentTextChanged.connect(
            partial(self.update_pipline_table_title)
        )

    def load_table_with_btn(self, obj_name):
        """
        load_table_with_btn

            by pushhing toolbuttom update tabel

        Parameters
        ----------
        obj_name : str
            by pushhing toolbuttom update tabel
        """
        algo_name = obj_name.split("_")[1]
        self.refresh_binary_models_table(
            filter_mode=True, wich_page="PBT", model_type=algo_name
        )
        self.remember_selected_item(algo_name=algo_name)

    def remember_selected_item(
        self,
        algo_name,
    ):
        """
        remember_selected_item function remember table change between model type changing

        _extended_summary_

        Parameters
        ----------
        algo_name :str
            indicate type of model
        """
        label = eval(
            "self.ui.{}".format(" LBL_of_selected_" + algo_name + "_model_in_PBT_page")
        )
        txt = label.text()
        if txt != "":
            row = int(txt[4]) - 1
            self.ui.table_of_binary_classifaction_in_PBT_page.item(
                row, 0
            ).setCheckState(Qt.CheckState.Checked)

    def update_evaluation_metrics_table(self, pipline_type):
        """
        update_evaluation_metrics_table used for updateing  types of table metrics in page 2 of pbt

        according to the type of pipline chage the cell structure of metrics table

        Parameters
        ----------
        pipline_type : str
            type of pipline:BY,BS,BSC,BSY
        """
        self.ui.tabWidget.clear()
        metrics_list = pipelines.MODELS_METRICS[pipline_type]
        tab_list = pipelines.TAB_TITLES[pipline_type]
        for i, each_tab in enumerate(tab_list):
            table = eval("self.ui.{}_table_metrics".format(each_tab))
            self.ui.tabWidget.addTab(table, each_tab)
            self.update_pipline_table_info(table=table, titles=metrics_list[i])

    def update_pipline_table_title(self, pipline_name):
        """
        update_pipline_table_title _summary_

        _extended_summary_

        Parameters
        ----------
        pipline_name : _type_
            _description_
        """
        _, pipline_info = self.db.get_selected_pipline_record(value=pipline_name)
        if pipline_info != []:
            self.len_model_piplines = len(
                pipelines.TABLE_TITLE[pipline_info[0]["pipline_type"]]
            )

            self.update_evaluation_metrics_table(
                pipline_type=pipline_info[0]["pipline_type"]
            )

            self.update_pipline_table_info(
                table=self.ui.tableWidget_pipline_info,
                titles=pipelines.TABLE_TITLE[pipline_info[0]["pipline_type"]],
                language=True,
            )
            self.assign_table_column(
                table=self.ui.tableWidget_pipline_info,
                number_of_rows=self.len_model_piplines,
                refresh=True,
            )
            if pipline_name == self.pipline_name:
                if self.binary_model_flag:
                    self.update_table_value(
                        table=self.ui.tableWidget_pipline_info,
                        value=texts.MESSEGES["Part_is_ready"][self.language],
                        row=0,
                    )
                if self.segmentation_model_flag:
                    self.update_table_value(
                        table=self.ui.tableWidget_pipline_info,
                        value=texts.MESSEGES["Part_is_ready"][self.language],
                        row=1,
                    )
                if self.classification_model_flag:
                    self.update_table_value(
                        table=self.ui.tableWidget_pipline_info,
                        value=texts.MESSEGES["Part_is_ready"][self.language],
                        row=2,
                    )
                if self.yolo_model_flag:
                    if pipline_info[0]["pipline_type"] == "BY":
                        row = 1
                    else:
                        row = 2
                    self.update_table_value(
                        table=self.ui.tableWidget_pipline_info,
                        value=texts.MESSEGES["Part_is_ready"][self.language],
                        row=row,
                    )

        elif pipline_name != "":
            self.ui.create_alert_message(
                title="ERROR",
                message=texts.ERRORS["pipline_info_unfetchable"][self.language],
            )

    def update_pipline_table_info(self, table, titles, language=False):
        """
        update_pipline_table_info for refeshing table in page 2 of pbt

        _extended_summary_

        Parameters
        ----------
        table : _type_
            table obj
        titles : list
            list of string we want dispaly as title of colume one
        language : bool, optional
            _description_, by default False
        """
        table.resizeColumnsToContents()
        table.setColumnCount(2)
        table.setRowCount(len(titles))
        table.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(sQHeaderView.Stretch)
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)
        for i, item in enumerate(titles):
            if language:
                table_item = sQTableWidgetItem(item[self.language])
            else:
                table_item = sQTableWidgetItem(item)
            table.setItem(i, 0, table_item)

    def update_table_value(self, table, value, row, col=1):
        """
        update_table_value used for chage vales of one item in tables

        used for 3 table in page 2 of pbt
        for changeing value of each label in colume two

        Parameters
        ----------
        table : _type_
            table obj ,we want to change value of it
        value : str
            value we want to dispaly on cell of table
        row : int
            number of row of the cell
        col : int, optional
            number of colume of the cell, by default 1
        """
        table_value = sQTableWidgetItem(value)
        table.setItem(row, col, table_value)

    def assign_table_column(self, table, number_of_rows, data_list=None, refresh=True):
        """
        assign_table_column

        used for assigne value of refreshing tables in page 2 of pbt

        Parameters
        ----------
        table : _type_
            table obj
        number_of_rows : int
            number of rows of tabel
        data_list : list, optional
            list of data we want to assinge on tables item, by default None
        refresh : bool, optional
           indicate we want to refesh table or not , by default True
        """
        if refresh:
            for i in range(number_of_rows):
                self.update_table_value(
                    table=table,
                    value="",
                    row=i,
                )
        else:
            for i, item in enumerate(data_list):
                self.update_table_value(
                    table=table,
                    value=str(item),
                    row=i,
                )

    def refresh_loadDataset_tabs_in_PBT(self):
        """
        refresh_loadDataset_tabs_in_PBT used for refresh and reset page one of pbt

        """
        # tabel of data:
        self.update_pipline_table_info(
            table=self.ui.tableWidget_data_info,
            titles=[
                texts.Titles["validation data"][self.language],
                texts.Titles["perfect_pbt"][self.language],
                texts.Titles["defect_pbt"][self.language],
            ],
        )
        # table of pipline:
        self.update_pipline_table_title(
            pipline_name=self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.currentText()
        )
        # combobox updating
        self.ui.cbBox_of_dataset_in_PBT_page_load_dataset.clear()
        self.ui.cbBox_of_dataset_in_PBT_page_load_dataset.addItems(self.PBT_option_list)
        self.add_piplines_in_combobox()
        # checkbox updating
        self.ui.chbox_prefectdata_in_PBT_page.setChecked(False)
        # lineEdit updating
        self.ui.lineEdit_of_path_displayment_in_PBT_page.setText("")

        for i, _ in enumerate(pipelines.MODELS_METRICS["BY"][0]):
            self.update_table_value(
                table=self.ui.binary_table_metrics,
                value="",
                row=i,
            )
        if "Y" in self.pipline_type:
            for i, _ in enumerate(pipelines.MODELS_METRICS["BY"][1]):
                self.update_table_value(
                    table=self.ui.yolo_table_metrics,
                    value="",
                    row=i,
                )
        elif "S" in self.pipline_type:
            for i, _ in enumerate(pipelines.MODELS_METRICS["BSC"][1]):
                self.update_table_value(
                    table=self.ui.segmention_table_metrics,
                    value="",
                    row=i,
                )
        elif "C" in self.pipline_type:
            for i, _ in enumerate(pipelines.MODELS_METRICS["BSC"][2]):
                self.update_table_value(
                    table=self.ui.classification_table_metrics,
                    value="",
                    row=i,
                )
        else:
            print("what happend!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def button_connector(self):
        """this function is used to connet UI buttons to their functionality"""

        self.ui.storage_btn.clicked.connect(lambda: self.show_storage_window(start=False))

        # ______________JJ Zone start
        self.ui.BTN_apply_of_binary_classifaction_in_PBT_page.clicked.connect(
            partial(self.apply_selected_model_after_push_applyBTN_in_PBT_page)
        )
        self.ui.pbt_btn.clicked.connect(
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
        self.ui.pipline_type_rdBTN_BY.toggled.connect(
            lambda: self.set_stackedWidget_in_history_pbt_page(
                self.ui.pipline_type_rdBTN_BY
            )
        )
        self.ui.pipline_type_rdBTN_BS.toggled.connect(
            lambda: self.set_stackedWidget_in_history_pbt_page(
                self.ui.pipline_type_rdBTN_BS
            )
        )
        self.ui.pipline_type_rdBTN_BSC.toggled.connect(
            lambda: self.set_stackedWidget_in_history_pbt_page(
                self.ui.pipline_type_rdBTN_BSC
            )
        )
        self.ui.pipline_type_rdBTN_BSY.toggled.connect(
            lambda: self.set_stackedWidget_in_history_pbt_page(
                self.ui.pipline_type_rdBTN_BSY
            )
        )

        # ______________ JJ

        # self.ui.storage_btn.clicked.connect(self.show_storage_window)
        self.ui.technical_zoom_in.clicked.connect(partial(self.technical_zoom_in))
        self.ui.technical_zoom_out.clicked.connect(partial(self.technical_zoom_out))
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
        self.ui.yolo_train.clicked.connect(partial(self.set_y_parms))
        self.ui.save_dataset_btn.clicked.connect(partial(self.save_train_ds))
        self.ui.save_all_dataset_btn.clicked.connect(partial(self.save_all_train_ds))
        self.ui.heatmap_btn.clicked.connect(partial(self.create_Heatmap))
        self.ui.suggested_defects_btn.clicked.connect(
            partial(self.image_processing_suggest)
        )
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

        self.ui.l_select_prep.clicked.connect(
            partial(self.select_localization_pretrain_path)
        )
        self.ui.l_select_dp.clicked.connect(partial(self.select_localization_dataset))
        self.ui.l_delete_ds.clicked.connect(partial(self.delete_localization_dataset))
        self.ui.l_add_ok.clicked.connect(partial(self.ok_add_localization_ds))

        self.ui.y_select_dp.clicked.connect(partial(self.select_yolo_dataset))
        self.ui.y_delete_ds.clicked.connect(partial(self.delete_yolo_dataset))
        self.ui.y_add_ok.clicked.connect(partial(self.ok_add_yolo_ds))

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
        self.ui.checkBox_suggested_defects.stateChanged.connect(
            partial(self.load_suggestions)
        )

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

        # yolo-model history
        self.ui.yolo_tabel_prev.clicked.connect(
            partial(lambda: self.yolo_model_tabel_nextorprev(next=False))
        )
        self.ui.yolo_tabel_next.clicked.connect(
            partial(lambda: self.yolo_model_tabel_nextorprev(next=True))
        )
        self.ui.Yolo_btn.clicked.connect(
            partial(self.refresh_yolo_models_table_onevent)
        )
        self.ui.yolo_history.clicked.connect(
            partial(self.refresh_yolo_models_table_onevent)
        )
        self.ui.yolo_table_refresh_btn.clicked.connect(
            partial(self.refresh_yolo_models_table_onevent)
        )
        self.ui.yolo_filter_btn.clicked.connect(
            partial(lambda: self.refresh_yolo_models_table(filter_mode=True))
        )
        self.ui.yolo_clearfilter_btn.clicked.connect(partial(self.clear_yolo_filters))

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
        self.ui.BTN_reset_pipline_in_PBT_page.clicked.connect(self.reset_pipline)

        self.ui.BTN_prev_original_image_in_PBT_page.clicked.connect(
            partial(
                lambda: self.update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
                    prevornext="prev", predict_eval=self.image_slider_path
                )
            )
        )
        self.ui.BTN_next_original_image_in_PBT_page.clicked.connect(
            partial(
                lambda: self.update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
                    prevornext="next", predict_eval=self.image_slider_path
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
        self.ui.Yolo_btn.clicked.connect(
            partial(lambda: self.user_access_pages(self.ui.Yolo_btn.objectName()))
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
        # self.ui.show_details_pipline.clicked.connect(self.show_pipline_details_func)
        self.ui.toolButton_binary.clicked.connect(
            lambda: self.load_table_with_btn(self.ui.toolButton_binary.objectName())
        )
        self.ui.toolButton_localization.clicked.connect(
            lambda: self.load_table_with_btn(
                self.ui.toolButton_localization.objectName()
            )
        )
        self.ui.toolButton_classification.clicked.connect(
            lambda: self.load_table_with_btn(
                self.ui.toolButton_classification.objectName()
            )
        )
        self.ui.toolButton_yolo.clicked.connect(
            lambda: self.load_table_with_btn(self.ui.toolButton_yolo.objectName())
        )
        self.ui.history_pbt_btn.clicked.connect(self.laod_bpt_jsons)
        self.ui.pipline_tabel_next_PBT.clicked.connect(self.next_page_pipline_history)
        self.ui.pipline_tabel_prev_PBT.clicked.connect(self.prev_page_pipline_history)
        self.ui.BTN_search_and_filter_in_PBT.clicked.connect(self.json_filter_btn)
        self.ui.BTN_clear_filter_in_PBT.clicked.connect(self.json_clear_filter_btn)

        # plc
        self.ui.connect_plc_btn.clicked.connect(self.connect_plc)
        self.ui.disconnect_plc_btn.clicked.connect(self.disconnect_plc)

        self.ui.line_thickness_slider.valueChanged.connect(
            self.change_label_line_thickness
        )
        self.ui.point_thickness_slider.valueChanged.connect(
            self.change_label_point_thickness
        )

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
            "Yolo_btn": self.ui.page_Yolo,
        }
        if self.logged_in:
            eval(
                'self.ui.set_widget_page(self.ui.stackedWidget,dic["{}"])'.format(
                    btn_name
                )
            )
            for btn in [
                "Binary_btn",
                "Localization_btn",
                "Classification_btn",
                "Yolo_btn",
            ]:
                eval(
                    'self.ui.{}.setStyleSheet("background-color: rgb(230, 230, 230); color: black; text-align:center;")'.format(
                        btn
                    )
                )

            eval(
                'self.ui.{}.setStyleSheet("background-color: rgb(170, 170, 212); color: black; text-align:center;")'.format(
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
        sheet, pos, img_path = self.move_on_list.get_current("selected_imgs_for_label")
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

            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["Sheet_empty"],
                message=texts.MESSEGES["No_sheet_load"]["en"],
                level=1,
            )
            return
        self.move_on_list.add(sheets_id, "sheets_id")
        for sheet_id in sheets_id:
            if sheet_id not in self.sheet_imgprocessing_mem.keys():
                self.sheet_imgprocessing_mem[sheet_id] = False
        self.selected_images_for_label.clear()
        self.ui.clear_table()
        # self.ui.load_sheets_win.close()
        self.load_sheet()
        

        # ----------------------------------------------------------------------------------------

    # load sheet by its id in software
    # ----------------------------------------------------------------------------------------
    def load_sheet(self):
        try:
            selceted_sheets_id = self.move_on_list.get_current(
                "sheets_id"
            )  # get current value on list that corespond to "coils_id" name
            self.sheet = self.db.load_sheet(
                selceted_sheets_id
            )  # load inference of Sheet class from database by sheet id
            self.build_sheet_technical(self.sheet)  # build technical sheet
            self.ui.show_sheet_details(
                self.sheet.get_info_dict()
            )  # show sheet details in UI.details_label
            self.load_filter_params()

            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["Sheet_loaded"],
                message=texts.MESSEGES["sheet_loaded"]["en"],
                level=1,
            )
        except:
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["Sheet_loaded_eror"],
                message=texts.MESSEGES["sheet_load_eror"]["en"],
                level=1,
            )

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

    def load_suggestions(self, state=0):
        if self.ui.checkBox_suggested_defects.isChecked():
            jsons_main_path = self.db.get_suggestions_path()
            jsons_path = pathStructure.sheet_suggestions_path(jsons_main_path, self.sheet.get_id())
            if not os.path.exists(jsons_path):
                self.sheet_imgprocessing_mem[self.sheet.get_id()] = False
                pathStructure.create_sheet_suggestions_path(jsons_main_path, self.sheet.get_id())

            self.ui.set_enabel(self.ui.load_coil_btn, False)
            self.ui.set_enabel(self.ui.next_coil_btn, False)
            self.ui.set_enabel(self.ui.prev_coil_btn, False)
            self.ui.set_enabel(self.ui.checkBox_suggested_defects, False)

            if not self.sheet_imgprocessing_mem[self.sheet.get_id()]:
                self.reset_suggestion_progressbar(self.sheet.get_cameras()[1] * 2 * self.sheet.get_nframe() * 2)

                self.start_suggestion_threads(jsons_main_path=jsons_main_path, n_threads=12)

            else:
                self.reset_suggestion_progressbar(self.sheet.get_cameras()[1] * 2 * self.sheet.get_nframe())
                self.update_technical_with_suggestions()
        else:
            self.build_sheet_technical(self.sheet)

    def start_suggestion_threads(self, jsons_main_path, n_threads):
        self.suggestion_nthreads = n_threads
        self.suggestion_thread_cnt = 0

        step = NCAMERA//n_threads

        self.suggestion_threads = []
        self.suggestion_workers = []

        for i in range(n_threads):
            self.suggestion_threads.append(sQThread())
            self.suggestion_workers.append(
                image_processing_worker.image_processing_worker(
                    n_cameras=((i*step)+1, (i+1)*step),
                    n_frames=(1, self.sheet.get_nframe()),
                    res_main_path=jsons_main_path,
                    sheet_id=self.sheet.get_id(),
                    active_cameras = self.sheet.get_cameras(),
                    img_format=self.sheet.get_image_format(),
                    img_shape=data_grabber.IMAGE_SHAPE,
                    api_obj=self,
                    ui_obj=self.ui,
                    db_obj=self.db,
                )
            )
            self.suggestion_workers[-1].moveToThread(self.suggestion_threads[-1])
            self.suggestion_threads[-1].started.connect(self.suggestion_workers[-1].run_algorithm)
            self.suggestion_workers[-1].finished.connect(self.finish_suggestion_loading_threads)
            self.suggestion_workers[-1].update_progressbar.connect(self.update_suggestion_progressbar)
            self.suggestion_workers[-1].finished.connect(self.suggestion_threads[-1].quit)
            self.suggestion_workers[-1].finished.connect(self.suggestion_workers[-1].deleteLater)
            self.suggestion_threads[-1].finished.connect(self.suggestion_threads[-1].deleteLater)

            self.suggestion_threads[-1].start()

    def finish_suggestion_loading_threads(self):
        self.suggestion_thread_cnt += 1
        if self.suggestion_thread_cnt == self.suggestion_nthreads:
            self.sheet_imgprocessing_mem[self.sheet.get_id()] = True

            self.update_technical_with_suggestions()

    def update_technical_with_suggestions(self):
        # loading_process = subprocess.Popen(['/bin/python3', 'Loading_page/loading.py', self.language])
        for side, _ in self.ui.get_technical(name=False).items():
            self.thechnicals_backend[side].set_show_bboxes()
            # self.thechnicals_backend[side].update_defect()
            self.start_update_defects_threads(self.thechnicals_backend[side], n_threads=1)
            # selecteds = self.selected_images_for_label.get_sheet_side_selections(
            #     str(self.sheet.get_id()), side
            # )

            # self.thechnicals_backend[side].update_selected(selecteds)
            # self.thechnicals_backend[side].update_real_imgs()
            # self.current_technical_side = side
            # self.refresh_thechnical(fp=1)

        # loading_process.terminate()

    def start_update_defects_threads(self, technical_obj, n_threads):
        side  = technical_obj.get_side()
        self.update_defect_workers[side] = []
        self.update_defect_threads[side] = []

        ncamera = technical_obj.sheet.get_cameras()
        nframe = technical_obj.sheet.get_nframe()

        batch_frame = int(np.ceil(nframe / n_threads)) 
        self.update_defect_nthreads = n_threads
        self.update_defect_thread_cnt[side] = 0

        for i in range(n_threads):
            self.update_defect_threads[side].append(sQThread())

            start_cam = ncamera[0]
            end_cam = ncamera[1] + 1

            start_frame = (i*batch_frame)+1
            end_frame = min((i+1)*batch_frame+1, nframe+1)
            
            self.update_defect_workers[side].append( 
                image_processing_worker.update_defects_worker(
                                            technical_obj,
                                            n_cameras=(start_cam, end_cam),
                                            n_frames=(start_frame, end_frame),
                                            )
                                        )
            
            self.update_defect_workers[side][-1].moveToThread(self.update_defect_threads[side][-1])
            self.update_defect_threads[side][-1].started.connect(self.update_defect_workers[side][-1].run)
            self.update_defect_workers[side][-1].finished.connect(self.finish_update_defects_threads(side))
            self.update_defect_workers[side][-1].update_progressbar_update_defects.connect(self.update_suggestion_progressbar2)
            self.update_defect_workers[side][-1].finished.connect(self.update_defect_threads[side][-1].quit)
            self.update_defect_workers[side][-1].finished.connect(self.update_defect_workers[side][-1].deleteLater)
            self.update_defect_threads[side][-1].finished.connect(self.update_defect_threads[side][-1].deleteLater)

            self.update_defect_threads[side][-1].start()

    def finish_update_defects_threads(self, side):
        def func():
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
        return func

    def update_suggestion_progressbar(self):
        self.ui.suggested_defects_progressBar.setValue(
            self.ui.suggested_defects_progressBar.value() + 1
        )
        
    def update_suggestion_progressbar2(self):
        self.ui.suggested_defects_progressBar.setValue(
            self.ui.suggested_defects_progressBar.value() + 1
        )

    def reset_suggestion_progressbar(self, max_value):
        self.ui.suggested_defects_progressBar.setValue(0)
        if max_value:
            self.ui.suggested_defects_progressBar.setMaximum(max_value)
        else:
            self.ui.load_sheets_win.suggested_defects_progressBar.setMaximum(100)

    def update_loading_progressBar(self):
        self.ui.load_sheets_win.loading_progressBar.setValue(
            self.ui.load_sheets_win.loading_progressBar.value() + 1
        )

    def reset_loading_progressBar(self, max_value):
        self.ui.load_sheets_win.loading_progressBar.setValue(0)
        if max_value:
            self.ui.load_sheets_win.loading_progressBar.setMaximum(max_value)
        else:
            self.ui.load_sheets_win.loading_progressBar.setMaximum(100)

    def technical_zoom_in(self):
        current_side = self.current_technical_side
        self.technical_scale = min(self.technical_scale*2, 4)
        for side, _ in self.ui.get_technical(name=False).items():
            self.thechnicals_backend[side].set_zoom_scale(self.technical_scale)
            self.current_technical_side = side
            self.refresh_thechnical(fp=1)

        self.current_technical_side = current_side

    def technical_zoom_out(self):
        current_side = self.current_technical_side
        self.technical_scale = max(self.technical_scale*0.5, 0.125)
        for side, _ in self.ui.get_technical(name=False).items():
            self.thechnicals_backend[side].set_zoom_scale(self.technical_scale)
            self.current_technical_side = side
            self.refresh_thechnical(fp=1)

        self.current_technical_side = current_side

    def build_sheet_technical(self, sheet):
        try:
            self.ui.set_enabel(self.ui.checkBox_suggested_defects, False)
            self.ui.set_enabel(self.ui.next_coil_btn, False)
            self.ui.set_enabel(self.ui.prev_coil_btn, False)
            self.ui.set_enabel(self.ui.load_sheets_win.load_btn, False)
            self.reset_loading_progressBar(sheet.get_nframe()*(sheet.get_cameras()[1]-sheet.get_cameras()[0]+1)*2)
            self.technical_backend = {}
            for side, _ in self.ui.get_technical(name=False).items():
                self.thechnicals_backend[side] = data_grabber.sheetOverView(
                                                            sheet,
                                                            side,  # side of sheet that is UO
                                                            (HEIGHT_FRAME_SIZE * sheet.get_nframe(), WIDTH_TECHNICAL_SIDE),
                                                            (self.sheet.get_nframe(), NCAMERA),
                                                            actives_camera=sheet.get_cameras(),
                                                        )
                
                self.start_technical_loading_threads(self.thechnicals_backend[side], n_threads=5)

        except Exception as e:
            print('*'*20)
            print(e)
            print('*'*20)

    def start_technical_loading_threads(self, technical_obj: data_grabber.sheetOverView, n_threads: int):
        side  = technical_obj.get_side()
        self.technical_workers[side] = []
        self.technical_threads[side] = []

        ncamera = technical_obj.sheet.get_cameras()
        nframe = technical_obj.sheet.get_nframe()

        batch_frame = int(np.ceil(nframe / n_threads)) 
        self.technical_nthreads = n_threads
        self.technical_thread_cnt[side] = 0
        self.close_technical_nside = 2
        self.close_technical_cnt = 0

        for i in range(n_threads):
            self.technical_threads[side].append(sQThread())

            start_cam = ncamera[0]
            end_cam = ncamera[1] + 1

            start_frame = (i*batch_frame)+1
            end_frame = min((i+1)*batch_frame+1, nframe+1)
            
            self.technical_workers[side].append( 
                technical_load_sheet_worker(
                                            technical_obj,
                                            camera_range=(start_cam, end_cam),
                                            frame_range=(start_frame, end_frame),
                                            )
                                        )
            
            self.technical_workers[side][-1].moveToThread(self.technical_threads[side][-1])
            self.technical_threads[side][-1].started.connect(self.technical_workers[side][-1].run)
            self.technical_workers[side][-1].finished.connect(self.finish_technical_loading_threads(side))
            self.technical_workers[side][-1].update_progressbar.connect(self.update_loading_progressBar)
            self.technical_workers[side][-1].finished.connect(self.technical_threads[side][-1].quit)
            self.technical_workers[side][-1].finished.connect(self.technical_workers[side][-1].deleteLater)
            self.technical_threads[side][-1].finished.connect(self.technical_threads[side][-1].deleteLater)

            self.technical_threads[side][-1].start()

    def finish_technical_loading_threads(self, side):
        def func():
            self.technical_thread_cnt[side] += 1
            if self.technical_thread_cnt[side] == self.technical_nthreads:
                selecteds = self.selected_images_for_label.get_sheet_side_selections(
                        str(self.sheet.get_id()), side
                    )
                self.thechnicals_backend[side].update_selected(selecteds)
                self.current_technical_side = side
                self.refresh_thechnical(fp=1)  
                self.close_load_sheet_win()
        return func
    
    def close_load_sheet_win(self):
        self.close_technical_cnt += 1
        if self.close_technical_cnt == self.close_technical_nside:
            self.ui.load_sheets_win.close()
            self.ui.set_enabel(self.ui.checkBox_suggested_defects, True)
            self.ui.set_enabel(self.ui.next_coil_btn, True)
            self.ui.set_enabel(self.ui.prev_coil_btn, True)
            self.ui.set_enabel(self.ui.load_sheets_win.load_btn, True)
            self.ui.set_enabel(self.ui.technical_zoom_in, True)
            self.ui.set_enabel(self.ui.technical_zoom_out, True)
            if self.ui.checkBox_suggested_defects.isChecked():
                self.load_suggestions()

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


        current_cam = self.thechnicals_backend[
            self.current_technical_side
        ].actives_camera[1]

        if self.baselines==None:
            self.baselines = self.db.get_baselines()
        current =0
        current = self.baselines[current_cam-1]
        if current_cam>1:
            current += (self.baselines[current_cam-1] - self.baselines[current_cam-2])/2
            # current+=self.baselines[1]
            x = current*x



        n_frame = self.thechnicals_backend[self.current_technical_side].sheet.get_nframe()
        h,w,base = self.db.get_camera_config()
        y*=n_frame*base/(w/2)*h   

        # x *= self.sheet.get_width()
        # y *= self.sheet.get_length()
        y = np.round(y, 1)
        x = np.round(x, 1)
        self.ui.show_current_position((x, y))

    def update_technical_pointer_keyboard(self, key):
        self.thechnicals_backend[self.current_technical_side].update_pointer_keyboard(
            key
        )
        self.refresh_thechnical(fp=1)
        self.show_pointer_position()
        print( self.thechnicals_backend[self.current_technical_side].get_pos())

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
            self.refresh_thechnical(fp=1)
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
            # self.ui.close_loading_page()
            self.ui.load_sheets_win.set_warning(
                texts.MESSEGES["refresh_success"][self.language], level=1
            )
        except:
            self.ui.load_sheets_win.set_warning(
                texts.ERRORS["refresh_failed"][self.language], level=3
            )
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["Sheet_page_eror"],
                message=texts.MESSEGES["sheet_page_eror"]["en"],
                level=5,
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
            cameras = list(range(self.sheet.cameras[0], int(self.sheet.cameras[1]) + 1))
            frames = list(range(1, self.sheet.nframe + 1))
        else:
            s = self.ui.comboBox_side_SI.currentText()
            if s == "TOP":
                side = ["up"]
            elif s == "BOTTOM":
                side = ["down"]
            elif s == "BOTH":
                side = ["up", "down"]
            if self.ui.checkBox_all_camera_SI.isChecked():
                cameras = list(
                    range(self.sheet.cameras[0], int(self.sheet.cameras[1] + 1))
                )
            else:
                cameras = self.ui.comboBox_ncamera_SI.getValue()
                cameras = list(map(int, cameras))
            if self.ui.checkBox_all_frame_SI.isChecked():
                frames = list(range(1, self.sheet.nframe + 1))
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
            cameras = list(range(self.sheet.cameras[0], self.sheet.cameras[1] + 1))
            frames = list(range(1, self.sheet.nframe + 1))
        else:
            s = self.ui.comboBox_side_SI.currentText()
            if s == "TOP":
                side = ["up"]
            elif s == "BOTTOM":
                side = ["down"]
            elif s == "BOTH":
                side = ["up", "down"]
            if self.ui.checkBox_all_camera_SI.isChecked():
                cameras = list(range(self.sheet.cameras[0], self.sheet.cameras[1] + 1))
            else:
                cameras = self.ui.comboBox_ncamera_SI.getValue()
                cameras = list(map(int, cameras))
            if self.ui.checkBox_all_frame_SI.isChecked():
                frames = list(range(1, self.sheet.nframe + 1))
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

            x = main_path.split("/")
            path = pathStructure.sheet_image_path(x[0], x[-1], side, cam, frame, ".png")

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

            # self.ds.save_to_temp(paths, sheets, filtered_selected)

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
                        f.append(
                            [
                                i["class"],
                                np.array(i["mask"]),
                                i["line_thickness"],
                                i["point_thickness"],
                            ]
                        )
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
                img = np.zeros((1024, 1792, 3), dtype='uint8')
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
                    f.append(
                        [
                            i["class"],
                            np.array(i["mask"]),
                            i["line_thickness"],
                            i["point_thickness"],
                        ]
                    )
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
        _, _, img_path = self.move_on_list.get_current("selected_imgs_for_label")
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
        _, _, img_path = self.move_on_list.get_current("selected_imgs_for_label")
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

                elif ret == "editing":
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
            sheet, pos, img_path = self.move_on_list.get_current(
                "selected_imgs_for_label"
            )
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
            if self.ui.mask_table_widget.item(i, 0).checkState() == Qt.Checked:
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
        try:
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

            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["Logout_successfully"],
                message=texts.MESSEGES["Logout_successfully"]["en"],
                level=1,
            )

        except:
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["Logout_unsuccessfully"],
                message=texts.MESSEGES["Logout_unsuccessfully"]["en"],
                level=5,
            )

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
        if (
            self.ui.stackedWidget_2.currentIndex() != 0
            and self.ui.stackedWidget_2.currentIndex() != 3
        ):
            chart_funcs.update_userprofile_piechart(
                ui_obj=self.ui, binary_len=binary_count
            )
            classification_count = self.ds_json.get_classification_count(
                os.path.join(
                    self.datasets[current]["path"],
                    self.datasets[current]["name"] + ".json",
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
        if (
            self.ui.stackedWidget_2.currentIndex() != 0
            and self.ui.stackedWidget_2.currentIndex() != 3
        ):
            chart_funcs.update_userprofile_piechart(
                ui_obj=self.ui, binary_len=binary_count
            )
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
                texts.MESSEGES["SET_DATASET"][self.language],
                "profile",
                texts_codes.SubTypes["SET_DATASET"],
                level=1,
            )
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["SET_DATASET"],
                message=texts.MESSEGES["SET_DATASET"]["en"],
                level=1,
            )
            self.ui.set_b_default_db_parms(self.ds.dataset_path)
            self.ui.set_l_default_db_parms(self.ds.dataset_path)
            self.ui.set_y_default_db_parms(self.ds.dataset_path)
        except:
            self.ui.set_warning(
                texts.ERRORS["SET_DATASET_FAILED"][self.language],
                "profile",
                texts_codes.SubTypes["SET_DATASET_FAILED"],
                level=3,
            )
            self.ui.logger.create_new_log(
                code=texts_codes.SubTypes["SET_DATASET_FAILED"],
                message=texts.ERRORS["SET_DATASET_FAILED"]["en"],
                level=5,
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
                    texts_codes.SubTypes["CREATE_DATASET_EXIST"],
                    level=2,
                )
                self.ui.logger.create_new_log(
                    message=texts.WARNINGS["CREATE_DATASET_EXIST"]["en"],
                    code=texts_codes.SubTypes["CREATE_DATASET_EXIST"],
                    level=2,
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
                    texts.MESSEGES["CREATE_DATASET"][self.language],
                    "profile",
                    texts_codes.SubTypes["CREATE_DATASET"],
                    level=1,
                )
                self.ui.logger.create_new_log(
                    message=texts.MESSEGES["CREATE_DATASET"]["en"],
                    code=texts_codes.SubTypes["CREATE_DATASET"],
                    level=1,
                )
            except:
                self.ui.set_warning(
                    texts.ERRORS["CREATE_DATASET_FAILED"][self.language],
                    "profile",
                    texts_codes.SubTypes["CREATE_DATASET_FAILED"],
                    level=3,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["CREATE_DATASET_FAILED"]["en"],
                    code=texts_codes.SubTypes["CREATE_DATASET_FAILED"],
                    level=5,
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

        

        # return




        if self.widget_name == "down_side_technical":
            x, y = self.obj_sheet_down.get_pos()

            self.baselines


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
        if not self.running_b_model:
            # #print('statrt training binary model')
            b_parms = self.ui.get_binary_parms()
            if not b_parms:
                return

            # update chart axis given train data
            self.update_b_chart_axis(b_parms[3])

            self.bmodel_train_thread = sQThread()
            # Step 3: Create a worker object
            self.bmodel_train_worker = binary_model_funcs.Binary_model_train_worker()
            self.bmodel_train_worker.assign_parameters(
                b_parms=b_parms,
                api_obj=self,
                ui_obj=self.ui,
                db_obj=self.db,
                ds_obj=self.ds,
            )
            # Step 4: Move worker to the thread
            self.bmodel_train_worker.moveToThread(self.bmodel_train_thread)
            # Step 5: Connect signals and slots
            self.bmodel_train_thread.started.connect(
                self.bmodel_train_worker.train_model
            )
            self.bmodel_train_worker.finished.connect(self.bmodel_train_thread.quit)
            self.bmodel_train_worker.finished.connect(
                self.bmodel_train_worker.show_bmodel_train_result
            )
            self.bmodel_train_worker.finished.connect(
                self.bmodel_train_worker.deleteLater
            )
            self.bmodel_train_thread.finished.connect(
                self.bmodel_train_thread.deleteLater
            )

            self.bmodel_train_worker.warning.connect(self.ui.set_warning)
            self.bmodel_train_worker.reset_progressbar.connect(
                self.reset_binary_train_progressBar
            )
            self.bmodel_train_worker.set_progressbar.connect(
                self.set_binary_train_progressBar
            )
            self.bmodel_train_worker.update_charts.connect(
                self.assign_new_value_to_b_chart
            )

            # Step 6: Start the thread
            self.running_b_model = True
            self.bmodel_train_thread.start()

            self.ui.binary_train.setEnabled(False)

    def reset_binary_train_progressBar(self, value, text):
        self.ui.binary_train_progressBar.setValue(0)
        self.ui.binary_train_progressBar.setMaximum(value)
        self.ui.binary_train_progressBar_label.setText(text + " ... ")

    def set_binary_train_progressBar(self):
        self.ui.binary_train_progressBar.setValue(
            self.ui.binary_train_progressBar.value() + 1
        )

    def update_b_chart_axis(self, nepoch):
        chart_funcs.update_axisX_range(ui_obj=self.ui, nepoch=nepoch)
        chart_funcs.clear_series_date(
            ui_obj=self.ui, chart_postfixes=self.ui.chart_names
        )
        self.ui.binary_chart_checkbox.setEnabled(True)

    def assign_new_value_to_b_chart(self, last_epoch, logs):
        try:
            chart_funcs.update_chart(
                ui_obj=self.ui,
                chart_postfixes=self.ui.chart_names,
                last_epoch=last_epoch,
                logs=logs,
                scroll_obj=self.ui.binary_chart_scrollbar,
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["UPDATE_BCHART"]["en"].format(last_epoch)
            )
        except:
            self.ui.logger.create_new_log(
                message=texts.ERRORS["UPDATE_BCHART_FAILED"]["en"].format(last_epoch),
                level=5,
            )
            self.ui.set_warning(
                texts.ERRORS["UPDATE_BCHART_FAILED"][self.language].format(last_epoch),
                "train",
                None,
                3,
            )

    def set_l_parms(self):
        if not self.running_l_model:
            l_parms = self.ui.get_localization_parms()
            if not l_parms:
                return

            # update chart axis given train data
            self.update_l_chart_axis(l_parms[4])

            self.lmodel_train_thread = sQThread()
            # Step 3: Create a worker object
            self.lmodel_train_worker = (
                localization_model_funcs.Localization_model_train_worker()
            )
            self.lmodel_train_worker.assign_parameters(
                l_parms=l_parms,
                api_obj=self,
                ui_obj=self.ui,
                db_obj=self.db,
                ds_obj=self.ds,
            )
            # Step 4: Move worker to the thread
            self.lmodel_train_worker.moveToThread(self.lmodel_train_thread)
            # Step 5: Connect signals and slots
            self.lmodel_train_thread.started.connect(
                self.lmodel_train_worker.train_model
            )
            self.lmodel_train_worker.finished.connect(self.lmodel_train_thread.quit)
            self.lmodel_train_worker.finished.connect(
                self.lmodel_train_worker.show_lmodel_train_result
            )
            self.lmodel_train_worker.finished.connect(
                self.lmodel_train_worker.deleteLater
            )
            self.lmodel_train_thread.finished.connect(
                self.lmodel_train_thread.deleteLater
            )

            self.lmodel_train_worker.warning.connect(self.ui.set_warning)
            self.lmodel_train_worker.reset_progressbar.connect(
                self.reset_localization_train_progressBar
            )
            self.lmodel_train_worker.set_progressbar.connect(
                self.set_localization_train_progressBar
            )
            self.lmodel_train_worker.update_charts.connect(
                self.assign_new_value_to_l_chart
            )

            # Step 6: Start the thread
            self.running_l_model = True
            self.lmodel_train_thread.start()

            self.ui.localization_train.setEnabled(False)

    def reset_localization_train_progressBar(self, value, text):
        self.ui.localization_train_progressBar.setValue(0)
        self.ui.localization_train_progressBar.setMaximum(value)
        self.ui.localization_train_progressBar_label.setText(text + " ... ")

    def set_localization_train_progressBar(self):
        self.ui.localization_train_progressBar.setValue(
            self.ui.localization_train_progressBar.value() + 1
        )

    def update_l_chart_axis(self, nepoch):
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
            chart_funcs.update_chart(
                ui_obj=self.ui,
                chart_postfixes=self.ui.loc_chart_names,
                last_epoch=last_epoch,
                logs=logs,
                scroll_obj=self.ui.localization_chart_scrollbar,
                chart_type="localization",
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["UPDATE_LCHART"]["en"].format(last_epoch)
            )
        except:
            self.ui.logger.create_new_log(
                message=texts.ERRORS["UPDATE_LCHART_FAILED"]["en"].format(last_epoch),
                level=5,
            )
            self.ui.set_warning(
                texts.ERRORS["UPDATE_LCHART_FAILED"][self.ui.language].format(
                    last_epoch
                ),
                "l_train",
                None,
                3,
            )

    def set_y_parms(self):
        if not self.running_y_model:
            y_parms = self.ui.get_yolo_parms()
            if not y_parms:
                return

            # update chart axis given train data
            self.update_yolo_chart_axis(y_parms[3])

            self.ymodel_train_thread = sQThread()
            # Step 3: Create a worker object
            self.ymodel_train_worker = yolo_model_funcs.Yolo_model_train_worker()
            self.ymodel_train_worker.assign_parameters(
                y_parms=y_parms,
                api_obj=self,
                ui_obj=self.ui,
                db_obj=self.db,
                ds_obj=self.ds,
            )
            # Step 4: Move worker to the thread
            self.ymodel_train_worker.moveToThread(self.ymodel_train_thread)
            # Step 5: Connect signals and slots
            self.ymodel_train_thread.started.connect(
                self.ymodel_train_worker.train_model
            )
            self.ymodel_train_worker.finished.connect(self.ymodel_train_thread.quit)
            self.ymodel_train_worker.finished.connect(
                self.ymodel_train_worker.show_ymodel_train_result
            )
            self.ymodel_train_worker.finished.connect(
                self.ymodel_train_worker.deleteLater
            )
            self.ymodel_train_thread.finished.connect(
                self.ymodel_train_thread.deleteLater
            )

            self.ymodel_train_worker.warning.connect(self.ui.set_warning)
            self.ymodel_train_worker.reset_progressbar.connect(
                self.reset_yolo_train_progressBar
            )
            self.ymodel_train_worker.set_progressbar.connect(
                self.set_yolo_train_progressBar
            )
            self.ymodel_train_worker.update_charts.connect(
                self.assign_new_value_to_yolo_chart
            )

            # Step 6: Start the thread
            self.running_y_model = True
            self.ymodel_train_thread.start()

            self.ui.yolo_train.setEnabled(False)

    def reset_yolo_train_progressBar(self, value, text):
        self.ui.yolo_train_progressBar.setValue(0)
        self.ui.yolo_train_progressBar.setMaximum(value)
        self.ui.yolo_train_progressBar_label.setText(text + " ... ")

    def set_yolo_train_progressBar(self):
        self.ui.yolo_train_progressBar.setValue(
            self.ui.yolo_train_progressBar.value() + 1
        )

    def update_yolo_chart_axis(self, nepoch):
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
            ui_obj=self.ui, chart_postfixes=self.ui.yolo_chart_names
        )
        self.ui.yolo_chart_checkbox.setEnabled(True)
        # self.ui.localization_chart_checkbox.setChecked(True)

    def assign_new_value_to_yolo_chart(self, last_epoch, logs):
        try:
            chart_funcs.update_chart(
                ui_obj=self.ui,
                chart_postfixes=self.ui.yolo_chart_names,
                last_epoch=last_epoch,
                logs=logs,
                scroll_obj=self.ui.yolo_chart_scrollbar,
                chart_type="yolo",
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["UPDATE_YCHART"]["en"].format(last_epoch)
            )
        except:
            self.ui.logger.create_new_log(
                message=texts.ERRORS["UPDATE_YCHART_FAILED"]["en"].format(last_epoch),
                level=5,
            )
            self.ui.set_warning(
                texts.ERRORS["UPDATE_YCHART_FAILED"][self.ui.language].format(
                    last_epoch
                ),
                "y_train",
                None,
                3,
            )

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
        self.worker.assign_parameters(api_obj=self, count=count)
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
        self.ui.save_all_dataset_btn.setEnabled(False)
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
        self.ui.save_all_dataset_btn.setEnabled(True)

    def update_save_all_progressbar(self):
        self.ui.save_all_progressBar.setValue(self.ui.save_all_progressBar.value() + 1)

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

        self.ui.select_ds_dialog.ok_btn.clicked.connect(
            lambda: self.ok_selected_binary_datasets(page)
        )
        self.ui.select_ds_dialog.show()

    def ok_selected_binary_datasets(self, page="train"):
        selecteds = self.ui.select_ds_dialog.get_select_datasets()

        for selected in selecteds:
            dname = selected
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
        dname = QFileDialog.getOpenFileName(
            self.l_select_pre_dialog, "open", path, filter
        )[0]

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

        self.ui.select_ds_dialog.ok_btn.clicked.connect(
            lambda: self.ok_selected_localization_datasets(page)
        )
        self.ui.select_ds_dialog.show()

    def ok_selected_localization_datasets(self, page="l_train"):
        selecteds = self.ui.select_ds_dialog.get_select_datasets()

        for selected in selecteds:
            dname = selected
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

    def select_yolo_dataset(self, page="y_train"):
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

        self.ui.select_ds_dialog.ok_btn.clicked.connect(
            lambda: self.ok_selected_yolo_datasets(page)
        )
        self.ui.select_ds_dialog.show()

    def ok_selected_yolo_datasets(self, page="y_train"):
        selecteds = self.ui.select_ds_dialog.get_select_datasets()

        for selected in selecteds:
            dname = selected
            if not self.ds.check_yolo_dataset(dname):
                self.ui.set_warning(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], page, level=2
                )
                return
            #
            if page == "y_train":
                text = self.ui.y_dp.toPlainText()
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
                self.ui.y_dp.setPlainText(text + str(n) + ". " + dname)
                #
            elif page == "binarylist":
                self.ui.binarylist_dataset_lineedit.setText(dname)
                self.ui.binarylist_dataset_annot_lineedit.setText(dname)

    def delete_yolo_dataset(self):
        ds_n = self.ui.y_ds_num.value() - 1
        text = self.ui.y_dp.toPlainText()
        pattern = r"[0-9]+. "
        datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]
        if ds_n >= len(datasets):
            self.ui.set_warning(
                texts.WARNINGS["DATASET_NUMBER"][self.language], "y_train", level=2
            )
            return
        datasets.pop(ds_n)
        text = ""
        for i in range(len(datasets)):
            text += str(i + 1) + ". " + datasets[i]
            if i != len(datasets) - 1:
                text += "\n"

        self.ui.y_dp.setPlainText(text)

    def ok_add_yolo_ds(self):
        path = self.ui.y_add_ds_lineedit.text().lstrip()
        path = path.rstrip()
        if not os.path.exists(path):
            self.ui.set_warning(
                texts.WARNINGS["INVALID_DATASET"][self.language], "y_train", level=2
            )
            return
        elif not self.ds.check_yolo_dataset(path):
            self.ui.set_warning(
                texts.WARNINGS["DATASET_FORMAT"][self.language], "y_train", level=2
            )
            return

        text = self.ui.y_dp.toPlainText()
        pattern = r"[0-9]+. "

        datasets = [os.path.abspath(s.rstrip()) for s in re.split(pattern, text)[1:]]

        if os.path.abspath(path) in datasets:
            self.ui.set_warning(
                texts.WARNINGS["DATASET_EXIST"][self.language], "y_train", level=2
            )
        else:
            n = len(datasets) + 1
            if text != "":
                text += " \n"
            self.ui.y_dp.setPlainText(text + str(n) + ". " + path)
        self.ui.y_add_ds_lineedit.setText("")

        height = self.ui.y_add_ds_frame.height()
        if height == 67:
            self.left_box = QPropertyAnimation(self.ui.y_add_ds_frame, b"maximumHeight")
            self.left_box.setDuration(Settings.TIME_ANIMATION)
            self.left_box.setStartValue(100)
            self.left_box.setEndValue(0)
            self.left_box.setEasingCurve(QEasingCurve.InOutQuart)
            self.group = QParallelAnimationGroup()
            self.group.addAnimation(self.left_box)
            self.group.start()

    # -------------------------------------------Camera conection and show ----------------------------------------

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
        print(selected_cameras)

        self.camera_threads = []
        self.ret_dict ={}
        for cam_num , cam in enumerate(selected_cameras):
            if cam:
                cam_parms = self.get_camera_config(str(cam_num+1))
                thread = threading.Thread(target=self.cameras.add_camera,args=(str(cam_num+1), cam_parms,self.ret_dict,self.ui.logger))
                thread.start()
                self.camera_threads.append(thread)
        
        self.set_btns(False)
        threading.Thread(target=self.check_finished).start()


    def set_btns(self,mode):
        self.ui.set_buttons_enable_or_disable(
            [self.ui.disconnect_camera_btn, self.ui.connect_camera_btn],
            enable=mode,
        )
        self.ui.checkBox_top.setEnabled(mode)
        self.ui.checkBox_bottom.setEnabled(mode)
        self.ui.checkBox_all.setEnabled(mode)
        for i in range(1, 25):
            if i < 10:
                btn_name = eval("self.ui.camera0%s_btn" % i)
            else:
                btn_name = eval("self.ui.camera%s_btn" % i)
            btn_name.setEnabled(mode)


    def check_finished(self):
        for thread in self.camera_threads:
            thread.join()
        self.update_camera_ui()
        
    def update_camera_ui(self):
        self.set_available_cameras()
        self.start_grab_camera()

        myKeys = list(self.ret_dict.keys())
        myKeys.sort()
        sorted_dict = {i: self.ret_dict[i] for i in myKeys}

        for cam_id, value in zip(sorted_dict.keys(),sorted_dict.values()):
            if value[0]:
                self.ui.set_img_btn_camera(cam_id)
            else:
                self.ui.set_img_btn_camera(cam_id, status="False")
        self.set_btns(True)


    def connect_camera_old(self):
        """
        This camera is used to connect selected cameras
        """
        selected_cameras = self.ui.get_selected_cameras()

        if not any(selected_cameras):
            self.ui.set_warning(
                texts.WARNINGS["no_camera_selected"][self.ui.language],
                "camera_connection",
                level=2,
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
            # threading.Thread(target=self.cameras.add_camera,args=(str(cam_num), cam_parms))

            if ret == "True":
                self.ui.set_warning(
                    texts.MESSEGES["Camera_successful"][self.ui.language].format(
                        cam_num
                    ),
                    "camera_connection",
                    level=1,
                )
                self.ui.set_img_btn_camera(cam_num)

            else:
                if ret == "Camera Not Connected":
                    self.ui.set_warning(
                        texts.ERRORS["Camera_serial_error"][self.ui.language].format(
                            cam_num
                        ),
                        "camera_connection",
                        level=3,
                    )
                else:
                    self.ui.set_warning(
                        texts.ERRORS["control_config_error"][self.ui.language].format(
                            cam_num
                        ),
                        "camera_connection",
                        level=3,
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
                self.start_grab_camera()
                return
            if selected_cameras[self.i]:
                QTimer.singleShot(1, self.connect_camera)  # defult time 3000
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
                level=2,
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
                    level=1,
                )
                self.ui.set_img_btn_camera(cam_num, status="Disconnect")

            elif ret == "no_connection":
                self.ui.set_warning(
                    texts.ERRORS["no_connect"][self.ui.language].format(cam_num),
                    "camera_connection",
                    level=3,
                )

            else:
                self.ui.set_warning(
                    texts.ERRORS["disconnect_error"][self.ui.language].format(cam_num),
                    "camera_connection",
                    level=3,
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
                QTimer.singleShot(1, self.disconnect_camera)  # defult time 3000
                return

    def set_available_cameras(self):
        connected_cameras = self.cameras.get_connected_cameras_by_id()
        sn_available = sorted(list(connected_cameras.keys()))
        # sn_available = [str(i) for i in range(1, 25)]
        self.ui.comboBox_connected_cams.clear()
        self.ui.comboBox_connected_cams.addItems(sn_available)
        val = self.ui.comboBox_connected_cams.currentText()
        self.change_live_camera(val)

    def start_grab_camera(self):
        connected_cameras = self.cameras.get_connected_cameras_by_id()
        for camera in connected_cameras:
            # print('grabed')
            connected_cameras[camera].start_grabbing()

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
            # self.grab_timer = QTimer(self.ui)
            # self.grab_timer.timeout.connect(self.grab_image)
            # self.grab_main_thread = threading.Thread(target=self.run_grab)
            self.ImageManager.first_check_finished.connect(self.start_capture_timers)
            self.ImageManager.second_check_finished.connect(self.stop_capture_timers)
            # self.start_capture_flag = True
            self.ready_capture_flag = True

        if self.sensor and not disable_ui:
            self.start_capture_flag = True
            self.ImageManager.set_live_type(self.live_type)
            self.ImageManager.set_save_flag(self.ui.checkBox_save_images.isChecked())
            self.ImageManager.set_manual_flag(self.ui.manual_camera)
            # self.ui.set_enabel(self.ui.stop_capture_btn, False)
            # QTimer().singleShot(1000, self.ImageManager.start_sheet_checking)
            # QTimer().singleShot(1000, lambda: self.ui.set_enabel(self.ui.stop_capture_btn, True))
            # self.ImageManager.start_sheet_checking()
            self.start_capture_timers()
            # self.init_check_plc()

    def stop_capture_func(self, disable_ui=True):
        if disable_ui:
            self.ui.set_enabel(self.ui.connect_camera_btn, True)
            self.ui.set_enabel(self.ui.disconnect_camera_btn, True)
            self.ui.set_enabel(self.ui.start_capture_btn, True)
            self.ui.set_enabel(self.ui.stop_capture_btn, False)
            self.ready_capture_flag = False
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
        # try:
        #     self.ImageManager.stop_sheet_checking()
        # except:
        #     pass
        if self.l2_connection.last_speed:
            self.ImageManager.start()
        self.live_timer.start(self.ui.update_timer_live_frame)
        self.grab_main_thread = threading.Thread(target=self.run_grab)
        self.grab_main_thread.start()
            # self.grab_timer.start(int(1000/(self.ui.frame_rate)))

    def stop_capture_timers(self):
        self.ImageManager.stop()
        self.live_timer.stop()
        self.stop_grab_image()

    def run_grab(self):
        while True:
            if self.stop_grab:
                return
            self.grab_time = time.time()
            self.grab_image()
            self.grab_time = time.time() - self.grab_time
            if self.stop_grab:
                return
            t = 1/self.ui.frame_rate
            if self.grab_time<t:
                time.sleep(t - self.grab_time)

    def grab_image(self):
        self.ImageManager.stop()
        if self.l2_connection.last_speed:
            self.ImageManager.start()

    def stop_grab_image(self):
        if self.grab_main_thread:
            self.stop_grab = True
            self.grab_main_thread.join()
        self.stop_grab = False

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
        """
        refresh_binary_models_table_onevent _summary_

        this function  used for refreshing and loading data of table

        Parameters
        ----------
        wich_page : str, optional
            this value set that function used update ui of pbt part or other part,
            for using in pbt pass PBT string as value_, by default "not PBT"
        """
        self.bmodel_tabel_itr = 1
        if wich_page == "PBT":
            self.ui.lineEdit_of_pageNumber_displayment_in_PBT_page.setText(
                str(self.bmodel_tabel_itr)
            )
            self.ui.refresh_pipline_tabs_in_PBT()

            # __________________________
            self.ui.radioButton_use_yolo.setChecked(True)
            self.ui.radioButton_use_unet.setChecked(False)
            self.set_pipline_mode("yolo")
            self.load_table_with_btn(self.ui.toolButton_binary.objectName())
            self.load_table_with_btn(self.ui.toolButton_yolo.objectName())
            # __________________________

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
            self.ui.LBL_tabel_title.setText("Binary Models")
        elif model_type == "classification":
            model_type_ = "classification_models"
            self.ui.LBL_tabel_title.setText("Classification Models")
        elif model_type == "localization":
            model_type_ = "localization_models"
            self.ui.LBL_tabel_title.setText("Localization Models")
        elif model_type == "yolo":
            model_type_ = "yolo_models"
            self.ui.LBL_tabel_title.setText("Yolo Models")
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
                    ui_obj=self.ui,
                    bmodels_list=bmodels_list,
                    model_type=model_type,
                    language=self.language,
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
            self.load_binary_images_list_in_PBT_load_dataset_page(
                use_customized_flag=True
            )
        else:
            self.ui.LBL_data_is_ready.setFixedHeight(0)
            self.assign_table_column(
                table=self.ui.tableWidget_data_info, number_of_rows=3
            )
            self.ui.create_alert_message(
                title="WARNING",
                message=texts.ERRORS["data_not_ready"][self.language],
            )

    def load_binary_images_list_in_PBT_load_dataset_page(
        self, use_customized_flag=False
    ):
        if use_customized_flag:
            selected_datasets = self.customized_datasets
            text = "Customized"
        else:
            text = self.ui.cbBox_of_dataset_in_PBT_page_load_dataset.currentText()
            selected_datasets = dataset.get_selected_datasets_for_PBT_loadDataSet_page(
                text, self.datasets_list
            )
        if len(selected_datasets) == 0:
            self.ui.set_warning(
                texts.WARNINGS["SELECT_NO_DATASET"][self.language],
                "binarylist",
                level=2,
            )
            self.ui.create_alert_message(
                title="WARNING",
                message=texts.WARNINGS["SELECT_NO_DATASET"][self.language],
            )
            return

        self.selected_datasets = selected_datasets
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
            self.path_list = []
            self.update_table_value(
                table=self.ui.tableWidget_data_info,
                value="",
                row=0,
            )
            self.update_table_value(
                table=self.ui.tableWidget_data_info,
                value="",
                row=1,
            )
            self.update_table_value(
                table=self.ui.tableWidget_data_info,
                value="",
                row=2,
            )
            self.ui.LBL_data_is_ready.setFixedHeight(30)
            self.ui.LBL_data_is_ready.setText(
                texts.MESSEGES["Data_Is_Not_Ready"][self.language]
            )
            self.ui.LBL_data_is_ready.setStyleSheet(
                            "color: rgb(170, 0, 0);"
                        )


            self.ui.set_warning(
                texts.MESSEGES["NO_IMAGE_AVAILABLE_IN_DATASET"][self.language],
                "binarylist",
                level=2,
            )
            self.ui.create_alert_message(
                title="WARNING",
                message=texts.MESSEGES["NO_IMAGE_AVAILABLE_IN_DATASET"][self.language],
            )
        else:
            # msg
            self.ui.set_warning(
                texts.MESSEGES["LOAD_IMAGES_DATASETS"][self.language],
                "binarylist",
                level=1,
            )
            if self.perfect_show:
                self.path_list = perfect_image_pathes + defect_image_pathes
            else:
                self.path_list = defect_image_pathes
            random.shuffle(self.path_list)
            self.update_table_value(
                table=self.ui.tableWidget_data_info,
                value=str(len(self.path_list)),
                row=0,
            )
            self.update_table_value(
                table=self.ui.tableWidget_data_info,
                value=str(binary_count["perfect"]),
                row=1,
            )
            self.update_table_value(
                table=self.ui.tableWidget_data_info,
                value=str(binary_count["defect"]),
                row=2,
            )
            self.ui.LBL_data_is_ready.setFixedHeight(30)
            self.ui.LBL_data_is_ready.setText(
                texts.MESSEGES["Data_Is_Ready"][self.language]
            )
            self.ui.LBL_data_is_ready.setStyleSheet(
                            "color: rgb(0, 170, 0);"
                        )
            
            self.data_is_ready = True
            if self.pipline_is_ready:
                self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(True)

    def evaluation_ui_update(self, metrics_info, image_slider_path):
        """this function after evaluation operation completed

        Parameters
        ----------
        metrics_info : list
            dictionary of evalution reports of each pipline's part
        """

        for i, metrics in enumerate(metrics_info["binary"]):
            self.update_table_value(
                table=self.ui.binary_table_metrics,
                value=str(metrics),
                row=i,
            )
        if "Y" in self.pipline_type:
            for i, metrics in enumerate(metrics_info["yolo"]):
                self.update_table_value(
                    table=self.ui.yolo_table_metrics,
                    value=str(metrics),
                    row=i,
                )
        elif "S" in self.pipline_type:
            for i, metrics in enumerate(metrics_info["segmention"]):
                self.update_table_value(
                    table=self.ui.segmention_table_metrics,
                    value=str(metrics),
                    row=i,
                )
        elif "C" in self.pipline_type:
            for i, metrics in enumerate(metrics_info["classification"]):
                self.update_table_value(
                    table=self.ui.classification_table_metrics,
                    value=str(metrics),
                    row=i,
                )
        else:
            print("what happend!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # ________________slider data_________________#
        self.original_and_evaluated_image_in_PBT.add(
            mylist=list(image_slider_path.keys()),
            name="original",
        )
        self.original_image_list_next_func = (
            self.original_and_evaluated_image_in_PBT.build_next_func(name="original")
        )
        self.original_image_list_prev_func = (
            self.original_and_evaluated_image_in_PBT.build_prev_func(name="original")
        )
        self.ui.BTN_next_original_image_in_PBT_page.setEnabled(True)
        self.ui.BTN_prev_original_image_in_PBT_page.setEnabled(True)
        self.update_rawANDmask_images_on_loadDataSetSlider_in_PBT(
            predict_eval=image_slider_path
        )
        self.image_slider_path = image_slider_path

    def pipline_saveing(self, pipline):
        """
        pipline_saveing save pipline obj as .json filr

        _extended_summary_

        Parameters
        ----------
        pipline :pipline class
            obj of evalution of pipline
        """
        pipline.save_json()

    def set_signal_from_evaluate_thread(self, percentage):
        """this function used to update progressbar percentage

        Parameters
        ----------
        percentage : float
            new quantity of progressbar ,that should update
        """
        self.ui.pgbar_evalution_precess.setValue(percentage)

    def evaluate_model_on_selected_model(self):
        """this function connect to evaluate button in ui ,at PBT page
        if click it at proper time ,process of evalution with
        selected pipline , on selected dataset will done
        and it's data save as .json , some of the data will
        show on ui
        """

        self.pipline_OBJ.set(
            key=pipelines.EVALUATED_DATASETS, value=self.selected_datasets[0]["path"]
        )

        self.ui.chbox_prefectdata_in_PBT_page.setEnabled(False)
        self.ui.BTN_load_in_PBT_page.setEnabled(False)
        self.ui.BTN_load_image_in_PBT_page.setEnabled(False)
        self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(False)
        self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.setEnabled(False)

        # display progressBar of progress of evaluating  dataset
        self.pgbar_value = 0
        self.ui.pgbar_evalution_precess.setValue(self.pgbar_value)
        self.ui.frame_118.setFixedHeight(60)
        self.evaluation_thread = QThread()
        self.evaluation = Evaluation_worker()
        self.evaluation.set_params(
            data_path=self.path_list,
            pipline_obj=self.pipline_OBJ,
            input_type=self.inputtype,
            input_size=self.inputsize[0],
            data_nc=self.classes_num,
            binary_model=self.b_model,
            binary_threshold=0.5,
            yolo_model=self.yolo_model,
            yolo_conf_thres=0.001,
            yolo_iou_thres=0.6,
            yolo_max_det=300,
        )
        self.evaluation.moveToThread(self.evaluation_thread)
        self.evaluation_thread.started.connect(self.evaluation.evaluate)
        self.evaluation.finished.connect(self.evaluation_thread.quit)
        self.evaluation.finished.connect(self.evaluation.deleteLater)
        self.evaluation_thread.finished.connect(self.evaluation_thread.deleteLater)
        self.evaluation.progress.connect(self.evaluation_ui_update)
        self.evaluation.pgb_bar_signal.connect(self.set_signal_from_evaluate_thread)
        self.evaluation.pipline_signal.connect(self.pipline_saveing)
        self.evaluation_thread.start()

        self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(False)
        self.evaluation_thread.finished.connect(
            lambda: self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(True)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.frame_118.setFixedHeight(0)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.BTN_refresh_loadDataset_tab_in_PBT.setEnabled(True)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.chbox_prefectdata_in_PBT_page.setEnabled(True)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.setEnabled(True)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(True)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.BTN_load_image_in_PBT_page.setEnabled(True)
        )
        self.evaluation_thread.finished.connect(
            lambda: self.ui.BTN_load_in_PBT_page.setEnabled(True)
        )

    def set_pipline_of_model(self, id, flag_creation):
        """this function connect to the thread of model creation
        for getting it's signal and update UI

        Parameters
        ----------
        id : int
            this number indicate the pesentage of model creation process
        """

        if id == 0:
            self.ui.create_alert_message(
                title="ERROR",
                message=texts.ERRORS["pipline_info_unfetchable"][self.language],
            )
        elif id == 1:  # binary model build
            self.ui.frame_120.setFixedHeight(30)
            self.pipline_type = self.ModelsCreation.pipline_type
            if flag_creation:
                self.b_model = self.ModelsCreation.b_model
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_is_ready"][self.language],
                    row=0,
                )
                self.pgbar_value += 50
                self.binary_model_flag = True
            else:
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_can_not_build"][self.language],
                    row=0,
                )
                self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(True)
        elif id == 2:  # if there is no yolo in pipline structer,segmention model build
            if flag_creation:
                self.l_model = self.ModelsCreation.l_model
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_is_ready"][self.language],
                    row=1,
                )
                if self.pipline_type == "BS":
                    self.pgbar_value += 50
                else:
                    self.pgbar_value += 30
                self.segmentation_model_flag = True
            else:
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_can_not_build"][self.language],
                    row=1,
                )
                self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(True)
        elif id == 3:
            if flag_creation:
                self.c_model = self.ModelsCreation.c_model
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_is_ready"][self.language],
                    row=2,
                )
                self.pgbar_value += 20
                self.classification_model_flag = True
            else:
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_can_not_build"][self.language],
                    row=2,
                )
                self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(True)
        elif id == 4:  # yolo model build
            self.use_yolo = True
            if self.pipline_type == "BY":
                row = 1
                self.pgbar_value += 50
            else:
                row = 2
                self.pgbar_value += 20
            if flag_creation:
                self.yolo_model = self.ModelsCreation.yolo_model
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_is_ready"][self.language],
                    row=row,
                )
                self.yolo_model_flag = True
            else:
                self.update_table_value(
                    table=self.ui.tableWidget_pipline_info,
                    value=texts.MESSEGES["Part_can_not_build"][self.language],
                    row=3,
                )
                self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(True)
        self.pipline_check = {
            "BY": (self.yolo_model_flag and self.binary_model_flag),
            "BS": (self.binary_model_flag and self.segmentation_model_flag),
            "BSY": (
                self.yolo_model_flag
                and self.binary_model_flag
                and self.segmentation_model_flag
            ),
            "BSC": (
                self.binary_model_flag
                and self.segmentation_model_flag
                and self.classification_model_flag
            ),
        }

        if self.pipline_check[self.pipline_type]:
            self.ui.LBL_pipline_is_ready.setFixedHeight(20)
            self.ui.LBL_pipline_is_ready.setText(
                texts.MESSEGES["Complete_Pipline"][self.language]
            )
        else:
            self.ui.LBL_pipline_is_ready.setFixedHeight(20)
            self.ui.LBL_pipline_is_ready.setText(
                texts.MESSEGES["Pipline_Is_Not_Ready"][self.language]
            )

        if self.pgbar_value > 100:
            self.pgbar_value = 100

        self.ui.pgbar_pipline_creation.setValue(self.pgbar_value)
        if self.pgbar_value == 100:
            self.ui.frame_120.setFixedHeight(0)
            self.ui.BTN_set_pipline_in_PBT_page.setEnabled(False)
            self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(True)
            self.pipline_is_ready = True
            if self.data_is_ready:
                self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(True)

        try:
            self.pipline_OBJ = self.ModelsCreation.pipline_OBJ
            self.classes_num = self.ModelsCreation.classes_num
            self.pipline_type = self.ModelsCreation.pipline_type
            self.inputtype = self.ModelsCreation.inputtype
            self.inputsize = self.ModelsCreation.inputsize
            self.split_size = self.b_model.layers[0].output_shape[0][1:-1]
        except:
            pass

    def reset_pipline(self):
        """
        reset_pipline reset all param of the creating pipline process

        _extended_summary_
        """
        self.pgbar_value = 0
        self.ui.pgbar_pipline_creation.setValue(self.pgbar_value)
        self.ui.frame_120.setFixedHeight(0)
        self.assign_table_column(
            table=self.ui.tableWidget_pipline_info,
            number_of_rows=self.len_model_piplines,
            refresh=True,
        )
        self.binary_model_flag = False
        self.segmentation_model_flag = False
        self.classification_model_flag = False
        self.yolo_model_flag = False
        self.ui.LBL_pipline_is_ready.setText("")
        self.ui.LBL_pipline_is_ready.setFixedHeight(0)
        self.ui.BTN_set_pipline_in_PBT_page.setEnabled(True)
        self.ui.BTN_reset_pipline_in_PBT_page.setEnabled(False)
        self.pipline_name = ""
        self.pipline_is_ready = False
        self.ui.BTN_evaluate_image_in_PBT_page_2.setEnabled(False)

    def set_pipline(self):
        """this function connect to set button in ui,at PBT page
        this creates models of selected
        this shows notif of it on ui
        """

        self.pipline_name = (
            self.ui.cbBox_of_pipline_in_PBT_page_load_dataset.currentText()
        )
        self.assign_table_column(
            table=self.ui.tableWidget_pipline_info,
            number_of_rows=self.len_model_piplines,
            data_list=[texts.MESSEGES["Part_is_not_ready"][self.language]]
            * self.len_model_piplines,
            refresh=False,
        )

        self.pgbar_value = 0
        self.ui.pgbar_pipline_creation.setValue(self.pgbar_value)
        self.binary_model_flag = False
        self.segmentation_model_flag = False
        self.classification_model_flag = False
        self.yolo_model_flag = False
        self.ui.LBL_pipline_is_ready.setText("")
        self.ui.LBL_pipline_is_ready.setFixedHeight(0)

        # Threading............................
        self.ModelsCreation_thread = QThread()
        self.ModelsCreation = ModelsCreation_worker()
        self.ModelsCreation.set_params(
            pipline_name=self.pipline_name,
            database=self.db,
            login_user_name=self.login_user_name,
        )

        self.ModelsCreation.moveToThread(self.ModelsCreation_thread)
        self.ModelsCreation_thread.started.connect(self.ModelsCreation.build_pipline)
        self.ModelsCreation.finished.connect(self.ModelsCreation_thread.quit)
        self.ModelsCreation.finished.connect(self.ModelsCreation.deleteLater)
        self.ModelsCreation_thread.finished.connect(
            self.ModelsCreation_thread.deleteLater
        )
        self.ModelsCreation.model_creation_signal.connect(self.set_pipline_of_model)
        self.ModelsCreation_thread.start()

        self.ui.BTN_set_pipline_in_PBT_page.setEnabled(False)

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
                texts_codes.SubTypes["BUILD_BINARYLIST_SLIDER_ERROR"],
                level=3,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"]["en"],
                code=texts_codes.SubTypes["BUILD_BINARYLIST_SLIDER_ERROR"],
                level=4,
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
                    texts_codes.SubTypes["READ_BINARYLIST_IMAGES_ERROR"],
                    level=3,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"]["en"],
                    code=texts_codes.SubTypes["READ_BINARYLIST_IMAGES_ERROR"],
                    level=4,
                )

        except Exception as e:
            self.ui.set_warning(
                texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"][self.language],
                "binarylist",
                texts_codes.SubTypes["READ_BINARYLIST_IMAGES_ERROR"],
                level=3,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["READ_BINARYLIST_IMAGES_ERROR"]["en"],
                code=texts_codes.SubTypes["READ_BINARYLIST_IMAGES_ERROR"],
                level=5,
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
        """
        update_rawANDmask_images_on_loadDataSetSlider_in_PBT for moving slider on image list

        Parameters
        ----------
        prevornext : str, optional
            _description_, by default "False"
        predict_eval : _type_, optional
            List of corresponding pred images, by default None
        """
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
        res = binary_list_funcs.set_image_to_ui_slider_eidted_version(
            ui_obj=self.ui,
            image_path_list=current_image_list,
            predict_eval=predict_eval,
        )

    # ------------------------------------------------------------------------------------------------------------------------
    # yolo-model history page functions

    def refresh_yolo_models_table_onevent(self):
        """this function is used to refresh yolo models table"""

        self.ymodel_tabel_itr = 1  # reset page number to first (1)
        self.ui.yolo_tabel_page.setText(str(self.ymodel_tabel_itr))

        self.refresh_yolo_models_table(get_count=True)
        self.refresh_yolo_models_table()
        self.ui.clear_yolo_filters_fields()
        self.yfilter_mode = False
        self.ui.set_warning(
            texts.MESSEGES["REFRESH_TABLE"][self.language],
            "yolo_model_history",
            level=1,
        )

    def refresh_yolo_models_table(
        self, nextorprev=False, get_count=False, filter_mode=False
    ):
        """this function is used to refresh/update yolo models table on UI

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
                    self.ymodel_count,
                ) = yolo_model_funcs.get_yolo_models_from_db(
                    db_obj=self.db, count=get_count
                )
                self.ymodel_count = self.ymodel_count[0]["count(*)"]

                # validation
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_ymodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )
                #
                self.yolo_model_tabel_nextorprev(check=True)
                return
            except:
                return
        # load filterd models
        if filter_mode:
            # reset table page number to first (1)
            self.ymodel_tabel_itr = 1
            self.ui.yolo_tabel_page.setText(str(self.ymodel_tabel_itr))

            res = self.filter_yolo_models(filter_signal=True, count=True)

            if res[0]:
                self.ymodel_count = res[1][0]["count(*)"]
                self.yolo_model_tabel_nextorprev(check=True)

                res = self.filter_yolo_models(filter_signal=True)

                if res[0]:
                    ymodels_list = res[1]
                else:
                    self.refresh_yolo_models_table(get_count=True)
                    (
                        res,
                        ymodels_list,
                    ) = yolo_model_funcs.get_yolo_models_from_db(db_obj=self.db)
                    if not res:
                        self.ui.notif_manager.append_new_notif(
                            message=texts.ERRORS["database_get_ymodels_failed"][
                                self.ui.language
                            ],
                            level=3,
                        )

            else:
                self.refresh_yolo_models_table(get_count=True)
                (
                    res,
                    ymodels_list,
                ) = yolo_model_funcs.get_yolo_models_from_db(db_obj=self.db)
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_ymodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )

        else:
            if not nextorprev:
                (
                    res,
                    ymodels_list,
                ) = yolo_model_funcs.get_yolo_models_from_db(db_obj=self.db)
                if not res:
                    self.ui.notif_manager.append_new_notif(
                        message=texts.ERRORS["database_get_ymodels_failed"][
                            self.ui.language
                        ],
                        level=3,
                    )

            else:
                if not self.yfilter_mode:
                    (
                        res,
                        ymodels_list,
                    ) = yolo_model_funcs.get_yolo_models_from_db(
                        db_obj=self.db,
                        limit_size=yolo_model_funcs.yolo_table_nrows,
                        offset=(self.ymodel_tabel_itr - 1)
                        * yolo_model_funcs.yolo_table_nrows,
                    )
                    if not res:
                        self.ui.notif_manager.append_new_notif(
                            message=texts.ERRORS["database_get_ymodels_failed"][
                                self.ui.language
                            ],
                            level=3,
                        )

                else:
                    res = self.filter_yolo_models(
                        limit_size=yolo_model_funcs.yolo_table_nrows,
                        offset=(self.ymodel_tabel_itr - 1)
                        * yolo_model_funcs.yolo_table_nrows,
                    )
                    ymodels_list = res[1]

        if len(ymodels_list) == 0 and nextorprev:
            return False

        # set returned models to UI table
        else:
            yolo_model_funcs.set_ymodels_on_ui_tabel(
                ui_obj=self.ui, ymodels_list=ymodels_list
            )
            return True

    # next and prev buttons for yolo models table functionality
    def yolo_model_tabel_nextorprev(self, next=True, check=False):
        """this function is used to get next/prev page for yolo models table

        :param next: boolean determining whether to get next page, defaults to True
        :type next: bool, optional
        :param check: _description_, defaults to False
        :type check: bool, optional
        """
        if check:
            page_max = int(
                math.ceil(self.ymodel_count / yolo_model_funcs.yolo_table_nrows)
            )

            if self.ymodel_tabel_itr >= page_max:
                self.ui.yolo_tabel_next.setEnabled(False)
            else:
                self.ui.yolo_tabel_next.setEnabled(True)
            #
            if self.ymodel_tabel_itr > 1:
                self.ui.yolo_tabel_prev.setEnabled(True)
            else:
                self.ui.yolo_tabel_prev.setEnabled(False)

            return

        #
        if next:
            self.ymodel_tabel_itr += 1

        elif self.ymodel_tabel_itr > 1:
            self.ymodel_tabel_itr -= 1

        #
        res = self.refresh_yolo_models_table(nextorprev=True)
        self.yolo_model_tabel_nextorprev(check=True)
        self.ui.yolo_tabel_page.setText(str(self.ymodel_tabel_itr))

    # filter function for yolo models
    def filter_yolo_models(
        self,
        limit_size=yolo_model_funcs.yolo_table_nrows,
        offset=0,
        filter_signal=False,
        count=False,
    ):
        """this function is used to filter yolo models given filter params on UI

        :param limit_size: n table rows in database to return, defaults to yolo_model_funcs.yolo_table_nrows
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
            self.filter_params = yolo_model_funcs.get_yolo_model_filter_info_from_ui(
                ui_obj=self.ui
            )
        #
        if not self.filter_params:
            return False, filter_signal

        res = yolo_model_funcs.get_filtered_yolo_models_from_db(
            ui_obj=self.ui,
            db_obj=self.db,
            filter_params=self.filter_params,
            limit_size=limit_size,
            offset=offset,
            count=count,
        )

        if res[0] == "error":
            self.yfilter_mode = False
            return False, res[1]

        if res[0] == "all":
            self.yfilter_mode = False
            return False, res[1]

        else:
            self.yfilter_mode = True
            self.ui.set_warning(
                texts.MESSEGES["FILTERED_RESAULTS_SUCCUSSFULL"][self.language],
                "yolo_model_history",
                level=1,
            )
            return True, res[1]

    # clear filters for yolo models
    def clear_yolo_filters(self):
        """this function is used tp clear filters for yolo models list"""

        self.yfilter_mode = False  # diactive filter mode
        # reset table page number
        self.ymodel_tabel_itr = 1
        self.ui.yolo_tabel_page.setText(str(self.ymodel_tabel_itr))
        #
        self.refresh_yolo_models_table(get_count=True)
        self.refresh_yolo_models_table()
        self.ui.clear_yolo_filters_fields()
        self.ui.set_warning(
            texts.MESSEGES["FILTERED_RESAULTS_CLEAR"][self.language],
            "yolo_model_history",
            level=1,
        )

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
                    texts_codes.SubTypes["LOAD_IMAGES_WITH_DEFECT"],
                    level=1,
                )
                self.ui.logger.create_new_log(
                    message=texts.MESSEGES["LOAD_IMAGES_WITH_DEFECT"]["en"],
                    code=texts_codes.SubTypes["LOAD_IMAGES_WITH_DEFECT"],
                    level=1,
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
                message=texts.ERRORS["piechart_create_failed"]["en"],
                code=texts_codes.SubTypes["piechart_create_failed"],
                level=5,
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
                texts_codes.SubTypes["FILTERED_RESAULTS_SUCCUSSFULL"],
                level=1,
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["FILTERED_RESAULTS_SUCCUSSFULL"]["en"],
                code=texts_codes.SubTypes["FILTERED_RESAULTS_SUCCUSSFULL"],
                level=1,
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
        n = int(widget_name.split("_")[-1])
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
            live_update_time,
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
            live_update_time,
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
        self.init_check_plc()

    def set_camera_parms(self):
        self.db.set_camera_params(
            self.ui.manual_camera,
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
        self.my_plc = plc_managment.management(ip, ui_obj=self.ui,logger=self.ui.logger)
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
                    texts.ERRORS["database_get_plc_params_failed"][self.ui.language],
                    "camera_connection",
                    texts_codes.SubTypes["database_get_plc_params_failed"],
                    level=2,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["database_get_plc_params_failed"]["en"],
                    code=texts_codes.SubTypes["database_get_plc_params_failed"],
                    level=3,
                )
                return
            else:
                # self.ui.show_mesagges(self.ui.plc_warnings, texts.MESSEGES['database_get_plc_params'][self.ui.language], level=0)

                self.ui.logger.create_new_log(
                    message=texts.MESSEGES["database_get_plc_params"]["en"],
                    code=texts_codes.SubTypes["database_get_plc_params"],
                    level=1,
                )

            # self.ui.show_mesagges(self.ui.plc_warnings, texts.MESSEGES['plc_connection_apply'][self.ui.language], level=0)
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["plc_connection_apply"]["en"],
                code=texts_codes.SubTypes["plc_connection_apply"],
                level=1,
            )
            self.plc_connection_status = True
            self.ui.change_plc_status(status="connect")
            self.plc_retry_connection = 0

            self.ui.disconnect_plc_btn.setEnabled(True)
            self.ui.connect_plc_btn.setEnabled(False)

        else:
            self.ui.set_status_plc(mode=False)
            # self.ui.show_mesagges(self.ui.plc_warnings, texts.ERRORS['plc_connection_apply_failed'][self.ui.language], level=2)
            self.ui.logger.create_new_log(
                message=texts.ERRORS["plc_connection_apply_failed"]["en"],
                code=texts_codes.SubTypes["plc_connection_apply_failed"],
                level=4,
            )

            # self.connect_plc()
            if self.retry_connecting_plc < 1:                   # retry connection
                self.retry_connecting_plc += 1
                self.ui.change_plc_status(status="retry")
                self.plc_connection_status = False
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
                self.plc_connection_status = False
                self.ui.change_plc_status(status="disconnect")
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
        try:
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
        except:
            return False
        # #print('-'*50,self.up_high_threshold)
        # #print('88888888888888',self.dict_spec_pathes)

        # #print('parms',self.parms)
        return True

    # def disconnect_plc(self, on_close=False, force_close=False):
    #     """
    #     this function is used to disconnect from plc

    #     Args:
    #         on_close (bool, optional): a boolean determining if function is called on app close. Defaults to False.
    #         force_close (bool, optional): a boolean determining to force close the plc (whenever plc is disconnected suddenly)
    #     """

    #     # force close the plc, this is for those times that plc is disconnecter by error
    #     if force_close:
    #         try:
    #             self.my_plc.disconnect()
    #         except:
    #             pass
    #         #
    #         self.timer_write_plc.stop()
    #         self.plc_connection_status = False
    #         del self.my_plc
    #         #
    #         # self.ui.show_mesagges(self.ui.plc_warnings, texts.ERRORS['plc_disconnected_by_error'][self.ui.language], level=2)
    #         self.ui.notif_manager.append_new_notif(
    #             message=texts.ERRORS["plc_disconnected_by_error"][self.ui.language],
    #             level=3,
    #         )
    #         self.ui.logger.create_new_log(
    #             message=texts.ERRORS["plc_disconnected_by_error"]["en"], code=texts_codes.SubTypes['plc_disconnected_by_error'], level=4
    #         )
    #         #
    #         self.ui.disconnect_plc_btn.setEnabled(False)
    #         self.ui.connect_plc_btn.setEnabled(True)
    #         #
    #         # self.ui.plc_main_frame.setEnabled(False)

    #         return

    #     try:
    #         self.my_plc.disconnect()
    #         self.timer_write_plc.stop()
    #         self.plc_connection_status = False
    #         del self.my_plc
    #         #
    #         # self.ui.show_mesagges(self.ui.plc_warnings, texts.MESSEGES['plc_disconnected'][self.ui.language], level=0)
    #         self.ui.notif_manager.append_new_notif(
    #             message=texts.MESSEGES["plc_disconnected"][self.ui.language], level=1
    #         )
    #         self.ui.logger.create_new_log(
    #             message=texts.MESSEGES["plc_disconnected"]["en"], code=texts_codes.SubTypes['plc_disconnected'], level=1
    #         )
    #         #
    #         self.ui.disconnect_plc_btn.setEnabled(False)
    #         self.ui.connect_plc_btn.setEnabled(True)

    #     # failed to disconnect plc
    #     except:
    #         if not on_close:
    #             # self.ui.show_mesagges(self.ui.plc_warnings, texts.ERRORS['plc_disconnected_failed'][self.ui.language], level=2)
    #             self.ui.notif_manager.append_new_notif(
    #                 message=texts.ERRORS["plc_disconnected_failed"][self.ui.language],
    #                 level=3,
    #             )
    #             self.ui.logger.create_new_log(
    #                 message=texts.ERRORS["plc_disconnected_failed"]["en"], code=texts_codes.SubTypes['plc_disconnected_failed'], level=3
    #             )

    #     #
    #     # self.ui.plc_main_frame.setEnabled(False)

    def disconnect_plc(self, on_close=False, force_close=False):
        """
        this function is used to disconnect from plc

        Args:
            on_close (bool, optional): a boolean deermining if function is called on app close. Defaults to False.
            force_close (bool, optional): a boolean deermining to force close the plc (whenever plc is disconnected suddenly)
        """

        # force close the plc, this is for those times that plc is disconnecter by error
        if force_close:
            try:
                self.my_plc.disconnect()
            except:
                pass
            #
            self.plc_connection_status = False
            self.ui.change_plc_status(status="disconnect")
            self.ui.set_status_plc(mode=False)

            del self.my_plc
            #
            self.ui.show_mesagges(
                self.ui.plc_warnings,
                texts.ERRORS["plc_disconnected_by_error"][self.ui.language],
                level=2,
            )

            self.ui.notif_manager.append_new_notif(
                message=texts.ERRORS["plc_disconnected_by_error"][self.ui.language],
                level=3,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["plc_disconnected_by_error"]["en"], level=4
            )
            #
            self.ui.disconnect_plc_btn.setEnabled(False)
            self.ui.connect_plc_btn.setEnabled(True)

            return

        try:
            self.my_plc.disconnect()
            self.plc_connection_status = False
            self.ui.change_plc_status(status="disconnect")
            self.ui.set_status_plc(mode=False)

            del self.my_plc
            #
            self.ui.show_mesagges(
                self.ui.plc_warnings,
                texts.MESSEGES["plc_disconnected"][self.ui.language],
                level=0,
            )

            self.ui.notif_manager.append_new_notif(
                message=texts.MESSEGES["plc_disconnected"][self.ui.language], level=1
            )
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["plc_disconnected"]["en"], level=1
            )
            #
            self.ui.disconnect_plc_btn.setEnabled(False)
            self.ui.connect_plc_btn.setEnabled(True)

        # failed to disconnect plc
        except:
            if not on_close:
                self.ui.show_mesagges(
                    self.ui.plc_warnings,
                    texts.ERRORS["plc_disconnected_failed"][self.ui.language],
                    level=2,
                )

                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["plc_disconnected_failed"][self.ui.language],
                    level=3,
                )
                self.ui.logger.create_new_log(
                    message=texts.ERRORS["plc_disconnected_failed"]["en"], level=3
                )
        print('End function close thread plc')
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
                texts.ERRORS["database_get_plc_ip_failed"][self.ui.language],
                "camera_connection",
                texts_codes.SubTypes["database_get_plc_ip_failed"],
                level=2,
            )
            self.ui.logger.create_new_log(
                message=texts.ERRORS["database_get_plc_ip_failed"]["en"],
                code=texts_codes.SubTypes["database_get_plc_ip_failed"],
                level=4,
            )
            return
        #
        else:
            self.ui.logger.create_new_log(
                message=texts.MESSEGES["database_get_plc_ip"]["en"],
                code=texts_codes.SubTypes["database_get_plc_ip"],
                level=1,
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
            auto_wind_timer = (
                self.ui.update_wind_plc * 1000 + self.ui.auto_wind_intervals
            )
            self.auto_wind_timer.start(auto_wind_timer)

    def set_wind(self, mode=True):
        # print(type(self.sensor),self.sensor)
        if self.sensor and self.plc_connection_status:
            if self.ui.wind_itr == 1:
                # ret = self.my_plc.set_value(self.dict_spec_pathes["MemUpValve"], str(mode))
                t1 = time.time()
                threading.Thread(target=self.my_plc.set_value,args=(self.dict_spec_pathes["MemDownValve"], str(self.wind_mode))).start()
                threading.Thread(target=self.my_plc.set_value,args=(self.dict_spec_pathes["MemUpValve"], str(self.wind_mode))).start()
                # ret = self.my_plc.set_value(self.dict_spec_pathes["MemDownValve"], str(self.wind_mode))
                # print('set_wind',time.time()-t1)
                # if ret and mode:
                if mode:
                    self.ui.start_wind()
        
            self.wind_mode = not self.wind_mode
                
                
                

    def set_start_software_plc(self, mode):
        # #print("software on plc ", str(mode))
        try:
            self.my_plc.set_value(self.dict_spec_pathes["MemSoftwareStart"], str(mode))

        except:
            pass

    def get_sensor(self):
        # print(time.time())
        try:
            if not self.ui.manual_plc:
                self.sensor = self.my_plc.get_value(
                    self.dict_spec_pathes["MemDistanceSensor"]
                )

                if self.sensor[0] == "-":
                    if not self.ui.manual_plc:
                        # #print(";" * 50)
                        self.sensor = False
                else:
                    self.sensor = bool(self.sensor[0])

        except:
            self.sensor = False

        if self.sensor:
            self.slab_detect = True
        else:
            self.slab_detect = False

        if not self.ui.flag_close_win:
            threading.Timer(0.1, self.get_sensor).start()

    def get_temp_and_switch(self):
        try:
            self.top_temp = str(
                round(
                    self.my_plc.get_value(self.dict_spec_pathes["UpTemperature"])[0], 2
                )
            )
            self.bottom_temp = str(
                round(
                    self.my_plc.get_value(self.dict_spec_pathes["DownTemperature"])[0],
                    2,
                )
            )
        except:
            self.top_temp = "0"
            self.bottom_temp = "0"

        try:
            self.up_in = self.my_plc.get_value(
                self.dict_spec_pathes["MemUpLimitSwitchIn"]
            )
            if self.up_in[0] == "-":
                self.up_in = False
            else:
                self.up_in = bool(self.up_in[0])
            self.up_out = self.my_plc.get_value(
                self.dict_spec_pathes["MemUpLimitSwitchOut"]
            )
            if self.up_out[0] == "-":
                self.up_out = False
            else:
                self.up_out = bool(self.up_out[0])
            self.down_in = self.my_plc.get_value(
                self.dict_spec_pathes["MemDownLimitSwitchIn"]
            )
            if self.down_in[0] == "-":
                self.down_in = False
            else:
                self.down_in = bool(self.down_in[0])
            self.down_out = self.my_plc.get_value(
                self.dict_spec_pathes["MemDownLimitSwitchOut"]
            )
            if self.down_out[0] == "-":
                self.down_out = False
            else:
                self.down_out = bool(self.down_out[0])
        except:
            self.up_in = False
            self.up_out = False
            self.down_in = False
            self.down_out = False

        if not self.ui.flag_close_win:
            threading.Timer(5, self.get_temp_and_switch).start()


    def test_t(self):
        print("aaaa")

    def update_plc_values(self):

        threading.Timer(1,self.get_sensor).start()
        threading.Timer(1,self.get_temp_and_switch).start()

    #levl2 data

    def start_get_full_data(self):
        (
            n_camera,
            projectors,
            details
        ) = self.l2_connection.get_full_info()  # get data from level2
        if details and details != self.details:
            self.details = details
            self.n_camera = n_camera
            self.projectors = projectors
            self.ImageManager.update_sheet(self.n_camera, self.details, reset=False)
            self.ui.show_sheet_details(self.details, tab_live=True)
            self.get_info_flag = True

        else:
            threading.Timer(0.5, self.start_get_full_data).start()

    def start_get_date_time_info(self):
        (
            n_camera,
            projectors,
            details
        ) = self.l2_connection.get_date_time_info()
        self.ImageManager.update_sheet(n_camera, details, reset=False)
        self.ui.show_sheet_details(details, tab_live=True)

    def update_sensor_and_temp(self):
        try:
            if (
                self.top_temp > self.up_high_threshold
                or self.bottom_temp > self.down_high_threshold
            ):
                self.ui.notif_manager.append_new_notif(
                    message=texts.ERRORS["overhead_temp"][self.ui.language], level=3
                )
        except:
            # print('Except self.top_temp > self.up_high_threshold')
            pass
        #  self.up_high_threshold = self.my_plc.get_value(self.dict_spec_pathes["UpHighThreshold"])
        # self.up_low_threshold = self.my_plc.get_value(self.dict_spec_pathes["UpLowThreshold"])
        # self.down_high_threshold = self.my_plc.get_value(self.dict_spec_pathes["DownHighThreshold"])
        # self.down_low_threshold = self.my_plc.get_value(self.dict_spec_pathes["DownLowThreshold"])
        if self.ui.manual_plc:  # Manual change senssor   in final should be delete
            if self.itr <= 8:
                self.sensor = True
            else:
                self.sensor = False
                if self.itr >= 12:
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
        self.ui.change_place_check_status(side="up", inout="in", mode=self.up_in)
        self.ui.change_place_check_status(side="up", inout="out", mode=self.up_out)
        self.ui.change_place_check_status(side="down", inout="in", mode=self.down_in)
        self.ui.change_place_check_status(side="down", inout="out", mode=self.down_out)
        try:
            self.ui.update_plc_temp(self.top_temp, self.bottom_temp)
        except:
            pass

    def change_sensor_run(self):
        # #print(self.ready_capture_flag)
        if self.ready_capture_flag:
            if self.sensor:
                self.set_start_software_plc(True)
                # try:
                (
                    n_camera,
                    projectors,
                    details,
                ) = self.l2_connection.get_dummy_info()  # get data from level2
                # except:
                #     self.stop_capture_func(disable_ui=True)
                #     self.ui.create_alert_message(
                #         title=texts.Titles["connection_failed"],
                #         message=texts.MESSEGES["connection_failed"],
                #     )
                # print('%%%%%%'*5, details)
                self.ImageManager.update_sheet(n_camera, details)
                self.start_capture_func(disable_ui=False)
                # self.ui.show_sheet_details(details, tab_live=True)
                self.get_info_flag = False
                # if self.connection_status:
                # print('start thread set caemra and projector')
                
                threading.Timer(0.5, self.start_get_full_data).start()

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
                if self.start_capture_flag:
                    if not self.get_info_flag:
                        self.start_get_date_time_info()
                    self.ImageManager.rename_sheet()
                    self.ImageManager.update_database()
                self.stop_capture_func(disable_ui=False)
                # if self.connection_status:
                # self.my_plc.set_cams_and_prejector(3, 0)
                if self.show_save_notif:
                    self.ui.notif_manager.append_new_notif(
                        message=str(texts.MESSEGES["save_sheet"][self.ui.language]),
                        level=1,
                    )

    def init_check_plc(self):
        # if self.start_capture_flag:
        try:
            self.plc_timer.stop()
            # self.plc_update.stop()
        except:
            pass
        self.plc_timer.start(1000)
        # self.plc_update.start(self.ui.update_timer_plc)

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
                            texts_codes.SubTypes["REMOVE_PIP_FAILED"],
                            level=3,
                        )
                        self.ui.logger.create_new_log(
                            message=texts.ERRORS["REMOVE_PIP_FAILED"]["en"],
                            code=texts_codes.SubTypes["REMOVE_PIP_FAILED"],
                            level=5,
                        )

                    self.update_combo_piplines()
                    self.ui.set_warning(
                        texts.MESSEGES["REMOVE_PIP"][self.language],
                        "profile",
                        texts_codes.SubTypes["REMOVE_PIP"],
                        level=1,
                    )
                    self.ui.logger.create_new_log(
                        message=texts.MESSEGES["REMOVE_PIP"]["en"],
                        code=texts_codes.SubTypes["REMOVE_PIP"],
                        level=1,
                    )
                except:
                    self.ui.set_warning(
                        texts.ERRORS["REMOVE_PIP_FAILED"][self.language],
                        "profile",
                        texts_codes.SubTypes["REMOVE_PIP_FAILED"],
                        level=3,
                    )
                    self.ui.logger.create_new_log(
                        message=texts.ERRORS["REMOVE_PIP_FAILED"]["en"],
                        code=texts_codes.SubTypes["REMOVE_PIP_FAILED"],
                        level=5,
                    )

    # PBT Evaluate -----------------------------------------------

    def create_json_file(self, name):
        json_parent_path = self.db.get_json_parent_path()
        new_json = Pipeline(json_parent_path, name)

    def set_stackedWidget_in_history_pbt_page(self, b):
        if b.isChecked():
            if b.text() == "BY":
                self.ui.stackedWidget_LC_metrics.setCurrentIndex(1)
            elif b.text() == "BSY":
                self.ui.stackedWidget_LC_metrics.setCurrentIndex(2)
            elif b.text() == "BS":
                self.ui.stackedWidget_LC_metrics.setCurrentIndex(3)
            elif b.text() == "BSC":
                self.ui.stackedWidget_LC_metrics.setCurrentIndex(0)

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

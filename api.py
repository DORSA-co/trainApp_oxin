# from logging import _Level
import ast
import re
import sys
from ast import Try
from email import utils
from PySide6.QtCore import *
from PySide6.QtWidgets import QFileDialog
from cv2 import log

from PySide6 import QtGui
from PySide6.QtCharts import QPieSeries, QPieSlice, QChart, QChartView
from PySide6.QtCore import *
from PySide6.QtGui import QPen, QPainter
from PySide6.QtWidgets import QFileDialog
from matplotlib import pyplot as plt

from Defect_detection_modules.SteelSurfaceInspection import SSI, CreateHeatmap
from app_settings import Settings
from backend import data_grabber, camera_connection
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
from functools import partial
from backend import Label, chart_funcs, binary_model_funcs, binary_list_funcs,date_funcs, classification_model_funcs, classification_list_funcs, dataset, colors_pallete

import database_utils
from utils import *
from utils.move_on_list import moveOnList, moveOnImagrList

import texts  # eror and warnings texts
from utils import tempMemory, Utils

from backend.dataset import Dataset
from image_splitter import ImageCrops
import train_api

from labeling.labeling_UI import labeling

from FileDialog import FileDialog

from labeling import labeling_api
from pynput.mouse import Button, Controller

from login_win.login_api import login_API
from camera_live import live_manager
from multiprocessing import Process
import dataset_utils

WIDTH_TECHNICAL_SIDE = 49 * 12
HEIGHT_FRAME_SIZE = 51
NCAMERA = 12

TECHNICAL_WGT_NAME_TO_SIDE = {'up_side_technical', 'top', 'bottom'}


# down_side_technical     ,   up_side_technical
class API:
    def __init__(self, ui):
        self.ui = ui
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.move_on_list = moveOnList()
        self.db = database_utils.dataBaseUtils()
        self.create_label_color()
        self.create_default_ds()
        # self.mask_label_backend=Label.maskLbl(self.ui.get_size_label_image(), LABEL_COLOR)
        self.label_bakcend = {
            'mask': Label.maskLbl((1200, 1920), self.LABEL_COLOR),
            'bbox': Label.bboxLbl((1200, 1920), self.LABEL_COLOR)
        }

        # Label.bbox_lbl()
        self.label_memory = tempMemory.manageLabel()
        # self.technical_backend = {'top': data_grabber()}
        self.thechnicals_backend = {}
        self.detect_bboxs_imgs = []
        # self.ui.crop_image.mouseDoubleClickEvent = self.fit_image
        self.t = 0
        self.scale = 1
        self.position = [0, 0]
        self.pressed = None
        self.current_technical_side = ''
        self.selected_images_for_label = tempMemory.manageSelectedImage()
        self.finish_draw = 0
        self.language = 'en'
        self.size = self.db.get_split_size(id=0)
        self.img = None
        self.n_imgs = []
        # iterator for binary-model history tabel
        self.bmodel_tabel_itr = 1
        self.bmodel_count = 0
        self.filter_mode = False
        self.proc_start_flag = True

        # binarylist dataset parms
        self.dataset_params = {}

        self.ui.set_default_db_parms(self.ds.binary_path, self.size)

        self.logged_in = False
        # Create labeling window
        # -------------------------------------

        # self.labaling_UI=labeling_UI.labeling()
        # self.labeling_win=labeling()
        self.mouse_controll = Controller()

        self.get_defects()
        self.binary_pieChart()

        # self.defects_name,self.defects_info=self.db.get_defects()

        # -------------------------------------
        # connet buttons to correspondings functions in API               ////////////////////
        self.button_connector()
        # connet mouse event to correspondings functions in API
        self.mouse_connector()
        # connet keyboard event to correspondings functions in API
        self.keyboard_connector()
        # -------------------------------------
        # connect to camera connection
        self.cameras = camera_connection.connect_manage_cameras()

        # connecting camera

        self.index_num = 0

        # binary model start-up funcs
        self.refresh_binary_models_table(get_count=True)

        # create binarylist sliders on UI
        # perfect
        self.binarylist_sliders_check = []
        self.binarylist_sliders_check.append(binary_list_funcs.create_image_slider_on_ui(ui_obj=self.ui,
                                                                                         db_obj=self.db,
                                                                                         frame_obj=self.ui.binary_list_perfect_frame,
                                                                                         prefix=
                                                                                         binary_list_funcs.widjet_prefixes[
                                                                                             'perfect']))
        # defect
        self.binarylist_sliders_check.append(binary_list_funcs.create_image_slider_on_ui(ui_obj=self.ui,
                                                                                         db_obj=self.db,
                                                                                         frame_obj=self.ui.binary_list_defect_frame,
                                                                                         prefix=
                                                                                         binary_list_funcs.widjet_prefixes[
                                                                                             'defect']))

        # binarylist image object
        self.binary_image_list = moveOnImagrList(sub_directory='', step=binary_list_funcs.n_images_per_row)

        # ________________________________________________________________
        # create classlist slider on UI
        self.classification_image_list_name = 'classlist'
        self.classlist_slider_check = []
        self.classlist_slider_check.append(binary_list_funcs.create_image_slider_on_ui(ui_obj=self.ui,
                                                                                        db_obj=self.db,
                                                                                        frame_obj=self.ui.class_list_slider_frame,
                                                                                        prefix=self.classification_image_list_name,
                                                                                        image_per_row=binary_list_funcs.n_images_per_row_classlist))
        # classlist image object
        self.classification_image_list = moveOnImagrList(sub_directory='', step=binary_list_funcs.n_images_per_row)
        #_____________________________________________________________________

        # self.camera_process = Process(target=save_camera_images, args=(self.cameras, ))
        self.live = live_manager(self.ui, self.db.get_parent_path())
        self.camera_process = threading.Thread(target=self.live.save_camera_images, args=(self.cameras, ))

        # DEBUG_FUNCTIONS
        # -------------------------------------
        # self.__debug_load_sheet__(['996','997'])
        # self.__debug_select_random__()
        # self.__debug_select_for_label()

        self.create_classlist_pie_chart()

        

    def __debug_load_sheet__(self, ids):
        self.move_on_list.add(ids, 'sheets_id')
        self.selected_images_for_label.clear()
        self.load_sheet()

    def __debug_select_random__(self, ):
        for id in range(self.move_on_list.get_count('sheets_id')):
            self.next_sheet()
            for side in ['up', 'down']:
                for _ in range(np.random.randint(0, 5)):
                    cam = np.random.randint(self.sheet.get_cameras()[0], self.sheet.get_cameras()[1] + 1)
                    frame = np.random.randint(0, self.sheet.get_nframe() + 1)
                    self.selected_images_for_label.add(self.move_on_list.get_current('sheets_id'), side, (cam, frame))
                    self.thechnicals_backend[side].update_selected(
                        self.selected_images_for_label.get_sheet_side_selections(
                            self.move_on_list.get_current('sheets_id'),
                            side
                        )
                    )
        self.refresh_thechnical(fp=1)
        self.ui.add_selected_image(self.selected_images_for_label.get_all_selections_list())

    def __debug_select_for_label(self):
        self.ui.checkBox_select.setChecked(True)
        self.ui.select_unselect_all()
        self.label_selected_img()

    # ----------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    def create_default_ds(self):
        parms = self.db.get_dataset()
        parms = {'user_name': parms['user_own'], 'user_id': parms['id'], 'dataset_name': parms['name'], 'path': parms['path'], 'max_size': '15 Gb', 'date': '3-3-1401'}
        self.ds = Dataset(parms['path'])
        self.ds_json = dataset_utils.dataset_json()
        self.ds_json.create_json_dataset(parms)

    def button_connector(self):
        self.ui.load_sheets_win.load_btn.clicked.connect(partial(self.load_sheets))
        self.ui.add_btn_SI.clicked.connect(partial(self.append_select_img))
        self.ui.remove_btn_SI.clicked.connect(partial(self.remove_select_img))
        self.ui.load_coil_btn.clicked.connect(partial(self.show_sheet_loader))
        self.ui.next_coil_btn.clicked.connect(partial(self.next_sheet))
        self.ui.prev_coil_btn.clicked.connect(partial(self.prev_sheet))
        self.ui.save_btn_SI.clicked.connect(partial(self.save_temp_img_ds))
        self.ui.label_btn_SI.clicked.connect(partial(self.label_selected_img))

        self.ui.next_img_label_btn.clicked.connect(partial(self.next_label_img))
        self.ui.prev_img_label_btn.clicked.connect(partial(self.prev_label_img))
        self.ui.binary_train.clicked.connect(partial(self.set_b_parms))
        # self.ui.binary_train_stop.clicked.connect(partial(self.set_b_parms))
        self.ui.localization_train.clicked.connect(partial(self.set_l_parms))
        self.ui.save_dataset_btn.clicked.connect(partial(self.save_train_ds))
        self.ui.heatmap_btn.clicked.connect(partial(self.create_Heatmap))

        # trainig
        self.ui.b_select_dp.clicked.connect(partial(self.select_binary_dataset))
        self.ui.b_delete_ds.clicked.connect(partial(self.delete_binary_dataset))
        self.ui.b_add_ok.clicked.connect(partial(self.ok_add_binary_ds))

        #login
        self.login_user_name=''
        self.default_dataset_user = ''                                                      #///////////////////
        self.ui.login_btn.clicked.connect(partial(self.show_login))
        self.ui.btn_user_proflie.clicked.connect(partial(self.set_profile_page))
        self.ui.create_database_btn.clicked.connect(partial(self.create_dataset))
        self.ui.my_databases_2.clicked.connect(partial(self.set_user_databases))
        self.ui.set_default_database_btn.clicked.connect(partial(self.set_default_dataset))
        # self.ui.split_dataset.clicked.connect(partial(self.split_binary_dataset))

        # labeling

        # self.labaling_UI.save_btn.clicked.connect(partial(self.set_label))

        # data aquization
        self.ui.connect_camera_btn.clicked.connect(partial(self.camera_connection_func))
        self.ui.disconnect_camera_btn.clicked.connect(partial(self.camera_disconnection_func))

        # self.ui.comboBox_cam_select.currentTextChanged.connect(self.combo_image_preccess)

        # binary-model history
        self.ui.binary_tabel_prev.clicked.connect(partial(lambda: self.binary_model_tabel_nextorprev(next=False)))
        self.ui.binary_tabel_next.clicked.connect(partial(lambda: self.binary_model_tabel_nextorprev(next=True)))
        self.ui.Binary_btn.clicked.connect(partial(self.refresh_binary_models_table_onevent))
        self.ui.binary_history.clicked.connect(partial(self.refresh_binary_models_table_onevent))
        self.ui.binary_table_refresh_btn.clicked.connect(partial(self.refresh_binary_models_table_onevent))
        self.ui.binary_filter_btn.clicked.connect(partial(lambda: self.refresh_binary_models_table(filter_mode=True)))
        self.ui.binary_clearfilter_btn.clicked.connect(partial(self.clear_filters))

        # binary-list
        self.ui.binary_list.clicked.connect(partial(lambda: self.refresh_datasets_table(is_binarylist=True)))
        #self.ui.binary_list_dataset_btn.clicked.connect(partial(lambda: self.select_binary_dataset(page='binarylist')))
        self.ui.binary_list_show_btn.clicked.connect(partial(self.load_binary_images_list))
        self.ui.binary_list_perfect_prev_btn.clicked.connect(
            partial(lambda: self.update_binary_images_on_ui(prevornext='prev')))
        self.ui.binary_list_perfect_next_btn.clicked.connect(
            partial(lambda: self.update_binary_images_on_ui(prevornext='next')))
        self.ui.binary_list_defect_prev_btn.clicked.connect(
            partial(lambda: self.update_binary_images_on_ui(defect=True, prevornext='prev')))
        self.ui.binary_list_defect_next_btn.clicked.connect(
            partial(lambda: self.update_binary_images_on_ui(defect=True, prevornext='next')))

        # classification page
        self.ui.Classification_btn.clicked.connect(partial(self.refresh_classes_table))
        self.ui.classification_history.clicked.connect(partial(self.refresh_classes_table))
        self.ui.classification_class_list.clicked.connect(partial(self.refresh_classes_table))
        self.ui.classification_training.clicked.connect(partial(self.refresh_classes_table))
        self.ui.Classification_btn.clicked.connect(partial(self.refresh_datasets_table))
        self.ui.classification_class_list.clicked.connect(partial(self.refresh_datasets_table))
        self.ui.classlist_show_related_img_btn.clicked.connect(partial(self.show_class_related_images))
        self.ui.classlist_prev_btn.clicked.connect(partial(lambda: self.update_classlist_images_on_ui(prevornext='prev')))
        self.ui.classlist_next_btn.clicked.connect(partial(lambda: self.update_classlist_images_on_ui(prevornext='next')))
        # train model
        self.ui.class_check_train_btn.clicked.connect(partial(self.check_classification_train_params))
        # cls history
        self.ui.Classification_btn.clicked.connect(partial(self.refresh_cls_models_table_onevent))
        self.ui.classification_history.clicked.connect(partial(self.refresh_cls_models_table_onevent))
        self.ui.cls_table_refresh_btn.clicked.connect(partial(self.refresh_cls_models_table_onevent))
        self.ui.cls_filter_btn.clicked.connect(partial(lambda: self.refresh_cls_models_table(filter_mode=True)))
        self.ui.cls_tabel_prev.clicked.connect(partial(lambda: self.cls_model_tabel_nextorprev(next=False)))
        self.ui.cls_tabel_next.clicked.connect(partial(lambda: self.cls_model_tabel_nextorprev(next=True)))
        self.ui.cls_clearfilter_btn.clicked.connect(partial(self.clear_filters_cls))


        self.ui.Binary_btn.clicked.connect(partial(lambda:self.user_access_pages(self.ui.Binary_btn.objectName())))
        self.ui.Localization_btn.clicked.connect(partial(lambda:self.user_access_pages(self.ui.Localization_btn.objectName())))
        self.ui.Classification_btn.clicked.connect(partial(lambda:self.user_access_pages(self.ui.Classification_btn.objectName())))
        self.ui.pbt_btn.clicked.connect(partial(lambda:self.user_access_pages(self.ui.pbt_btn.objectName())))

    def user_access_pages(self,btn_name):

        dic={'Binary_btn':self.ui.page_Binary,
            'Localization_btn':self.ui.page_Localization,
            'Classification_btn':self.ui.page_Classification,
            'pbt_btn':self.ui.page_pbt}
        print(dic[btn_name])
        if self.logged_in:
            eval('self.ui.set_widget_page(self.ui.stackedWidget,dic["{}"])'.format(btn_name))
            # eval(self.stackedWidget.setCurrentWidget(self.page_Binary))
        
        else:
            self.ui.set_warning(texts.WARNINGS['LOGIN_FIRST'][self.language], 'app_erors', level=2)


    def mouse_connector(self):
        for _, technical_widget in self.ui.get_technical().items():
            self.mouse.connet(technical_widget, self.update_technical_pointer_mouse)

        self.mouse.connect_all(self.ui.image, self.label_image_mouse)
        self.mouse.connet_dbclick(self.ui.image, self.label_classify)

        self.mouse.connet_dbclick(self.ui.crop_image, self.fit_image)

        self.mouse.connet_dbclick(self.ui.image_up_left, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_up, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_up_right, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_left, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_right, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_bottom_left, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_bottom, self.enlarge_neighbour_image)
        self.mouse.connet_dbclick(self.ui.image_bottom_right, self.enlarge_neighbour_image)

    def keyboard_connector(self):
        self.keyboard.connet(self.ui, ['left', 'right', 'up', 'down'], [self.update_technical_pointer_keyboard],
                             'Technical View')

    def enlarge_neighbour_image(self, widget_name):
        if self.n_imgs == []:
            self.ui.set_warning(texts.WARNINGS['NO_IMAGE_LOADED'][self.language], 'label', level=2)
            return
        if widget_name == 'image_up_left':
            self.ui.show_neighbouring(self.n_imgs[0])
        if widget_name == 'image_up':
            self.ui.show_neighbouring(self.n_imgs[1])
        if widget_name == 'image_up_right':
            self.ui.show_neighbouring(self.n_imgs[2])
        if widget_name == 'image_left':
            self.ui.show_neighbouring(self.n_imgs[3])
        if widget_name == 'image_right':
            self.ui.show_neighbouring(self.n_imgs[4])
        if widget_name == 'image_bottom_left':
            self.ui.show_neighbouring(self.n_imgs[5])
        if widget_name == 'image_bottom':
            self.ui.show_neighbouring(self.n_imgs[6])
        if widget_name == 'image_bottom_right':
            self.ui.show_neighbouring(self.n_imgs[7])

    # ----------------------------------------------------------------------------------------
    # get id of sheets that user select in load_sheet_win and load first one
    # ----------------------------------------------------------------------------------------
    def load_sheets(self):

        sheets_id = self.ui.load_sheets_win.get_selected_sheetid()
        self.move_on_list.add(sheets_id, 'sheets_id')
        self.selected_images_for_label.clear()
        self.ui.load_sheets_win.close()
        self.load_sheet()

        # ----------------------------------------------------------------------------------------

    # load sheet by its id in software
    # ----------------------------------------------------------------------------------------
    def load_sheet(self):
        selceted_sheets_id = self.move_on_list.get_current(
            'sheets_id')  # get current value on list that corespond to "coils_id" name
        self.sheet = self.db.load_sheet(selceted_sheets_id)  # load inference of Sheet class from database by sheet id
        self.build_sheet_technical(self.sheet)  # build technical sheet
        self.ui.show_sheet_details(self.sheet.get_info_dict())  # show sheet details in UI.details_label

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def build_sheet_technical(self, sheet):
        try:
            self.thechnicals_backend = {}
            for side, _ in self.ui.get_technical(name=False).items():
                self.thechnicals_backend[side] = data_grabber.sheetOverView(sheet,
                                                                            side,  # side of sheet that is UO
                                                                            (HEIGHT_FRAME_SIZE * sheet.get_nframe(),
                                                                             WIDTH_TECHNICAL_SIDE),
                                                                            (self.sheet.get_nframe(), NCAMERA),
                                                                            # sheet.get_grade_shape(),
                                                                            actives_camera=sheet.get_cameras(),
                                                                            oriation=data_grabber.VERTICAL)

                selecteds = self.selected_images_for_label.get_sheet_side_selections(
                    str(self.sheet.get_id()),
                    side
                )

                self.thechnicals_backend[side].update_selected(selecteds)
                self.current_technical_side = side
                self.refresh_thechnical(fp=1)  #

        except:
            print('Error!: load_sheet() in API')

    # ----------------------------------------------------------------------------------------
    # when next next_coil_btn clicked this function move on next coil id and load it
    # ----------------------------------------------------------------------------------------
    def next_sheet(self):
        if self.move_on_list.check('sheets_id'):
            self.move_on_list.next_on_list('sheets_id')  # move previous on list that corespond to "coils_id" name
            self.load_sheet()  # laod current coil id

        else:
            self.ui.set_warning(texts.WARNINGS['NO_SHEET'][self.language], 'data_auquzation', level=2)

    # ----------------------------------------------------------------------------------------
    # when next next_coil_btn clicked this function move on privous coil id and load it
    # ----------------------------------------------------------------------------------------
    def prev_sheet(self):
        if self.move_on_list.check('sheets_id'):
            self.move_on_list.prev_on_list('sheets_id')  # move next on list that corespond to "coils_id" name
            self.load_sheet()  # laod current coil id
        else:
            self.ui.set_warning(texts.WARNINGS['NO_SHEET'][self.language], 'data_auquzation', level=2)

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
            self.current_technical_side].get_pos()  # get mouse position normilized between [0,1]
        x *= self.sheet.get_width()
        y *= self.sheet.get_lenght()
        y = np.round(y, 1)
        x = np.round(x, 1)
        self.ui.show_current_position((x, y))

    def update_technical_pointer_keyboard(self, key):
        self.thechnicals_backend[self.current_technical_side].update_pointer_keyboard(key)
        self.refresh_thechnical(fp=1)
        self.show_pointer_position()

    def update_technical_pointer_mouse(self, widget_name):
        if len(self.thechnicals_backend) == 0:
            self.ui.set_warning(texts.WARNINGS['NO_SHEET'][self.language], 'data_auquzation', level=2)

        else:
            self.current_technical_side = self.ui.get_technical_wgt_side(widget_name)
            pt = self.mouse.get_relative_position()  # get mouse position (x,y) that x,y are in [0,1] range
            self.thechnicals_backend[self.current_technical_side].update_pointer(
                pt)  # update corespond backend mouse position
            self.refresh_thechnical(fp=5)
            self.show_pointer_position()

    def refresh_thechnical(self, fp):
        if self.t % fp == 0:
            self.t = 1

            self.thechnicals_backend[self.current_technical_side].update_sheet_img()  # update technical image
            img = self.thechnicals_backend[
                self.current_technical_side].get_real_img()  # get image of sheet corespond to mouse position
            self.ui.set_crop_image(img)  # show image in UI
            self.update_sheet_img(self.current_technical_side)
            self.ui.show_selected_side(self.current_technical_side)

        else:
            self.t += 1

    # ----------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------
    def fit_image(self, widget_name):
        self.thechnicals_backend[self.current_technical_side].fit(self.mouse.get_relative_position())
        self.refresh_thechnical(1)
        real_img = self.thechnicals_backend[self.current_technical_side].get_real_img()
        self.ui.set_crop_image(real_img)
        self.ui.set_enabel(self.ui.add_btn_SI, True)
        self.show_pointer_position()

    # ----------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------
    def show_sheet_loader(self):
        sheets = self.db.report_last_sheets(10)
        self.ui.load_sheets_win.show_sheets_info(sheets)
        self.ui.data_loader_win_show()

    # ----------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------
    def append_select_img(self):
        cam, frame = self.thechnicals_backend[self.current_technical_side].get_current_img_position()
        # print(cam,frame, '^'*20)
        if (frame < 0) or (cam < 0):
            self.ui.set_warning(texts.WARNINGS['NO_CHOOSEN_IMG'][self.language], 'data_auquzation', level=2)
        else:

            side = self.thechnicals_backend[self.current_technical_side].get_side()
            main_path = self.sheet.get_path()
            self.selected_images_for_label.add(self.move_on_list.get_current('sheets_id'), self.current_technical_side,
                                               (cam, frame))
            self.thechnicals_backend[self.current_technical_side].update_selected(
                self.selected_images_for_label.get_sheet_side_selections(
                    self.move_on_list.get_current('sheets_id'),
                    self.current_technical_side
                )
            )
            self.refresh_thechnical(fp=1)

            self.ui.add_selected_image(self.selected_images_for_label.get_all_selections_list())

    def remove_select_img(self):

        selected_img_for_remove = self.ui.get_selected_img()
        if len(selected_img_for_remove):
            self.selected_images_for_label.remove_by_index(selected_img_for_remove)
            self.ui.add_selected_image(self.selected_images_for_label.get_all_selections_list())
        else:
            self.ui.set_warning(texts.WARNINGS['NO_CHOOSEN_IMG'][self.language], 'data_auquzation', level=2)

    # ----------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------
    def save_temp_img_ds(self, ):
        selected_imgs = self.selected_images_for_label.get_all_selections_list()
        selected_idxs = self.ui.get_selected_img()
        filtered_selected = Utils.get_selected_value(selected_imgs, selected_idxs)
        paths = self.db.get_path_sheet_image(filtered_selected)
        sheets = []
        self.ui.progressBar_SI.setMaximumWidth(150)
        for select_img in filtered_selected:
            sheets.append(self.db.load_sheet(select_img[0]))
            self.ui.progressBar_SI.setValue(100)
        self.ds.save_to_temp(paths, sheets)
        # print(filtered_selected)
        # self.create

        self.ui.progressBar_SI.setMaximumWidth(0)

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

            self.move_on_list.add(list(zip(sheets, filtered_selected, paths)), 'selected_imgs_for_label')
            self.ui.show_label_page()
            self.load_image_to_label_page()

        else:
            self.ui.set_warning(texts.WARNINGS['NO_CHOOSEN_IMG'][self.language], 'data_auquzation', level=2)

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
    def find_bboxs(self, img_path):
        params = self.db.get_image_processing_params()
        if img_path not in self.detect_bboxs_imgs:
            bboxs = SSI(self.img, *params)
            labels = []
            for bbox in bboxs:
                label = ['0', np.array(bbox)]
                labels.append(label)
            self.label_memory.append(img_path,
                                     labels,
                                     'bbox')
            self.detect_bboxs_imgs.append(img_path)

    # ----------------------------------------------------------------------------------------
    #
    # ----------------------------------------------------------------------------------------
    def load_image_to_label_page(self):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
        label_type = self.ui.get_label_type()
        self.img = Utils.read_image(img_path, 'color')
        self.find_bboxs(img_path)
        self.load_label_from_memory(img_path)

        label_img = self.label_bakcend[label_type].draw()
        self.img = Utils.add_layer_to_img(self.img, label_img, opacity=0.4, compress=0.5)
        self.ui.show_image_in_label(self.img)

        labels = self.label_bakcend[label_type].get()
        self.ui.show_labels(labels, label_type)

        # print(self.label_bakcend[label_type].get())
        # print(label, img_path)

        self.load_neighbour_images(selected_img_pos)

        self.ui.show_image_info_lable_page(sheet, selected_img_pos)

        self.ui.image.setScaledContents(True)
        self.scale = 1
        self.position = [0, 0]

    def load_label_from_memory(self, img_path):
        for label_type in ['bbox', 'mask']:
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

        paths = self.db.get_path_sheet_image(neighbours)

        self.n_imgs = []
        for path in paths:
            if os.path.exists(path):
                img = Utils.read_image(path, 'color')
            else:
                img = np.zeros((160, 100))
            self.n_imgs.append(img)

        self.ui.show_image_in_neighbour_labels(self.n_imgs)

    def next_label_img(self):
        self.move_on_list.next_on_list('selected_imgs_for_label')
        self.load_image_to_label_page()

    def prev_label_img(self):
        self.move_on_list.prev_on_list('selected_imgs_for_label')
        self.load_image_to_label_page()

    # ----------------------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------------------

    def create_label_color(self):
        self.LABEL_COLOR = {'black': (0, 0, 0)}
        defect_name, defect_info = self.get_defects()
        # print(len(defect_info),defect_info)
        for i in range(len(defect_info)):
            print(defect_name[i], defect_info[i]['color'])
            hex_color = defect_info[i]['color'].lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
            rgb = (rgb_color[2], rgb_color[1], rgb_color[0])
            self.LABEL_COLOR.update({defect_info[i]['defect_ID']: rgb})
        print('******************', self.LABEL_COLOR)

    def label_image_mouse(self, wgt_name=''):

        label_type = self.ui.get_label_type()
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()

        if self.ui.get_zoom_type() is None:
            try:
                sheet, pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
                img = Utils.read_image(img_path, 'color')
                self.label_bakcend[label_type].mouse_event(mouse_status, mouse_button, mouse_pt)
                if self.label_bakcend[label_type].is_drawing_finish():
                    self.label_bakcend[label_type].save('0')
                label_img = self.label_bakcend[label_type].draw()
                img = Utils.add_layer_to_img(img, label_img, opacity=0.4, compress=0.5)
                self.ui.show_image_in_label(img, self.scale, self.position)
                self.img = img

                labels = self.label_bakcend[label_type].get()
                self.label_memory.add(img_path,
                                      labels,
                                      label_type)
                self.ui.show_labels(labels, label_type)
            except:
                self.ui.set_warning(texts.WARNINGS['NO_IMAGE_LOADED'][self.language], 'label', level=2)
                return

        elif self.ui.get_zoom_type() != 'drag':
            if mouse_status == 'mouse_press':
                if self.ui.image.hasScaledContents():
                    self.scale = 1
                    self.position = [0, 0]
                    self.ui.image.setScaledContents(False)

                if self.ui.get_zoom_type() == 'zoom_in':
                    self.scale *= 1.25
                elif self.ui.get_zoom_type() == 'zoom_out':
                    self.scale /= 1.25
                    if self.scale < 1:
                        self.scale = 1
                        self.position = [0, 0]

                self.position = self.ui.show_image_in_label(self.img, self.scale, self.mouse.get_position())

        elif self.ui.get_zoom_type() == 'drag':
            if self.ui.image.hasScaledContents():
                self.scale = 1
                self.position = [0, 0]
            if mouse_status == 'mouse_press':
                if self.scale != 1:
                    self.pressed = self.mouse.get_position()
                    self.anchor = self.position
                    self.ui.image.setCursor(Qt.ClosedHandCursor)

            if mouse_status == 'mouse_move':
                x, y = self.mouse.get_position()
                if self.pressed:
                    self.ui.image.setCursor(Qt.ClosedHandCursor)
                    dx, dy = x - self.pressed[0], y - self.pressed[1]
                    self.position = self.anchor[0] - dx, self.anchor[1] - dy
                    self.position = self.ui.update_image(self.position)

            if mouse_status == 'mouse_release':
                self.pressed = None
                self.ui.image.setCursor(Qt.OpenHandCursor)

    def label_classify(self, wgt_name=''):
        if self.ui.get_zoom_type() is None:
            label_type = self.ui.get_label_type()
            mouse_position = self.mouse.get_relative_position()
            if label_type == 'mask':
                self.label_bakcend[label_type].delete_point_or_mask(mouse_position)
            self.show_labeling(mouse_position)

    def get_defects(self):
        self.defects_name, self.defects_info = self.db.get_defects()

        return self.defects_name, self.defects_info

    def show_labeling(self, mouse_position):
        label_type = self.ui.get_label_type()
        if self.label_bakcend[label_type].clicked_in_defect(mouse_position):
            current_mouse_position = self.mouse_controll.position
            print(current_mouse_position)

            sign_defect_table = self.db.ret_sign_defect_table()
            print('sign_defect_table', sign_defect_table)
            if sign_defect_table == 0:
                print('nochange')
            else:
                print('change')
                try:
                    self.defects_name, self.defects_info = self.db.get_defects()
                    self.db.update_sign_table('defects_info', '0')
                except:
                    pass
            # self.create_labeling()
            labeling_win = self.ui.ret_create_labeling()
            self.labeling_api = labeling_api.labeling_API(labeling_win, self.defects_name, self.defects_info)
            self.ui.labeling_win.win_set_geometry(left=current_mouse_position[0], top=current_mouse_position[1])
            self.ui.labeling_win.save_btn.clicked.connect(partial(self.set_label))
            self.ui.labeling_win.cancel_btn.clicked.connect(partial(self.close_labeling))
            self.ui.labeling_win.show()
            print('end show_labeling')

    # login ---------------------------------

    def show_login(self):

        if self.logged_in == False:

            login_window = self.ui.ret_create_login()
            self.login_api = login_API(login_window)
            # self.login_api.button_connector()
            login_window.login_btn.clicked.connect(partial(self.check_login))
            print('show_ui')
            self.ui.login_window.show()
        else:
            print('user_loged_in')
            self.show_message_logout()

    def show_message_logout(self):

        t = self.ui.show_question(texts.WARNINGS['ALREADY_SAVED_TITLE'][self.language],
                                  texts.WARNINGS['CONFIRM_LOGOUT'][self.language])
        if not t:
            return
        else:
            self.log_out()

    def log_out(self):
        self.logged_in = False
        self.ui.show_image_btn(self.ui.login_btn, 'images/icons/person.png')
        self.ui.user_name.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_label)
        self.ui.comboBox_user_datasets.clear()
        # self.ui.comboBox_default_dataset.clear()
        self.ui.clear_table_name(self.ui.tableWidget_user_dataset)
        self.ds_json.set_user_name_database('')

    def check_login(self):

        self.login_info = self.login_api.check_login()
        print('ret 0 ', self.login_info[0])
        if self.login_info[0] == True:
            print('ok')
            self.ui.user_name.setText(self.login_info[1]['user_name'])
            self.ui.show_image_btn(self.ui.login_btn, 'images/logout.png')
            self.logged_in = True
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_user_profile)
            self.set_parms_login_page(self.login_info)

            self.set_databases()
            self.set_user_databases()
            self.set_default_dataset()

    def set_parms_login_page(self, login_info):

        print('login_info', login_info)
        self.ui.user_name_2.setText(str(login_info[1]['user_name']))
        self.ui.user_name_3.setText(str(login_info[1]['user_name']))
        self.ui.date_created.setText(str(login_info[1]['date_created']))
        self.ui.user_id.setText(str(login_info[1]['id']))
        self.ui.role.setText(login_info[1]['role'])
        self.ui.default_dataset.setText(str(login_info[1]['default_dataset']))
        self.ui.today_date.setText(str(date_funcs.get_date(folder_path=True)))
        self.login_user_name = (str(login_info[1]['user_name']))
        self.ds_json.set_user_name_database(self.login_user_name)
        #print('username:', self.login_user_name)

    def set_profile_page(self):
        if self.logged_in == True:

            self.ui.set_widget_page(self.ui.stackedWidget, self.ui.page_user_profile)

        else:
            print('first login')
            self.ui.set_warning(texts.WARNINGS['LOGIN_FIRST'][self.language], 'setting_eror', level=2)

    def set_databases(self):
        dataset_names = []
        self.datasets = self.db.get_all_datasets()
        for i in range(len(self.datasets)):
            dataset_names.append(self.datasets[i]['name'])
        print('dataset_names', dataset_names)
        self.ui.comboBox_all_datasets.clear()
        self.ui.comboBox_all_datasets.addItems(dataset_names)
        self.ui.comboBox_all_datasets.currentTextChanged.connect(self.update_table_all_datasets)

    def update_table_all_datasets(self):
        current = self.ui.comboBox_all_datasets.currentIndex()
        self.ui.show_all_datasets(list(self.datasets[current].values()))

    def set_user_databases(self):
        dataset_names = []
        self.user_databases = self.db.get_user_databases(self.login_user_name)
        print('******************', self.user_databases)
        self.user_default_databases = self.db.get_default_dataset(self.login_user_name)
        for i in range(len(self.user_databases)):
            dataset_names.append(self.user_databases[i]['name'])
        print('dataset_names', dataset_names)
        self.ui.comboBox_user_datasets.clear()
        self.ui.comboBox_user_datasets.addItems(dataset_names)
        # self.ui.comboBox_default_dataset.addItems(dataset_names)
        self.update_user_datasts()
        self.ui.comboBox_user_datasets.currentTextChanged.connect(self.update_user_datasts)
        self.set_databases()

    def update_user_datasts(self):
        current = self.ui.comboBox_user_datasets.currentIndex()
        # print('asd',self.user_databases[current].values)
        self.ui.show_user_datasets(list(self.user_databases[current].values()))

    def set_default_dataset(self):
        current_index = self.ui.comboBox_user_datasets.currentIndex()
        self.current = self.user_databases[current_index]
        self.ds = Dataset(self.current['path'])
        self.size = ast.literal_eval(self.current['split_size'])
        self.ui.create_alert_message(texts.WARNINGS['SET_DATASET_TITLE'][self.language], texts.WARNINGS['SET_DATASET'][self.language])
        #
        # dataset_new=self.ui.comboBox_default_dataset.currentText()
        # if dataset_new == '': dataset_new = 'None'
        self.db.update_dataset_default(self.current['id'],self.login_user_name)
        # print('ok')
        self.ui.default_dataset.setText(self.current['name'])
        self.binary_pieChart()

    # ---------------------------------------------------------------------///////////////////////////////////////////
    # dataset

    def create_dataset(self):

        t = self.ui.show_question(texts.WARNINGS['ALREADY_SAVED_TITLE'][self.language],
                                  texts.WARNINGS['CREATE_DATABASE'][self.language])
        if not t:
            return
        else:
            parms = self.ui.get_create_dataset_parms()
            print(parms)

            if os.path.exists(os.path.join(parms['path'], parms['dataset_name'])):
                self.ui.create_alert_message(texts.WARNINGS['CREATE_DATASET_TITLE'][self.language], texts.WARNINGS['CREATE_DATASET'][self.language])
                return

            parms['path'] = os.path.join(parms['path'], parms['dataset_name'])
            Dataset(parms['path'])
            ds_json = dataset_utils.dataset_json()
            ds_json.create_json_dataset(parms)
            data = parms['dataset_name'], self.login_user_name, parms['path']
            self.db.add_dataset(data)

    # def create_folder(self,name,path):
    #     try:
    #         os.mkdir(os.path.join(path, name))
    #     except:
    #         print('eror')
    # path=os.path.join(path, name, "{name}.json")
    # os.mkdir(path)

    # ----------------------------------------------------------------------///////////////////////

    def set_label(self):
        mouse_position = self.mouse.get_relative_position()
        selected_label_name = self.labeling_api.ret_selcted_label()
        selected_label = self.db.get_defect_id(selected_label_name)
        print('***************', selected_label)
        label_type = self.ui.get_label_type()
        self.label_bakcend[label_type].update_label(str(selected_label), mouse_position)
        label_img = self.label_bakcend[label_type].draw()
        img = Utils.add_layer_to_img(self.img, label_img, opacity=0.4, compress=0.5)
        self.ui.show_image_in_label(img, self.scale, self.position)
        self.img = img
        print('end set_label', selected_label)
        self.ui.labeling_win.close_win()
        self.ui.labeling_win = None
        print(label_type)
        # label_type_dict=['masks','bboxs']

        labels = self.label_bakcend[label_type].get()
        # print(labels[1])

        self.ui.show_labels(labels, label_type)

    def close_labeling(self):
        self.ui.labeling_win = None

    def clear_cache_fun(self):
        dir = self.cache_path
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        self.ui.listWidget_logs.addItem('Cache Cleared')

    def show_current_pos(self, pt):
        if self.widget_name == 'down_side_technical':
            x, y = self.obj_sheet_down.get_pos()

            self.ui.current_pos_x.setText(str(int(x * 280)))  # zarbar arz varagh ya arzesh pixel

            self.ui.current_pos_y.setText(str(round(y * self.lenght, 2)))  # zarbar arz varagh ya arzesh pixel
        if self.widget_name == 'up_side_technical':
            x, y = self.obj_sheet_up.get_pos()

            self.ui.current_pos_x.setText(str(int(x * 280)))  # zarbar arz varagh ya arzesh pixel

            self.ui.current_pos_y.setText(str(round(y * self.lenght, 2)))  # zarbar arz varagh ya arzesh pixel

    def get_parent_path(self):

        self.db.report_last('default_setting', 'id', 30)
        parent_path = 'G:/oxin_image_grabber'  # MUST CHANGED -----------------
        # print('asdqwdf')
        return parent_path

    def set_b_parms(self):

        b_parms = self.ui.get_binary_parms()
        # ('Xbc', (300, 300), True, 2, 8, 0.001, 1, 0.2, ['/home/reyhane/PycharmProjects/trainApp_oxin1/dataset/binary', '/home/reyhane/PycharmProjects/trainApp_oxin1/dataset_user/binary'])
        if b_parms[2]:
            self.split_binary_dataset(b_parms[-1], b_parms[1])
        # update chart axes given train data
        self.update_b_chart_axes(b_parms[3])
        #
        t = threading.Thread(target=self.train_binary, args=(b_parms,))
        t.start()
        # t.join()

    def train_binary(self, b_parms):
        bmodel_records = train_api.train_binary(*b_parms, self.ds.weights_binary_path, self)
        binary_model_funcs.save_new_binary_model_record(ui_obj=self.ui, db_obj=self.db, bmodel_records=bmodel_records)

    def update_b_chart_axes(self, nepoch):
        for chart_postfix in self.ui.chart_names:
            eval('self.ui.axisX_%s' % chart_postfix).setRange(0, nepoch)
            if self.ui.binary_chart_checkbox.isChecked():
                eval('self.ui.axisX_%s' % chart_postfix).setTickCount(nepoch + 1)
            else:
                eval('self.ui.axisX_%s' % chart_postfix).setTickCount(chart_funcs.axisX_range + 1)
        chart_funcs.update_axisX_range(ui_obj=self.ui, nepoch=nepoch)
        chart_funcs.clear_series_date(ui_obj=self.ui, chart_postfixes=self.ui.chart_names)
        self.ui.binary_chart_checkbox.setEnabled(True)
        # self.ui.binary_chart_checkbox.setChecked(True)

    def assign_new_value_to_b_chart(self, last_epoch, logs):
        # print('here', last_epoch, logs)
        chart_funcs.update_chart(ui_obj=self.ui, chart_postfixes=self.ui.chart_names, last_epoch=last_epoch, logs=logs)

    def set_l_parms(self):

        l_parms = self.ui.get_localization_parms()

        print(l_parms)

    def save_to_dataset(self):
        sheet, pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
        self.ds.save(
            img_path=img_path,
            pos=pos,
            sheet=sheet,
            masks=self.label_bakcend['mask'].get(),
            bboxes=self.label_bakcend['bbox'].get()

        )

    def save_train_ds(self):
        masks = self.label_bakcend['mask'].get()
        bboxes = self.label_bakcend['bbox'].get()
        try:
            sheet, pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
            self.ds.save(
                img_path=img_path,
                pos=pos,
                sheet=sheet,
                masks=masks,
                bboxes=bboxes
            )
        except:
            self.ui.set_warning(texts.WARNINGS['NO_IMAGE_LOADED'][self.language], 'label', level=2)
            return

        labels = []
        for mask in masks:
            if mask[0] not in labels:
                labels.append(mask[0])

        for bbox in bboxes:
            if bbox[0] not in labels:
                labels.append(bbox[0])

        self.ds_json.add_update_classification(img_path, labels)

        saved_perfect = self.ds.check_saved_perfect(pos=pos)
        saved_defect = self.ds.check_saved_defect(pos=pos)

        if self.ui.no_defect.isChecked():
            # if saved_perfect:
            #     self.ui.set_warning(texts.WARNINGS['ALREADY_SAVED'][self.language], 'label', level=2)
            #     return
            if saved_defect:
                t = self.ui.show_question(texts.WARNINGS['ALREADY_SAVED_TITLE'][self.language],
                                          texts.WARNINGS['ALREADY_SAVED_DEFECT'][self.language])
                if not t:
                    return
                else:
                    self.ds.delete_from_defect(pos)
                    self.ds.delete_from_defect_splitted(pos)

            self.ds.save_to_perfect(img_path=img_path, pos=pos)
            crops = ImageCrops(Utils.read_image(img_path, 'gray'), self.size)
            self.ds.save_to_perfect_splitted(crops, pos=pos)
            self.binary_pieChart()
            self.ui.set_warning(texts.WARNINGS['IMAGE_SAVE_SUCCESSFULLY'][self.language], 'label', level=1)
            print('no defect')
            # try:
            self.ds_json.modify_perfect()
            # except:
            #     pass
        elif self.ui.yes_defect.isChecked():
            # if saved_defect:
            #     self.ui.set_warning(texts.WARNINGS['ALREADY_SAVED'][self.language], 'label', level=2)
            #     return
            if saved_perfect:
                t = self.ui.show_question(texts.WARNINGS['ALREADY_SAVED_TITLE'][self.language],
                                          texts.WARNINGS['ALREADY_SAVED_PERFECT'][self.language])
                if not t:
                    return
                else:
                    self.ds.delete_from_perfect(pos)
                    self.ds.delete_from_perfect_splitted(pos)
            self.ds.save_to_defect(img_path=img_path, pos=pos)
            crops = ImageCrops(Utils.read_image(img_path, 'gray'), self.size)
            self.ds.save_to_defect_splitted(crops, pos=pos)
            self.binary_pieChart()
            self.ui.set_warning(texts.WARNINGS['IMAGE_SAVE_SUCCESSFULLY'][self.language], 'label', level=1)
            try:
                self.ds_json.modify_defect()
            except:
                pass
        else:
            self.ui.set_warning(texts.WARNINGS['IMAGE_STATUS'][self.language], 'label', level=2)

    def split_binary_dataset(self, paths, size):
        for path in paths:
            if path == self.ds.binary_path and size == self.size:
                continue
            else:
                if path == self.ds.binary_path:
                    self.size = size
                    self.db.set_split_size(self.size, self.current['id'])
                if self.ds.check_binary_dataset(path):
                    self.ds.create_split_folder(path)

                    s = os.path.join(path, self.ds.defect_folder)
                    d = os.path.join(path, self.ds.defect_splitted_folder)
                    imgs = os.listdir(s)
                    for i in imgs:
                        img = Utils.read_image(os.path.join(s, i), color='color')
                        crops = ImageCrops(img, size)
                        self.ds.save_to_defect_splitted(crops, d, name=i.split('.')[0])

                    s = os.path.join(path, self.ds.perfect_folder)
                    d = os.path.join(path, self.ds.perfect_splitted_folder)
                    imgs = os.listdir(s)
                    for i in imgs:
                        img = Utils.read_image(os.path.join(s, i), color='color')
                        crops = ImageCrops(img, size)
                        self.ds.save_to_perfect_splitted(crops, d, i.split('.')[0])
                else:
                    self.ui.set_warning(texts.WARNINGS['DATASET_FORMAT'][self.language], 'train', level=2)
                    return

    def select_binary_dataset(self, page='train'):
        self.select_ds_dialog = FileDialog('Select a directory', '/')
        selected = self.select_ds_dialog.exec()

        if selected:
            dname = self.select_ds_dialog.selectedFiles()[0]
        else:
            return
        if dname == '':
            return
        if not self.ds.check_binary_dataset(dname):
            self.ui.set_warning(texts.WARNINGS['DATASET_FORMAT'][self.language], page, level=2)
            return
        #
        if page == 'train':
            text = self.ui.b_dp.toPlainText()
            pattern = r'[0-9]+. '
            datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]

            if dname in datasets:
                self.ui.set_warning(texts.WARNINGS['DATASET_EXIST'][self.language], page, level=2)
                return

            n = len(datasets) + 1
            if text != '': text += ' \n'
            self.ui.b_dp.setPlainText(text + str(n) + '. ' + dname)
        #
        elif page == 'binarylist':
            self.ui.binarylist_dataset_lineedit.setText(dname)
            self.ui.binarylist_dataset_annot_lineedit.setText(dname)

    def delete_binary_dataset(self):
        ds_n = self.ui.b_ds_num.value() - 1
        text = self.ui.b_dp.toPlainText()
        pattern = r'[0-9]+. '
        datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]
        if ds_n >= len(datasets):
            self.ui.set_warning(texts.WARNINGS['DATASET_NUMBER'][self.language], 'train', level=2)
            return
        datasets.pop(ds_n)
        text = ''
        for i in range(len(datasets)):
            text += str(i + 1) + '. ' + datasets[i]
            if i != len(datasets) - 1:
                text += '\n'

        self.ui.b_dp.setPlainText(text)

    def ok_add_binary_ds(self):
        path = self.ui.b_add_ds_lineedit.text().lstrip()
        path = path.rstrip()
        if not os.path.exists(path):
            self.ui.set_warning(texts.WARNINGS['INVALID_DATASET'][self.language], 'train', level=2)
            return
        elif not self.ds.check_binary_dataset(path):
            self.ui.set_warning(texts.WARNINGS['DATASET_FORMAT'][self.language], 'train', level=2)
            return

        text = self.ui.b_dp.toPlainText()
        pattern = r'[0-9]+. '

        datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]
        if path in datasets:
            self.ui.set_warning(texts.WARNINGS['DATASET_EXIST'][self.language], 'train', level=2)
        else:
            n = len(datasets) + 1
            if text != '': text += ' \n'
            self.ui.b_dp.setPlainText(text + str(n) + '. ' + path)
        self.ui.b_add_ds_lineedit.setText('')

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

    def get_camera_config(self, id):

        cam_parms = self.db.load_cam_params(id)
        return cam_parms

    def camera_connection_func(self):

        cam_num = self.ui.get_camera_parms()
        print('cam num', cam_num)

        if self.proc_start_flag:
            self.camera_process.start()
            # self.live.save_camera_images(self.cameras)
            self.proc_start_flag = False

        if cam_num != 'All':

            print('cam_num', cam_num)

            cam_parms = self.get_camera_config(str(cam_num))

            print('cam_parms', cam_parms)

            ret = self.cameras.add_camera(str(cam_num), cam_parms)

            if ret == 'True':
                self.ui.set_warning(texts.WARNINGS['Cmamera_successful'][self.language], 'camera_connection', level=1)

                self.ui.set_img_btn_camera(cam_num)

            else:
                if ret == 'Camera Not Connected':
                    self.ui.set_warning(texts.WARNINGS['Cmamera_serial_eror'][self.language], 'camera_connection',
                                        level=3)

                else:
                    self.ui.set_warning('Controlled by another application Or Config Eror ', 'camera_connection',
                                        level=3)

                self.ui.set_img_btn_camera(cam_num, status=False)

        else:
            self.auto_connect_all_cameras()

        self.set_available_caemras()

    def camera_disconnection_func(self):

        cam_num = self.ui.get_camera_parms()
        cam_parms = self.get_camera_config(str(cam_num))

        print('cam_num', cam_num)

        ret = self.cameras.disconnect_camera(cam_parms['serial_number'])

        if ret == 'True':
            self.ui.set_img_btn_camera(cam_num, status='Disconnect')
            self.ui.set_warning(texts.WARNINGS['Cmamera_successful'][self.language], 'camera_connection', level=1)
        elif ret == 'no_connection':
            self.ui.set_warning(texts.WARNINGS['no_connect'][self.language], 'camera_connection', level=2)

        else:
            self.ui.set_warning(texts.WARNINGS['disconnect_eror'][self.language], 'camera_connection', level=3)

    def auto_connect_all_cameras(self, first_cam=1):

        if self.index_num < 24:
            self.thread_connecting = threading.Timer(2, self.auto_connect_all_cameras).start()
            self.ui.update_combo_box(self.ui.comboBox_cam_select, self.index_num)
            self.camera_connection_func()

            self.index_num += 1
            print('asd')

        elif self.index_num == 24:

            self.index_num = 0

    # _________________________________________________________________________________________________
    # binary-model history page functions

    # binary-model history page functions
    def refresh_binary_models_table_onevent(self):
        self.bmodel_tabel_itr = 1
        self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))
        self.refresh_binary_models_table(get_count=True)
        self.refresh_binary_models_table()
        self.filter_mode = False
        self.ui.set_warning(texts.MESSEGES['REFRESH_TABLE'][self.language], 'binary_model_history', level=1)


    def refresh_binary_models_table(self, nextorprev=False, get_count=False, filter_mode=False):
        if get_count:
            self.bmodel_count = binary_model_funcs.get_binary_models_from_db(db_obj=self.db, count=get_count)[0][
                'count(*)']
            self.binary_model_tabel_nextorprev(check=True)
            return

        # load filterd models
        if filter_mode:
            self.bmodel_tabel_itr = 1
            self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))
            res = self.filter_binary_models(filter_signal=True, count=True)
            if res[0]:
                print(res[1])
                self.bmodel_count = res[1][0]['count(*)']
                self.binary_model_tabel_nextorprev(check=True)
                # print('count',self.bmodel_count)

                res = self.filter_binary_models(filter_signal=True)
                if res[0]:
                    bmodels_list = res[1]
                else:
                    self.refresh_binary_models_table(get_count=True)
                    bmodels_list = binary_model_funcs.get_binary_models_from_db(db_obj=self.db)
            else:
                self.refresh_binary_models_table(get_count=True)
                bmodels_list = binary_model_funcs.get_binary_models_from_db(db_obj=self.db)

        else:
            if not nextorprev:
                bmodels_list = binary_model_funcs.get_binary_models_from_db(db_obj=self.db)
            else:
                if not self.filter_mode:
                    bmodels_list = binary_model_funcs.get_binary_models_from_db(db_obj=self.db,
                                                                                limit_size=binary_model_funcs.binary_table_nrows,
                                                                                offset=(self.bmodel_tabel_itr - 1) * binary_model_funcs.binary_table_nrows)
                else:
                    res = self.filter_binary_models(
                        limit_size=binary_model_funcs.binary_table_nrows,
                        offset=(self.bmodel_tabel_itr - 1) * binary_model_funcs.binary_table_nrows)
                    bmodels_list = res[1]

        if len(bmodels_list) == 0 and nextorprev:
            return False

        # set returned models to UI table 
        else:
            binary_model_funcs.set_bmodels_on_ui_tabel(ui_obj=self.ui, bmodels_list=bmodels_list)
            return True


    # next and prev buttons for binary models table functionality
    def binary_model_tabel_nextorprev(self, next=True, check=False):
        if check:
            page_max = int(math.ceil(self.bmodel_count / binary_model_funcs.binary_table_nrows))
            if self.bmodel_tabel_itr >= page_max:
                self.ui.binary_tabel_next.setEnabled(False)
            else:
                self.ui.binary_tabel_next.setEnabled(True)
            #
            if self.bmodel_tabel_itr > 1:
                self.ui.binary_tabel_prev.setEnabled(True)
            else:
                self.ui.binary_tabel_prev.setEnabled(False)

            return
        #
        if next:
            self.bmodel_tabel_itr += 1

        elif self.bmodel_tabel_itr > 1:
            self.bmodel_tabel_itr -= 1
        #
        res = self.refresh_binary_models_table(nextorprev=True)
        self.binary_model_tabel_nextorprev(check=True)
        self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))

    # filter function for binary models
    def filter_binary_models(self, limit_size=binary_model_funcs.binary_table_nrows, offset=0, filter_signal=False, count=False):
        if filter_signal:
            self.filter_params = binary_model_funcs.get_binary_model_filter_info_from_ui(ui_obj=self.ui)
        #
        res = binary_model_funcs.get_filtered_binary_models_from_db(ui_obj=self.ui, db_obj=self.db,
                                                                    filter_params=self.filter_params, limit_size=limit_size, offset=offset,
                                                                    count=count)

        if res[0] == 'error':
            self.filter_mode = False
            return False, res[1]
        if res[0] == 'all':
            self.filter_mode = False
            return False, res[1]
        else:
            self.filter_mode = True
            self.ui.set_warning(texts.MESSEGES['FILTERED_RESAULTS_SUCCUSSFULL'][self.language], 'binary_model_history', level=1)
            return True, res[1]


    # clear filters for binary models
    def clear_filters(self):
        self.filter_mode = False
        self.bmodel_tabel_itr = 1
        self.ui.binary_tabel_page.setText(str(self.bmodel_tabel_itr))
        self.refresh_binary_models_table(get_count=True)
        self.refresh_binary_models_table()
        self.ui.set_warning(texts.MESSEGES['FILTERED_RESAULTS_CLEAR'][self.language], 'binary_model_history', level=1)

    # _________________________________________________________________________________________________
    # binary-list page functions
    # load binary images list
    def load_binary_images_list(self):
        if self.binarylist_sliders_check[0] and self.binarylist_sliders_check[1]:
            # get selected dataset parameters from
            #self.dataset_params = binary_list_funcs.get_params_from_ui(ui_obj=self.ui)
            # get selected datasets from ui
            datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
            selected_datasets = dataset.get_selected_datasets(ui_obj=self.ui, datasets_list=datasets_list, is_binarylist=True)
            if len(selected_datasets) == 0:
                self.ui.set_warning(texts.WARNINGS['SELECT_NO_DATASET'][self.language], 'binarylist', level=2)
                return
            
            # get image/annots list related to defect
            # get image pathes
            perfect_check, perfect_image_pathes, defect_check, defect_image_pathes, defect_annot_pathes, binary_count = binary_list_funcs.get_binarylist_image_pathes_list(ds_obj=self.ds,
                                                                                                                                        dataset_pathes=selected_datasets)
            print(perfect_check, defect_check)
            # validation
            if not perfect_check and not defect_check:
                self.ui.set_warning(texts.MESSEGES['NO_IMAGE_AVAILABLE_IN_DATASET'][self.language], 'binarylist', level=2)
            else:
                # msg
                self.ui.set_warning(texts.MESSEGES['LOAD_IMAGES_DATASETS'][self.language], 'binarylist', level=1)

            # create list object
            # perfect dir
            if perfect_check:
                self.binary_image_list.add(mylist=perfect_image_pathes, name=binary_list_funcs.image_list_object_names['perfect'])
                # create next and prev funcs
                self.perfect_image_list_next_func = self.binary_image_list.build_next_func(name=binary_list_funcs.image_list_object_names['perfect'])
                self.perfect_image_list_prev_func = self.binary_image_list.build_prev_func(name=binary_list_funcs.image_list_object_names['perfect'])
                # connect next and prev buttons to funcs
                self.ui.binary_list_perfect_prev_btn.setEnabled(True)
                self.ui.binary_list_perfect_next_btn.setEnabled(True)
                self.update_binary_images_on_ui()
            else:
                self.ui.binary_list_perfect_prev_btn.setEnabled(False)
                self.ui.binary_list_perfect_next_btn.setEnabled(False)
            
            # defect
            if defect_check:
                self.binary_image_list.add(mylist=defect_image_pathes, mylist_annots=defect_annot_pathes, name=binary_list_funcs.image_list_object_names['defect'])
                # create next and prev funcs
                self.defect_image_list_next_func = self.binary_image_list.build_next_func(name=binary_list_funcs.image_list_object_names['defect'])
                self.defect_image_list_prev_func = self.binary_image_list.build_prev_func(name=binary_list_funcs.image_list_object_names['defect'])
                # connect next and prev buttons to funcs
                self.ui.binary_list_defect_prev_btn.setEnabled(True)
                self.ui.binary_list_defect_next_btn.setEnabled(True)
                self.update_binary_images_on_ui(defect=True)
            else:
                self.ui.binary_list_defect_prev_btn.setEnabled(False)
                self.ui.binary_list_defect_next_btn.setEnabled(False)


            # update pie chart
            chart_funcs.update_binarylist_piechart(ui_obj=self.ui, binary_len=binary_count)

        # error in building image sliders
        else:
            self.ui.set_warning(texts.ERORS['BUILD_BINARYLIST_SLIDER_ERROR'][self.language], 'binarylist', level=3)


    # update slider images
    def update_binary_images_on_ui(self, defect=False, prevornext='False'):
        # next or prev on list
        if prevornext == 'next':
            if not defect:
                self.perfect_image_list_next_func()
            else:
                self.defect_image_list_next_func()
        # prev
        elif prevornext == 'prev':
            if not defect:
                self.perfect_image_list_prev_func()
            else:
                self.defect_image_list_prev_func()

        # get curent image list to set to UI
        if not defect:
            current_image_list = self.binary_image_list.get_n_current(name=binary_list_funcs.image_list_object_names['perfect'])
            current_annot_list =  ['' for i in range(len(current_image_list))]
        else:
            current_image_list, current_annot_list = self.binary_image_list.get_n_current(name=binary_list_funcs.image_list_object_names['defect'], get_annots=True)

        # set/update images on UI
        if not defect:
            res = binary_list_funcs.set_image_to_ui_slider(ui_obj=self.ui,
                                                           sub_directory=os.path.join(
                                                               self.dataset_params['dataset_path'],
                                                               self.ds.perfect_folder),
                                                           annot_sub_direcotory='./dataset/annotations',
                                                           image_path_list=current_image_list,
                                                           prefix=binary_list_funcs.widjet_prefixes['perfect'])
        else:
            res = binary_list_funcs.set_image_to_ui_slider(ui_obj=self.ui,
                                                           sub_directory=os.path.join(
                                                               self.dataset_params['dataset_path'],
                                                               self.ds.defect_folder),
                                                           annot_sub_direcotory='./dataset/annotations',
                                                           image_path_list=current_image_list,
                                                           prefix=binary_list_funcs.widjet_prefixes['defect'])
        # validate
        if not res:
            self.ui.set_warning(texts.ERORS['READ_BINARYLIST_IMAGES_ERROR'][self.language], 'binarylist', level=3)


    # classification page
    #------------------------------------------------------------------------------------------------------------------------
    # get defects from database and apply to defects table
    def refresh_classes_table(self):
        defects_list = classification_list_funcs.get_defects_from_db(db_obj=self.db)
        defects_list = classification_list_funcs.change_defect_group_id_to_name(db_obj=self.db, defects_list=defects_list)
        classification_list_funcs.set_defects_on_ui(ui_obj=self.ui, defects_list=defects_list)
        classification_list_funcs.set_defects_on_train_ui(ui_obj=self.ui, defects_list=defects_list)
        classification_model_funcs.set_defects_on_filter_ui(ui_obj=self.ui, defects_list=defects_list)


    # get datasets from database and apply to datasets table
    def refresh_datasets_table(self, is_binarylist=False):
        # get dataset
        # read all datasets in table (must update)
        datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
        # show on UI
        if not is_binarylist:
            # classlist
            dataset.set_datasets_on_ui(ui_obj=self.ui, datasets_list=datasets_list, current_user=self.login_user_name, default_dataset=self.default_dataset_user)
        else:
            # binarylist
            dataset.set_datasets_on_ui(ui_obj=self.ui,
                                        datasets_list=datasets_list,
                                        current_user=self.login_user_name,
                                        default_dataset=self.default_dataset_user,
                                        is_binarylist=is_binarylist)
    

    # show class related images on UI
    def show_class_related_images(self):
        # get selected defects from UI
        defects_list = classification_list_funcs.get_defects_from_db(db_obj=self.db)
        selected_defects = classification_list_funcs.get_selected_defects(ui_obj=self.ui)
        if len(selected_defects) > 1:
            self.ui.set_warning(texts.WARNINGS['SELECT_MORE_THAN_ONE_DEFECT_CLASS'][self.language], 'classlist_msg_label', level=2)
        elif len(selected_defects) == 0:
            self.ui.set_warning(texts.WARNINGS['SELECT_NO_DEFECT_CLASS'][self.language], 'classlist_msg_label', level=2)
        else:
            # get selected datasets from ui
            datasets_list = dataset.get_datasets_list_from_db(db_obj=self.db)
            selected_datasets = dataset.get_selected_datasets(ui_obj=self.ui, datasets_list=datasets_list)
            if len(selected_datasets) == 0:
                self.ui.set_warning(texts.WARNINGS['SELECT_NO_DATASET'][self.language], 'classlist_msg_label', level=2)
                return

            # get image/annots list related to defect
            annotation_list, image_list, binary_count, classes_count = classification_list_funcs.load_images_related_to_defect(datasets_list=selected_datasets, defect_id=selected_defects[0])

            # create list object
            self.classification_image_list.add(mylist=image_list, mylist_annots=annotation_list, name=self.classification_image_list_name)
            # create next and prev funcs
            self.classification_image_list_next_func = self.classification_image_list.build_next_func(name=self.classification_image_list_name)
            self.classification_image_list_prev_func = self.classification_image_list.build_prev_func(name=self.classification_image_list_name)
            # 
            self.update_classlist_images_on_ui()
            
            # no images available
            if len(annotation_list) == 0 and len(image_list) == 0:
                # msg
                self.ui.set_warning(texts.MESSEGES['NO_IMAGE_AVAILABLE_WITH_DEFECT'][self.language], 'classlist_msg_label', level=2)
                # disable next/prev/buttons
                self.ui.classlist_prev_btn.setEnabled(False)
                self.ui.classlist_next_btn.setEnabled(False)
            else:
                # msg
                self.ui.set_warning(texts.MESSEGES['LOAD_IMAGES_WITH_DEFECT'][self.language], 'classlist_msg_label', level=1)
                # disable next/prev/buttons
                self.ui.classlist_prev_btn.setEnabled(True)
                self.ui.classlist_next_btn.setEnabled(True)
            
            # update pie chart
            chart_funcs.update_classlist_piechart(ui_obj=self.ui, binary_len=binary_count, classes_len=classes_count, classes_list=defects_list)
        
    
    # update slider images
    def update_classlist_images_on_ui(self, prevornext='False'):
        # next or prev on list
        if prevornext == 'next':
            self.classification_image_list_next_func()
        # prev
        elif prevornext == 'prev':
            self.classification_image_list_prev_func()

        # get curent image list to set to UI
        current_image_list, current_annots_list = self.classification_image_list.get_n_current(name=self.classification_image_list_name, get_annots=True)

        # set/update images on UI
        res = binary_list_funcs.set_image_to_ui_slider_full_path(ui_obj=self.ui,
                                                                image_path_list=current_image_list,
                                                                annot_path_list=current_annots_list,
                                                                prefix=self.classification_image_list_name,
                                                                image_per_row=binary_list_funcs.n_images_per_row_classlist)

        # validate (must update)
        # if not res:
        #     self.ui.set_warning(texts.WARNINGS['READ_BINARYLIST_IMAGES_ERROR'][self.language], 'binarylist', level=2)

    
    # check classification params
    def check_classification_train_params(self):
        # get train params from UI
        cls_parms = self.ui.get_classification_parms()
        selected_defects = classification_list_funcs.get_selected_defects_for_train(ui_obj=self.ui)
        #
        if len(selected_defects) == 0:
            self.ui.show_mesagges(self.ui.classification_train_msg_label, 'Please select at least one class', color=colors_pallete.failed_red)
        
        else:
            cls_parms += [selected_defects]
            print('cls params:', cls_parms)
        # update chart axes given train data
        #self.update_b_chart_axes(b_parms[3])
        #
        #bmodel_records = train_api.train_binary(*b_parms, self.ds.weights_binary_path, self)
        #binary_model_funcs.save_new_binary_model_record(ui_obj=self.ui, db_obj=self.db, bmodel_records=bmodel_records)
    

    # pie chart funcs
    def create_classlist_pie_chart(self):
        # classlist page
        chart_funcs.create_classlist_piechart_on_ui(ui_obj=self.ui, frame_obj_binary=self.ui.binary_chart_frame, frame_obj_classlist=self.ui.classlist_chart_frame)
        # binarylist page
        chart_funcs.create_binarylist_piechart_on_ui(ui_obj=self.ui, frame_obj_binary=self.ui.binarylist_chart_frame)


    
    # _________________________________________________________________________________________________
    # classification-model history page functions
    def refresh_cls_models_table_onevent(self):
        self.clsmodel_tabel_itr = 1
        self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))
        self.refresh_cls_models_table(get_count=True)
        self.refresh_cls_models_table()
        self.cls_filter_mode = False
        self.ui.set_warning(texts.MESSEGES['REFRESH_TABLE'][self.language], 'classification_model_history', level=1)


    def refresh_cls_models_table(self, nextorprev=False, get_count=False, filter_mode=False):
        if get_count:
            self.clsmodel_count = classification_model_funcs.get_cls_models_from_db(db_obj=self.db, count=get_count)[0]['count(*)']
            self.cls_model_tabel_nextorprev(check=True)
            return

        # load filterd models
        if filter_mode:
            self.clsmodel_tabel_itr = 1
            self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))
            res = self.filter_cls_models(filter_signal=True, count=True)
            if res[0]:
                print(res[1])
                self.clsmodel_count = res[1][0]['count(*)']
                self.cls_model_tabel_nextorprev(check=True)

                res = self.filter_cls_models(filter_signal=True)
                if res[0]:
                    clsmodels_list = res[1]
                else:
                    self.refresh_cls_models_table(get_count=True)
                    clsmodels_list = classification_model_funcs.get_cls_models_from_db(db_obj=self.db)
            else:
                self.refresh_cls_models_table(get_count=True)
                clsmodels_list = classification_model_funcs.get_cls_models_from_db(db_obj=self.db)

        else:
            if not nextorprev:
                clsmodels_list = classification_model_funcs.get_cls_models_from_db(db_obj=self.db)
            else:
                if not self.cls_filter_mode:
                    clsmodels_list = classification_model_funcs.get_cls_models_from_db(db_obj=self.db,
                                                                                    limit_size=classification_model_funcs.cls_table_nrows,
                                                                                    offset=(self.clsmodel_tabel_itr - 1) * classification_model_funcs.cls_table_nrows)
                else:
                    res = self.filter_cls_models(
                        limit_size=classification_model_funcs.cls_table_nrows,
                        offset=(self.clsmodel_tabel_itr - 1) * classification_model_funcs.cls_table_nrows)
                    clsmodels_list = res[1]

        if len(clsmodels_list) == 0 and nextorprev:
            return False

        # set returned models to UI table 
        else:
            classification_model_funcs.set_clsmodels_on_ui_tabel(ui_obj=self.ui, models_list=clsmodels_list)
            return True
    

    # next and prev buttons for binary models table functionality
    def cls_model_tabel_nextorprev(self, next=True, check=False):
        if check:
            page_max = int(math.ceil(self.clsmodel_count / classification_model_funcs.cls_table_nrows))
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
    def filter_cls_models(self, limit_size=classification_model_funcs.cls_table_nrows, offset=0, filter_signal=False, count=False):
        if filter_signal:
            self.cls_filter_params = classification_model_funcs.get_cls_model_filter_info_from_ui(ui_obj=self.ui)
        #
        res = classification_model_funcs.get_filtered_cls_models_from_db(ui_obj=self.ui, db_obj=self.db,
                                                                        filter_params=self.cls_filter_params, limit_size=limit_size, offset=offset,
                                                                        count=count)

        if res[0] == 'error':
            self.cls_filter_mode = False
            return False, res[1]
        if res[0] == 'all':
            self.cls_filter_mode = False
            return False, res[1]
        else:
            self.cls_filter_mode = True
            self.ui.set_warning(texts.MESSEGES['FILTERED_RESAULTS_SUCCUSSFULL'][self.language], 'classification_model_history', level=1)
            return True, res[1]
            
    
    
    # clear filters for binary models
    def clear_filters_cls(self):
        self.cls_filter_mode = False
        self.clsmodel_tabel_itr = 1
        self.ui.cls_tabel_page.setText(str(self.clsmodel_tabel_itr))
        self.refresh_cls_models_table(get_count=True)
        self.refresh_cls_models_table()
        self.ui.set_warning(texts.MESSEGES['FILTERED_RESAULTS_CLEAR'][self.language], 'classification_model_history', level=1)



    #_____________________________________________________________________________________________________

    def set_available_caemras(self):

        connected_cameras = self.cameras.get_connected_cameras()

        sn_available = connected_cameras.keys()

        self.ui.set_list_combo_boxes(self.ui.comboBox_connected_cams, sn_available)

    def update_cameras(self):

        print('asd')

    def get_image(self):
        return self.img

    def binary_pieChart(self):
        labels = ['Yes', 'No']
        num_yes = len(os.listdir(self.ds.defect_path))
        num_no = len(os.listdir(self.ds.perfect_path))
        sizes = [num_yes, num_no]
        self.show_pieChart(labels, sizes)

    def show_pieChart(self, labels, sizes):
        if sizes != [0, 0]:
            self.ui.pieChart.figure.clf()
            ax = self.ui.pieChart.figure.add_subplot(111)
            ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                   shadow=True, startangle=90)
            # Equal aspect ratio ensures that pie is drawn as a circle
            ax.axis('equal')
            self.ui.pieChart.draw()

    def create_mask_from_mask(self, img_path):
        labels = self.label_memory.get_label('mask', img_path)
        mask = np.zeros((self.img.shape[0], self.img.shape[1]))
        for lbl, cnt in labels:
            cv2.drawContours(mask, [cnt], 0, color=255, thickness=-1)
        return mask

    def create_mask_from_bbox(self, img_path):
        labels = self.label_memory.get_label('bbox', img_path)
        mask = np.zeros((self.img.shape[0], self.img.shape[1]))
        for label in labels:
            point = label[1].flatten()
            cv2.rectangle(mask, (point[0], point[1]), (point[2], point[3]), 255, -1)
        return mask

    def create_Heatmap(self):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
        self.create_mask_from_mask(img_path)
        img = Utils.read_image(img_path, 'gray')
        label_type = self.ui.get_label_type()
        if label_type == 'mask':
            df = self.create_mask_from_mask(img_path)
            hm = CreateHeatmap(img, df)
        elif label_type == 'bbox':
            df = self.create_mask_from_bbox(img_path)
            hm = CreateHeatmap(img, df)
        self.ui.show_neighbouring(hm)

    # def create_piechart(self):
    #     series = QPieSeries()
    #     series.append("Yes", 80)
    #     series.append("No", 50)
    #     series.setLabelsVisible(True)
    #
    #     series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
    #     for slice in series.slices():
    #         slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
    #
    #     # adding slice
    #     # slice = series.slices()[2]
    #     # slice.setExploded(True)
    #     # slice.setLabelVisible(True)
    #     # slice.setPen(QPen(Qt.darkGreen, 2))
    #     # slice.setBrush(Qt.red)
    #
    #     chart = QChart()
    #     chart.legend().hide()
    #     chart.addSeries(series)
    #     chart.createDefaultAxes()
    #     chart.setAnimationOptions(QChart.SeriesAnimations)
    #     chart.setMargins(QMargins(0, 0, 0, 0))
    #
    #     chart.legend().setVisible(True)
    #     chart.legend().setAlignment(Qt.AlignBottom)
    #
    #     chart.legend().markers(series)[0].setLabel("Yes")
    #     chart.legend().markers(series)[1].setLabel("No")
    #
    #     chartview = self.ui.piechart
    #     chartview.setChart(chart)
    #     chartview.setRenderHint(QPainter.Antialiasing)

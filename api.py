# from logging import _Level
import re
import sys
from ast import Try
from email import utils

from PySide6 import QtGui
from PySide6.QtCharts import QPieSeries, QPieSlice, QChart, QChartView
from PySide6.QtCore import *
from PySide6.QtGui import QPen, QPainter
from PySide6.QtWidgets import QFileDialog
from matplotlib import pyplot as plt

from Defect_detection_modules.SteelSurfaceInspection import SSI, CreateHeatmap_bbox
from app_settings import Settings
from backend import data_grabber
from backend.mouse import Mouse
from backend.keyboard import Keyboard
# from backend import Label
import cv2
import threading
import time
from PIL import ImageQt
import numpy as np
import os
from datetime import date, time, datetime
from PyQt5.QtWidgets import QListWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
# from backend import add_remove_label
from PyQt5 import QtCore, QtWidgets
from Sheet_loader_win import get_data
from functools import partial
from backend import Label

import database_utils
from utils import *
from utils.move_on_list import moveOnList

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
        self.ds = Dataset(self.db.get_dataset_path(), self.db.get_dataset_path_uesr(), self.db.get_weights_path())
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
        self.size = self.db.get_split_size()
        self.img = None
        self.n_imgs = []

        self.ui.set_default_db_parms(self.ds.binary_path, self.size)

        self.logged_in=False
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




        # DEBUG_FUNCTIONS
        # -------------------------------------
        # self.__debug_load_sheet__(['996','997'])
        # self.__debug_select_random__()
        # self.__debug_select_for_label()

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

    #----------------------------------------------------------------------------------------
    # 
    #----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------

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
        self.ui.login_btn.clicked.connect(partial(self.show_login))
        # self.ui.split_dataset.clicked.connect(partial(self.split_binary_dataset))

        # labeling

        # self.labaling_UI.save_btn.clicked.connect(partial(self.set_label))





    def mouse_connector(self):
        for _, technical_widget in self.ui.get_technical().items():
            self.mouse.connet(technical_widget, self.update_technical_pointer_mouse)

        self.mouse.connect_all(self.ui.image, self.label_image_mouse)
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
        if img_path not in self.detect_bboxs_imgs:
            bboxs = SSI(self.img, block_size='Medium', defect_th=0, noise_th=7, noise=True, heatmap=False)
            for bbox in bboxs:
                t = self.label_bakcend['bbox'].get()
                label = ['oil', np.array(bbox)]
                t.append(label)
                self.label_memory.add(img_path,
                                      t,
                                      'bbox')
            self.detect_bboxs_imgs.append(img_path)

    def load_image_to_label_page(self):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
        label_type=self.ui.get_label_type()
        self.img = Utils.read_image( img_path, 'color')
        self.find_bboxs(img_path)
        label = self.label_memory.get_label(label_type, img_path)
        self.label_bakcend[label_type].load(label)

        label_img = self.label_bakcend[label_type].draw()
        self.img = Utils.add_layer_to_img(self.img, label_img, opacity=0.4, compress=0.5 )
        self.ui.show_image_in_label( self.img )

        print(self.label_bakcend[label_type].get())
        print(label, img_path)

        self.load_neighbour_images(selected_img_pos)

        self.ui.show_image_info_lable_page(sheet,selected_img_pos)

        self.ui.image.setScaledContents(True)
        self.scale = 1
        self.position = [0, 0]

    def load_neighbour_images(self, selected_img_pos):
        c = selected_img_pos[-1][0]
        f = selected_img_pos[-1][1]
        neighbours = []
        n_up_left = [selected_img_pos[0], selected_img_pos[1], (c-1, f-1)]
        neighbours.append(n_up_left)
        n_up = [selected_img_pos[0], selected_img_pos[1], (c, f-1)]
        neighbours.append(n_up)
        n_up_right = [selected_img_pos[0], selected_img_pos[1], (c+1, f-1)]
        neighbours.append(n_up_right)
        n_left = [selected_img_pos[0], selected_img_pos[1], (c-1, f)]
        neighbours.append(n_left)
        n_right = [selected_img_pos[0], selected_img_pos[1], (c+1, f)]
        neighbours.append(n_right)
        n_down_left = [selected_img_pos[0], selected_img_pos[1], (c-1, f+1)]
        neighbours.append(n_down_left)
        n_down = [selected_img_pos[0], selected_img_pos[1], (c, f+1)]
        neighbours.append(n_down)
        n_down_right = [selected_img_pos[0], selected_img_pos[1], (c+1, f+1)]
        neighbours.append(n_down_right)

        paths = self.db.get_path_sheet_image(neighbours)

        self.n_imgs = []
        label_type = self.ui.get_label_type()
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
        self.LABEL_COLOR = {'black': (0, 0,0)}
        defect_name,defect_info=self.get_defects()
        # print(len(defect_info),defect_info)
        for i in range(len(defect_info)):
            print(defect_name[i],defect_info[i]['color'])
            hex_color=defect_info[i]['color'].lstrip('#')
            rgb_color=tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            rgb=(rgb_color[2],rgb_color[1],rgb_color[0])
            self.LABEL_COLOR.update({defect_name[i]:rgb})

    def label_image_mouse(self, wgt_name=''):

        label_type=self.ui.get_label_type()
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()

        if self.ui.get_zoom_type() is None:
            try:
                sheet, pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
                img = Utils.read_image( img_path, 'color')
                self.label_bakcend[label_type].mouse_event(mouse_status, mouse_button, mouse_pt)
                if self.label_bakcend[label_type].is_drawing_finish():
                    if label_type=='mask':
                        # print('asdwqdqwd')
                        self.finish_draw+=1
                        if self.finish_draw==2:
                            self.finish_draw=0

                        # self.label_bakcend[label_type].save('1')
                            self.show_labeling(label_type)
                    elif self.ui.labeling_win==None:
                        self.show_labeling(label_type)
                label_img = self.label_bakcend[label_type].draw()
                img = Utils.add_layer_to_img(img, label_img, opacity=0.4, compress=0.5 )
                self.ui.show_image_in_label(img, self.scale, self.position)
                self.img = img

                self.label_memory.add(  img_path,
                                        self.label_bakcend[label_type].get(),
                                        label_type )
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



    def get_defects(self):
        self.defects_name,self.defects_info=self.db.get_defects()

        return self.defects_name,self.defects_info


    def show_labeling(self,label_type):

            current_mouse_position = self.mouse_controll.position
            print(current_mouse_position)

            sign_defect_table=self.db.ret_sign_defect_table()
            print('sign_defect_table',sign_defect_table)
            if sign_defect_table==0:
                print('nochange')
            else:
                print('change')
                try:
                    self.defects_name,self.defects_info=self.db.get_defects()
                    self.db.update_sign_table('defects_info','0')
                except:
                    pass
            # self.create_labeling()
            labeling_win=self.ui.ret_create_labeling()
            self.labeling_api=labeling_api.labeling_API(labeling_win,self.defects_name,self.defects_info)
            self.ui.labeling_win.win_set_geometry(left=current_mouse_position[0],top=current_mouse_position[1])
            self.ui.labeling_win.save_btn.clicked.connect(partial(self.set_label))
            self.ui.labeling_win.cancel_btn.clicked.connect(partial(self.close_labeling))
            self.ui.labeling_win.show()
            print('end show_labeling')

    def show_login(self):

        if self.logged_in==False:

            login_window=self.ui.ret_create_login()
            self.login_api=login_API(login_window)
            # self.login_api.button_connector()
            login_window.login_btn.clicked.connect(partial(self.check_login))
            print('show_ui')
            self.ui.login_window.show()
        else :
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
        self.logged_in=False
        self.ui.show_image_btn(self.ui.login_btn,'images/icons/person.png')
        self.ui.user_name.setText('')


    def check_login(self):

        self.login_info=self.login_api.check_login()
        print('ret 0 ',self.login_info[0])
        if self.login_info[0]==True:

            print('ok')
            self.ui.user_name.setText(self.login_info[1]['user_name'])
            self.ui.show_image_btn(self.ui.login_btn,'images/logout.png')
            self.logged_in=True

    def set_label(self):

            selected_label=self.labeling_api.ret_selcted_label()
            label_type=self.ui.get_label_type()
            self.label_bakcend[label_type].save(str(selected_label))
            print('end set_label',selected_label)
            self.ui.labeling_win.close_win()
            self.ui.labeling_win = None
            print(label_type)
            # label_type_dict=['masks','bboxs']

            labels=self.label_bakcend[label_type].get()
            # print(labels[1])

            self.ui.show_labels(labels,label_type)

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
        train_api.train_binary(*b_parms, self.ds.weights_binary_path)

    def set_l_parms(self):

        l_parms = self.ui.get_localization_parms()

        print(l_parms)



    def save_to_dataset(self):
        sheet, pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
        self.ds.save(
            img_path=img_path,
            pos = pos,
            sheet= sheet,
            masks= self.label_bakcend['mask'].get(),
            bboxes=self.label_bakcend['bbox'].get()

        )

    def save_train_ds(self):
        try:
            sheet, pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
            self.ds.save(
                img_path=img_path,
                pos=pos,
                sheet=sheet,
                masks=self.label_bakcend['mask'].get(),
                bboxes=self.label_bakcend['bbox'].get()
            )
        except:
            self.ui.set_warning(texts.WARNINGS['NO_IMAGE_LOADED'][self.language], 'label', level=2)
            return

        saved_perfect = self.ds.check_saved_perfect(pos=pos)
        saved_defect = self.ds.check_saved_defect(pos=pos)

        if self.ui.no_defect.isChecked():
            if saved_perfect:
                self.ui.set_warning(texts.WARNINGS['ALREADY_SAVED'][self.language], 'label', level=2)
                return
            if saved_defect:
                t = self.ui.show_question(texts.WARNINGS['ALREADY_SAVED_TITLE'][self.language],
                                          texts.WARNINGS['ALREADY_SAVED_DEFECT'][self.language])
                if not t:
                    return
                else:
                    self.ds.delete_from_defect(pos)
                    self.ds.delete_from_defect_splitted(pos)

            self.ds.save_to_perfect(img_path=img_path, pos=pos)
            crops = ImageCrops(self.img, self.size)
            self.ds.save_to_perfect_splitted(crops, pos=pos)
            self.binary_pieChart()
            self.ui.set_warning(texts.WARNINGS['IMAGE_SAVE_SUCCESSFULLY'][self.language], 'label', level=1)

        elif self.ui.yes_defect.isChecked():
            if saved_defect:
                self.ui.set_warning(texts.WARNINGS['ALREADY_SAVED'][self.language], 'label', level=2)
                return
            if saved_perfect:
                t = self.ui.show_question(texts.WARNINGS['ALREADY_SAVED_TITLE'][self.language],
                                          texts.WARNINGS['ALREADY_SAVED_PERFECT'][self.language])
                if not t:
                    return
                else:
                    self.ds.delete_from_perfect(pos)
                    self.ds.delete_from_perfect_splitted(pos)
            self.ds.save_to_defect(img_path=img_path, pos=pos)
            crops = ImageCrops(self.img, self.size)
            self.ds.save_to_defect_splitted(crops, pos=pos)
            self.binary_pieChart()
            self.ui.set_warning(texts.WARNINGS['IMAGE_SAVE_SUCCESSFULLY'][self.language], 'label', level=1)

        else:
            self.ui.set_warning(texts.WARNINGS['IMAGE_STATUS'][self.language], 'label', level=2)


    def split_binary_dataset(self, paths, size):
        for path in paths:
            if path == self.ds.binary_path and size == self.size:
                continue
            else:
                if path == self.ds.binary_path:
                    self.size = size
                    self.db.set_split_size(self.size)
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

    def select_binary_dataset(self):
        self.select_ds_dialog = FileDialog('Select a directory', self.ds.dataset_path_user)
        selected = self.select_ds_dialog.exec()

        if selected:
            dname = self.select_ds_dialog.selectedFiles()[0]
        else:
            return
        if dname == '':
            return
        if not self.ds.check_binary_dataset(dname):
            self.ui.set_warning(texts.WARNINGS['DATASET_FORMAT'][self.language], 'train', level=2)
            return
        text = self.ui.b_dp.toPlainText()
        pattern = r'[0-9]+. '
        datasets = [s.rstrip() for s in re.split(pattern, text)[1:]]

        if dname in datasets:
            self.ui.set_warning(texts.WARNINGS['DATASET_EXIST'][self.language], 'train', level=2)
            return

        n = len(datasets) + 1
        if text != '': text += ' \n'
        self.ui.b_dp.setPlainText(text + str(n) + '. ' + dname)

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

    def create_mask_from_mask(self):
        pass

    def create_mask_from_bbox(self):
        sheet, selected_img_pos, img_path = self.move_on_list.get_current('selected_imgs_for_label')
        labels = self.label_memory.get_label('bbox', img_path)
        mask = np.zeros((self.img.shape[0], self.img.shape[1]))
        for label in labels:
            point = label[1].flatten()
            cv2.rectangle(mask, (point[0], point[1]), (point[2], point[3]), 255, -1)
        return mask

    def create_Heatmap(self):
        label_type = self.ui.get_label_type()
        if label_type == 'bbox':
            df = self.create_mask_from_bbox()
            hm = CreateHeatmap_bbox(self.img, df)
            cv2.imshow('', hm)


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

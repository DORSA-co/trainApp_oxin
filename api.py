
# from logging import _Level
from ast import Try
from email import utils
from PySide6.QtCore import *
from backend import data_grabber
from backend.mouse import Mouse
from backend.keyboard import Keyboard
from backend import Label
import cv2
import threading
import time
from PIL import ImageQt
import numpy as np
import os
from datetime import date, time, datetime
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtGui import QPixmap,QImage
# from backend import add_remove_label
from PyQt5 import QtCore
from Sheet_loader_win import get_data
from functools import partial
from backend import Label

import database_utils
from utils import *
from utils.move_on_list import moveOnList

import texts #eror and warnings texts
from utils import tempMemory, Utils

from backend.Dataset import Dataset

WIDTH_TECHNICAL_SIDE = 49*12
HEIGHT_FRAME_SIZE = 51
NCAMERA = 12

TECHNICAL_WGT_NAME_TO_SIDE = {'up_side_technical', 'top', 'bottom'}
LABEL_COLOR = {'1':(0,0,255)}






#down_side_technical     ,   up_side_technical
class API:

    def __init__(self,ui):
        self.ui = ui
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.move_on_list = moveOnList()
        self.db = database_utils.dataBaseUtils()
        self.ds = Dataset(self.db.get_dataset_path())
        #self.mask_label_backend=Label.maskLbl(self.ui.get_size_label_image(), LABEL_COLOR)
        self.label_bakcend = {
                            'mask': Label.maskLbl((1200,1920), LABEL_COLOR),
                            'bbox': Label.bboxLbl((1200,1920), LABEL_COLOR)
                            }
        
        
        #Label.bbox_lbl()

        #self.technical_backend = {'top': data_grabber()}
        self.thechnicals_backend = {}
        #self.ui.crop_image.mouseDoubleClickEvent = self.fit_image
        self.t = 0
        self.current_technical_side = ''
        self.selected_images_for_label = tempMemory.manageSelectedImage()

        self.language='en' 


        #-------------------------------------
        #connet buttons to correspondings functions in API               ////////////////////
        self.button_connector()
        #connet mouse event to correspondings functions in API
        self.mouse_connector()
        #connet keyboard event to correspondings functions in API
        self.keyboard_connector()
        #-------------------------------------

        #DEBUG_FUNCTIONS
        #-------------------------------------
        self.__debug_load_sheet__(['996','997'])
        self.__debug_select_random__()
        self.__debug_select_for_label()




    def __debug_load_sheet__(self,ids):
        self.move_on_list.add(ids, 'sheets_id')
        self.selected_images_for_label.clear()
        self.load_sheet()
    
    def __debug_select_random__(self,):
        for id in range(self.move_on_list.get_count('sheets_id')):
            self.next_sheet()
            for side in ['up','down']:
                for _ in range( np.random.randint(0,5)):
                    cam = np.random.randint( self.sheet.get_cameras()[0],  self.sheet.get_cameras()[1] +1)
                    frame = np.random.randint(0, self.sheet.get_nframe()+1)
                    self.selected_images_for_label.add( self.move_on_list.get_current('sheets_id'), side, (cam,frame) ) 
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

    def mouse_connector(self):
        for _,technical_widget in self.ui.get_technical().items():
            self.mouse.connet( technical_widget, self.update_technical_pointer_mouse )

        self.mouse.connect_all(self.ui.image, self.label_image_mouse)
        self.mouse.connet_dbclick( self.ui.crop_image, self.fit_image)


    def keyboard_connector(self):
        self.keyboard.connet( self.ui, ['left','right','up','down'], [self.update_technical_pointer_keyboard], 'Technical View' )



        
    #----------------------------------------------------------------------------------------
    #get id of sheets that user select in load_sheet_win and load first one
    #---------------------------------------------------------------------------------------- 
    def load_sheets(self): 
        
        sheets_id = self.ui.load_sheets_win.get_selected_sheetid()
        self.move_on_list.add(sheets_id, 'sheets_id')
        self.selected_images_for_label.clear()
        self.ui.load_sheets_win.close()
        self.load_sheet()        
    
    #----------------------------------------------------------------------------------------
    #load sheet by its id in software
    #---------------------------------------------------------------------------------------- 
    def load_sheet(self): 
        selceted_sheets_id = self.move_on_list.get_current('sheets_id')#get current value on list that corespond to "coils_id" name 
        self.sheet = self.db.load_sheet( selceted_sheets_id )#load inference of Sheet class from database by sheet id
        self.build_sheet_technical( self.sheet  ) #build technical sheet          
        self.ui.show_sheet_details(self.sheet.get_info_dict())   # show sheet details in UI.details_label

    #----------------------------------------------------------------------------------------
    #
    #---------------------------------------------------------------------------------------- 
    def build_sheet_technical(self,sheet):
        try:
            self.thechnicals_backend = {}
            for side,_ in self.ui.get_technical(name=False).items():
                self.thechnicals_backend[side] = data_grabber.sheetOverView(sheet,
                                                                            side, #side of sheet that is UO
                                                                            (HEIGHT_FRAME_SIZE*sheet.get_nframe(),WIDTH_TECHNICAL_SIDE),
                                                                            (self.sheet.get_nframe(), NCAMERA),#sheet.get_grade_shape(),
                                                                            actives_camera=sheet.get_cameras(),
                                                                            oriation=data_grabber.VERTICAL)
                

                selecteds = self.selected_images_for_label.get_sheet_side_selections( 
                                                                                    str(self.sheet.get_id()),
                                                                                    side
                                                                                        )

                self.thechnicals_backend[side].update_selected(selecteds)
                self.current_technical_side = side
                self.refresh_thechnical(fp=1) #
            
        except:
            print('Error!: load_sheet() in API')
    #----------------------------------------------------------------------------------------
    #when next next_coil_btn clicked this function move on next coil id and load it
    #----------------------------------------------------------------------------------------
    def next_sheet(self):
        if self.move_on_list.check('sheets_id'):
            self.move_on_list.next_on_list('sheets_id')#move previous on list that corespond to "coils_id" name
            self.load_sheet()# laod current coil id 
        
        else:
            self.ui.set_warning_data_page(texts.WARNINGS['NO_SHEET'][self.language],'data_auquzation',level=2)
    #----------------------------------------------------------------------------------------
    #when next next_coil_btn clicked this function move on privous coil id and load it
    #----------------------------------------------------------------------------------------
    def prev_sheet(self):
        if self.move_on_list.check('sheets_id'):
            self.move_on_list.prev_on_list('sheets_id')#move next on list that corespond to "coils_id" name
            self.load_sheet()# laod current coil id 
        else:
            self.ui.set_warning_data_page(texts.WARNINGS['NO_SHEET'][self.language],'data_auquzation',level=2)
    

    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def update_sheet_img(self, name):
        img=self.thechnicals_backend[name].get_sheet_img()
        self.ui.set_img_sheet(img, name)
    #----------------------------------------------------------------------------------------
    #
    #----------------------------------------------------------------------------------------
    def show_pointer_position(self):
        x,y = self.thechnicals_backend[ self.current_technical_side ].get_pos()#get mouse position normilized between [0,1]
        x*=self.sheet.get_width()
        y*=self.sheet.get_lenght()
        y = np.round(y,1)
        x = np.round(x,1)
        self.ui.show_current_position((x,y))



    def update_technical_pointer_keyboard(self,key):
        self.thechnicals_backend[ self.current_technical_side ].update_pointer_keyboard(key)    
        self.refresh_thechnical(fp=1)
        self.show_pointer_position()

    def update_technical_pointer_mouse(self,widget_name):
        if len( self.thechnicals_backend ) == 0:
            self.ui.set_warning_data_page(texts.WARNINGS['NO_SHEET'][self.language],'data_auquzation',level=2)
        
        else:
            self.current_technical_side = self.ui.get_technical_wgt_side( widget_name )
            pt = self.mouse.get_relative_position() #get mouse position (x,y) that x,y are in [0,1] range
            self.thechnicals_backend[self.current_technical_side].update_pointer(pt) #update corespond backend mouse position
            self.refresh_thechnical(fp=5)
            self.show_pointer_position()
        
    def refresh_thechnical(self,fp):
        if self.t%fp==0:
            self.t=1

            self.thechnicals_backend[self.current_technical_side].update_sheet_img() #update technical image
            img = self.thechnicals_backend[self.current_technical_side].get_real_img() #get image of sheet corespond to mouse position
            self.ui.set_crop_image(img)#show image in UI
            self.update_sheet_img(self.current_technical_side)
            self.ui.show_selected_side(self.current_technical_side)

        else:
            self.t+=1
    
    
    #----------------------------------------------------------------------------------------
    # 
    #----------------------------------------------------------------------------------------   
    def fit_image(self, widget_name):
        self.thechnicals_backend[self.current_technical_side].fit(  self.mouse.get_relative_position()  )
        self.refresh_thechnical(1)
        real_img = self.thechnicals_backend[self.current_technical_side].get_real_img()
        self.ui.set_crop_image(real_img)
        self.ui.set_enabel(self.ui.add_btn_SI, True)
        self.show_pointer_position()


        
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def show_sheet_loader(self):
        sheets=self.db.report_last_sheets(10)
        self.ui.load_sheets_win.show_sheets_info(sheets)
        self.ui.data_loader_win_show()
    
    
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def append_select_img(self):
        cam, frame = self.thechnicals_backend[self.current_technical_side].get_current_img_position()
        # print(cam,frame, '^'*20)
        if (frame <0 )or (cam<0):
            self.ui.set_warning_data_page(texts.WARNINGS['NO_CHOOSEN_IMG'][self.language],'data_auquzation',level=2)
        else:

            side = self.thechnicals_backend[self.current_technical_side].get_side()
            main_path=self.sheet.get_path()
            self.selected_images_for_label.add( self.move_on_list.get_current('sheets_id'), self.current_technical_side, (cam,frame) ) 
            self.thechnicals_backend[self.current_technical_side].update_selected(
                                                                                        self.selected_images_for_label.get_sheet_side_selections( 
                                                                                            self.move_on_list.get_current('sheets_id'),
                                                                                            self.current_technical_side
                                                                                        )
                                                                                    )
            self.refresh_thechnical(fp=1)

            self.ui.add_selected_image(self.selected_images_for_label.get_all_selections_list())



    def remove_select_img(self):

        selected_img_for_remove=self.ui.get_selected_img()
        if len(selected_img_for_remove):
            self.selected_images_for_label.remove_by_index(selected_img_for_remove)
            self.ui.add_selected_image(self.selected_images_for_label.get_all_selections_list())
        else:
            self.ui.set_warning_data_page(texts.WARNINGS['NO_CHOOSEN_IMG'][self.language],'data_auquzation',level=2)


    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def save_temp_img_ds(self,):
        selected_imgs = self.selected_images_for_label.get_all_selections_list()
        selected_idxs = self.ui.get_selected_img()
        filtered_selected = Utils.get_selected_value( selected_imgs, selected_idxs )
        paths = self.db.get_path_sheet_image(filtered_selected)
        sheets = []
        self.ui.progressBar_SI.setMaximumWidth(150)
        for select_img in filtered_selected:
            sheets.append( self.db.load_sheet(select_img[0]) )
            self.ui.progressBar.setValue(100)
        self.ds.save_to_temp( paths , sheets)
        # print(filtered_selected)
        # self.create

        self.ui.progressBar_SI.setMaximumWidth(0)
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def label_selected_img(self):
        selected_imgs = self.selected_images_for_label.get_all_selections_list()
        selected_idxs = self.ui.get_selected_img()
        if len(selected_idxs) > 0:

            filtered_selected = Utils.get_selected_value( selected_imgs, selected_idxs )
            paths = self.db.get_path_sheet_image(filtered_selected)
            sheets = []
            for select_img in filtered_selected:
                sheets.append( self.db.load_sheet(select_img[0]) )
            
            self.move_on_list.add( list(zip(sheets, selected_imgs, paths)), 'selected_imgs_for_label')
            self.ui.show_label_page()
            self.load_image_to_label_page()
        
        else:
            self.ui.set_warning_data_page(texts.WARNINGS['NO_CHOOSEN_IMG'][self.language],'data_auquzation',level=2)

    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def refresh_label_img(self,img, fp=5):
        if self.t%fp==0:
            self.t=1
            self.ui.show_image_in_label(img)

        else:
            self.t+=1

    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def load_image_to_label_page(self):
        sheet, selected_img, img_path = self.move_on_list.get_current('selected_imgs_for_label')    
        img = Utils.read_image( img_path, 'color')
        self.ui.show_image_in_label(img)


    def next_label_img(self):
        self.move_on_list.next_on_list('selected_imgs_for_label')
        self.load_image_to_label_page()
    

    def prev_label_img(self):
        self.move_on_list.prev_on_list('selected_imgs_for_label')
        self.load_image_to_label_page()

    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def label_image_mouse(self, wgt_name):
        
        label_type=self.ui.get_label_type()
        mouse_status = self.mouse.get_status()
        mouse_button = self.mouse.get_button()
        mouse_pt = self.mouse.get_relative_position()

        sheet, selected_img, img_path = self.move_on_list.get_current('selected_imgs_for_label')    
        img = Utils.read_image( img_path, 'color')

        self.label_bakcend[label_type].mouse_event(mouse_status, mouse_button, mouse_pt )
        if self.label_bakcend[label_type].is_drawing_finish():
            self.label_bakcend[label_type].save('1')
        
        label_img = self.label_bakcend[label_type].draw()
        img = Utils.add_layer_to_img(img, label_img, opacity=0.4, compress=0.5 )
        self.ui.show_image_in_label( img )
            


        # if label_type == 'mask':
        #     self.mask_label_backend.mouse_event(mouse_status, mouse_button, mouse_pt )
        #     if self.mask_label_backend.is_drawing_finish():
        #         self.mask_label_backend.save_mask('1')
            
        #     mask = self.mask_label_backend.draw_mask()
        #     img = Utils.add_layer_to_img(img,mask,opacity=0.4, compress=0.5 )

        # if label_type == 'bbox':
        #     self.bbox_label_backend.mouse_event(mouse_status, mouse_button, mouse_pt )
        #     if self.bbox_label_backend.is_drawing_finish():
        #         self.bbox_label_backend.save_bbox('1')

        #     bbox = self.bbox_label_backend.draw_bboxs()
        #     img = Utils.add_layer_to_img(img,bbox,opacity=0.4, compress=0.5 )
        
        # self.ui.show_image_in_label( img )
        # if mouse_status == 'mouse_move':
        #     self.refresh_label_img(img, fp=3)
        # else:
        #     self.refresh_label_img(img, fp=1)
    
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    # def save_img(self,user='admin'):
    #     # listWidget = QListWidget()
    #     # print(self.ui.win.path)
    #     path=os.path.join(self.ui.win.path,'save_imgs')
    #     # print(path)
    #     # item = QListWidgetItem("Item %i" % i)
    #     user='admin'
    #     image = ImageQt.fromqpixmap(self.ui.crop_image.pixmap())
    #     # image=np.ascontiguousarray(image)

    #     # cv2.imshow('img',image)
    #     # cv2.waitKey(0)
    #     x =datetime.now()
    #     x=x.strftime("%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%S")
    #     x=str(x)+" "+str(user)
    #     image.save('{}/{}.jpg'.format(path,x))
    #     self.ui.listWidget_logs.addItem('Image Saved : '+'{}/{}.jpg'.format(path,x))

    def clear_list(self):
        self.ui.listWidget_logs.clear()
    
    # def append(self):
    #     image = ImageQt.fromqpixmap(self.ui.crop_image.pixmap())
    #     x =datetime.now()
    #     x=x.strftime("%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%S")
    #     # x=str(x)+" "+str(user)
    #     image.save('{}/{}.jpg'.format(self.cache_path,x))        
    #     self.ui.listWidget_logs.addItem('Image Append to cache storage : '+'{}/{}.jpg'.format(self.cache_path,x))


    
    # def add_remove_label(self):
    #     #print('add')
    #     #print(self.ui.add_label_text.text())
    #     add_remove_label.add_remove_label(self.ui.add_label_text.text())
    #     self.set_labels()
 

    def clear_cache_fun(self):
        dir = self.cache_path
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        self.ui.listWidget_logs.addItem('Cache Cleared')



    def show_current_pos(self,pt):
        if self.widget_name == 'down_side_technical':
            x,y=self.obj_sheet_down.get_pos()

            self.ui.current_pos_x.setText(str(int(x*280)))  # zarbar arz varagh ya arzesh pixel
            

            self.ui.current_pos_y.setText(str(round(y*self.lenght,2)))  # zarbar arz varagh ya arzesh pixel
        if self.widget_name == 'up_side_technical':
            x,y=self.obj_sheet_up.get_pos()

            self.ui.current_pos_x.setText(str(int(x*280)))  # zarbar arz varagh ya arzesh pixel
            

            self.ui.current_pos_y.setText(str(round(y*self.lenght,2)))  # zarbar arz varagh ya arzesh pixel



    def get_parent_path(self):

        self.db.report_last('default_setting','id',30)
        parent_path='G:/oxin_image_grabber'    #MUST CHANGED -----------------
        #print('asdqwdf')
        return parent_path

    
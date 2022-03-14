
from ast import Pass
# from logging import _Level
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

from Sheet_loader_win.data_loader_UI import data_loader

import database_utils
from utils import *
from utils.move_on_list import moveOnList

import texts              #eror and warnings texts


#MUST BE CHANGED
#MUST BE DELETE

EVENTS_TYPE={

    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release'
}



WIDTH_TECHNICAL_SIDE = 144 * 4
HEIGHT_FRAME_SIZE = 50



class API:

    def __init__(self,ui):
        self.ui = ui
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.move_on_list = moveOnList()

        self.db = database_utils.dataBaseUtils()
        #Label.bbox_lbl()

        #self.technical_backend = {'top': data_grabber()}
        self.thechnicals_backend = {}
        #self.ui.crop_image.mouseDoubleClickEvent = self.fit_image
        self.t = 0
        self.current_technical_widget = ''
        self.selected_images_for_label = {}

        self.language='en' 


        #-------------------------------------
        #connet buttons to correspondings functions in API               ////////////////////
        self.button_connector()
        #connet mouse event to correspondings functions in API
        self.mouse_connector()
        #connet keyboard event to correspondings functions in API
        self.keyboard_connector()
        #-------------------------------------

        #technical view btns                                             ///////////////////
        self.ui.save_btn.clicked.connect(self.save_img)
        self.ui.clear_all_btn.clicked.connect(self.clear_list)
        self.cache_path='G:/oxin_image_grabber/cache'
        #self.ui.append_btn.clicked.connect(self.append)
        self.ui.clear_cache.clicked.connect(self.clear_cache_fun)


        
        

    
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def button_connector(self):
        self.ui.load_sheets_win.load_btn.clicked.connect(partial(self.load_sheets))
        self.ui.append_btn.clicked.connect(partial(self.append_select_img))
        self.ui.load_coil_btn.clicked.connect(partial(self.show_sheet_loader))
        self.ui.next_coil_btn.clicked.connect(partial(self.next_sheet))
        self.ui.prev_coil_btn.clicked.connect(partial(self.prev_sheet))

    def mouse_connector(self):
        for _,technical_widget in self.ui.get_technical().items():
            self.mouse.connet( technical_widget, self.update_technical_pointer_mouse )

        self.mouse.connet_dbclick( self.ui.crop_image, self.fit_image)


    def keyboard_connector(self):
        self.keyboard.connet( self.ui, ['left','right','up','down'], [self.update_technical_pointer_keyboard], 'Technical View' )
        #self.keyboard.connet( self.ui, ['left','right','up','down'], [self.test], None )



        
    #----------------------------------------------------------------------------------------
    #get id of sheets that user select in load_sheet_win and load first one
    #---------------------------------------------------------------------------------------- 
    def load_sheets(self): 
        sheets_id = self.ui.load_sheets_win.get_selected_sheetid()
        self.move_on_list.add(sheets_id, 'sheets_id')
        self.ui.load_sheets_win.close()
        for id in sheets_id:
            self.selected_images_for_label[id] = {'pos':[]}
        
        self.load_sheet()
        #selceted_sheets_id = self.move_on_list.get_current('sheets_id')#get current value on list that corespond to "coils_id" name 
        #self.sheet = self.db.load_sheet( selceted_sheets_id )
        #self.load_sheet( self.sheet  ) #build technical sheet 
        x=0
        
    
    #----------------------------------------------------------------------------------------
    #load sheet by its id in software
    #---------------------------------------------------------------------------------------- 
    def load_sheet(self): 
        #print('%'*100)
        selceted_sheets_id = self.move_on_list.get_current('sheets_id')#get current value on list that corespond to "coils_id" name 
        self.sheet = self.db.load_sheet( selceted_sheets_id )#load inference of Sheet class from database by sheet id
        self.build_sheet_technical( self.sheet  ) #build technical sheet 
        

        

        self.ui.show_sheet_details(self.sheet.get_info_dict())   # show sheet details in UI.details_label

        # return self.sheet
         
        # path=2
        # path=self.db.get_sheet_path(path)                #MUST BE CHANGED
        # self.load_sheet(path)
        # self.ui.details_label.setText(str(self.ui.win.details))
    #----------------------------------------------------------------------------------------
    #when next next_coil_btn clicked this function move on next coil id and load it
    #----------------------------------------------------------------------------------------
    def next_sheet(self):
        self.move_on_list.next_on_list('sheets_id')#move previous on list that corespond to "coils_id" name
        self.load_sheet()# laod current coil id 
        

    #----------------------------------------------------------------------------------------
    #when next next_coil_btn clicked this function move on privous coil id and load it
    #----------------------------------------------------------------------------------------
    def prev_sheet(self):
        self.move_on_list.prev_on_list('sheets_id')#move next on list that corespond to "coils_id" name
        self.load_sheet()# laod current coil id 
    #----------------------------------------------------------------------------------------
    #
    #---------------------------------------------------------------------------------------- 
    def build_sheet_technical(self,sheet):
        #try:
            self.thechnicals_backend = {}
            for side,technical_widget in self.ui.get_technical(name=False).items():
                #print(side, technical_widget.objectName())
                self.thechnicals_backend[technical_widget.objectName()] = data_grabber.sheetOverView(sheet.get_path(), #main path of coil images that contain to folder for top and bottom images
                                                                                                     side, #side of sheet that is UO
                                                                                                     (HEIGHT_FRAME_SIZE*sheet.get_nframe(),WIDTH_TECHNICAL_SIDE),
                                                                                                     sheet.get_grade_shape(),
                                                                                                     actives_camera=sheet.get_cameras(),
                                                                                                    oriation=data_grabber.VERTICAL)
                

                self.current_technical_widget = technical_widget.objectName()
                self.refresh_thechnical(fp=1) #load technical image and real images
            #MUST BE CHANGED
            #self.ui.show_coil_loaded(self.load_coil_win.id)
            
        #except:
        #    print('Error!: load_sheet() in API')

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
        x,y = self.thechnicals_backend[ self.current_technical_widget ].get_pos()#get mouse position normilized between [0,1]
        x*=self.sheet.get_width()
        y*=self.sheet.get_lenght()
        y = np.round(y,1)
        x = np.round(x,1)
        self.ui.show_current_position((x,y))



    def update_technical_pointer_keyboard(self,key):
        self.thechnicals_backend[ self.current_technical_widget ].update_pointer_keyboard(key)    
        self.refresh_thechnical(fp=1)
        self.show_pointer_position()

    def update_technical_pointer_mouse(self,widget_name):
        if len( self.thechnicals_backend ) == 0:
            self.ui.set_warning_data_page(texts.WARNINGS['NO_SHEET'][self.language],'data_auquzation',level=2)
        
        else:
            self.current_technical_widget = widget_name
            pt = self.mouse.get_relative_position() #get mouse position (x,y) that x,y are in [0,1] range
            self.thechnicals_backend[widget_name].update_pointer(pt) #update corespond backend mouse position
            self.refresh_thechnical(fp=5)
            self.show_pointer_position()
        
    def refresh_thechnical(self,fp):
        if self.t%fp==0:
            self.t=1

            self.thechnicals_backend[self.current_technical_widget].update_sheet_img() #update technical image
            img = self.thechnicals_backend[self.current_technical_widget].get_real_img() #get image of sheet corespond to mouse position
            self.ui.set_crop_image(img)#show image in UI
            self.update_sheet_img(self.current_technical_widget)
            self.ui.show_selected_side(self.current_technical_widget)

        else:
            self.t+=1
    
    
    #----------------------------------------------------------------------------------------
    # 
    #----------------------------------------------------------------------------------------   
    def fit_image(self, widget_name):
        self.thechnicals_backend[self.current_technical_widget].fit(  self.mouse.get_relative_position()  )
        self.refresh_thechnical(1)
        real_img = self.thechnicals_backend[self.current_technical_widget].get_real_img()
        self.ui.set_crop_image(real_img)
        self.ui.set_enabel(self.ui.append_btn, True)
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
        cam, frame = self.thechnicals_backend[self.current_technical_widget].get_current_img()
        # print(cam,frame, '^'*20)
        if (frame <0 )or (cam<0):
            self.ui.set_warning_data_page(texts.WARNINGS['FIT'][self.language],'data_auquzation',level=2)
        else:

            side = self.thechnicals_backend[self.current_technical_widget].get_side()
            main_path=self.sheet.get_path()
            self.selected_images_for_label[ self.move_on_list.get_current('sheets_id') ]['pos'].append([cam,frame]) 
            self.thechnicals_backend[self.current_technical_widget].update_selected(
                                                                                        self.selected_images_for_label[ self.move_on_list.get_current('sheets_id') ]['pos']
                                                                                    )
            self.refresh_thechnical(fp=1)
                                                                                
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 


    def save_img(self,user='admin'):
        # listWidget = QListWidget()
        # print(self.ui.win.path)
        path=os.path.join(self.ui.win.path,'save_imgs')
        # print(path)
        # item = QListWidgetItem("Item %i" % i)
        user='admin'
        image = ImageQt.fromqpixmap(self.ui.crop_image.pixmap())
        # image=np.ascontiguousarray(image)

        # cv2.imshow('img',image)
        # cv2.waitKey(0)
        x =datetime.now()
        x=x.strftime("%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%S")
        x=str(x)+" "+str(user)
        image.save('{}/{}.jpg'.format(path,x))
        self.ui.listWidget_logs.addItem('Image Saved : '+'{}/{}.jpg'.format(path,x))

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

    
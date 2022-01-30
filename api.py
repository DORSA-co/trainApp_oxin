
from PySide6.QtCore import *
from backend import data_grabber
from backend.mouse import mouse
import cv2
import threading
import time
from PIL import ImageQt
import numpy as np
import os
from datetime import date, time, datetime
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtGui import QPixmap,QImage
from backend import add_remove_label
from PyQt5 import QtCore
from trainApp_loader import get_data
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
        self.mouse = mouse()
        self.db = get_data.database()
        self.ui.up_side_technical.keyPressEvent = self.on_key


        #self.technical_backend = {'top': data_grabber()}
        self.thechnicals_backend = {}
        #self.ui.crop_image.mouseDoubleClickEvent = self.fit_image
        self.t = 0
        self.current_technical_widget = ''
        #self.load_data() #MUST BE DELETE
        #-------------------------------------
        #connet buttons to correspondings functions in API               ////////////////////
        self.button_connector()
        #connet mouse event to correspondings functions in API
        self.mouse_connector()
        #-------------------------------------

        #technical view btns                                             ///////////////////
        self.ui.save_btn.clicked.connect(self.save_img)
        self.ui.clear_all_btn.clicked.connect(self.clear_list)
        self.cache_path='G:/oxin_image_grabber/cache'
        self.ui.append_btn.clicked.connect(self.append)
        self.ui.clear_cache.clicked.connect(self.clear_cache_fun)
    

    def on_key(self,e):
        print('sssssssss')
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def button_connector(self):
        self.ui.win.load_btn.clicked.connect(self.load_data)


    def mouse_connector(self):
        for _,technical_widget in self.ui.get_technical().items():
            self.mouse.connet( technical_widget, self.thechnical )

        self.mouse.connet_dbclick( self.ui.crop_image, self.fit_image)
    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def load_data(self):
        path=self.db.get_sheet_path(2)                #MUST BE CHANGED
        self.load_sheet(path)
        self.ui.details_label.setText(str(self.ui.win.details))
    

    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def load_sheet(self,path,nframe=20):
        try:
            self.thechnicals_backend = {}
            for side,technical_widget in self.ui.get_technical(name=False).items():
                self.thechnicals_backend[technical_widget.objectName()] = data_grabber.sheetOverView(path,
                                                                                                     side,
                                                                                                     (HEIGHT_FRAME_SIZE*nframe,WIDTH_TECHNICAL_SIDE),
                                                                                                     (nframe,12),
                                                                                                     actives_camera=(0,12),
                                                                                                     oriation=data_grabber.VERTICAL)

            self.update_sheet_img()
            #MUST BE CHANGED
            self.ui.show_coil_loaded(self.win.id)
        except:
            print('Error!: load_sheet() in API')

    #----------------------------------------------------------------------------------------
    # 
    #---------------------------------------------------------------------------------------- 
    def update_sheet_img(self, name):
        img=self.thechnicals_backend[name].get_sheet_img()
        self.ui.set_img_sheet(img, name)
    #----------------------------------------------------------------------------------------
    # 
    #----------------------------------------------------------------------------------------     
    def thechnical(self, widget_name):
        self.current_technical_widget = widget_name
        self.ui.set_enabel(self.ui.append_btn, False)

        if self.t%5==0:
            self.t=1

            pt = self.mouse.get_relative_position() #get mouse position (x,y) that x,y are in [0,1] range
            self.thechnicals_backend[widget_name].update_pointer(pt) #update corespond backend mouse position
            self.thechnicals_backend[widget_name].update_sheet_img() #update technical image
            img = self.thechnicals_backend[widget_name].get_real_img() #get image of sheet corespond to mouse position
            self.ui.set_crop_image(img)#show image in UI
            self.update_sheet_img(widget_name)
            self.ui.show_selected_side(widget_name)

        else:
            self.t+=1
    
   
    #----------------------------------------------------------------------------------------
    # 
    #----------------------------------------------------------------------------------------   
    def fit_image(self, widget_name):
        self.thechnicals_backend[self.current_technical_widget].fit(  self.mouse.get_relative_position()  )
        real_img = self.thechnicals_backend[self.current_technical_widget].get_real_img()
        self.ui.set_crop_image(real_img)
        self.ui.set_enabel(self.ui.append_btn, True)
        
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
    
    def append(self):
        image = ImageQt.fromqpixmap(self.ui.crop_image.pixmap())
        x =datetime.now()
        x=x.strftime("%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%S")
        # x=str(x)+" "+str(user)
        image.save('{}/{}.jpg'.format(self.cache_path,x))        
        self.ui.listWidget_logs.addItem('Image Append to cache storage : '+'{}/{}.jpg'.format(self.cache_path,x))

    def next_coil(self):
        self.ui.win.next_coil()
        self.load_data()

    def prev_coil(self):
        self.ui.win.prev_coil()
        self.load_data()
    
    def add_remove_label(self):
        print('add')
        print(self.ui.add_label_text.text())
        add_remove_label.add_remove_label(self.ui.add_label_text.text())
        self.set_labels()
 

    def clear_cache_fun(self):
        dir = self.cache_path
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        self.ui.listWidget_logs.addItem('Cache Cleared')

    def change_with_key(self,arrow):
        if arrow=='right':
            self.x=self.x+0.02
        elif arrow=='left':
            self.x=self.x-0.02
        elif arrow=='up':
            self.y=self.y-0.01
        elif arrow=='down':
            self.y=self.y+0.01
        elif arrow=='right_up':
            self.x=self.x+0.02
            self.y=self.y-0.01
        elif arrow=='right_down':
            self.x=self.x+0.02
            self.y=self.y+0.01
        elif arrow=='left_up':
            self.x=self.x-0.02
            self.y=self.y-0.01
        elif arrow=='left_down':
            self.x=self.x-0.02
            self.y=self.y+0.01
        if self.widget_name == 'down_side_technical':
            self.update_sheet_real_img('down',(self.x,self.y))
        elif self.widget_name == 'up_side_technical':
            self.update_sheet_real_img('up',(self.x,self.y))


    def show_current_pos(self,pt):
        if self.widget_name == 'down_side_technical':
            x,y=self.obj_sheet_down.get_pos()

            self.ui.current_pos_x.setText(str(int(x*280)))  # zarbar arz varagh ya arzesh pixel
            

            self.ui.current_pos_y.setText(str(round(y*self.lenght,2)))  # zarbar arz varagh ya arzesh pixel
        if self.widget_name == 'up_side_technical':
            x,y=self.obj_sheet_up.get_pos()

            self.ui.current_pos_x.setText(str(int(x*280)))  # zarbar arz varagh ya arzesh pixel
            

            self.ui.current_pos_y.setText(str(round(y*self.lenght,2)))  # zarbar arz varagh ya arzesh pixel

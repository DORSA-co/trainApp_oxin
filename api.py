
from PySide6.QtCore import *
from backend import data_grabber
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


EVENTS_TYPE={

    QEvent.Type.MouseMove : 'mouse_move',
    QEvent.Type.MouseButtonPress : 'mouse_press',
    QEvent.Type.MouseButtonRelease : 'mouse_release'
}


class API:

    def __init__(self,ui):
        self.ui = ui
        
        #mouse up-down////////////////////

        self.ui.down_side_technical.mouseMoveEvent = self.mouseevent(self.ui.down_side_technical)
        self.ui.down_side_technical.mouseReleaseEvent = self.mouseevent(self.ui.down_side_technical)

        self.ui.up_side_technical.mouseMoveEvent = self.mouseevent(self.ui.up_side_technical)
        self.ui.up_side_technical.mouseReleaseEvent = self.mouseevent(self.ui.up_side_technical)
        
        
        
        self.ui.crop_image.mouseDoubleClickEvent = self.fit_image

        
        self.t = 0
        #-------------------------------------

        #data loader////////////////////
        # self.ui.win.load_btn.clicked.connect(self.load_path)
        #-------------------------------------

        #technical view btns//////////////
        self.ui.save_btn.clicked.connect(self.save_img)
        self.ui.clear_all_btn.clicked.connect(self.clear_list)
        self.cache_path='G:/oxin_image_grabber/cache'
        self.ui.append_btn.clicked.connect(self.append)
        self.ui.clear_cache.clicked.connect(self.clear_cache_fun)



        self.set_labels()

        

     
            # self.deleteLater()
        # elif e.key() == QtCore.Qt.Key_Enter:
        #     self.proceed()
        # e.accept()
       


        self.load_sheet('G:\oxin_image_grabber/1',20)
        self.x=0
        self.y=0
        self.lenght=50
    
    def mouseevent(self,widget):
        # print('yes')
        def func(e):
            # print('yes')
            x = e.x() / widget.width()
            y = e.y() / widget.height()
            x = min(max(x,0),1)
            y = min(max(y,0),1)
            self.x=x
            self.y=y
            self.status = EVENTS_TYPE[e.type()]
            self.widget_name = widget.objectName()
            # print(self.x,self.y,self.widget_name,self.status)


            # if self.widget_name=="down_side_technical" and self.status=="mouse_move":
            #     if time.time() - self.t >0.15:
            #         self.t = time.time()
            #         self.update_sheet_real_img('down',(self.x,self.y))
            #print(self.t)

            # if self.status=="mouse_move":



            if self.widget_name=="down_side_technical" and self.status=="mouse_move":
                if self.t%5==0:
                    self.t=1
                    self.update_sheet_real_img('down',(self.x,self.y))
                    self.ui.up_side_technical.setDisabled(True)
                    # self.cursur_show(e)
                    self.ui.show_side.setText(str(self.widget_name))

                else:
                    self.t+=1


            if self.widget_name=="up_side_technical" and self.status=="mouse_move":
                if self.t%5==0:
                    self.t=1
                    self.update_sheet_real_img('up',(self.x,self.y))
                    self.ui.down_side_technical.setDisabled(True)
                    # self.cursur_show(e)
                    self.ui.show_side.setText(str(self.widget_name))

                else:
                    self.t+=1
            if self.status=="mouse_release":
                
                self.ui.down_side_technical.setDisabled(False)
                self.ui.up_side_technical.setDisabled(False)


        return func

    def fit_image(self,event):
        print('yes',event.x(),event.y())
        x = event.x() / self.ui.crop_image.width()
        y = event.y() / self.ui.crop_image.height()
        self.show_current_pos((x,y))
        x = min(max(x,0),1)
        y = min(max(y,0),1)

        if self.widget_name == 'down_side_technical':
            self.obj_sheet_down.fit((x,y))
            real_img = self.obj_sheet_down.get_real_img()
            self.ui.set_crop_image(real_img)
            # print(self.obj_sheet_down.is_fit)
            # print('pt', self.obj_sheet_down.pt)
            # self.show_current_pos((x,y))

        if self.widget_name == 'up_side_technical':
            self.obj_sheet_up.fit((x,y))
            real_img = self.obj_sheet_up.get_real_img()
            self.ui.set_crop_image(real_img)
            # self.show_current_pos(self.obj_sheet_up.pt)
            # print(self.obj_sheet_up.is_fit)
        if (self.obj_sheet_down.is_fit and  self.widget_name == 'down_side_technical') or (self.obj_sheet_up.is_fit and self.widget_name == 'up_side_technical'):
            self.ui.append_btn.setDisabled(False)
        else:
            self.ui.append_btn.setDisabled(True)              
        
        self.update_sheet_img()
        
        
        




    def update_sheet_real_img(self,side,pt):

        self.ui.append_btn.setDisabled(True) 
        self.show_current_pos(pt)
        if side=="down":
            self.obj_sheet_down.update_pointer(pt)
            real_img = self.obj_sheet_down.get_real_img()
            self.update_sheet_img()
            self.ui.set_crop_image(real_img)
            
            # print(self.obj_sheet_down.is_fit)
            # self.ui.up_side_technical.setDisabled(True)

            # cv2.waitKey(5)
        if side=="up":
            self.obj_sheet_up.update_pointer(pt)
            real_img = self.obj_sheet_up.get_real_img()
            self.update_sheet_img()
            self.ui.set_crop_image(real_img)
            
            # print(self.obj_sheet_up.is_fit)
            # self.ui.down_side_technical.setDisabled(True)
            # print(self.ui.crop_image.width(),self.ui.crop_image.height())
            # cv2.waitKey(5)



    def load_sheet(self,path,lenght=20):

        try:
            lenght=self.ui.win.lenght
            lenght=int(float(lenght))+1
            self.lenght=lenght
        except:
            print('no_len')
        try:
            # print("*"*100,lenght)
        # 'G:\oxin_image_grabber/001'
            self.obj_sheet_up=data_grabber.sheetOverView(path,
                                                    data_grabber.UP,(50*lenght,576),(lenght,12),actives_camera=(0,12),
                                                    oriation=data_grabber.VERTICAL)

            self.obj_sheet_down=data_grabber.sheetOverView(path,
                                                    data_grabber.DOWN,(50*lenght,576),(lenght,12),actives_camera=(0,12),
                                                    oriation=data_grabber.VERTICAL)

            self.obj_sheet_down.update_line(int(lenght))
            self.obj_sheet_up.update_line(int(lenght))
            self.update_sheet_img()
            self.ui.listWidget_logs.addItem('Coil {} Selected'.format(self.ui.win.id))
        except:
            print('eror')
            # self.ui.listWidget_logs_2.addItem('Cant load coil')

        


    def update_sheet_img(self):
        #threading.Timer(0.1, self.update_sheet_img).start()
        img=self.obj_sheet_down.get_sheet_img()
        self.ui.set_img_sheet(img,"down")
        img=self.obj_sheet_up.get_sheet_img()
        self.ui.set_img_sheet(img,"up")
        


    def sheet_top_img():
        pass

    def cursur_show(self,e):
        
        self.ui.cursor_status.setText(str(e.x()))

    
    def save_img(self,user='admin'):
        # listWidget = QListWidget()
        # print(self.ui.win.path)
        path=os.path.join(self.ui.win.path,'save_imgs')
        # print(path)
        # item = QListWidgetItem("Item %i" % i)
        user='admin'
        image = ImageQt.fromqpixmap(self.ui.crop_image.pixmap())
        # image=np.ascontiguousarray(image)
        x =datetime.now()
        x=x.strftime("%Y"+"-"+"%m"+"-"+"%d"+"-"+"%H"+"-"+"%M"+"-"+"%S")
        x=str(x)+" "+str(user)
        image.save('{}/{}.jpg'.format(path,x))
        self.ui.listWidget_logs.addItem('Image Saved : '+'{}/{}.jpg'.format(path,x))
        # cv2.imshow('img',image)
        # cv2.waitKey(0)

    def load_path(self):
        path=self.ui.win.path

        # print('path',path)
        self.load_sheet(path)
        self.ui.details_label.setText(str(self.ui.win.details))
    
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
        self.load_path()

    def prev_coil(self):
        self.ui.win.prev_coil()
        self.load_path()
    
    def add_remove_label(self):
        print('add')
        print(self.ui.add_label_text.text())
        add_remove_label.add_remove_label(self.ui.add_label_text.text())
        self.set_labels()
    
    def set_labels(self):
        labels=add_remove_label.catch_labels()

        self.ui.comboBox_labels.clear()      
        self.ui.comboBox_labels.addItems(labels)       


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

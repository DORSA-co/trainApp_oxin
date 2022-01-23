
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
        self.t = 0
        #-------------------------------------

        #data loader////////////////////
        self.ui.win.load_btn.clicked.connect(self.load_path)
        #-------------------------------------

        #technical view btns//////////////
        self.ui.save_btn.clicked.connect(self.save_img)
        self.ui.clear_all_btn.clicked.connect(self.clear_list)
        self.cache_path='G:/oxin_image_grabber/cache'
        self.ui.append_btn.clicked.connect(self.append)
        self.ui.clear_cache.clicked.connect(self.clear_cache_fun)







        # self.load_sheet('G:\oxin_image_grabber/1')
    
    def mouseevent(self,widget):

        def func(e):
            
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
                    # self.cursur_show(e)

                else:
                    self.t+=1


            if self.widget_name=="up_side_technical" and self.status=="mouse_move":
                if self.t%5==0:
                    self.t=1
                    self.update_sheet_real_img('up',(self.x,self.y))
                    # self.cursur_show(e)

                else:
                    self.t+=1


        return func


    def update_sheet_real_img(self,side,pt):
        if side=="down":
            self.obj_sheet_down.update_pointer(pt)
            real_img = self.obj_sheet_down.get_real_img()
            self.update_sheet_img()
            self.ui.set_crop_image(real_img)
            cv2.waitKey(5)
        if side=="up":
            self.obj_sheet_up.update_pointer(pt)
            real_img = self.obj_sheet_up.get_real_img()
            self.update_sheet_img()
            self.ui.set_crop_image(real_img)
            cv2.waitKey(5)



    def load_sheet(self,path):

        try:
            lenght=self.ui.win.lenght
            lenght=int(float(lenght))+1
            print("*"*100,lenght)
        # 'G:\oxin_image_grabber/001'
            self.obj_sheet_up=data_grabber.sheetOverView(path,
                                                    data_grabber.UP,(50*lenght,280),(lenght,12),actives_camera=(0,12),
                                                    oriation=data_grabber.VERTICAL)

            self.obj_sheet_down=data_grabber.sheetOverView(path,
                                                    data_grabber.DOWN,(50*lenght,280),(lenght,12),actives_camera=(0,12),
                                                    oriation=data_grabber.VERTICAL)

            self.obj_sheet_down.update_line(int(lenght))
            self.obj_sheet_up.update_line(int(lenght))
            self.update_sheet_img()
            self.ui.listWidget_logs.addItem('Coil {} Selected'.format(self.ui.win.id))
        except:
            self.ui.listWidget_logs.addItem('Cant load coil')

        


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
        print(self.ui.win.path)
        path=os.path.join(self.ui.win.path,'save_imgs')
        print(path)
        # item = QListWidgetItem("Item %i" % i)
        user='admin'
        image = ImageQt.fromqpixmap(self.ui.crop_image_up.pixmap())
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

        print('path',path)
        self.load_sheet(path)
        self.ui.details_label.setText(str(self.ui.win.details))
    
    def clear_list(self):
        self.ui.listWidget_logs.clear()
    
    def append(self):
        image = ImageQt.fromqpixmap(self.ui.crop_image_up.pixmap())
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

    # def label(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.page_label)
    #     # image = ImageQt.fromqpixmap(self.ui.crop_image_up.pixmap())
    #     # image=np.ascontiguousarray(image)
    #     # image = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
    #     # self.ui.image.setPixmap(QPixmap.fromImage(image))
    #     image = ImageQt.fromqpixmap(self.ui.crop_image_up.pixmap())
    #     image=np.ascontiguousarray(image)
    #     # self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)
    #     # self.fs_cam_name.setText(self.dataset_cam_4_name.text())
    #     # self.fs_pause_sign.setText('')
    #     self.fs = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
        
    #     self.ui.image.setPixmap(QPixmap.fromImage(self.fs)) 
    def clear_cache_fun(self):
        dir = self.cache_path
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        self.ui.listWidget_logs.addItem('Cache Cleared')

 
from ast import Return
import datetime
import os
from backend import pathStructure
class Sheet:
    def __init__(self,
                id = None,
                sheet_id=None,
                main_path=None,
                image_format=None,
                heat_number=None,
                ps_number=None,
                pdl_number=None,
                width=None,
                lenght=None,
                thickness=None,
                date=None,
                time=None,
                user=None,
                nframe=None,
                cameras=[],
                ):

        self.id = id
        self.sheet_id = sheet_id
        self.main_path = main_path
        self.image_format = image_format
        self.heat_number = heat_number
        self.ps_number = ps_number #product scechule number
        self.pdl_number = pdl_number #product d??? number
        self.width = width
        self.lenght = lenght
        self.thickness = thickness
        self.date = date
        self.time = time
        self.user = user
        self.nframe = nframe
        self.cameras = cameras

    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    def set_id(self,sheet_id):
        self.sheet_id = sheet_id

    def set_heatnumber(self, heat_num):
        self.heat_number = heat_num

    def set_pdlnumber(self,num):
        self.pdl_number = num
    
    def set_psnumber(self, num):
        self.ps_number = num

    def set_width(self, w):
        self.width = w

    def set_lenght(self, l):
        self.lenght = l

    def set_thickness(self, t):
        self.thickness = t

    def set_dimentions(self, w, l, t):
        self.width = w
        self.lenght = l
        self.thickness = t

    def set_date(self,y,m,d):
        self.date = datetime.datetime(y,m,d)

    def set_time(self,h,min):
        self.time = datetime.time( h, min)
        
    def set_user(self, name):
        self.user = name

    def set_path(self,path):
        self.main_path = path

    def set_nframe(self, n):
        self.nframe = n

    def set_cameras(self, start , end):
        self.cameras = [start, end]
    
    def set_image_format(self,fromat):
        if '.' in fromat:
            self.image_format = fromat
        else:
            self.image_format = '.' + fromat
    
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    def get_id(self):
        return self.sheet_id

    def get_heatnumber(self):
        return self.heat_number

    def get_pdlnumber(self):
        return self.pdl_number
    
    def get_psnumber(self):
        return self.ps_number

    def get_width(self):
        return self.width

    def get_lenght(self):
        return self.lenght

    def get_thickness(self):
        return self.thickness

    def get_dimentions(self):
        return self.width, self.lenght, self.thickness

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time
        
    def get_user(self):
        return self.user

    def get_path(self):
        return pathStructure.sheet_path(self.main_path,self.sheet_id)

    def get_main_path(self):
        return self.main_path

    def get_nframe(self):
        return self.nframe

    def get_cameras(self):
        return self.cameras

    def get_grade_shape(self):
        nf = self.nframe
        nc = self.cameras[1] - self.cameras[0] + 1
        return nf,nc

    def get_image_format(self):
        return self.image_format


    
    def get_info_dict(self):
        return {
            'sheet_id':self.sheet_id,
            'heat_number': self.heat_number,
            'lenght': self.lenght,
            'width' : self.width
            #'order number': self.order_numb
        }
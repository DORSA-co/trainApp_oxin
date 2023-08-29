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
                order_id=None,
                heat_id=None,
                qc_standard=None,
                width=None,
                length=None,
                thickness=None,
                width_order=None,
                length_order=None,
                thickness_order=None,
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
        self.order_id = order_id
        self.heat_id = heat_id
        self.qc_standard = qc_standard 
        self.width = width
        self.length = length
        self.thickness = thickness
        self.width_order = width_order
        self.length_order = length_order
        self.thickness_order = thickness_order
        self.date = date
        self.time = time
        self.user = user
        self.nframe = nframe
        self.cameras = cameras

    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    def set_id(self,sheet_id):
        self.sheet_id = sheet_id

    def set_orderid(self, order_id):
        self.order_id = order_id

    def set_heatid(self, heat_id):
        self.heat_id = heat_id

    def set_qcstandard(self, qc_standard):
        self.qc_standard = qc_standard

    def set_width(self, w):
        self.width = w

    def set_length(self, l):
        self.length = l

    def set_thickness(self, t):
        self.thickness = t

    def set_widthorder(self, w_order):
        self.width_order = w_order

    def set_lengthorder(self, l_order):
        self.length_order = l_order

    def set_thicknessorder(self, t_order):
        self.thickness_order = t_order

    def set_dimentions(self, w, l, t):
        self.width = w
        self.length = l
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
    
    def get_orderid(self):
        return self.order_id

    def get_heatid(self):
        return self.heat_id

    def get_qcstandard(self):
        return self.qc_standard

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_thickness(self):
        return self.thickness

    def get_widthorder(self):
        return self.width_order

    def get_lengthorder(self):
        return self.length_order

    def get_thicknessorder(self):
        return self.thickness_order

    def get_dimentions(self):
        return self.width, self.length, self.thickness

    def get_date_string(self):
        return str(self.date.strftime('%Y/%m/%d'))

    def get_time(self):
        return self.time

    def get_time_string(self):
        return str(self.time.strftime('%H:%M'))
        
    def get_user(self):
        return self.user

    def get_path(self):
        return pathStructure.sheet_path(self.main_path,self.sheet_id)

    def get_main_path(self):
        return self.main_path

    def get_nframe(self):
        return int(self.nframe)

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
            'PLATE_ID':self.sheet_id,
            'date': self.get_date_string(),
            'time': self.get_time_string(),
            'ORDER_ID': self.order_id,
            'HEAT_ID': self.heat_id,
            'QC_STANDARD': self.qc_standard,
            'LENGHT': self.length,
            'WIDTH' : self.width,
            'THICKNESS': self.thickness,
            'LENGHT_ORDER': self.length_order,
            'WIDTH_ORDER' : self.width_order,
            'THICKNESS_ORDER': self.thickness_order,
        }

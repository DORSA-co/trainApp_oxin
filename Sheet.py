from ast import Return
import datetime
import os

class Sheet:
    def __init__(self,
                id=None,
                main_path=None,
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
        self.path = main_path
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
    def set_id(self,id):
        self.id = id

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
        self.path = path

    def set_nframe(self, n):
        self.nframe = n

    def set_cameras(self, start , end):
        self.cameras = [start, end]
    
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    def get_id(self):
        return self.id

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
        return os.path.join( self.path ,str( self.id ))

    def get_main_path(self):
        return self.path

    def get_nframe(self):
        return self.nframe

    def get_cameras(self):
        return self.cameras

    def get_grade_shape(self):
        nf = self.nframe
        nc = self.cameras[1] - self.cameras[0] + 1
        return nf,nc

    
    def get_info_dict(self):
        return {
            'id':self.id,
            'heat_number': self.heat_number,
            'lenght': self.lenght,
            'width' : self.width
            #'order number': self.order_numb
        }
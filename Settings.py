import datetime

class cameraSetting:
    def __init__(self,
                gain_top=None,
                gain_bottom=None,
                expo_top=None,
                expo_buttom=None,
                width=None,
                height=None,
                offset_x=None,
                offset_y=None,
                interpacket_delay=None,
                packet_size=None,
                ):


        self.gain_top = gain_top
        self.path = main_path
        self.heat_id = heat_id
        self.ps_number = ps_number #product scechule number
        self.pdl_number = pdl_number #product d??? number
        self.width = width
        self.length = length
        self.thickness = thickness
        self.date = date
        self.time = time
        self.user = user

    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    def set_id(self,id):
        self.id = id

    def set_heatnumber(self, heat_num):
        self.heat_id = heat_num

    def set_pdlnumber(self,num):
        self.pdl_number = num
    
    def set_psnumber(self, num):
        self.ps_number = num

    def set_width(self, w):
        self.width = w

    def set_length(self, l):
        self.length = l

    def set_thickness(self, t):
        self.thickness = t

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
        self.path = path
    
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    def get_id(self):
        return self.id

    def get_heatnumber(self):
        return self.heat_id

    def get_pdlnumber(self):
        return self.pdl_number
    
    def get_psnumber(self):
        return self.ps_number

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_thickness(self):
        return self.thickness

    def get_dimentions(self):
        return self.width, self.length, self.thickness

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time
        
    def get_user(self):
        return self.user

    def get_path(self):
        return self.path

import numpy as np
import random
import string
import re
import socket
try:
    import date_funcs
except:
    from backend import date_funcs

RANDOM=True

class connection_level2():

    def __init__(self, db_obj):
        # self.ui_obj=ui_obj
        # self.sheet_id = 900
        self.db_obj = db_obj
        self.data = None
        self.max_cameras = 12
        self.max_width = 5000
        self.max_projectors = 6

        self.dummy_dict = {'PLATE_ID': 'ABC12345A', 'ORDER_ID': '123456789', 'HEAT_ID': '123456', 'QC_STANDARD': 'ASTM450', 'LENGHT': '6040', 'WIDTH': '2020', 'THICKNESS': '25.23', 'LENGHT_ORDER': '6000', 'WIDTH_ORDER': '2000', 'THICKNESS_ORDER': '25', 'speed': '1500'}

    def ret_sheet_details(self):
        ret,details=self.connect()
        return ret,details
    
    def calculate_camera_and_projector(self):

        #calculate number of camera and projector
        ret, details=self.ret_sheet_details() 
        if ret:
            # cameras=round(details['width']/250)     # this should be change 
            # projector =int(details['width'] /14)
            cameras=np.random.choice([4, 6, 8, 10, 12])
            cameras=12
            projector=6
            # speed = np.random.choice([-1, 0, 1], p=[0.1, 0.1, 0.8])
            speed = 1
            return cameras, projector ,speed, details
 
        else:
            return 0, 0, None

    def get_number_camera_projector(self):
        cameras,projectors,_=self.calculate_camera_and_projector()
        return cameras,projectors

    def get_full_info(self):
        if self.data:
            cameras = int(np.ceil(float(self.data['WIDTH'])*self.max_cameras/self.max_width))
            projectors = int(np.ceil(float(self.data['WIDTH'])*self.max_projectors/self.max_width))
            projectors = 6
            cameras = 12
            return cameras, projectors, self.data
        else:
            res =self.dummy_dict.copy()
            date = date_funcs.get_date(folder_path=True)
            time = date_funcs.get_time(folder_path=True)
            date_time = '{}_{}'.format(date, time)
            res['PLATE_ID'] = date_time
            return 12, 6, res

    def convert_data(self, data):
        cleaned_data = data.decode("ISO-8859-1") 
        cleaned_data = ''.join(cleaned_data.split())
        cleaned_data = re.sub(r'[^a-zA-Z0-9_.]', '', cleaned_data)

        keywords = ['PLATE_ID', 'ORDER_ID', 'HEAT_ID', 'QC_STANDARD', 'LENGHT', 'WIDTH', 'THICKNESS', 'LENGHT_ORDER', 'WIDTH_ORDER', 'THICKNESS_ORDER', 'speed']
        indices = [cleaned_data.find(k) for k in keywords]

        indices = list(filter(lambda x: x>0, indices))
        keywords = keywords[:len(indices)]

        res = {}

        for i, k in enumerate(keywords):
            if i != len(keywords) - 1:
                res[k] = cleaned_data[indices[i]+len(k): indices[i+1]]
            else:
                res[k] = cleaned_data[indices[i]+len(k):]
                res[k] = re.sub("[^.0-9]", "", res[k])
        last_plate = self.db_obj.report_last_sheets(count=1)
        if last_plate:
            last_plate_id = last_plate[0].get_id()
            if res['PLATE_ID'] == last_plate_id:
                date = date_funcs.get_date(folder_path=True)
                time = date_funcs.get_time(folder_path=True)
                date_time = '{}_{}'.format(date, time)
                res['PLATE_ID'] += '_{}'.format(date_time)
        self.data = res

    def connect(self):
        # Should add connection function here and get details
        try:
            details={}
            if RANDOM:
                details.update({"sheet_id": str(self.sheet_id) + ''.join(random.choices(string.ascii_letters + string.digits, k = 2))})
                details.update({"pdl_number": np.random.randint(100,1000)})
                details.update({"heat_id": np.random.randint(100,1000)})
                details.update({"ps_number": np.random.randint(100,1000)})
                details.update({"width": np.random.randint(2950, 3050)})
                details.update({"length": np.random.randint(1000,10000)})
                details.update({"thickness": np.random.randint(10,50)})
                self.details=details
                self.sheet_id += 1
                # #print(details)
                return True,details
        except:
            return False,None

    def create_connection(self):

        try:

            host='176.16.32.6'
            port=11000

            self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # try:
            self.socket.bind((host,port))
            self.socket.listen(2)
        
        except:
            print('Error open port')

    def get_data(self):
        while 1:
            try:
                conn,addr=self.socket.accept()
                data=conn.recv(100000)
        
                conn.send(data)
                self.convert_data(data)
                # print('gg')
            except Exception as e:
                # print(e)
                pass

if __name__=='__main__':

    conn=connection_level2()
    conn.create_connection()
    # cameras,projectors,details = conn.get_full_info()
    #print(cameras,projectors,details )
    conn.get_data()
        

import numpy as np
import random
import string
import re
import socket
import logging as log
import time
import threading
from datetime import datetime
import time
try:
    import date_funcs
except:
    from backend import date_funcs
try:
    import texts_codes
    import texts
except:
    pass
RANDOM=True
PORT_DATA = 11000
PORT_SPEED = 12000
PORT_CHECK = 13000

DEBUG=True

if DEBUG:
    MAX_RETRY=1
else:
    MAX_RETRY=10


SAMPLE = "\x00\x01\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x04\x01\x00\x00\x00\xe2\x01System.Collections.Generic.Dictionary`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x04\x00\x00\x00\x07Version\x08Comparer\x08HashSize\rKeyValuePairs\x00\x03\x00\x03\x08\x92\x01System.Collections.Generic.GenericEqualityComparer`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x08\xe6\x01System.Collections.Generic.KeyValuePair`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]][]\x14\x00\x00\x00\t\x02\x00\x00\x00%\x00\x00\x00\t\x03\x00\x00\x00\x04\x02\x00\x00\x00\x92\x01System.Collections.Generic.GenericEqualityComparer`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x00\x00\x00\x00\x07\x03\x00\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00\x03\xe4\x01System.Collections.Generic.KeyValuePair`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x04\xfc\xff\xff\xff\xe4\x01System.Collections.Generic.KeyValuePair`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x02\x00\x00\x00\x03key\x05value\x01\x02\x06\x05\x00\x00\x00\x07speedT1\x06\x06\x00\x00\x00\x0b1000.000000\x01\xf9\xff\xff\xff\xfc\xff\xff\xff\x06\x08\x00\x00\x00\x07speedT2\x06\t\x00\x00\x00\x0b1000.000000\x01\xf6\xff\xff\xff\xfc\xff\xff\xff\x06\x0b\x00\x00\x00\x07speedT3\x06\x0c\x00\x00\x00\x0b1000.000000\x01\xf3\xff\xff\xff\xfc\xff\xff\xff\x06\x0e\x00\x00\x00\x07speedT4\x06\x0f\x00\x00\x00\x0b1000.000000\x01\xf0\xff\xff\xff\xfc\xff\xff\xff\x06\x11\x00\x00\x00\x07speedT5\x06\x12\x00\x00\x00\x0b1000.000000\x01\xed\xff\xff\xff\xfc\xff\xff\xff\x06\x14\x00\x00\x00\x07speedT6\x06\x15\x00\x00\x00\x0b1000.000000\x01\xea\xff\xff\xff\xfc\xff\xff\xff\x06\x17\x00\x00\x00\x07speedT7\x06\x18\x00\x00\x00\x0b1000.000000\x01\xe7\xff\xff\xff\xfc\xff\xff\xff\x06\x1a\x00\x00\x00\x07speedT8\x06\x1b\x00\x00\x00\x0b1000.000000\x01\xe4\xff\xff\xff\xfc\xff\xff\xff\x06\x1d\x00\x00\x00\x07speedT9\x06\x1e\x00\x00\x00\x0b1000.000000\x01\xe1\xff\xff\xff\xfc\xff\xff\xff\x06 \x00\x00\x00\x08speedT10\x06!\x00\x00\x00\x0b1000.000000\x01\xde\xff\xff\xff\xfc\xff\xff\xff\x06#\x00\x00\x00\x08speedT11\x06$\x00\x00\x00\x0b1000.000000\x01\xdb\xff\xff\xff\xfc\xff\xff\xff\x06&\x00\x00\x00\x08speedT12\x06'\x00\x00\x00\x0b1000.000000\x01\xd8\xff\xff\xff\xfc\xff\xff\xff\x06)\x00\x00\x00\x08speedT13\x06*\x00\x00\x00\x0b1000.000000\x01\xd5\xff\xff\xff\xfc\xff\xff\xff\x06,\x00\x00\x00\x08speedT14\x06-\x00\x00\x00\x0b1000.000000\x01\xd2\xff\xff\xff\xfc\xff\xff\xff\x06/\x00\x00\x00\x08speedT15\x060\x00\x00\x00\x0b1000.000000\x01\xcf\xff\xff\xff\xfc\xff\xff\xff\x062\x00\x00\x00\x08speedT16\x063\x00\x00\x00\x0b1000.000000\x01\xcc\xff\xff\xff\xfc\xff\xff\xff\x065\x00\x00\x00\x08speedT17\x066\x00\x00\x00\x0b1000.000000\x01\xc9\xff\xff\xff\xfc\xff\xff\xff\x068\x00\x00\x00\x08speedT18\x069\x00\x00\x00\x0b1000.000000\x01\xc6\xff\xff\xff\xfc\xff\xff\xff\x06;\x00\x00\x00\x08speedT19\x06<\x00\x00\x00\x0b1000.000000\x01\xc3\xff\xff\xff\xfc\xff\xff\xff\x06>\x00\x00\x00\x08speedT20\x06?\x00\x00\x00\x0b1000.000000\x0b"


SAMPLE = "\x00\x01\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x04\x01\x00\x00\x00\xe2\x01System.Collections.Generic.Dictionary`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x04\x00\x00\x00\x07Version\x08Comparer\x08HashSize\rKeyValuePairs\x00\x03\x00\x03\x08\x92\x01System.Collections.Generic.GenericEqualityComparer`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x08\xe6\x01System.Collections.Generic.KeyValuePair`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]][]\x14\x00\x00\x00\t\x02\x00\x00\x00%\x00\x00\x00\t\x03\x00\x00\x00\x04\x02\x00\x00\x00\x92\x01System.Collections.Generic.GenericEqualityComparer`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x00\x00\x00\x00\x07\x03\x00\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00\x03\xe4\x01System.Collections.Generic.KeyValuePair`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x04\xfc\xff\xff\xff\xe4\x01System.Collections.Generic.KeyValuePair`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Object, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]]\x02\x00\x00\x00\x03key\x05value\x01\x02\x06\x05\x00\x00\x00\x07speedT1\x06\x06\x00\x00\x00\x0b1000.000000\x01\xf9\xff\xff\xff\xfc\xff\xff\xff\x06\x08\x00\x00\x00\x07speedT2\x06\t\x00\x00\x00\x0b000.000000\x01\xf6\xff\xff\xff\xfc\xff\xff\xff\x06\x0b\x00\x00\x00\x07speedT3\x06\x0c\x00\x00\x00\x0b1000.000000\x01\xf3\xff\xff\xff\xfc\xff\xff\xff\x06\x0e\x00\x00\x00\x07speedT4\x06\x0f\x00\x00\x00\x0b1000.000000\x01\xf0\xff\xff\xff\xfc\xff\xff\xff\x06\x11\x00\x00\x00\x07speedT5\x06\x12\x00\x00\x00\x0b1000.000000\x01\xed\xff\xff\xff\xfc\xff\xff\xff\x06\x14\x00\x00\x00\x07speedT6\x06\x15\x00\x00\x00\x0b1000.000000\x01\xea\xff\xff\xff\xfc\xff\xff\xff\x06\x17\x00\x00\x00\x07speedT7\x06\x18\x00\x00\x00\x0b1000.000000\x01\xe7\xff\xff\xff\xfc\xff\xff\xff\x06\x1a\x00\x00\x00\x07speedT8\x06\x1b\x00\x00\x00\x0b1000.000000\x01\xe4\xff\xff\xff\xfc\xff\xff\xff\x06\x1d\x00\x00\x00\x07speedT9\x06\x1e\x00\x00\x00\x0b1000.000000\x01\xe1\xff\xff\xff\xfc\xff\xff\xff\x06 \x00\x00\x00\x08speedT10\x06!\x00\x00\x00\x0b1000.000000\x01\xde\xff\xff\xff\xfc\xff\xff\xff\x06#\x00\x00\x00\x08speedT11\x06$\x00\x00\x00\x0b1000.000000\x01\xdb\xff\xff\xff\xfc\xff\xff\xff\x06&\x00\x00\x00\x08speedT12\x06'\x00\x00\x00\x0b1000.000000\x01\xd8\xff\xff\xff\xfc\xff\xff\xff\x06)\x00\x00\x00\x08speedT13\x06*\x00\x00\x00\x0b1000.000000\x01\xd5\xff\xff\xff\xfc\xff\xff\xff\x06,\x00\x00\x00\x08speedT14\x06-\x00\x00\x00\x0b1000.000000\x01\xd2\xff\xff\xff\xfc\xff\xff\xff\x06/\x00\x00\x00\x08speedT15\x060\x00\x00\x00\x0b1000.000000\x01\xcf\xff\xff\xff\xfc\xff\xff\xff\x062\x00\x00\x00\x08speedT16\x063\x00\x00\x00\x0b1000.000000\x01\xcc\xff\xff\xff\xfc\xff\xff\xff\x065\x00\x00\x00\x08speedT17\x066\x00\x00\x00\x0b1000.000000\x01\xc9\xff\xff\xff\xfc\xff\xff\xff\x068\x00\x00\x00\x08speedT18\x069\x00\x00\x00\x0b1000.000000\x01\xc6\xff\xff\xff\xfc\xff\xff\xff\x06;\x00\x00\x00\x08speedT19\x06<\x00\x00\x00\x0b1000.000000\x01\xc3\xff\xff\xff\xfc\xff\xff\xff\x06>\x00\x00\x00\x08speedT20\x06?\x00\x00\x00\x0b0000.000000\x0b"

class connection_level2():

    def __init__(self, db_obj,close_ui,logger=False):
        # self.ui_obj=ui_obj
        # self.sheet_id = 900
        self.db_obj = db_obj
        self.close_ui = close_ui

        self.logger = logger
        # ------------------------------------------
        self.get_data_timer = 1
        self.data = None
        self.check_data = False
        self.max_cameras = 12
        self.max_width = 4800
        self.max_projectors = 6
        self.retry_get_data = 0
        self.retry_get_speed = 0
        self.retry_get_check_data=0
        self.last_speed = -1
        self.dummy_dict = {'PLATE_ID': 'ABC12345A', 'ORDER_ID': '123456789', 'HEAT_ID': '123456', 'QC_STANDARD': 'ASTM450', 'LENGHT': '6040', 'WIDTH': '2020', 'THICKNESS': '25.23', 'LENGHT_ORDER': '6000', 'WIDTH_ORDER': '2000', 'THICKNESS_ORDER': '25', 'speed': '1500'}
        # self.get_data_socket = self.create_connection(PORT_DATA)
        # self.get_speed_socket = self.create_connection(PORT_SPEED)
        # self.check_socket = self.create_connection(PORT_CHECK)





    def set_get_data_timer(self, timer):
        self.get_data_timer = timer

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
    
    def get_dummy_info(self):
        return 12, 6, self.dummy_dict
    
    def get_date_time_info(self):
        res =self.dummy_dict.copy()
        date = date_funcs.get_date(folder_path=True)
        time = date_funcs.get_time(folder_path=True)
        date_time = '{}_{}'.format(date, time)
        res['PLATE_ID'] = date_time
        return 12, 6, res 

    def get_full_info(self):
        if self.data:
            cameras = int(np.ceil(float(self.data['WIDTH'])*self.max_cameras/self.max_width))
            projectors = int(np.ceil(float(self.data['WIDTH'])*self.max_projectors/self.max_width))
            projectors = 6
            # cameras = 12
            return cameras, projectors, self.data
        else:
            return 0, 0, None
            

    def convert_data(self, data):
        cleaned_data = data.decode("ISO-8859-1") 
        cleaned_data = ''.join(cleaned_data.split())
        cleaned_data = re.sub(r'[^a-zA-Z0-9_.]', '', cleaned_data)
        keywords = ['PLATE_ID', 'ORDER_ID', 'HEAT_ID', 'QC_STANDARD', 'LENGHT', 'WIDTH', 'THICKNESS', 'LENGHT_ORDER', 'WIDTH_ORDER', 'THICKNESS_ORDER', 'speed']
        indices = [cleaned_data.find(k) for k in keywords]

        filterd_data = [(index, key) for index, key in zip(indices, keywords) if index!=-1]
        indices, keywords = zip(*filterd_data)

        res = self.dummy_dict.copy()

        for i, k in enumerate(keywords):
            if i != len(keywords) - 1:
                res[k] = cleaned_data[indices[i]+len(k): indices[i+1]]
            else:
                res[k] = cleaned_data[indices[i]+len(k):]
                res[k] = re.sub("[^.0-9]", "", res[k])
        
        self.data = res
    def convert_speed(self,data,last_speed=True):
        
    
        cleaned_data = data.decode("ISO-8859-1") 
        cleaned_data = ''.join(cleaned_data.split())
        cleaned_data = re.sub(r'[^a-zA-Z0-9_.]', '', cleaned_data)
        keywords = ['T'+str(i) for i in range(21)]
        if last_speed:
            keywords = ['speed' for i in range(21)]

        indices = [cleaned_data.find(k) for k in keywords]

        filterd_data = [(index, key) for index, key in zip(indices, keywords) if index!=-1]
        indices = [x.start() for x in re.finditer('speed', cleaned_data)]
        res = []
        for i in range(len(indices) - 1):
            res.append(cleaned_data[indices[i]+5:indices[i+1]])
        res.append(cleaned_data[indices[-1]+5:])

        if last_speed:
            # try:
            if len(res)>9:
                self.last_speed=(float(res[-1][3:]))
            else:
                self.last_speed = float(res[-1][2:])
            return self.last_speed
            # except:
            #     print('Get Speed Error')
            #     return -1
                        
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

    def create_connection(self,port):

        try:
            host='176.16.32.6'
            port=port

            socket_=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # try:
            socket_.bind((host,port))
            socket_.listen(2)
            return socket_
        except:
            print('Error open port')

    def get_data(self):
        try:
            conn, addr = self.get_data_socket.accept()
            data = conn.recv(100000)
            conn.send(data)
            self.convert_data(data)
            self.retry_get_data = 0
            if self.logger:
                self.logger.create_new_log(
                    code=texts_codes.SubTypes["Get_data_SUCCUSSFULL"],
                    message=texts.MESSEGES["Get_data_SUCCUSSFULL"]["en"]+str(self.data),
                    level=1,
                )
        except:
            self.retry_get_data+=1
            if self.retry_get_data<MAX_RETRY:
                self.get_data_socket = self.create_connection(PORT_DATA)
                if self.logger:
                    self.logger.create_new_log(
                        code=texts_codes.SubTypes["Get_data_FAILED"],
                        message=texts.MESSEGES["Get_data_FAILED"]["en"],
                        level=5,
                    )
            self.data=False
            time.sleep(1)
        if not self.close_ui:
            threading.Timer(self.get_data_timer, self.get_data).start()
               

    def get_check_data(self):
        try:
            t1 = datetime.now()
            conn,addr=self.check_socket.accept()
            self.check_data=conn.recv(100000)
            # conn.send(data)
            # self.convert_data(data)
            self.retry_get_check_data = 0
            if self.logger:
                self.logger.create_new_log(
                    code=texts_codes.SubTypes["Get_check_data_SUCCUSSFULL"],
                    message=texts.MESSEGES["Get_check_data_SUCCUSSFULL"]["en"],
                    level=1,
                )
        except:
            self.retry_get_check_data+=1
            if self.retry_get_check_data<MAX_RETRY:
                self.check_socket = self.create_connection(PORT_DATA)    
                if self.logger:      
                    self.logger.create_new_log(
                        code=texts_codes.SubTypes["Get_check_data_FAILED"],
                        message=texts.MESSEGES["Get_check_data_FAILED"]["en"],
                        level=5,
                    )
            time.sleep(1)
            self.check_data=False

        if not self.close_ui:
            threading.Timer(self.get_data_timer, self.get_check_data).start()

    def get_speed(self):
        
        try:
            # print('start get speed')
            t1 = datetime.now()
            conn,addr=self.get_speed_socket.accept()
            data=conn.recv(100000)
            conn.send(data)
            self.convert_speed(data)
            self.retry_get_speed = 0
            # if self.logger:
            #     self.logger.create_new_log(
            #         code=texts_codes.SubTypes["Get_speed_SUCCUSSFULL"],
            #         message=texts.MESSEGES["Get_speed_SUCCUSSFULL"]["en"]+'  '+str(self.last_speed),
            #         level=1,
            #     )

        except:
            self.retry_get_speed+=1
            if self.retry_get_speed<MAX_RETRY:
                self.get_speed_socket = self.create_connection(PORT_SPEED)
                if self.logger:
                    self.logger.create_new_log(
                    code=texts_codes.SubTypes["Get_speed_FAILED"],
                    message=texts.MESSEGES["Get_speed_FAILED"]["en"],
                    level=5,
                    )
            self.last_speed=False
            time.sleep(1)

        if not self.close_ui:
            threading.Timer(0.9, self.get_speed).start()



    def set_ui_status_time(self,frame_name,status,time):

        self.ui_obj.set_style_sheet(frame_name,status)
        self.ui_obj.set_time(frame_name,time)


    def reset_retry_values(self):
        self.retry_get_data=0
        self.retry_get_speed=0
        self.retry_get_check_data=0

if __name__=='__main__':

    conn=connection_level2(None, False,logger=False)
    # conn.create_connection()
    # cameras,projectors,details = conn.get_full_info()
    #print(cameras,projectors,details )
    # conn.get_data()
    threading.Thread(target= conn.get_speed).start()
    threading.Thread(target= conn.get_check_data).start()
    
    conn.get_data()
        
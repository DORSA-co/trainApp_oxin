

# from sqlalchemy import false, true
import database
import datetime

import os


class dataBaseUtils():
    def __init__(self) :
        self.db=database.dataBase('root','root','localhost','saba_database')

        self.table_user='users'
        self.table_cameras = 'camera_settings'
        self.table_general_settings = 'settings'
        self.camera_id = 'id'
        self.setting_tabel = 'settings'
        self.general_settings_id = 'id'

    #________________________________________________________________
    #
    #________________________________________________________________
    def search_user(self,input_user_name):



        try:
            record = self.db.search( self.table_user , 'user_name', str(input_user_name) )[0]
            #print('asd',record)
            print('rec',record)
            return record
        except:
            return []


    def search_camera_by_ip(self, input_camera_ip):
        try:
            record = self.db.search( self.table_cameras , 'ip_address', input_camera_ip)[0]
            #print('asd',record)
            return record
        except:
            return []
    

    def load_cam_params(self, input_camera_id):
        print('asdwa')
        try:
            record = self.db.search( self.table_cameras , 'id', input_camera_id )[0]
            #print('camera info:', record)
            print('recor',record)
            return record
        except:
            return []

    def update_cam_params(self, input_camera_id, input_camera_params):
        try:
            for camera_param in input_camera_params.keys():
                res = self.db.update_record(self.table_cameras, camera_param, str(input_camera_params[camera_param]), self.camera_id, input_camera_id)
            return res
        except:
            return False


    def update_general_setting_params(self, input_setting_params):
        try:
            for param in input_setting_params.keys():
                res = self.db.update_record(self.table_general_settings, param, str(input_setting_params[param]), self.general_settings_id, '0')
            return res
        except:
            return False

    def load_general_setting_params(self):
        try:
            record = self.db.search( self.table_general_settings , self.general_settings_id, '0' )[0]
            #print('camera info:', record)
            return record
        except:
            return []



    def load_users(self):
        try:
            users=self.db.get_all_content('users')

            return users
        
        except:

            return []


    def remove_users(self,users_name):

        for i in range(len(users_name)):
            
            self.db.remove_record(col_name='user_name',id=users_name[i],table_name='users')

    def add_user(self,parms):
        data=(parms['user_id'],parms['user_pass'],parms['user_role'])
        print(data)
        try:
            self.db.add_record(data, table_name='users', parametrs='(user_name,password,role)', len_parameters=3)
            return 'True'
        
        except:
            return 'Databas Eror'



    def set_image_processing_parms(self,data):

        # print(data[0])
        # self.db.update_record(table_name='image_processing', col_name=col_name[i], value=data[col_name[i]], id='id', id_value='0')
        print('asd',data)

        col_name=['block_size','defect','noise']

        print('asdwqd',data[col_name[0]])

        for i in range(3):

            # print(data[i])

            self.db.update_record(table_name='image_processing', col_name=col_name[i], value=str(data[col_name[i]]), id='id', id_value='0')







    def get_dataset_path(self):
        record =self.db.search(table_name=self.setting_tabel,param_name='id',value=0)[0 ]
        return record['parent_path']






if __name__ == '__main__':
    db = dataBaseUtils()
    # records = db.load_coil_info(996)
    # db.get_camera_setting()
    #db.set_dataset_path('G:/dataset/')
    # print(db.get_dataset_path())

    # db.get_path(['997', 'up', (5, 5)])
    # pass

    # db.load_cam_params('1')

    # x=db.load_users()

    # user=['ali']

    # db.remove_users(user)


    x=db.get_dataset_path()

    print(x)
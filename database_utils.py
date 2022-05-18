

from itertools import count
import database
import datetime
from Sheet import Sheet
import os
from backend import pathStructure, binary_model_funcs

class dataBaseUtils():
    def __init__(self) :
        self.db=database.dataBase('root','root','localhost','saba_database')
        self.sheets_info_tabel = 'sheets_info'
        self.setting_tabel = 'settings'
        self.camera_settings_table='camera_settings'
        self.defects_table = 'defects_info'
        self.sign_tables='sign_tables'
        self.table_cameras = 'camera_settings'

    #________________________________________________________________
    #
    #________________________________________________________________
    def build_sheet(self,record):
        y,m,d = record['date'].split('/')
        hh,mm = record['time'].split(':')
        sheet_obj = Sheet(
            id          = record['id'],
            sheet_id    = record['sheet_id'],
            main_path   = record['main_path'],
            image_format= record['image_format'],
            heat_number = record['heat_number'],
            ps_number   = record['ps_number'],
            pdl_number  = record['pdl_number'],
            width       = record['width'],
            lenght      = record['lenght'],
            thickness   = record['thickness'],
            date        = datetime.date(int(y),int(m),int(d)),
            time        = datetime.time(int(hh),int(mm)),
            user        = record['user'],
            nframe      = record['nframe'],
            cameras     = [int( record['cameras'].split('-')[0] ) , int( record['cameras'].split('-')[1] )]
        )
        return sheet_obj

    #________________________________________________________________
    #
    #________________________________________________________________
    def load_sheet(self,id):
        record = self.db.search( self.sheets_info_tabel , 'sheet_id', id )[0]
        
        return self.build_sheet(record)

    #________________________________________________________________
    #
    #________________________________________________________________
    def load_sheets(self,ids):
        sheets = []
        for id in ids:
            record = self.db.search( self.sheets_info_tabel , 'sheet_id', id )[0]
            sheets.append( self.build_sheet(record) )
        return sheets
    #________________________________________________________________
    #
    #________________________________________________________________
    def get_camera_setting(self):
        x=self.db.report_last(self.camera_settings_table,'id','0')


        # cam_setting = self.db.search( 'camera_settings', 'id', id )[0]

    #________________________________________________________________
    #
    #________________________________________________________________
    def report_last_sheets(self,count):
        
        records=self.db.report_last(self.sheets_info_tabel,'sheet_id',count)
        res = []
        for record in records:
            res.append( self.build_sheet( record ) )
        return res

    #________________________________________________________________
    #
    #________________________________________________________________
    def set_dataset_path(self,path):
        #  update_record(self,data,table_name,col_name,value,id,id_value):
        self.db.update_record(table_name= self.setting_tabel,col_name='path_dataset',value=path,id='id',id_value=0)


    def get_dataset_path(self):
        record =self.db.search(table_name=self.setting_tabel,param_name='id',value=0)[0 ]
        return record['path_dataset']

    def set_dataset_path_user(self,path):
        #  update_record(self,data,table_name,col_name,value,id,id_value):
        self.db.update_record(table_name= self.setting_tabel,col_name='path_dataset_user',value=path,id='id',id_value=0)

    def get_dataset_path_uesr(self):
        record =self.db.search(table_name=self.setting_tabel,param_name='id',value=0)[0 ]
        print('record',record)
        return record['path_dataset_user']

    def set_weights_path(self,path):
        #  update_record(self,data,table_name,col_name,value,id,id_value):
        self.db.update_record(table_name= self.setting_tabel,col_name='path_weights',value=path,id='id',id_value=0)

    def get_weights_path(self):
        record =self.db.search(table_name=self.setting_tabel,param_name='id',value=0)[0 ]
        return record['path_weights']

    def set_split_size(self, size):
        self.db.update_record(table_name=self.setting_tabel, col_name='split_size', value=str(size), id='id', id_value=0)

    def get_split_size(self):
        record =self.db.search(table_name=self.setting_tabel,param_name='id',value=0)[0 ]
        return eval(record['split_size'])

    def get_path_sheet_image(self,filtered_selected):
        paths = []
        for sheet_id, side, (ncam, nframe) in filtered_selected:
            sheet = self.load_sheet(sheet_id)
            path = pathStructure.sheet_image_path(
                sheet.get_main_path(),
                sheet_id,
                side,
                ncam,
                nframe,
                sheet.get_image_format()
            )

            paths.append( path )
        
        return paths


    def get_defects(self):

        defects_info=self.db.get_all_content(self.defects_table)

        print('asdasd',defects_info)
        name_list=[]
        for i in range(len(defects_info)):
            name_list.append(defects_info[i]['name'])

        return name_list,defects_info            


    def ret_sign_defect_table(self):

        sign=self.db.search(self.sign_tables, 'id', '0')

        return sign[0]['defects_info']


    def update_sign_table(self,col_name,value,id='id',id_value=0):

        self.db.update_record(self.sign_tables, col_name, value, id, id_value)

    def load_cam_params(self, input_camera_id):
        print('asdwa')
        try:
            record = self.db.search( self.table_cameras , 'id', input_camera_id )[0]
            #print('camera info:', record)
            # print('recor',record)
            return record
        except:
            return []

    #_____________________________________________________________________________________
    # binary-models
    
    def get_binary_models(self, count=False, limit=False, limit_range=[0,20]):
        try:
            bmodels=self.db.get_all_content('binary_models', count=count, limit=limit, limit_range=limit_range)
            #print('--------------------------------------------', defects)
            return bmodels
        except:
            return []
    

    def add_binary_model_record(self, params):
        #print('params:', params)
        data = ()
        db_headers = ''
        for db_header in binary_model_funcs.binary_headers_db:
            data = data + (params[db_header], )
            db_headers = db_headers + db_header + ','
        db_headers = '(' + db_headers[:-1] + ')'
        #print('bmodel_record:', data, 'cols:', db_headers)
        try:
            self.db.add_record(data, table_name='binary_models', parametrs=db_headers, len_parameters=len(binary_model_funcs.binary_headers_db))
            return 'True'
        
        except:
            return 'Databas Eror'
    

    def search_binary_model_by_filter(self, parms, cols, limit=False, limit_range=[0,20], count=False):
        try:
            #print('here')
            record = self.db.search_with_range('binary_models', cols, parms, limit=limit, limit_range=limit_range, count=count)
            #print('asd',record)
            return record

        except:
            return []






if __name__ == '__main__':
    db = dataBaseUtils()
    # records = db.load_coil_info(996)
    # db.get_camera_setting()
    # db.set_dataset_path('G:/dataset/')
    # print(db.get_dataset_path())

    # name,defects=db.get_defects()
    # print('name',name)
    # print('defe',defects)

    # x=db.get_sign('defects_info')

    db.update_sign_table('defects_info','4')

    # print(x)
    name,defects=db.get_defects()
    print('name',name)
    print('defe',defects)


    # db.get_path(['997', 'up', (5, 5)])
    # pass


from itertools import count
import database
import datetime
from Sheet import Sheet
import os
from backend import pathStructure, binary_model_funcs
import inspect
class dataBaseUtils():
    def __init__(self,user_name='root',password='') :
        self.db=database.dataBase(user_name,password,'localhost','saba_database')
        self.sheets_info_tabel = 'sheets_info'
        self.setting_tabel = 'settings'
        self.datasets_table = 'datasets'
        self.camera_settings_table='camera_settings'
        self.defects_table = 'defects_info'
        self.sign_tables='sign_tables'
        self.table_user='users'
        self.table_cameras = 'camera_settings'
        self.image_processing = 'image_processing'
        self.dataset='datasets '


    def check_table_exist(self,table_name):
        ret=self.db.check_table_exist(table_name)
        return ret
    
    def check_connection(self):
        ret=self.db.check_connection()
        return ret
            #________________________________________________________________
    #
    #________________________________________________________________
    def build_sheet(self,record):
        y,m,d = record['date'].split('/')
        hh,mm,_ = record['time'].split(':')
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

    # ________________________________________________________________
    #
    # ________________________________________________________________
    def set_sheet(self, coil_dict):
        data = ()
        db_headers = ''
        for key in coil_dict:
            data = data + (coil_dict[key],)
            db_headers = db_headers + key + ','
        db_headers = '(' + db_headers[:-1] + ')'
        # print('bmodel_record:', data, 'cols:', db_headers)
        try:
            self.db.add_record(data, table_name=self.sheets_info_tabel, parametrs=db_headers,
                               len_parameters=len(coil_dict))
            return 'True'

        except:
            return 'Databas Eror'

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


    def get_dataset(self, value=0):
        record =self.db.search(table_name=self.datasets_table, param_name='id', value=value)[0 ]
        return record

    def get_parent_path(self, value=0):
        record = self.db.search(table_name=self.setting_tabel, param_name='id', value=value)[0]
        return record['parent_path']

    def set_dataset_path_user(self,path):
        #  update_record(self,data,table_name,col_name,value,id,id_value):
        self.db.update_record(table_name= self.setting_tabel,col_name='path_dataset_user',value=path,id='id',id_value=0)

    # def set_split_size(self, size, id):
    #     self.db.update_record(table_name=self.datasets_table, col_name='split_size', value=str(size), id='id', id_value=id)
    #
    # def get_split_size(self, id):
    #     record =self.db.search(table_name=self.datasets_table,param_name='id',value=id)[0 ]
    #     return eval(record['split_size'])

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

    def get_image_processing_params(self):
        img_proc_info = self.db.get_all_content(self.image_processing)[0]
        return list(img_proc_info.values())[1:]

    def get_defects(self):

        defects_info=self.db.get_all_content(self.defects_table)

        print('asdasd',defects_info)
        name_list=[]
        for i in range(len(defects_info)):
            name_list.append(defects_info[i]['name'])

        return name_list, defects_info

    def get_defect_id(self, selected_label):
        try:
            record = self.db.search(self.defects_table, 'name', selected_label, int_type=False)[0]
            # print('asd',record)
            return record['defect_ID']
        except:
            return []

    def search_defect_by_id(self, input_defect_id):
        try:
            record = self.db.search( 'defects_info' , 'defect_ID', input_defect_id)[0]
            #print('asd',record)
            return record
        except:
            return []


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
    
    def get_binary_models(self, count=False, limit=False, limit_size=20, offset=0):
        try:
            bmodels=self.db.get_all_content('binary_models', count=count, limit=limit, limit_size=limit_size, offset=offset, reverse_order=True)
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
    

    def search_binary_model_by_filter(self, parms, cols, limit=False, limit_size=20, offset=0, count=False):
        try:
            #print('here')
            record = self.db.search_with_range('binary_models', cols, parms, limit=limit, limit_size=limit_size, offset=offset, count=count)
            #print('asd',record)
            return record

        except:
            return []
    

    #________________________________________________________________________________________________________
    # classification models
    def get_cls_models(self, count=False, limit=False, limit_size=20, offset=0):
        try:
            bmodels=self.db.get_all_content('classification_models', count=count, limit=limit, limit_size=limit_size, offset=offset, reverse_order=True)
            #print('--------------------------------------------', defects)
            return bmodels
        except:
            return []
    

    # 
    def search_cls_model_by_filter(self, parms, cols, limit=False, limit_size=20, offset=0, count=False):
        try:
            #print('here')
            record = self.db.search_with_range_with_classes('classification_models', cols, parms, limit=limit, limit_size=limit_size, offset=offset, count=count)
            #print('asd',record)
            return record

        except:
            return []



    # ______________________________________________________________________________________
    # defects
    def load_defects(self):
        try:
            defects=self.db.get_all_content('defects_info')

            return defects
        
        except:

            return []


    def search_defect_group_by_id(self, input_defect_group_id):
        try:
            record = self.db.search( 'defect_groups' , 'defect_group_id', input_defect_group_id)[0]
            #print('asd',record)
            return record
        except:
            return []

    #______________________________________________________________________________________________
    #______________________________________________________________________________________
    # datasets
    def load_datasets(self):
        try:
            datasets=self.db.get_all_content('datasets')
            return datasets
        except:
            return []
    
    #___________________________________________________________________________________


    def search_user(self,input_user_name):

        try:
            record = self.db.search( self.table_user , 'user_name', input_user_name ,int_type=False)[0]
            record_ds = self.db.search(self.datasets_table, 'id', record['default_dataset'], int_type=False)[0]
            record['default_dataset'] = record_ds['name']
            print(record)
            #print('asd',record)
            return record
        except:
            return []


    def get_default_dataset(self,user_name):

        try:
            record = self.db.search( self.table_user ,'user_name', user_name ,int_type=False)[0]

            print('record',record)

            return record['default_dataset']
        except:
            print('except')
            return []

    def get_dateset_name(self, id):
        try:
            record = self.db.search( self.datasets_table ,'id', id ,int_type=False)[0]

            print('record',record)

            return record['name']
        except:
            print('except')
            return []

    def get_path_dataset(self,dataset_id):

    # try:
        record = self.db.search( self.dataset ,'id', dataset_id ,int_type=False)[0]

        print('record',record)

        return record['path']
        # except:
        #     print('except')
        #     return []

    def get_all_datasets(self):
        
        records = self.db.report_last(self.dataset,'id',99, side='ASC')

        return records


    def get_user_databases(self,user_name, default=True):

        # try:
        record = self.db.search( self.dataset ,'user_own', user_name ,int_type=False)

        if default:
            default_record = self.db.search( self.dataset ,'id', 0 ,int_type=False)
            record += default_record

        default_ds = self.get_default_dataset(user_name)
        print('*********{}**********'.format(default_ds))

        for i in range(len(record)):
            if str(record[i]['id']) == default_ds:
                break

        record.insert(0, record.pop(i))

        print('****record',record)
        return record
    # except:
        #     print('except')
        #     return []


    def update_dataset_default(self,dataset_id,user_name):
    
        self.db.update_record(self.table_user, 'default_dataset', str(dataset_id), 'user_name', user_name)


    def add_dataset(self,data):

        # try:
        self.db.add_record(data, table_name=self.dataset, parametrs='(name,user_own,path)', len_parameters=3)
        return 'True'
        
        # except:
        #     return 'Databas Eror'


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

    # db.update_sign_table('defects_info','4')
    # d=db.get_user_databases('ali')
    data=('dataset_name','ali','adwad')
    d=db.add_dataset(data)
    print(d)
    # print(x)
    # name,defects=db.get_defects()
    # print('name',name)
    # print('defe',defects)


    # db.get_path(['997', 'up', (5, 5)])
    # pass
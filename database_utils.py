

import database
from Sheet import Sheet
import os
from backend import pathStructure

class dataBaseUtils():
    def __init__(self) :
        self.db=database.dataBase('root','Dorsa1400@','localhost','saba_database')
        self.sheets_info_tabel = 'sheets_info'
        self.setting_tabel = 'settings'

    #________________________________________________________________
    #
    #________________________________________________________________
    def build_sheet(self,record):
        print(record)
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
            date        = record['date'],
            time        = record['time'],
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
    def get_camera_setting(self):
        x=self.db.report_last('camera_settings','id','0')

        print(x)

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
        return record['parent_path']


   

    def get_path_sheet_image(self,filtered_selected):
        paths = []
        print(filtered_selected)
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
            
            #record =self.db.search(table_name=self.sheets_info_tabel,param_name='sheet_id',value=sheet_id)[0 ]
            
            #

            #record=self.db.search(table_name=self.sheets_info_tabel,param_name='id',value=filtered_selected[item][0])

            # path=os.path.join(sheet.get_path(),   )

            






if __name__ == '__main__':
    db = dataBaseUtils()
    # records = db.load_coil_info(996)
    # db.get_camera_setting()
    # db.set_dataset_path('G:/datasdet/')
    print(db.get_dataset_path())

    db.get_path(['997', 'up', (5, 5)])
    pass
from cv2 import split
import database
from Sheet import Sheet

class dataBaseUtils():
    def __init__(self) :
        self.db=database.dataBase('root','Dorsa1400@','localhost','saba_database')
        self.sheets_info_tabel = 'coils_info'

    #________________________________________________________________
    #
    #________________________________________________________________
    def build_sheet(self,record):
        sheet_obj = Sheet(
            id          = record['id'],
            main_path   = record['main_path'],
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
        record = self.db.search( self.sheets_info_tabel , 'id', id )[0]
        
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
        
        records=self.db.report_last(self.sheets_info_tabel,'id',count)
        res = []
        for record in records:
            res.append( self.build_sheet( record ) )
        return res





if __name__ == '__main__':
    db = dataBaseUtils()
    # records = db.load_coil_info(996)
    db.get_camera_setting()
    pass
#########################################
#////////////////////////////////////////
#
#  Data set stracture include
#   Binary-->
#           Defect
#           Perfect
#
#   Annotation
#   Images
#   temp_annotations
#   temp_images
#   
#   Dataset-name.json
#
#
#////////////////////////////////////////
#########################################



import os
from backend import date_funcs
from database_utils import dataBaseUtils
# from main_UI import SHAMSI_DATE
SHAMSI_DATE = False

settings = {
    'image_format' : '.jpg'
}

def create_sheet_path(main_path, id):
    year, month, day = date_funcs.get_date(persian=SHAMSI_DATE).split('/')
    sides = ['BOTTOM', 'TOP']
    cams = 12
    for side in sides:
        for cam in range(1, cams+1):
            path = os.path.join(main_path, year, month, day, str(id), side, str(cam))
            if not os.path.exists(path):
                os.makedirs(path)

def sheet_image_path(main_path,id, side, camera_numbers, n_frame, format_img):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date = db.load_sheet_date(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'TOP', str(camera_numbers), str(n_frame) + str(format_img) ))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'BOTTOM', str(camera_numbers), str(n_frame) + str(format_img)))

def sheet_path(main_path, id):
    db = dataBaseUtils(ui_obj='Null')
    date = db.load_sheet_date(id)
    year, month, day = date.split('/')
    return(os.path.join(main_path, year, month, day, str(id)))



# def create_dataset_stracture(path):
#
#     os.mkdir(os.path.join(path,'annotations'))
#     os.mkdir(os.path.join(path,'binary'))
#     os.mkdir(os.path.join(path,'temp_annotations'))
#     os.mkdir(os.path.join(path,'temp_images'))


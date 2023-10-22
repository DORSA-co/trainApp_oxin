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


OPERATOR_IMAGES_PATH='Images'
OPERATOR_ANNOTATIONS_PATH='Annotations'
OPERATOR_INFO_PATH='Sheets_Info'


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
        date, main_path = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'TOP', str(camera_numbers), str(n_frame) + str(format_img) ))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'BOTTOM', str(camera_numbers), str(n_frame) + str(format_img)))

def sheet_image_path_operator(main_path,id, side, camera_numbers, n_frame, format_img):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, main_path = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id),OPERATOR_IMAGES_PATH, 'TOP', str(camera_numbers), str(n_frame) + str(format_img) ))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id),OPERATOR_IMAGES_PATH ,'BOTTOM', str(camera_numbers), str(n_frame) + str(format_img)))
    
def sheet_annotation_path_operator(main_path, id, side, camera_numbers, n_frame, format='.json'):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, main_path = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id),OPERATOR_ANNOTATIONS_PATH, 'TOP', str(camera_numbers), str(n_frame) + str(format)))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id),OPERATOR_ANNOTATIONS_PATH ,'BOTTOM', str(camera_numbers), str(n_frame) + str(format)))
    
def sheet_info_path_operator(main_path, id, format='.json'):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, main_path = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    return(os.path.join(main_path, year, month, day, str(id), OPERATOR_INFO_PATH, 'info{}'.format(format)))

def get_image_annotation_path(annotation_path, id, side, camera_numbers, n_frame, annotation_format='.json'):
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(annotation_path, id+'up'+str(camera_numbers)+'_'+str(n_frame)+annotation_format))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(annotation_path, id+'down'+str(camera_numbers)+'_'+str(n_frame)+annotation_format))


def sheet_camera_path(main_path,id, side, camera_numbers):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, main_path = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'TOP', str(camera_numbers)))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'BOTTOM', str(camera_numbers)))

def sheet_path(main_path, id):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, main_path = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    return(os.path.join(main_path, year, month, day, str(id)))

def rename_sheet_folder(main_path, old_id, new_id):
    old_path = sheet_path(main_path, old_id)
    new_path = sheet_path(main_path, new_id)
    os.rename(old_path, new_path)

def create_sheet_suggestions_path(main_path, id):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, _ = db.load_sheet_date_mainpath(id)
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    sides = ['BOTTOM', 'TOP']
    cams = 12
    for side in sides:
        for cam in range(1, cams+1):
            path = os.path.join(main_path, year, month, day, str(id), side, str(cam))
            if not os.path.exists(path):
                os.makedirs(path)

def sheet_suggestions_json_path(main_path,id, side, camera_numbers, n_frame, format='.json'):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, _ = db.load_sheet_date_mainpath(id)
        main_path = db.get_suggestions_path()
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'TOP', str(camera_numbers), str(n_frame) + str(format) ))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'BOTTOM', str(camera_numbers), str(n_frame) + str(format)))
    
def sheet_suggestions_camera_path(main_path, id, side, camera_numbers):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, _ = db.load_sheet_date_mainpath(id)
        main_path = db.get_suggestions_path()
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    if 'top' in side.lower() or 'up' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'TOP', str(camera_numbers)))
    
    elif 'bot' in side.lower() or 'down' in side.lower():
        return(os.path.join(main_path, year, month, day, str(id), 'BOTTOM', str(camera_numbers)))

def sheet_suggestions_path(main_path, id):
    try:
        db = dataBaseUtils(ui_obj='Null')
        date, _ = db.load_sheet_date_mainpath(id)
        main_path = db.get_suggestions_path()
    except:
        date = date_funcs.get_date(persian=SHAMSI_DATE)
    year, month, day = date.split('/')
    return(os.path.join(main_path, year, month, day, str(id)))



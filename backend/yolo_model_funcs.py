from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
from PySide6.QtGui import Qt

from backend import colors_pallete, chart_funcs, date_funcs
import train_api, texts
import os
import json
from utils import Utils
from random_split import *

SHAMSI_DATE = False

# yolo table headers
yolo_headers = ['Algorithm Name', 'Pretrained weights Path', 'Input-Size', 'Input-Type',
                    'N-Epochs', 'Batch-Size', 'Learning-Rate',
                    'Split Ratio', 'Loss', 'Accuracy', 'IOU', 'FScore',
                    'Val-Loss', 'Val-Accuracy', 'Val-IOU', 'Val-FScore',
                    'Dataset Path', 'Weights Path', 'Date Created']
yolo_headers_fa = [
    "نام الگوریتم",
    "آدرس وزن‌های از پیش آموزش دیده",
    "اندازه ورودی",
    "نوع ورودی",
    "تعداد اپوک",
    "اندازه دسته",
    "نرخ یادگیری",
    "نسبت تقسیم داده",
    "خطا",
    "دقت",
    "IOU",
    "FScore",
    "خطا اعتبارسنجی",
    "دقت اعتبارسنجی",
    "اعتبارسنجی IOU",
    "اعتبارسنجی FScore",
    "آدرس مجموعه داده",
    "آدرس وزن‌ها",
    "تاریخ ایجاد",
]

# headers in database
yolo_headers_db = [
    'algo_name', 
    'input_size', 
    'input_type',               
    'epochs',
    'batch_size', 
    'split_ratio',
    'dataset_pathes',
    'weights_path',  
    'date_',
    'box_loss', 
    'obj_loss', 
    'cls_loss',
    'val_precision',
    'val_recall',
    'val_mAP_0.5',
    'val_mAP_0.5:0.95',
    'val_box_loss',
    'val_obj_loss',
    'val_cls_loss',
]

# table number of rows and cols
yolo_table_ncols = len(yolo_headers)
yolo_table_nrows = 20


# get yolo-models from database
def get_yolo_models_from_db(db_obj, count=False, limit_size=yolo_table_nrows, offset=0):
    """this function is used to get yolo models info list from database

    :param db_obj: database object
    :type db_obj: _type_
    :param count: a boolean determining whether to get count of table, defaults to False
    :type count: boolean, optional
    :param limit_size: number of returning rows from database, defaults to yolo_table_nrows
    :type limit_size: int, optional
    :param offset: start row index in table to return next n rows, defaults to 0
    :type offset: int, optional
    :return: list of yolo model info (in dict)
    :rtype: list of dicts
    """

    res, ymodels_list = db_obj.get_yolo_models(limit=True, count=count, limit_size=limit_size, offset=offset)
    return res, ymodels_list

# translate yolo model to id
def translate_yolo_algorithm_id_to_name(algo_id, reverse=False):
    """this function is used to translate yolo algorithm id to its name

    :param algo_id: algorithm id
    :type algo_id: int
    :param reverse: boolean to determine whether to translate name to id, defaults to False
    :type reverse: bool, optional
    :return: _description_
    :rtype: yolo algorithm name/id (by respect to reverse value)
    """

    if not reverse:
        return train_api.ALGORITHM_NAMES['yolo'][int(algo_id)]

    else:
        try:
            return train_api.ALGORITHM_NAMES['yolo'].index(algo_id)

        except:
            return -1

# show/set models history to UI tabel
def set_ymodels_on_ui_tabel(ui_obj, ymodels_list):
    """this function is used to set yolo models list on ui yolo models list (yolo history page)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param ymodels_list: list of yolo model params (in dict)
    :type ymodels_list: list of dicts
    """

    # definr table parameters
    ui_obj.yolo_history_tabel.resizeColumnsToContents()
    ui_obj.yolo_history_tabel.setColumnCount(yolo_table_ncols)

    if len(ymodels_list) != 0:
        ui_obj.yolo_history_tabel.setRowCount(yolo_table_nrows)
    else:
        ui_obj.yolo_history_tabel.setRowCount(0)

    ui_obj.yolo_history_tabel.verticalHeader().setVisible(True)
    # ui_obj.yolo_history_tabel.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.yolo_history_tabel.setHorizontalHeaderLabels(yolo_headers if ui_obj.language=='en' else yolo_headers_fa)

    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, ymodel in enumerate(ymodels_list):
        for col_idx in range(yolo_table_ncols):

            # translate algo-ids to name
            if col_idx == 0:
                ymodel[
                    yolo_headers_db[col_idx]
                ] = translate_yolo_algorithm_id_to_name(
                    algo_id=ymodel[yolo_headers_db[col_idx]]
                )
            if col_idx == 1:
                ymodel[
                    yolo_headers_db[col_idx]
                ] = '-' if ymodel[yolo_headers_db[col_idx]] == '' else ymodel[yolo_headers_db[col_idx]]
            if col_idx == 3:
                ymodel[
                    yolo_headers_db[col_idx]
                ] = 'Split' if ymodel[yolo_headers_db[col_idx]] == '1' else 'Resize'
            table_item = sQTableWidgetItem(str(ymodel[yolo_headers_db[col_idx]]))
            # set checkbox (only first col)
            # if col_idx == 0:
                # table_item.setFlags(
                #     sQtCore.Qt.ItemFlag.ItemIsUserCheckable 
                #     | sQtCore.Qt.ItemFlag.ItemIsEnabled
                # )
                # table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            table_item.setTextAlignment(Qt.AlignCenter)
            ui_obj.yolo_history_tabel.setItem(row_idx, col_idx, table_item)
    try:
        ui_obj.yolo_history_tabel.setRowCount(row_idx+1)
        
    except Exception as e:
        return

# add new model training info to database
def add_new_yolo_model_to_db(db_obj, new_ymodel_info):
    """this function is used to add a new yolo model params to dataabse

    :param db_obj: database object
    :type db_obj: _type_
    :param new_ymodel_info: model parameters
    :type new_ymodel_info: _type_
    :return: resault: boolean
    :rtype: boolean
    """

    res = db_obj.add_yolo_model_record(new_ymodel_info)
    return res


def save_new_yolo_model_record(ui_obj, db_obj, ymodel_records):
    """this functino is used to add new trained model parameters to database

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: databse object
    :type db_obj: _type_
    :param ymodel_records: model parameters
    :type ymodel_records: _type_
    :return: result
    :rtype: bool
    """

    # add
    if add_new_yolo_model_to_db(db_obj=db_obj, new_ymodel_info=ymodel_records):
        ui_obj.notif_manager.append_new_notif(
            message=texts.MESSEGES['database_add_ymodel'][ui_obj.language], level=1
        )
        return True

    else:
        ui_obj.notif_manager.append_new_notif(
            message=texts.ERRORS['database_add_ymodel_failed'][ui_obj.language], level=3
            )
        return False


# get yolo model information from UI filter section
def get_yolo_model_filter_info_from_ui(ui_obj):
    """this function is used to get filter params in yolo models list on UI

    :param ui_obj: main ui obj
    :type ui_obj: _type_
    :return: _description_
    :rtype: _type_
    """

    try: 
    # get params from UI
        ymodel_info = {}
        ymodel_info['algo_name'] = [translate_yolo_algorithm_id_to_name(algo_id=ui_obj.yolo_name_filter_combo.currentText(), reverse=True)]
        ymodel_info['epochs'] = [ui_obj.yolo_epoch_min_filter_lineedit.text(), ui_obj.yolo_epoch_max_filter_lineedit.text()]
        ymodel_info['batch_size'] = [ui_obj.yolo_batch_min_filter_lineedit.text(), ui_obj.yolo_batch_max_filter_lineedit.text()]
        ymodel_info['split_ratio'] = [ui_obj.yolo_split_min_filter_lineedit.text(), ui_obj.yolo_split_max_filter_lineedit.text()]
        ymodel_info['val_loss'] = [ui_obj.yolo_loss_min_filter_lineedit.text(), ui_obj.yolo_loss_max_filter_lineedit.text()]
        ymodel_info['val_accuracy'] = [ui_obj.yolo_acc_min_filter_lineedit.text(), ui_obj.yolo_acc_max_filter_lineedit.text()]
        ymodel_info['val_iou'] = [ui_obj.yolo_iou_min_filter_lineedit_2.text(), ui_obj.yolo_iou_max_filter_lineedit_2.text()]
        ymodel_info['val_fscore'] = [ui_obj.yolo_fscore_min_filter_lineedit.text(), ui_obj.yolo_fscore_max_filter_lineedit.text()]

        # date
        ymodel_info['start_date'] = [ui_obj.yolo_start_year_lineedit.text(), ui_obj.yolo_start_month_lineedit.text(), ui_obj.yolo_start_day_lineedit.text()]
        ymodel_info['end_date'] = [ui_obj.yolo_end_year_lineedit.text(), ui_obj.yolo_end_month_lineedit.text(), ui_obj.yolo_end_day_lineedit.text()]

        return ymodel_info
           
    except:
        ui_obj.logger.create_new_log(message=texts.ERRORS['ui_get_ymodel_filter_params_failed']['en'], level=5)
        return []
    

# get users from database
def get_filtered_yolo_models_from_db(ui_obj, db_obj, filter_params, limit_size=yolo_table_nrows, offset=0, count=False):
    """this function is used to get filtered yolo models from database using filter params

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param filter_params: filtering parameters
    :type filter_params: _type_
    :param limit_size: n returning rows from database, defaults to yolo_table_nrows
    :type limit_size: int, optional
    :param offset: starting row index to return n next rows, defaults to 0
    :type offset: int, optional
    :param count: boolean determining whther to get count of filtered rows, defaults to False
    :type count: bool, optional
    :return: _description_
    :rtype: _type_
    """

    # input parameters and column names in database
    params = []
    cols = []
    # add parameters and col names to build the input sql query

    # algo name
    if filter_params['algo_name'][0] != -1:
        params.append(filter_params['algo_name'])
        cols.append('algo_name')

    # epoch
    try:
        if filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '' and int(filter_params['epochs'][0]) > int(filter_params['epochs'][1]):
            ui_obj.set_warning(texts.ERRORS['EPOCH_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['epochs'][0] == '') ^ bool(filter_params['epochs'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['EPOCH_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '':
            params.append([str(int(filter_params['epochs'][0])), str(int(filter_params['epochs'][1]))])
            cols.append('epochs')
    except:
        ui_obj.set_warning(texts.ERRORS['EPOCH_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # batch-size
    try:
        if filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '' and int(filter_params['batch_size'][0]) > int(filter_params['batch_size'][1]):
            ui_obj.set_warning(texts.ERRORS['BATCHSIZE_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['batch_size'][0] == '') ^ bool(filter_params['batch_size'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['BATCHSIZE_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '':
            params.append([str(int(filter_params['batch_size'][0])), str(int(filter_params['batch_size'][1]))])
            cols.append('batch_size')
    except:
        ui_obj.set_warning(texts.ERRORS['BATCHSIZE_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # split ration
    try:
        if filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '' and float(filter_params['split_ratio'][0]) > float(filter_params['split_ratio'][1]):
            ui_obj.set_warning(texts.ERRORS['SPLITRATIO_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['split_ratio'][0] == '') ^ bool(filter_params['split_ratio'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['SPLITRATIO_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '':
            params.append([str(float(filter_params['split_ratio'][0])), str(float(filter_params['split_ratio'][1]))])
            cols.append('split_ratio')
    except:
        ui_obj.set_warning(texts.ERRORS['SPLITRATIO_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # loss
    try:
        if filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '' and float(filter_params['val_loss'][0]) > float(filter_params['val_loss'][1]):
            ui_obj.set_warning(texts.ERRORS['LOSS_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_loss'][0] == '') ^ bool(filter_params['val_loss'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['LOSS_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '':
            params.append([str(float(filter_params['val_loss'][0])), str(float(filter_params['val_loss'][1]))])
            cols.append('val_loss')
    except:
        ui_obj.set_warning(texts.ERRORS['LOSS_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # acc
    try:
        if filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '' and float(filter_params['val_accuracy'][0]) > float(filter_params['val_accuracy'][1]):
            ui_obj.set_warning(texts.ERRORS['ACCU_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_accuracy'][0] == '') ^ bool(filter_params['val_accuracy'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['ACCU_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '':
            params.append([str(float(filter_params['val_accuracy'][0])), str(float(filter_params['val_accuracy'][1]))])
            cols.append('val_accuracy')
    except:
        ui_obj.set_warning(texts.ERRORS['ACCU_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # precision
    try:
        if filter_params['val_iou'][0] != '' and filter_params['val_iou'][1] != '' and float(filter_params['val_iou'][0]) > float(filter_params['val_iou'][1]):
            ui_obj.set_warning(texts.ERRORS['IOU_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_iou'][0] == '') ^ bool(filter_params['val_iou'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['IOU_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['val_iou'][0] != '' and filter_params['val_iou'][1] != '':
            params.append([str(float(filter_params['val_iou'][0])), str(float(filter_params['val_iou'][1]))])
            cols.append('val_iou')
    except:
        ui_obj.set_warning(texts.ERRORS['IOU_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # recall
    try:
        if filter_params['val_fscore'][0] != '' and filter_params['val_fscore'][1] != '' and float(filter_params['val_fscore'][0]) > float(filter_params['val_fscore'][1]):
            ui_obj.set_warning(texts.ERRORS['FSCORE_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_fscore'][0] == '') ^ bool(filter_params['val_fscore'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['FSCORE_RANGE_EMPTY'][ui_obj.language], 'yolo_model_history', level=2)
            return 'error',[]
        elif filter_params['val_fscore'][0] != '' and filter_params['val_fscore'][1] != '':
            params.append([str(float(filter_params['val_fscore'][0])), str(float(filter_params['val_fscore'][1]))])
            cols.append('val_fscore')
    except:
        ui_obj.set_warning(texts.ERRORS['FSCORE_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
        return 'error',[]

    # date
    # start year
    if filter_params['start_date'][0] != '' or filter_params['start_date'][1] != '' or filter_params['start_date'][2] != ''\
        or filter_params['end_date'][0] != '' or filter_params['end_date'][1] != '' or filter_params['end_date'][2] != '':
        #
        year = int(date_funcs.get_date(persian=SHAMSI_DATE).split('/')[0])
        try:
            if int(filter_params['start_date'][0]) < year - 10 or int(filter_params['start_date'][0]) > year + 10:
                ui_obj.set_warning(texts.ERRORS['YEAR_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['YEAR_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        #start month
        try:
            if int(filter_params['start_date'][1]) < 1 or int(filter_params['start_date'][1]) > 12:
                ui_obj.set_warning(texts.ERRORS['MONTH_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['MONTH_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        #start day
        try:
            if int(filter_params['start_date'][2]) < 1 or int(filter_params['start_date'][2]) > 31:
                ui_obj.set_warning(texts.ERRORS['DAY_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['DAY_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        #
        # end year
        try:
            if int(filter_params['end_date'][0]) < year - 10 or int(filter_params['end_date'][0]) > year + 10:
                ui_obj.set_warning(texts.ERRORS['YEAR_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['YEAR_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        #start month
        try:
            if int(filter_params['end_date'][1]) < 1 or int(filter_params['end_date'][1]) > 12:
                ui_obj.set_warning(texts.ERRORS['MONTH_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['MONTH_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        #start day
        try:
            if int(filter_params['end_date'][2]) < 1 or int(filter_params['end_date'][2]) > 31:
                ui_obj.set_warning(texts.ERRORS['DAY_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['DAY_FORMAT_INVALID'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error',[]
        #
        try:
            if len(filter_params['start_date'][1]) < 2:
                filter_params['start_date'][1] = '0' + filter_params['start_date'][1]
            if len(filter_params['start_date'][2]) < 2:
                filter_params['start_date'][2] = '0' + filter_params['start_date'][2]
            if len(filter_params['end_date'][1]) < 2:
                filter_params['end_date'][1] = '0' + filter_params['end_date'][1]
            if len(filter_params['end_date'][2]) < 2:
                filter_params['end_date'][2] = '0' + filter_params['end_date'][2]
            #
            start_date = filter_params['start_date'][0] + '/' + filter_params['start_date'][1] + '/' + filter_params['start_date'][2]
            end_date = filter_params['end_date'][0] + '/' + filter_params['end_date'][1] + '/' + filter_params['end_date'][2]
            if start_date > end_date:
                ui_obj.set_warning(texts.ERRORS['DATE_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
                return 'error', []
            else:
                params.append(['"'+start_date+'"', '"'+end_date+'"'])
                cols.append('date_')

        except:
            ui_obj.set_warning(texts.ERRORS['DATE_RANGE_INCORRECT'][ui_obj.language], 'yolo_model_history', level=3)
            return 'error', []


    # check not wmpty
    if len(params) == 0 or len(cols) == 0:
        return 'all', []
    

    # get from db
    try:
        res, defects_list = db_obj.search_yolo_model_by_filter(parms=params, cols=cols, limit=True, limit_size=limit_size, offset=offset, count=count)
        if res:
            return 'filtered', defects_list
        
        else:
            ui_obj.notif_manager.append_new_notif(message=texts.ERRORS['database_get_ymodels_failed'][ui_obj.language], level=4)
            return 'error', []
    
    except:
        return []


def class_to_id(db_obj):
    ids = db_obj.get_defects_id()
    return dict(zip(ids, range(len(ids))))


def id_to_class(db_obj):
    ids = db_obj.get_defects_id()
    return dict(zip(range(len(ids)), ids))

class Yolo_model_train_worker(sQObject):
    """this class is worker for yolo model training Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()
    warning = sSignal(str, str, str, int)
    reset_progressbar = sSignal(int , str)
    set_progressbar = sSignal()
    update_charts = sSignal(int, dict)

    def assign_parameters(self, y_parms, api_obj, ui_obj, db_obj, ds_obj):
        self.y_parms = y_parms
        self.api_obj = api_obj
        self.ui_obj = ui_obj
        self.db_obj = db_obj
        self.ds_obj = ds_obj

    def annotation_to_yolo(self, annotation, size):
        self.class_name_to_id_mapping = class_to_id(self.db_obj)
        text = ''
        for b in annotation["obj_masks"]:
            class_id = self.class_name_to_id_mapping[b["class"]]
            
            xmin, ymin, w, h = cv2.boundingRect(np.array(b['mask']))
            xmax = xmin + w
            ymax = ymin + h
            b_center_x = (xmin + xmax) / 2 
            b_center_y = (ymin + ymax) / 2
            b_width    = (xmax - xmin)
            b_height   = (ymax - ymin)

            image_h, image_w = size
            b_center_x /= image_w 
            b_center_y /= image_h 
            b_width    /= image_w 
            b_height   /= image_h

            text += "{} {:.3f} {:.3f} {:.3f} {:.3f}".format(class_id, b_center_x, b_center_y, b_width, b_height)
            text += '\n'

        return text

    def split_yolo_dataset(self, paths, size):
        for i, path in enumerate(paths):
            if self.ds_obj.check_yolo_dataset(path):
                self.ds_obj.create_y_split_folder(path)

                s_label = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_label)
                s_image = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_image)
                s_annotaions = os.path.join(path, self.ds_obj.annotations_folder)
                d_label = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_label_splitted)
                d_image = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_image_splitted)
                d_annotation = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_annotations)
                imgs = os.listdir(s_image)
                self.reset_progressbar.emit(len(imgs), 'Splitting dataset {}'.format(i+1))
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_image, i), color="color")
                    label = Utils.read_image(os.path.join(s_label, i), color="color")
                    annotation_path = os.path.join(s_annotaions, i.replace(i.split('.')[-1], 'json'))
                    if img is None or label is None or not os.path.exists(annotation_path):
                        continue
                    with open(annotation_path) as f:
                        annotation = json.load(f)

                    image_crops, label_crops, crops_annotations = get_crops_random(img, label, size, annotation)
                    crops_yolo_text = list(map(self.annotation_to_yolo, crops_annotations, [size]*len(crops_annotations)))
                    self.ds_obj.save_yolo_splits(
                        image_crops, label_crops, crops_yolo_text, d_image, d_label, d_annotation, name=i.split(".")[0]
                    )
                    self.set_progressbar.emit()
            else:
                self.warning.emit(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], "y_train", None, 2
                )
                return

    def resize_yolo_dataset(self, paths):
        for i, path in enumerate(paths):
            if self.ds_obj.check_yolo_dataset(path):
                self.ds_obj.create_y_split_folder(path, ann=True)
                s_image = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_image)
                s_annotaions = os.path.join(path, self.ds_obj.annotations_folder)
                d_annotation = os.path.join(path, self.ds_obj.localization_folder, self.ds_obj.localization_folder_annotations)
                imgs = os.listdir(s_image)
                self.reset_progressbar.emit(len(imgs), 'Resizing dataset {}'.format(i+1))
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_image, i), color="color")
                    annotation_path = os.path.join(s_annotaions, i.replace(i.split('.')[-1], 'json'))
                    if img is None or not os.path.exists(annotation_path):
                        continue
                    with open(annotation_path) as f:
                        annotation = json.load(f)
                    yolo_text = self.annotation_to_yolo(annotation, (img.shape[0], img.shape[1]))
                    self.ds_obj.save_yolo_resizes(yolo_text, d_annotation, name=i.split(".")[0])

                    self.set_progressbar.emit()

    def train_model(self):
        if self.y_parms[2]:
            self.split_yolo_dataset(self.y_parms[-1], self.y_parms[1])
        else:
            self.resize_yolo_dataset(self.y_parms[-1])
        
        self.reset_progressbar.emit(self.y_parms[3], 'Training')
        ymodel_records = train_api.train_yolo(
            *self.y_parms, self.api_obj.ds.weights_yolo_path, self.class_name_to_id_mapping, self.api_obj
        )
        if not ymodel_records[0]:
            self.warning.emit(ymodel_records[1][0], ymodel_records[1][1], None, ymodel_records[1][2])
        else:
            ymodel_records = ymodel_records[1]
            if ymodel_records:
                # notif
                self.ui_obj.notif_manager.append_new_notif(
                    message=texts.MESSEGES['ymodel_trained'][self.ui_obj.language], level=1
                )

                # add record to database
                self.api_obj.ymodel_train_result = save_new_yolo_model_record(
                    ui_obj=self.ui_obj, db_obj=self.db_obj, ymodel_records=ymodel_records
                )

                if self.api_obj.ymodel_train_result:
                    self.warning.emit(texts.MESSEGES['train_successfuly'][self.api_obj.language], 'y_train', None, 1)
                else:
                    self.warning.emit(texts.ERRORS['database_add_ymodel_failed'][self.api_obj.language], 'y_train', None, 3)

        self.finished.emit()

    def assign_new_value_to_yolo_chart(self, last_epoch, logs):
        self.set_progressbar.emit()
        self.update_charts.emit(last_epoch, logs)
       
    def save_y_model(self, model, path, epoch):
        try:
            model.save(path)
            self.ui_obj.logger.create_new_log(message=texts.MESSEGES['SAVE_YMODEL_EPOCH']['en'].format(epoch))
        except:
            self.ui_obj.logger.create_new_log(message=texts.ERRORS['SAVE_YMODEL_EPOCH_FAILED']['en'].format(epoch), level=5)
            self.warning.emit(texts.ERRORS['SAVE_YMODEL_EPOCH_FAILED'][self.api_obj.language].format(epoch), 'y_train', None, 3)
    
    def show_ymodel_train_result(self):
        self.reset_progressbar.emit(1, '')
        self.ui_obj.yolo_train.setEnabled(True)
        self.api_obj.runing_y_model=False
        return

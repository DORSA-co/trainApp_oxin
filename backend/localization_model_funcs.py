from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal

from backend import colors_pallete
import train_api, texts

# localization table headers
localization_headers = ['Algorithm', 'Input-Size', 'Input-Type',
                    'N-Epochs', 'Batch-Size', 'Learning-Rate',
                    'Split Ratio', 'Loss', 'Accuracy', 'Precision', 'Recall',
                    'Val-Loss', 'Val-Accuracy', 'Val-Precision', 'Val-Recall',
                    'Dataset Path', 'Weights Path', 'Date Created']
localization_headers_fa = [
    "نام الگوریتم",
    "اندازه ورودی",
    "نوع ورودی",
    "تعداد اپوک",
    "اندازه دسته",
    "نرخ یادگیری",
    "نسبت تقسیم داده",
    "Loss",
    "Accuracy",
    "Precision",
    "Recall",
    "اعتبارسنجی Loss",
    "اعتبارسنجی Accuracy",
    "اعتبارسنجی Precision",
    "اعتبارسنجی Recall",
    "آدرس مجموعه داده",
    "آدرس وزن ها",
    "تاریخ ایجاد",
]

# headers in database
localization_headers_db = ['algo_name', 'input_size', 'input_type',
                    'epochs', 'batch_size', 'lr',
                    'split_ratio', 'loss', 'accuracy', 'precision_', 'recall',
                    'val_loss', 'val_accuracy', 'val_precision', 'val_recall',
                    'dataset_pathes', 'weights_path', 'date_']

# table number of rows and cols
localization_table_ncols = len(localization_headers)
localization_table_nrows = 20


# get localization-models from database
def get_localization_models_from_db(db_obj, count=False, limit_size=localization_table_nrows, offset=0):
    """this function is used to get localization models info list from database

    :param db_obj: database object
    :type db_obj: _type_
    :param count: a boolean determining whether to get count of table, defaults to False
    :type count: boolean, optional
    :param limit_size: number of returning rows from database, defaults to localization_table_nrows
    :type limit_size: int, optional
    :param offset: start row index in table to return next n rows, defaults to 0
    :type offset: int, optional
    :return: list of localization model info (in dict)
    :rtype: list of dicts
    """

    res, lmodels_list = db_obj.get_localization_models(limit=True, count=count, limit_size=limit_size, offset=offset)
    return res, lmodels_list

# translate localization model to id
def translate_localization_algorithm_id_to_name(algo_id, reverse=False):
    """this function is used to translate localization algorithm id to its name

    :param algo_id: algorithm id
    :type algo_id: int
    :param reverse: boolean to determine whether to translate name to id, defaults to False
    :type reverse: bool, optional
    :return: _description_
    :rtype: localization algorithm name/id (by respect to reverse value)
    """

    if not reverse:
        return train_api.ALGORITHM_NAMES['localization'][int(algo_id)]

    else:
        try:
            return train_api.ALGORITHM_NAMES['localization'].index(algo_id)

        except:
            return -1

# show/set models history to UI tabel
def set_lmodels_on_ui_tabel(ui_obj, lmodels_list):
    """this function is used to set localization models list on ui localization models list (localization history page)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param lmodels_list: list of localization model params (in dict)
    :type lmodels_list: list of dicts
    """

    # definr table parameters
    ui_obj.localization_history_tabel.resizeColumnsToContents()
    ui_obj.localization_history_tabel.setColumnCount(localization_table_ncols)

    if len(lmodels_list) != 0:
        ui_obj.localization_history_tabel.setRowCount(localization_table_nrows)
    else:
        ui_obj.localization_history_tabel.setRowCount(0)

    ui_obj.localization_history_tabel.verticalHeader().setVisible(True)
    # ui_obj.localization_history_tabel.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.localization_history_tabel.setHorizontalHeaderLabels(localization_headers if ui_obj.language=='en' else localization_headers_fa)

    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, lmodel in enumerate(lmodels_list):
        for col_idx in range(localization_table_ncols):

            # translate algo-ids to name
            if col_idx == 0:
                lmodel[localization_headers_db[col_idx]] = translate_localization_algorithm_id_to_name(algo_id=lmodel[localization_headers_db[col_idx]])
            table_item = sQTableWidgetItem(str(lmodel[localization_headers_db[col_idx]]))
            # set checkbox (only first col)
            if col_idx == 0:
                table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
                table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            ui_obj.localization_history_tabel.setItem(row_idx, col_idx, table_item)
    try:
        ui_obj.localization_history_tabel.setRowCount(row_idx+1)
        
    except Exception as e:
        return

# add new model training info to database
def add_new_localization_model_to_db(db_obj, new_lmodel_info):
    """this function is used to add a new localization model params to dataabse

    :param db_obj: database object
    :type db_obj: _type_
    :param new_lmodel_info: model parameters
    :type new_lmodel_info: _type_
    :return: resault: boolean
    :rtype: boolean
    """

    res = db_obj.add_localization_model_record(new_lmodel_info)
    return res


def save_new_localization_model_record(ui_obj, db_obj, lmodel_records):
    """this functino is used to add new trained model parameters to database

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: databse object
    :type db_obj: _type_
    :param lmodel_records: model parameters
    :type lmodel_records: _type_
    :return: result
    :rtype: bool
    """

    # add
    if add_new_localization_model_to_db(db_obj=db_obj, new_lmodel_info=lmodel_records):
        ui_obj.notif_manager.append_new_notif(message=texts.MESSEGES['database_add_lmodel'][ui_obj.language], level=1)
        return True

    else:
        ui_obj.notif_manager.append_new_notif(message=texts.ERRORS['database_add_lmodel_failed'][ui_obj.language], level=3)
        return False


# get localization model information from UI filter section
def get_localization_model_filter_info_from_ui(ui_obj):
    """this function is used to get filter params in localization models list on UI

    :param ui_obj: main ui obj
    :type ui_obj: _type_
    :return: _description_
    :rtype: _type_
    """

    try: 
    # get params from UI
        lmodel_info = {}
        lmodel_info['algo_name'] = [translate_localization_algorithm_id_to_name(algo_id=ui_obj.localization_name_filter_combo.currentText(), reverse=True)]
        lmodel_info['epochs'] = [ui_obj.localization_epoch_min_filter_lineedit.text(), ui_obj.localization_epoch_max_filter_lineedit.text()]
        lmodel_info['batch_size'] = [ui_obj.localization_batch_min_filter_lineedit.text(), ui_obj.localization_batch_max_filter_lineedit.text()]
        lmodel_info['split_ratio'] = [ui_obj.localization_split_min_filter_lineedit.text(), ui_obj.localization_split_max_filter_lineedit.text()]
        lmodel_info['val_loss'] = [ui_obj.localization_loss_min_filter_lineedit.text(), ui_obj.localization_loss_max_filter_lineedit.text()]
        lmodel_info['val_accuracy'] = [ui_obj.localization_acc_min_filter_lineedit.text(), ui_obj.localization_acc_max_filter_lineedit.text()]
        lmodel_info['val_precision'] = [ui_obj.localization_prec_min_filter_lineedit.text(), ui_obj.localization_prec_max_filter_lineedit.text()]
        lmodel_info['val_recall'] = [ui_obj.localization_rec_min_filter_lineedit.text(), ui_obj.localization_rec_max_filter_lineedit.text()]

        # date
        lmodel_info['start_date'] = [ui_obj.localization_start_year_lineedit.text(), ui_obj.localization_start_month_lineedit.text(), ui_obj.localization_start_day_lineedit.text()]
        lmodel_info['end_date'] = [ui_obj.localization_end_year_lineedit.text(), ui_obj.localization_end_month_lineedit.text(), ui_obj.localization_end_day_lineedit.text()]

        return lmodel_info
           
    except:
        ui_obj.logger.create_new_log(message=texts.ERRORS['ui_get_lmodel_filter_params_failed']['en'], level=5)
        return []
    

# get users from database
def get_filtered_localization_models_from_db(ui_obj, db_obj, filter_params, limit_size=localization_table_nrows, offset=0, count=False):
    """this function is used to get filtered localization models from database using filter params

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param filter_params: filtering parameters
    :type filter_params: _type_
    :param limit_size: n returning rows from database, defaults to localization_table_nrows
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
            ui_obj.set_warning(texts.ERRORS['EPOCH_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['epochs'][0] == '') ^ bool(filter_params['epochs'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['EPOCH_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '':
            params.append([str(int(filter_params['epochs'][0])), str(int(filter_params['epochs'][1]))])
            cols.append('epochs')
    except:
        ui_obj.set_warning(texts.ERRORS['EPOCH_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # batch-size
    try:
        if filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '' and int(filter_params['batch_size'][0]) > int(filter_params['batch_size'][1]):
            ui_obj.set_warning(texts.ERRORS['BATCHSIZE_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['batch_size'][0] == '') ^ bool(filter_params['batch_size'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['BATCHSIZE_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '':
            params.append([str(int(filter_params['batch_size'][0])), str(int(filter_params['batch_size'][1]))])
            cols.append('batch_size')
    except:
        ui_obj.set_warning(texts.ERRORS['BATCHSIZE_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # split ration
    try:
        if filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '' and float(filter_params['split_ratio'][0]) > float(filter_params['split_ratio'][1]):
            ui_obj.set_warning(texts.ERRORS['SPLITRATIO_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['split_ratio'][0] == '') ^ bool(filter_params['split_ratio'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['SPLITRATIO_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '':
            params.append([str(float(filter_params['split_ratio'][0])), str(float(filter_params['split_ratio'][1]))])
            cols.append('split_ratio')
    except:
        ui_obj.set_warning(texts.ERRORS['SPLITRATIO_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # loss
    try:
        if filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '' and float(filter_params['val_loss'][0]) > float(filter_params['val_loss'][1]):
            ui_obj.set_warning(texts.ERRORS['LOSS_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_loss'][0] == '') ^ bool(filter_params['val_loss'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['LOSS_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '':
            params.append([str(float(filter_params['val_loss'][0])), str(float(filter_params['val_loss'][1]))])
            cols.append('val_loss')
    except:
        ui_obj.set_warning(texts.ERRORS['LOSS_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # acc
    try:
        if filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '' and float(filter_params['val_accuracy'][0]) > float(filter_params['val_accuracy'][1]):
            ui_obj.set_warning(texts.ERRORS['ACCU_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_accuracy'][0] == '') ^ bool(filter_params['val_accuracy'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['ACCU_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '':
            params.append([str(float(filter_params['val_accuracy'][0])), str(float(filter_params['val_accuracy'][1]))])
            cols.append('val_accuracy')
    except:
        ui_obj.set_warning(texts.ERRORS['ACCU_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # precision
    try:
        if filter_params['val_precision'][0] != '' and filter_params['val_precision'][1] != '' and float(filter_params['val_precision'][0]) > float(filter_params['val_precision'][1]):
            ui_obj.set_warning(texts.ERRORS['PREC_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_precision'][0] == '') ^ bool(filter_params['val_precision'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['PREC_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['val_precision'][0] != '' and filter_params['val_precision'][1] != '':
            params.append([str(float(filter_params['val_precision'][0])), str(float(filter_params['val_precision'][1]))])
            cols.append('val_precision')
    except:
        ui_obj.set_warning(texts.ERRORS['PREC_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # recall
    try:
        if filter_params['val_recall'][0] != '' and filter_params['val_recall'][1] != '' and float(filter_params['val_recall'][0]) > float(filter_params['val_recall'][1]):
            ui_obj.set_warning(texts.ERRORS['RECA_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        elif bool(filter_params['val_recall'][0] == '') ^ bool(filter_params['val_recall'][1] == ''):
            ui_obj.set_warning(texts.WARNINGS['RECA_RANGE_EMPTY'][ui_obj.language], 'localization_model_history', level=2)
            return 'error',[]
        elif filter_params['val_recall'][0] != '' and filter_params['val_recall'][1] != '':
            params.append([str(float(filter_params['val_recall'][0])), str(float(filter_params['val_recall'][1]))])
            cols.append('val_recall')
    except:
        ui_obj.set_warning(texts.ERRORS['RECA_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
        return 'error',[]

    # date
    #start year
    if filter_params['start_date'][0] != '' or filter_params['start_date'][1] != '' or filter_params['start_date'][2] != ''\
        or filter_params['end_date'][0] != '' or filter_params['end_date'][1] != '' or filter_params['end_date'][2] != '':
        #
        try:
            if int(filter_params['start_date'][0]) < 1402 or int(filter_params['start_date'][0]) > 1500:
                ui_obj.set_warning(texts.ERRORS['YEAR_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['YEAR_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        #start month
        try:
            if int(filter_params['start_date'][1]) < 1 or int(filter_params['start_date'][1]) > 12:
                ui_obj.set_warning(texts.ERRORS['MONTH_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['MONTH_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        #start day
        try:
            if int(filter_params['start_date'][2]) < 1 or int(filter_params['start_date'][2]) > 31:
                ui_obj.set_warning(texts.ERRORS['DAY_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['DAY_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        #
        # end year
        try:
            if int(filter_params['end_date'][0]) < 1402 or int(filter_params['end_date'][0]) > 1500:
                ui_obj.set_warning(texts.ERRORS['YEAR_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['YEAR_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        #start month
        try:
            if int(filter_params['end_date'][1]) < 1 or int(filter_params['end_date'][1]) > 12:
                ui_obj.set_warning(texts.ERRORS['MONTH_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['MONTH_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
            return 'error',[]
        #start day
        try:
            if int(filter_params['end_date'][2]) < 1 or int(filter_params['end_date'][2]) > 31:
                ui_obj.set_warning(texts.ERRORS['DAY_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error',[]
        except:
            ui_obj.set_warning(texts.ERRORS['DAY_FORMAT_INVALID'][ui_obj.language], 'localization_model_history', level=3)
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
                ui_obj.set_warning(texts.ERRORS['DATE_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
                return 'error', []
            else:
                params.append(['"'+start_date+'"', '"'+end_date+'"'])
                cols.append('date_')

        except:
            ui_obj.set_warning(texts.ERRORS['DATE_RANGE_INCORRECT'][ui_obj.language], 'localization_model_history', level=3)
            return 'error', []


    # check not wmpty
    if len(params) == 0 or len(cols) == 0:
        return 'all', []
    

    # get from db
    try:
        res, defects_list = db_obj.search_localization_model_by_filter(parms=params, cols=cols, limit=True, limit_size=limit_size, offset=offset, count=count)
        if res:
            return 'filtered', defects_list
        
        else:
            ui_obj.notif_manager.append_new_notif(message=texts.ERRORS['database_get_bmodels_failed'][ui_obj.language], level=4)
            return 'error', []
    
    except:
        return []


class Localization_model_train_worker(sQObject):
    """this class is worker for localization model training Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()

    def assign_parameters(self, l_parms, api_obj, ui_obj, db_obj):
        self.l_parms = l_parms
        self.api_obj = api_obj
        self.ui_obj = ui_obj
        self.db_obj = db_obj


    def train_model(self):
        lmodel_records = train_api.train_localization(*self.l_parms, self.api_obj.ds.weights_localization_path, self.api_obj)
        if lmodel_records:
            # notif
            self.ui_obj.notif_manager.append_new_notif(message=texts.MESSEGES['lmodel_trained'][self.ui_obj.language], level=1)

            # add record to database
            self.api_obj.lmodel_train_result = save_new_localization_model_record(ui_obj=self.ui_obj, db_obj=self.db_obj, lmodel_records=lmodel_records)
        self.finished.emit()

       
    def show_lmodel_train_result(self):
        return
from itertools import count
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from pyparsing import col

from backend import colors_pallete
# import train_api


# table number of rows and cols
binary_headers = ['Algorithm', 'Input-Size', 'Input-Type',
                    'N-Epochs', 'N-Tuning Epochs', 'Batch-Size', 'Learning-Rate',
                    'Split Ratio', 'Loss', 'Accuracy', 'Precision', 'Recall',
                    'Val-Loss', 'Val-Accuracy', 'Val-Precision', 'Val-Recall',
                    'Dataset Path', 'Weights Path', 'Date Created']
#
binary_headers_db = ['algo_name', 'input_size', 'input_type',
                    'epochs', 'tuning_epochs', 'batch_size', 'lr',
                    'split_ratio', 'loss', 'accuracy', 'precision_', 'recall',
                    'val_loss', 'val_accuracy', 'val_precision', 'val_recall',
                    'dataset_pathes', 'weights_path', 'date_']

binary_table_ncols = len(binary_headers)
binary_table_nrows = 20








#table binary ----------------------------------------

# show/set models history to UI tabel
def set_header_binary_on_ui_tabel(ui_obj, bmodels_list):
    # definr table parameters
    ui_obj.binary_history_tabel.resizeColumnsToContents()
    ui_obj.binary_history_tabel.setColumnCount(binary_table_ncols)
    if len(bmodels_list) != 0:
        ui_obj.binary_history_tabel.setRowCount(binary_table_nrows)
    else:
        ui_obj.binary_history_tabel.setRowCount(0)
    ui_obj.binary_history_tabel.verticalHeader().setVisible(True)
    ui_obj.binary_history_tabel.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.binary_history_tabel.setHorizontalHeaderLabels(binary_headers)
    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, bmodel in enumerate(bmodels_list):
        for col_idx in range(binary_table_ncols):
            # translate algo-ids to name
            if col_idx == 0:
                bmodel[binary_headers_db[col_idx]] = translate_binary_algorithm_id_to_name(algo_id=bmodel[binary_headers_db[col_idx]])
            table_item = sQTableWidgetItem(str(bmodel[binary_headers_db[col_idx]]))
            # set checkbox (only first col)
            if col_idx == 0:
                table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
                table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            ui_obj.binary_history_tabel.setItem(row_idx, col_idx, table_item)

    try:
        ui_obj.binary_history_tabel.setRowCount(row_idx+1)
    except:
        return













# get binary-models from database
def get_binary_models_from_db(db_obj, count=False, limit_size=binary_table_nrows, offset=0):
    bmodels_list = db_obj.get_binary_models(limit=True, count=count, limit_size=limit_size, offset=offset)
    return bmodels_list


# translate binary model to id
def translate_binary_algorithm_id_to_name(algo_id, reverse=False):
    if not reverse:
        return train_api.ALGORITHM_NAMES['binary'][algo_id]
    else:
        try:
            return train_api.ALGORITHM_NAMES['binary'].index(algo_id)
        except:
            return -1


# show/set models history to UI tabel
def set_bmodels_on_ui_tabel(ui_obj, bmodels_list):
    # definr table parameters
    ui_obj.binary_history_tabel.resizeColumnsToContents()
    ui_obj.binary_history_tabel.setColumnCount(binary_table_ncols)
    if len(bmodels_list) != 0:
        ui_obj.binary_history_tabel.setRowCount(binary_table_nrows)
    else:
        ui_obj.binary_history_tabel.setRowCount(0)
    ui_obj.binary_history_tabel.verticalHeader().setVisible(True)
    ui_obj.binary_history_tabel.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.binary_history_tabel.setHorizontalHeaderLabels(binary_headers)
    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, bmodel in enumerate(bmodels_list):
        for col_idx in range(binary_table_ncols):
            # translate algo-ids to name
            if col_idx == 0:
                bmodel[binary_headers_db[col_idx]] = translate_binary_algorithm_id_to_name(algo_id=bmodel[binary_headers_db[col_idx]])
            table_item = sQTableWidgetItem(str(bmodel[binary_headers_db[col_idx]]))
            # set checkbox (only first col)
            if col_idx == 0:
                table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
                table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            ui_obj.binary_history_tabel.setItem(row_idx, col_idx, table_item)

    try:
        ui_obj.binary_history_tabel.setRowCount(row_idx+1)
    except:
        return


# add new model training info to database
def add_new_binary_model_to_db(db_obj, new_bmodel_info):
    res = db_obj.add_binary_model_record(new_bmodel_info)
    return res


# add new defect
def save_new_binary_model_record(ui_obj, db_obj, bmodel_records):
    # # change defect-name to id
    # new_defect_info = defect_management_funcs.change_defect_group_id_to_name(db_obj=self.db, defects_list=new_defect_info, reverse=True)
    # add defect to database
    if add_new_binary_model_to_db(db_obj=db_obj, new_bmodel_info=bmodel_records) == 'True':
        # alert
        ui_obj.create_alert_message(title='Training Result', message='Model is Successfully Trained, Records are Saved to History')

    else:
        ui_obj.create_alert_message(title='Training Result', message='Failed to Save Model Records to History')


# get binary model information from UI filter section
def get_binary_model_filter_info_from_ui(ui_obj):
    try: 
    # get params from UI
        bmodel_info = {}
        bmodel_info['algo_name'] = [translate_binary_algorithm_id_to_name(algo_id=ui_obj.binary_name_filter_combo.currentText(), reverse=True)]
        bmodel_info['epochs'] = [ui_obj.binary_epoch_min_filter_lineedit.text(), ui_obj.binary_epoch_max_filter_lineedit.text()]
        bmodel_info['tuning_epochs'] = [ui_obj.binary_tepoch_min_filter_lineedit.text(), ui_obj.binary_tepoch_max_filter_lineedit.text()]
        bmodel_info['batch_size'] = [ui_obj.binary_batch_min_filter_lineedit.text(), ui_obj.binary_batch_max_filter_lineedit.text()]
        bmodel_info['split_ratio'] = [ui_obj.binary_split_min_filter_lineedit.text(), ui_obj.binary_split_max_filter_lineedit.text()]
        bmodel_info['val_loss'] = [ui_obj.binary_loss_min_filter_lineedit.text(), ui_obj.binary_loss_max_filter_lineedit.text()]
        bmodel_info['val_accuracy'] = [ui_obj.binary_acc_min_filter_lineedit.text(), ui_obj.binary_acc_max_filter_lineedit.text()]
        bmodel_info['val_precision'] = [ui_obj.binary_prec_min_filter_lineedit.text(), ui_obj.binary_prec_max_filter_lineedit.text()]
        bmodel_info['val_recall'] = [ui_obj.binary_rec_min_filter_lineedit.text(), ui_obj.binary_rec_max_filter_lineedit.text()]
        bmodel_info['date_'] = [ui_obj.binary_date_min_filter_lineedit.text(), ui_obj.binary_date_max_filter_lineedit.text()]
        return bmodel_info
           
    except:
        return []
    

# get users from database
def get_filtered_binary_models_from_db(ui_obj, db_obj, filter_params, limit_size=binary_table_nrows, offset=0, count=False):
    # input parameters and column names in database
    params = []
    cols = []
    # add parameters and col names to build the input sql query
    if filter_params['algo_name'][0] != -1:
        params.append(filter_params['algo_name'])
        cols.append('algo_name')
    #
    if filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '' and int(filter_params['epochs'][0]) > int(filter_params['epochs'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Epoch Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['epochs'][0] == '') ^ bool(filter_params['epochs'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Epoch Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '':
        params.append(filter_params['epochs'])
        cols.append('epochs')
    #
    if filter_params['tuning_epochs'][0] != '' and filter_params['tuning_epochs'][1] != '' and int(filter_params['tuning_epochs'][0]) > int(filter_params['tuning_epochs'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Tunning Epoch Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['tuning_epochs'][0] == '') ^ bool(filter_params['tuning_epochs'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Tunning Epoch Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['tuning_epochs'][0] != '' and filter_params['tuning_epochs'][1] != '':
        params.append(filter_params['tuning_epochs'])
        cols.append('tuning_epochs')
    #
    if filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '' and int(filter_params['batch_size'][0]) > int(filter_params['batch_size'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Batch-Size Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['batch_size'][0] == '') ^ bool(filter_params['batch_size'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Batch-Size Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '':
        params.append(filter_params['batch_size'])
        cols.append('batch_size')
    #
    if filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '' and int(filter_params['split_ratio'][0]) > int(filter_params['split_ratio'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Split_Ratio Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['split_ratio'][0] == '') ^ bool(filter_params['split_ratio'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Split_Ratio Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '':
        params.append(filter_params['split_ratio'])
        cols.append('split_ratio')
    #
    if filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '' and int(filter_params['val_loss'][0]) > int(filter_params['val_loss'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Loss Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_loss'][0] == '') ^ bool(filter_params['val_loss'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Loss Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '':
        params.append(filter_params['val_loss'])
        cols.append('val_loss')
    #
    if filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '' and int(filter_params['val_accuracy'][0]) > int(filter_params['val_accuracy'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Accuracy Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_accuracy'][0] == '') ^ bool(filter_params['val_accuracy'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Accuracy Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '':
        params.append(filter_params['val_accuracy'])
        cols.append('val_accuracy')
    #
    if filter_params['val_precision'][0] != '' and filter_params['val_precision'][1] != '' and int(filter_params['val_precision'][0]) > int(filter_params['val_precision'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Precision Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_precision'][0] == '') ^ bool(filter_params['val_precision'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Precision Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_precision'][0] != '' and filter_params['val_precision'][1] != '':
        params.append(filter_params['val_precision'])
        cols.append('val_precision')
    #
    if filter_params['val_recall'][0] != '' and filter_params['val_recall'][1] != '' and int(filter_params['val_recall'][0]) > int(filter_params['val_recall'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Recall Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_recall'][0] == '') ^ bool(filter_params['val_recall'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.binary_tabel_label, text='Recall Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_recall'][0] != '' and filter_params['val_recall'][1] != '':
        params.append(filter_params['val_recall'])
        cols.append('val_recall')
    #
    # #print('-----------------------------------------------------------')
    # #print('params:', params)
    # #print('cols:', cols)
    # #print('-----------------------------------------------------------')
    # return
    
    # check not wmpty
    if len(params) == 0 or len(cols) == 0:
        return 'all', []
    

    # get from db
    try:
        defects_list = db_obj.search_binary_model_by_filter(parms=params, cols=cols, limit=True, limit_size=limit_size, offset=offset, count=count)
        return 'filtered', defects_list
    
    except:
        return []





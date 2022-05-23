from itertools import count
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from pyparsing import col

from backend import colors_pallete
import train_api


# table number of rows and cols
cls_headers = ['Algorithm', 'Input-Size', 'Input-Type', 'Classes',
                    'N-Epochs', 'N-Tuning Epochs', 'Batch-Size', 'Learning-Rate',
                    'Split Ratio', 'Loss', 'Accuracy', 'Precision', 'Recall',
                    'Val-Loss', 'Val-Accuracy', 'Val-Precision', 'Val-Recall',
                    'Dataset Path', 'Weights Path', 'Date Created']
#
cls_headers_db = ['algo_name', 'input_size', 'input_type', 'classes',
                    'epochs', 'tuning_epochs', 'batch_size', 'lr',
                    'split_ratio', 'loss', 'accuracy', 'precision_', 'recall',
                    'val_loss', 'val_accuracy', 'val_precision', 'val_recall',
                    'dataset_pathes', 'weights_path', 'date_']

headers_filter = ['Defect Name', 'Defect ID', 'Defect Level']

cls_table_ncols = len(cls_headers)
cls_table_nrows = 20



# get binary-models from database
def get_cls_models_from_db(db_obj, count=False, limit_size=cls_table_nrows, offset=0):
    cslmodels_list = db_obj.get_cls_models(limit=True, count=count, limit_size=limit_size, offset=offset)
    return cslmodels_list


# translate binary model to id
def translate_cls_algorithm_id_to_name(algo_id, reverse=False):
    if not reverse:
        return train_api.ALGORITHM_NAMES['binary'][int(algo_id)]
    else:
        try:
            return train_api.ALGORITHM_NAMES['binary'].index(algo_id)
        except:
            return -1


# translate classes
def translate_cls_model_classes(classes_string):
    return classes_string[1:-1]


# show/set models history to UI tabel
def set_clsmodels_on_ui_tabel(ui_obj, models_list):
    # definr table parameters
    ui_obj.cls_history_tabel.resizeColumnsToContents()
    ui_obj.cls_history_tabel.setColumnCount(cls_table_ncols)
    if len(models_list) != 0:
        ui_obj.cls_history_tabel.setRowCount(cls_table_nrows)
    else:
        ui_obj.cls_history_tabel.setRowCount(0)
    ui_obj.cls_history_tabel.verticalHeader().setVisible(True)
    ui_obj.cls_history_tabel.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.cls_history_tabel.setHorizontalHeaderLabels(cls_headers)
    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, bmodel in enumerate(models_list):
        for col_idx in range(cls_table_ncols):
            # translate algo-ids to name
            if col_idx == 0:
                bmodel[cls_headers_db[col_idx]] = translate_cls_algorithm_id_to_name(algo_id=bmodel[cls_headers_db[col_idx]])
            # translate classes
            if col_idx == 3:
                bmodel[cls_headers_db[col_idx]] = translate_cls_model_classes(classes_string=bmodel[cls_headers_db[col_idx]])
                
            table_item = sQTableWidgetItem(str(bmodel[cls_headers_db[col_idx]]))
            # set checkbox (only first col)
            if col_idx == 0:
                table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
                table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            ui_obj.cls_history_tabel.setItem(row_idx, col_idx, table_item)

    try:
        ui_obj.cls_history_tabel.setRowCount(row_idx+1)
    except:
        return


# add new model training infoes to database
def add_new_cls_model_to_db(db_obj, new_bmodel_info):
    res = db_obj.add_binary_model_record(new_bmodel_info)
    return res


# add new defect
def save_new_cls_model_record(ui_obj, db_obj, bmodel_records):
    # # change defect-name to id
    # new_defect_info = defect_management_funcs.change_defect_group_id_to_name(db_obj=self.db, defects_list=new_defect_info, reverse=True)
    # add defect to database
    if add_new_cls_model_to_db(db_obj=db_obj, new_bmodel_info=bmodel_records) == 'True':
        # alert
        ui_obj.create_alert_message(title='Training Result', message='Model is Successfully Trained, Records are Saved to History')

    else:
        ui_obj.create_alert_message(title='Training Result', message='Failed to Save Model Records to History')


# get binary model information from UI filter section
def get_cls_model_filter_info_from_ui(ui_obj):
    try: 
        # get params from UI
        model_info = {}
        model_info['algo_name'] = [translate_cls_algorithm_id_to_name(algo_id=ui_obj.cls_name_filter_combo.currentText(), reverse=True)]
        model_info['epochs'] = [ui_obj.cls_epoch_min_filter_lineedit.text(), ui_obj.cls_epoch_max_filter_lineedit.text()]
        model_info['tuning_epochs'] = [ui_obj.cls_tepoch_min_filter_lineedit.text(), ui_obj.cls_tepoch_max_filter_lineedit.text()]
        model_info['batch_size'] = [ui_obj.cls_batch_min_filter_lineedit.text(), ui_obj.cls_batch_max_filter_lineedit.text()]
        model_info['split_ratio'] = [ui_obj.cls_split_min_filter_lineedit.text(), ui_obj.cls_split_max_filter_lineedit.text()]
        model_info['val_loss'] = [ui_obj.cls_loss_min_filter_lineedit.text(), ui_obj.cls_loss_max_filter_lineedit.text()]
        model_info['val_accuracy'] = [ui_obj.cls_acc_min_filter_lineedit.text(), ui_obj.cls_acc_max_filter_lineedit.text()]
        model_info['val_precision'] = [ui_obj.cls_prec_min_filter_lineedit.text(), ui_obj.cls_prec_max_filter_lineedit.text()]
        model_info['val_recall'] = [ui_obj.cls_rec_min_filter_lineedit.text(), ui_obj.cls_rec_max_filter_lineedit.text()]
        model_info['date_'] = [ui_obj.cls_date_min_filter_lineedit.text(), ui_obj.cls_date_max_filter_lineedit.text()]
        # classes
        model_info['classes'] = get_selected_defects_for_filter(ui_obj=ui_obj)

        return model_info
           
    except:
        return []


    

# get users from database
def get_filtered_cls_models_from_db(ui_obj, db_obj, filter_params, limit_size=cls_table_nrows, offset=0, count=False):
    # input parameters and column names in database
    params = []
    cols = []
    if len(filter_params) == 0:
        return 'error',[]

    # add parameters and col names to build the input sql query
    if filter_params['algo_name'][0] != -1:
        params.append(filter_params['algo_name'])
        cols.append('algo_name')
    #
    if filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '' and int(filter_params['epochs'][0]) > int(filter_params['epochs'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Epoch Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['epochs'][0] == '') ^ bool(filter_params['epochs'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Epoch Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['epochs'][0] != '' and filter_params['epochs'][1] != '':
        params.append(filter_params['epochs'])
        cols.append('epochs')
    #
    if filter_params['tuning_epochs'][0] != '' and filter_params['tuning_epochs'][1] != '' and int(filter_params['tuning_epochs'][0]) > int(filter_params['tuning_epochs'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Tunning Epoch Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['tuning_epochs'][0] == '') ^ bool(filter_params['tuning_epochs'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Tunning Epoch Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['tuning_epochs'][0] != '' and filter_params['tuning_epochs'][1] != '':
        params.append(filter_params['tuning_epochs'])
        cols.append('tuning_epochs')
    #
    if filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '' and int(filter_params['batch_size'][0]) > int(filter_params['batch_size'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Batch-Size Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['batch_size'][0] == '') ^ bool(filter_params['batch_size'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Batch-Size Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['batch_size'][0] != '' and filter_params['batch_size'][1] != '':
        params.append(filter_params['batch_size'])
        cols.append('batch_size')
    #
    if filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '' and int(filter_params['split_ratio'][0]) > int(filter_params['split_ratio'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Split_Ratio Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['split_ratio'][0] == '') ^ bool(filter_params['split_ratio'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Split_Ratio Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['split_ratio'][0] != '' and filter_params['split_ratio'][1] != '':
        params.append(filter_params['split_ratio'])
        cols.append('split_ratio')
    #
    if filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '' and int(filter_params['val_loss'][0]) > int(filter_params['val_loss'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Loss Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_loss'][0] == '') ^ bool(filter_params['val_loss'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Loss Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_loss'][0] != '' and filter_params['val_loss'][1] != '':
        params.append(filter_params['val_loss'])
        cols.append('val_loss')
    #
    if filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '' and int(filter_params['val_accuracy'][0]) > int(filter_params['val_accuracy'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Accuracy Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_accuracy'][0] == '') ^ bool(filter_params['val_accuracy'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Accuracy Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_accuracy'][0] != '' and filter_params['val_accuracy'][1] != '':
        params.append(filter_params['val_accuracy'])
        cols.append('val_accuracy')
    #
    if filter_params['val_precision'][0] != '' and filter_params['val_precision'][1] != '' and int(filter_params['val_precision'][0]) > int(filter_params['val_precision'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Precision Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_precision'][0] == '') ^ bool(filter_params['val_precision'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Precision Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_precision'][0] != '' and filter_params['val_precision'][1] != '':
        params.append(filter_params['val_precision'])
        cols.append('val_precision')
    #
    if filter_params['val_recall'][0] != '' and filter_params['val_recall'][1] != '' and int(filter_params['val_recall'][0]) > int(filter_params['val_recall'][1]):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Recall Range Incorrect', color=colors_pallete.failed_red)
        return 'error',[]
    elif bool(filter_params['val_recall'][0] == '') ^ bool(filter_params['val_recall'][1] == ''):
        ui_obj.show_mesagges(label_name=ui_obj.cls_tabel_label, text='Recall Range Cant be Empty', color=colors_pallete.failed_red)
        return 'error',[]
    elif filter_params['val_recall'][0] != '' and filter_params['val_recall'][1] != '':
        params.append(filter_params['val_recall'])
        cols.append('val_recall')
    #
    if len(filter_params['classes']) != 0:
        params.append(filter_params['classes'])
        cols.append('classes')


    # print('-----------------------------------------------------------')
    # print('params:', params)
    # print('cols:', cols)
    # print('-----------------------------------------------------------')
    # return
    
    # check not wmpty
    if len(params) == 0 or len(cols) == 0:
        return 'all', []
    
    # get from db
    try:
        defects_list = db_obj.search_cls_model_by_filter(parms=params, cols=cols, limit=True, limit_size=limit_size, offset=offset, count=count)
        return 'filtered', defects_list
    
    except:
        return []

    
# 
def set_defects_on_filter_ui(ui_obj, defects_list, defect_group_name='None'):
    # definr table parameters
    ui_obj.table_classification_filter_class.resizeColumnsToContents()
    ui_obj.table_classification_filter_class.setColumnCount(len(headers_filter))
    if len(defects_list) != 0:
        ui_obj.table_classification_filter_class.setRowCount(cls_table_nrows)
    else:
        ui_obj.table_classification_filter_class.setRowCount(0)
    ui_obj.table_classification_filter_class.verticalHeader().setVisible(True)
    ui_obj.table_classification_filter_class.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.table_classification_filter_class.setHorizontalHeaderLabels(headers_filter)
    # add users to table
    for i, defect in enumerate(defects_list):
        # text color
        text_color = colors_pallete.failed_red if defect['groupp'] == defect_group_name else colors_pallete.black
        # set short name
        table_item = sQTableWidgetItem(str(defect['short_name']))
        table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
        table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
        table_item.setForeground(sQColor(text_color))
        ui_obj.table_classification_filter_class.setItem(i, 0, table_item)
        # set defect_ID
        table_item = sQTableWidgetItem(str(defect['defect_ID']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.table_classification_filter_class.setItem(i, 1, table_item)
        # set level
        table_item = sQTableWidgetItem(str(defect['level']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.table_classification_filter_class.setItem(i, 2, table_item)
    try:
        ui_obj.table_classification_filter_class.setRowCount(i+1)
    except:
        return


#
def get_selected_defects_for_filter(ui_obj):
    list = []
    for i in range(ui_obj.table_classification_filter_class.rowCount()):    
        if ui_obj.table_classification_filter_class.item(i, 0).checkState() == sQtCore.Qt.Checked:
            list.append(ui_obj.table_classification_filter_class.item(i, 1).text())
    # selected_defects = []
    # for i in range (len(list)):
    #     selected_defects.append(defects_list[list[i]]['defect_ID'])
    # return selected_defects
    return list





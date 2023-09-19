from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal
from requests import head

from backend import colors_pallete, chart_funcs, date_funcs
import train_api
import texts, texts_codes
import os
from utils1 import Utils
import json
from random_split import *


SHAMSI_DATE = False


# binary table headers
binary_headers = [
    "Algorithm",
    "Input-Size",
    "Input-Type",
    "N-Epochs",
    "N-Tuning Epochs",
    "Batch-Size",
    "Learning-Rate",
    "Split Ratio",
    "Loss",
    "Accuracy",
    "Precision",
    "Recall",
    "Val-Loss",
    "Val-Accuracy",
    "Val-Precision",
    "Val-Recall",
    "Dataset Path",
    "Weights Path",
    "Date Created",
]
binary_headers_fa = [
    "نام الگوریتم",
    "اندازه ورودی",
    "نوع ورودی",
    "تعداد اپوک",
    "تعداد اپوک تنظیم",
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
binary_headers_db = [
    "algo_name",
    "input_size",
    "input_type",
    "epochs",
    "tuning_epochs",
    "batch_size",
    "lr",
    "split_ratio",
    "loss",
    "accuracy",
    "precision_",
    "recall",
    "val_loss",
    "val_accuracy",
    "val_precision",
    "val_recall",
    "dataset_pathes",
    "weights_path",
    "date_",
]
# _______________________________________________________________________
binary_headers_dic = {
    "en": [
        "Algorithm",
        "Input-Size",
        "Input-Type",
        "N-Epochs",
        "N-Tuning Epochs",
        "Batch-Size",
        "Learning-Rate",
        "Split Ratio",
        "Dataset Path",
        "Weights Path",
        "Date Created",
        "Loss",
        "Accuracy",
        "Precision",
        "Recall",
        "Val-Loss",
        "Val-Accuracy",
        "Val-Precision",
        "Val-Recall",
    ],
    "fa": [
        "نام الگوریتم",
        "اندازه ورودی",
        "نوع ورودی",
        "تعداد اپوک",
        "تعداد اپوک تنظیم",
        "اندازه دسته",
        "نرخ یادگیری",
        "نسبت تقسیم داده",
        "آدرس مجموعه داده",
        "آدرس وزن ها",
        "تاریخ ایجاد",
        "Loss",
        "Accuracy",
        "Precision",
        "Recall",
        "اعتبارسنجی Loss",
        "اعتبارسنجی Accuracy",
        "اعتبارسنجی Precision",
        "اعتبارسنجی Recall",
    ],
    "db": [
        "algo_name",
        "input_size",
        "input_type",
        "epochs",
        "tuning_epochs",
        "batch_size",
        "lr",
        "split_ratio",
        "dataset_pathes",
        "weights_path",
        "date_",
        "loss",
        "accuracy",
        "precision_",
        "recall",
        "val_loss",
        "val_accuracy",
        "val_precision",
        "val_recall",
    ],
}

localization_headers = {
    "en": [
        "Algorithm",
        "Pretrain Weights",
        "Input-Size",
        "Input-Type",
        "N-Epochs",
        "Batch-Size",
        "Learning-Rate",
        "Split Ratio",
        "Loss",
        "Accuracy",
        "Iou",
        "Fscore",
        "Val-Loss",
        "Val-Accuracy",
        "Val-Iou",
        "Val-Fscore",
        "Dataset Path",
        "Weights Path",
        "Date Created",
    ],
    "fa": [
        "نام الگوریتم",
        "آدرس وزن از قبل آموزش دیده",
        "اندازه ورودی",
        "نوع ورودی",
        "تعداد اپوک",
        "اندازه دسته",
        "نرخ یادگیری",
        "نسبت تقسیم داده",
        "Loss",
        "Accuracy",
        "Iou",
        "Fscore",
        "اعتبارسنجی Loss",
        "اعتبارسنجی Accuracy",
        "اعتبارسنجی Iou",
        "اعتبارسنجی Fscore",
        "آدرس مجموعه داده",
        "آدرس وزن ها",
        "تاریخ ایجاد",
    ],
    "db": [
        "algo_name",
        "pretrain_path",
        "input_size",
        "input_type",
        "epochs",
        "batch_size",
        "lr",
        "split_ratio",
        "loss",
        "accuracy",
        "iou",
        "fscore",
        "val_loss",
        "val_accuracy",
        "val_iou",
        "val_fscore",
        "dataset_pathes",
        "weights_path",
        "date_",
    ],
}
# classification table headers
classification_headers = {
    "en": [
        "Algorithm",
        "Input-Size",
        "Input-Type",
        "N-Epochs",
        "Batch-Size",
        "Learning-Rate",
        "Split Ratio",
        "Target classes",
        "Loss",
        "Accuracy",
        "Precision",
        "Recall",
        "Val-Loss",
        "Val-Accuracy",
        "Val-Precision",
        "Val-Recall",
        "Dataset Path",
        "Weights Path",
        "Date Created",
        "Pretrain Weights",
    ],
    "fa": [
        "نام الگوریتم",
        "اندازه ورودی",
        "نوع ورودی",
        "تعداد اپوک",
        "اندازه دسته",
        "نرخ یادگیری",
        "نسبت تقسیم داده",
        "کلاس های هدف",
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
        "آدرس وزن از قبل آموزش دیده",
    ],
    "db": [
        "algo_name",
        "input_size",
        "input_type",
        "epochs",
        "batch_size",
        "lr",
        "split_ratio",
        "classes",
        "loss",
        "accuracy",
        "precision_",
        "recall",
        "val_loss",
        "val_accuracy",
        "val_precision",
        "val_recall",
        "dataset_pathes",
        "weights_path",
        "date_",
        "pretrain_path",
    ],
}
# yolo table headers
yolo_headers = {
    "en": [
        "Algorithm",
        "Input-Size",
        "Input-Type",
        "N-Epochs",
        "Batch-Size",
        "Learning-Rate",
        "Split Ratio",
        "Dataset Path",
        "Weights Path",
        "Date Created",
        "Target classes",
        "BOX-Loss",
        "OBJ-Loss",
        "CLS_Loss",
        "Val_Precision",
        "Val_Recall",
        "Val_mAP05",
        "Val_mAP0595",
        "Val_BOX-Loss",
        "Val_OBJ-Loss",
        "Val_CLS_Loss",
    ],
    "fa": [
        "نام الگوریتم",
        "اندازه ورودی",
        "تعداد اپوک",
        "اندازه دسته",
        "نرخ یادگیری",
        "نسبت تقسیم داده",
        "آدرس مجموعه داده",
        "آدرس وزن ها",
        "تاریخ ایجاد",
        "کلاس های هدف",
        "BOX-Loss",
        "OBJ-Loss",
        "CLS_Loss",
        "اعتبارسنجی Precision",
        "اعتبارسنجی Recall",
        "اعتبارسنجی mAP05",
        "اعتبارسنجی mAP0595",
        "اعتبارسنجی BOX-Loss",
        "اعتبارسنجی OBJ-Loss",
        "اعتبارسنجی CLS_Loss",
    ],
    "db": [
        "algo_name",
        "input_size",
        "input_type",
        "epochs",
        "batch_size",
        "lr",
        "split_ratio",
        "dataset_pathes",
        "weights_path",
        "date_",
        "classes",
        "box_loss",
        "obj_loss",
        "cls_loss",
        "val_precision",
        "val_recall",
        "val_mAP_0.5",
        "val_mAP_0.5:0.95",
        "val_box_loss",
        "val_obj_loss",
        "val_cls_loss",
    ],
}
# table number of rows and cols
binary_table_ncols = len(binary_headers)
binary_table_nrows = 20


# get binary-models from database
def get_binary_models_from_db(
    db_obj,
    count=False,
    limit_size=binary_table_nrows,
    offset=0,
    model_type="binary_models",
):
    """this function is used to get binary models infoes list from database

    :param db_obj: database object
    :type db_obj: _type_
    :param count: a boolean determining whether to get count of table, defaults to False
    :type count: boolean, optional
    :param limit_size: number of returning rows from database, defaults to binary_table_nrows
    :type limit_size: int, optional
    :param offset: start row index in table to return next n rows, defaults to 0
    :type offset: int, optional
    :return: list of binary model info (in dict)
    :rtype: list of dicts
    """

    res, bmodels_list = db_obj.get_binary_models(
        limit=True,
        count=count,
        limit_size=limit_size,
        offset=offset,
        type_model=model_type,
    )
    return res, bmodels_list


# translate binary model to id
def translate_binary_algorithm_id_to_name(
    algo_id,
    model_type="binary",
    reverse=False,
):
    """this function is used to translate binary algorithm id to its name

    :param algo_id: algorithm id
    :type algo_id: int
    :param reverse: boolean to determine whether to translate name to id, defaults to False
    :type reverse: bool, optional
    :return: _description_
    :rtype: binary algorithm name/id (by respect to reverse value)
    """
    if not reverse:
        return train_api.ALGORITHM_NAMES[model_type][int(algo_id)]
    else:
        try:
            return train_api.ALGORITHM_NAMES[model_type].index(algo_id)
        except:
            return -1


# ____________________________________________________________________JJ ZONE
def translate_model_algorithm_id_to_creator_function(
    algo_id, input_size, num_class=1, mode="binary", weights_path=None
):
    creator = train_api.ALGORITHM_CREATOR[algo_id]
    model = creator(input_size=input_size, num_class=num_class, mode=mode)
    if weights_path != None:
        model.load_weights(weights_path)
    return model


def strInputSize_2_intInputSize(string, use_for_other_parameter=False):
    string = string[1:-1].split(",")
    if not use_for_other_parameter:
        return (int(string[0]), int(string[1]), 3)
    else:
        return len(string), [int(x) for x in string]


# ____________________________________________________________________JJ ZONE


# show/set models history to UI tabel
def set_bmodels_on_ui_tabel(ui_obj, bmodels_list):
    """this function is used to set binary models list on ui binary models list (binary history page)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param bmodels_list: list of binary model params (in dict)
    :type bmodels_list: list of dicts
    """

    # definr table parameters
    ui_obj.binary_history_tabel.resizeColumnsToContents()
    ui_obj.binary_history_tabel.setColumnCount(binary_table_ncols)

    if len(bmodels_list) != 0:
        ui_obj.binary_history_tabel.setRowCount(binary_table_nrows)
    else:
        ui_obj.binary_history_tabel.setRowCount(0)

    ui_obj.binary_history_tabel.verticalHeader().setVisible(True)
    # ui_obj.binary_history_tabel.horizontalHeader().setSectionResizeMode(
    #     sQHeaderView.Stretch
    # )
    ui_obj.binary_history_tabel.setHorizontalHeaderLabels(
        binary_headers if ui_obj.language == "en" else binary_headers_fa
    )

    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, bmodel in enumerate(bmodels_list):
        for col_idx in range(binary_table_ncols):
            # translate algo-ids to name
            if col_idx == 0:
                bmodel[
                    binary_headers_db[col_idx]
                ] = translate_binary_algorithm_id_to_name(
                    algo_id=bmodel[binary_headers_db[col_idx]]
                )
            table_item = sQTableWidgetItem(str(bmodel[binary_headers_db[col_idx]]))
            # set checkbox (only first col)
            if col_idx == 0:
                table_item.setFlags(
                    sQtCore.Qt.ItemFlag.ItemIsUserCheckable
                    | sQtCore.Qt.ItemFlag.ItemIsEnabled
                )
                table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            ui_obj.binary_history_tabel.setItem(row_idx, col_idx, table_item)

    try:
        ui_obj.binary_history_tabel.setRowCount(row_idx + 1)

    except Exception as e:
        return


# show/set models history to UI tabel
def set_bmodels_on_ui_tabel_edited_version(
    ui_obj, bmodels_list, model_type="binary", language="en"
):
    if model_type == "binary":
        headers = binary_headers_dic[language]
        headers_db = binary_headers_dic["db"]
        table_ncols = len(binary_headers_dic[language])
    elif model_type == "yolo":
        headers = yolo_headers[language]
        table_ncols = len(yolo_headers[language])
        headers_db = yolo_headers["db"]
    elif model_type == "localization":
        headers = localization_headers[language]
        table_ncols = len(localization_headers[language])
        headers_db = localization_headers["db"]
    else:
        headers = classification_headers[language]
        table_ncols = len(classification_headers[language])
        headers_db = classification_headers["db"]

    # define table parameters
    ui_obj.table_of_binary_classifaction_in_PBT_page.resizeColumnsToContents()
    ui_obj.table_of_binary_classifaction_in_PBT_page.setColumnCount(table_ncols)
    if len(bmodels_list) != 0:
        ui_obj.table_of_binary_classifaction_in_PBT_page.setRowCount(binary_table_nrows)
    else:
        ui_obj.table_of_binary_classifaction_in_PBT_page.setRowCount(0)
    ui_obj.table_of_binary_classifaction_in_PBT_page.verticalHeader().setVisible(True)
    # ui_obj.table_of_binary_classifaction_in_PBT_page.horizontalHeader().setSectionResizeMode(
    #     sQHeaderView.Stretch
    # )

    ui_obj.table_of_binary_classifaction_in_PBT_page.setHorizontalHeaderLabels(headers)
    # text color
    text_color = colors_pallete.black
    # add users to table
    for row_idx, bmodel in enumerate(bmodels_list):
        for col_idx in range(table_ncols):
            # translate algo-ids to name
            if col_idx == 0:
                bmodel[headers_db[col_idx]] = translate_binary_algorithm_id_to_name(
                    algo_id=bmodel[headers_db[col_idx]], model_type=model_type
                )
            table_item = sQTableWidgetItem(str(bmodel[headers_db[col_idx]]))
            # set checkbox (only first col)
            if col_idx == 0:
                table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsEnabled)
                table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
            table_item.setForeground(sQColor(text_color))
            ui_obj.table_of_binary_classifaction_in_PBT_page.setItem(
                row_idx, col_idx, table_item
            )

    try:
        ui_obj.table_of_binary_classifaction_in_PBT_page.setRowCount(row_idx + 1)
    except:
        return


# add new model training infoes to database
def add_new_binary_model_to_db(db_obj, new_bmodel_info):
    """this function is used to add a new binary model params to dataabse

    :param db_obj: database object
    :type db_obj: _type_
    :param new_bmodel_info: model parameters
    :type new_bmodel_info: _type_
    :return: resault: boolean
    :rtype: boolean
    """

    res = db_obj.add_binary_model_record(new_bmodel_info)
    return res


def save_new_binary_model_record(ui_obj, db_obj, bmodel_records):
    """this functino is used to add new trained model parameters to database

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: databse object
    :type db_obj: _type_
    :param bmodel_records: model parameters
    :type bmodel_records: _type_
    :return: result
    :rtype: bool
    """

    # add
    # print(bmodel_records["weights_path"])
    if add_new_binary_model_to_db(db_obj=db_obj, new_bmodel_info=bmodel_records):
        ui_obj.notif_manager.append_new_notif(
            message=texts.MESSEGES["database_add_bmodel"][ui_obj.language], level=1
        )
        return True

    else:
        ui_obj.notif_manager.append_new_notif(
            message=texts.ERRORS["database_add_bmodel_failed"][ui_obj.language], level=3
        )
        return False


# get binary model information from UI filter section
def get_binary_model_filter_info_from_ui(ui_obj, wich_page, model_type="binary"):
    """this function is used to get filter params in binary models list on UI

    :param ui_obj: main ui obj
    :type ui_obj: _type_
    :return: _description_
    :rtype: _type_
    """

    try:
        # get params from UI
        bmodel_info = {}
        if wich_page == "PBT":
            if model_type == "binary":
                bmodel_info["algo_name"] = [
                    translate_binary_algorithm_id_to_name(
                        algo_id=ui_obj.cbBox_of_binary_model_in_PBT_page.currentText(),
                        reverse=True,
                    )
                ]
            elif model_type == "classification":
                bmodel_info["algo_name"] = [
                    translate_binary_algorithm_id_to_name(
                        algo_id=ui_obj.cbBox_of_classification_model_in_PBT_page.currentText(),
                        model_type="classification",
                        reverse=True,
                    )
                ]
            elif model_type == "localization":
                bmodel_info["algo_name"] = [
                    translate_binary_algorithm_id_to_name(
                        algo_id=ui_obj.cbBox_of_localization_model_in_PBT_page.currentText(),
                        model_type="localization",
                        reverse=True,
                    )
                ]
            elif model_type == "yolo":
                bmodel_info["algo_name"] = [
                    translate_binary_algorithm_id_to_name(
                        algo_id=ui_obj.cbBox_of_yolo_model_in_PBT_page.currentText(),
                        model_type="yolo",
                        reverse=True,
                    )
                ]

            bmodel_info["epochs"] = ["", ""]
            bmodel_info["tuning_epochs"] = ["", ""]
            bmodel_info["batch_size"] = ["", ""]
            bmodel_info["split_ratio"] = ["", ""]
            bmodel_info["val_loss"] = ["", ""]
            bmodel_info["val_accuracy"] = ["", ""]
            bmodel_info["val_precision"] = ["", ""]
            bmodel_info["val_recall"] = ["", ""]
            # date
            bmodel_info["start_date"] = ["", "", ""]
            bmodel_info["end_date"] = ["", "", ""]
        else:
            bmodel_info["algo_name"] = [
                translate_binary_algorithm_id_to_name(
                    algo_id=ui_obj.binary_name_filter_combo.currentText(), reverse=True
                )
            ]

            bmodel_info["epochs"] = [
                ui_obj.binary_epoch_min_filter_lineedit.text(),
                ui_obj.binary_epoch_max_filter_lineedit.text(),
            ]
            bmodel_info["tuning_epochs"] = [
                ui_obj.binary_tepoch_min_filter_lineedit.text(),
                ui_obj.binary_tepoch_max_filter_lineedit.text(),
            ]
            bmodel_info["batch_size"] = [
                ui_obj.binary_batch_min_filter_lineedit.text(),
                ui_obj.binary_batch_max_filter_lineedit.text(),
            ]
            bmodel_info["split_ratio"] = [
                ui_obj.binary_split_min_filter_lineedit.text(),
                ui_obj.binary_split_max_filter_lineedit.text(),
            ]
            bmodel_info["val_loss"] = [
                ui_obj.binary_loss_min_filter_lineedit.text(),
                ui_obj.binary_loss_max_filter_lineedit.text(),
            ]
            bmodel_info["val_accuracy"] = [
                ui_obj.binary_acc_min_filter_lineedit.text(),
                ui_obj.binary_acc_max_filter_lineedit.text(),
            ]
            bmodel_info["val_precision"] = [
                ui_obj.binary_prec_min_filter_lineedit.text(),
                ui_obj.binary_prec_max_filter_lineedit.text(),
            ]
            bmodel_info["val_recall"] = [
                ui_obj.binary_rec_min_filter_lineedit.text(),
                ui_obj.binary_rec_max_filter_lineedit.text(),
            ]

            # date
            bmodel_info["start_date"] = [
                ui_obj.binary_start_year_lineedit.text(),
                ui_obj.binary_start_month_lineedit.text(),
                ui_obj.binary_start_day_lineedit.text(),
            ]
            bmodel_info["end_date"] = [
                ui_obj.binary_end_year_lineedit.text(),
                ui_obj.binary_end_month_lineedit.text(),
                ui_obj.binary_end_day_lineedit.text(),
            ]

        return bmodel_info
    except:
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["ui_get_bmodel_filter_params_failed"]["en"], level=5
        )
        return []


# get users from database
def get_filtered_binary_models_from_db(
    ui_obj,
    db_obj,
    filter_params,
    limit_size=binary_table_nrows,
    offset=0,
    count=False,
    model_type="binary",
):
    """this function is used to get filtered binary models from databasem using filter params

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param filter_params: filtering parameters
    :type filter_params: _type_
    :param limit_size: n returning rows from database, defaults to binary_table_nrows
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
    if filter_params["algo_name"][0] != -1:
        params.append(filter_params["algo_name"])
        cols.append("algo_name")

    # epoch
    try:
        if (
            filter_params["epochs"][0] != ""
            and filter_params["epochs"][1] != ""
            and int(filter_params["epochs"][0]) > int(filter_params["epochs"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["EPOCH_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["epochs"][0] == "") ^ bool(
            filter_params["epochs"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["EPOCH_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif filter_params["epochs"][0] != "" and filter_params["epochs"][1] != "":
            params.append(
                [
                    str(int(filter_params["epochs"][0])),
                    str(int(filter_params["epochs"][1])),
                ]
            )
            cols.append("epochs")
    except:
        ui_obj.set_warning(
            texts.ERRORS["EPOCH_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # tune epochs
    try:
        if (
            filter_params["tuning_epochs"][0] != ""
            and filter_params["tuning_epochs"][1] != ""
            and int(filter_params["tuning_epochs"][0])
            > int(filter_params["tuning_epochs"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["TEPOCH_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["tuning_epochs"][0] == "") ^ bool(
            filter_params["tuning_epochs"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["TEPOCH_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif (
            filter_params["tuning_epochs"][0] != ""
            and filter_params["tuning_epochs"][1] != ""
        ):
            params.append(
                [
                    str(int(filter_params["tuning_epochs"][0])),
                    str(int(filter_params["tuning_epochs"][1])),
                ]
            )
            cols.append("tuning_epochs")
    except:
        ui_obj.set_warning(
            texts.ERRORS["TEPOCH_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # batch-size
    try:
        if (
            filter_params["batch_size"][0] != ""
            and filter_params["batch_size"][1] != ""
            and int(filter_params["batch_size"][0])
            > int(filter_params["batch_size"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["BATCHSIZE_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["batch_size"][0] == "") ^ bool(
            filter_params["batch_size"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["BATCHSIZE_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif (
            filter_params["batch_size"][0] != ""
            and filter_params["batch_size"][1] != ""
        ):
            params.append(
                [
                    str(int(filter_params["batch_size"][0])),
                    str(int(filter_params["batch_size"][1])),
                ]
            )
            cols.append("batch_size")
    except:
        ui_obj.set_warning(
            texts.ERRORS["BATCHSIZE_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # split ration
    try:
        if (
            filter_params["split_ratio"][0] != ""
            and filter_params["split_ratio"][1] != ""
            and float(filter_params["split_ratio"][0])
            > float(filter_params["split_ratio"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["SPLITRATIO_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["split_ratio"][0] == "") ^ bool(
            filter_params["split_ratio"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["SPLITRATIO_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif (
            filter_params["split_ratio"][0] != ""
            and filter_params["split_ratio"][1] != ""
        ):
            params.append(
                [
                    str(float(filter_params["split_ratio"][0])),
                    str(float(filter_params["split_ratio"][1])),
                ]
            )
            cols.append("split_ratio")
    except:
        ui_obj.set_warning(
            texts.ERRORS["SPLITRATIO_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # loss
    try:
        if (
            filter_params["val_loss"][0] != ""
            and filter_params["val_loss"][1] != ""
            and float(filter_params["val_loss"][0])
            > float(filter_params["val_loss"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["LOSS_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["val_loss"][0] == "") ^ bool(
            filter_params["val_loss"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["LOSS_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif filter_params["val_loss"][0] != "" and filter_params["val_loss"][1] != "":
            params.append(
                [
                    str(float(filter_params["val_loss"][0])),
                    str(float(filter_params["val_loss"][1])),
                ]
            )
            cols.append("val_loss")
    except:
        ui_obj.set_warning(
            texts.ERRORS["LOSS_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # acc
    try:
        if (
            filter_params["val_accuracy"][0] != ""
            and filter_params["val_accuracy"][1] != ""
            and float(filter_params["val_accuracy"][0])
            > float(filter_params["val_accuracy"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["ACCU_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["val_accuracy"][0] == "") ^ bool(
            filter_params["val_accuracy"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["ACCU_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif (
            filter_params["val_accuracy"][0] != ""
            and filter_params["val_accuracy"][1] != ""
        ):
            params.append(
                [
                    str(float(filter_params["val_accuracy"][0])),
                    str(float(filter_params["val_accuracy"][1])),
                ]
            )
            cols.append("val_accuracy")
    except:
        ui_obj.set_warning(
            texts.ERRORS["ACCU_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # precision
    try:
        if (
            filter_params["val_precision"][0] != ""
            and filter_params["val_precision"][1] != ""
            and float(filter_params["val_precision"][0])
            > float(filter_params["val_precision"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["PREC_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["val_precision"][0] == "") ^ bool(
            filter_params["val_precision"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["PREC_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif (
            filter_params["val_precision"][0] != ""
            and filter_params["val_precision"][1] != ""
        ):
            params.append(
                [
                    str(float(filter_params["val_precision"][0])),
                    str(float(filter_params["val_precision"][1])),
                ]
            )
            cols.append("val_precision")
    except:
        ui_obj.set_warning(
            texts.ERRORS["PREC_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # recall
    try:
        if (
            filter_params["val_recall"][0] != ""
            and filter_params["val_recall"][1] != ""
            and float(filter_params["val_recall"][0])
            > float(filter_params["val_recall"][1])
        ):
            ui_obj.set_warning(
                texts.ERRORS["RECA_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        elif bool(filter_params["val_recall"][0] == "") ^ bool(
            filter_params["val_recall"][1] == ""
        ):
            ui_obj.set_warning(
                texts.WARNINGS["RECA_RANGE_EMPTY"][ui_obj.language],
                "binary_model_history",
                level=2,
            )
            return "error", []
        elif (
            filter_params["val_recall"][0] != ""
            and filter_params["val_recall"][1] != ""
        ):
            params.append(
                [
                    str(float(filter_params["val_recall"][0])),
                    str(float(filter_params["val_recall"][1])),
                ]
            )
            cols.append("val_recall")
    except:
        ui_obj.set_warning(
            texts.ERRORS["RECA_FORMAT_INVALID"][ui_obj.language],
            "binary_model_history",
            level=3,
        )
        return "error", []

    # date
    # start year
    if (
        filter_params["start_date"][0] != ""
        or filter_params["start_date"][1] != ""
        or filter_params["start_date"][2] != ""
        or filter_params["end_date"][0] != ""
        or filter_params["end_date"][1] != ""
        or filter_params["end_date"][2] != ""
    ):
        #
        try:
            if (
                int(filter_params["start_date"][0]) < 1401
                or int(filter_params["start_date"][0]) > 1500
            ):
                ui_obj.set_warning(
                    texts.ERRORS["YEAR_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERRORS["YEAR_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        # start month
        try:
            if (
                int(filter_params["start_date"][1]) < 1
                or int(filter_params["start_date"][1]) > 12
            ):
                ui_obj.set_warning(
                    texts.ERRORS["MONTH_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERRORS["MONTH_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        # start day
        try:
            if (
                int(filter_params["start_date"][2]) < 1
                or int(filter_params["start_date"][2]) > 31
            ):
                ui_obj.set_warning(
                    texts.ERRORS["DAY_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERRORS["DAY_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        #
        # end year
        try:
            if (
                int(filter_params["end_date"][0]) < 1401
                or int(filter_params["end_date"][0]) > 1500
            ):
                ui_obj.set_warning(
                    texts.ERRORS["YEAR_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERRORS["YEAR_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        # start month
        try:
            if (
                int(filter_params["end_date"][1]) < 1
                or int(filter_params["end_date"][1]) > 12
            ):
                ui_obj.set_warning(
                    texts.ERRORS["MONTH_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERRORS["MONTH_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        # start day
        try:
            if (
                int(filter_params["end_date"][2]) < 1
                or int(filter_params["end_date"][2]) > 31
            ):
                ui_obj.set_warning(
                    texts.ERRORS["DAY_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERRORS["DAY_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        #
        try:
            if len(filter_params["start_date"][1]) < 2:
                filter_params["start_date"][1] = "0" + filter_params["start_date"][1]
            if len(filter_params["start_date"][2]) < 2:
                filter_params["start_date"][2] = "0" + filter_params["start_date"][2]
            if len(filter_params["end_date"][1]) < 2:
                filter_params["end_date"][1] = "0" + filter_params["end_date"][1]
            if len(filter_params["end_date"][2]) < 2:
                filter_params["end_date"][2] = "0" + filter_params["end_date"][2]
            #
            start_date = (
                filter_params["start_date"][0]
                + "/"
                + filter_params["start_date"][1]
                + "/"
                + filter_params["start_date"][2]
            )
            end_date = (
                filter_params["end_date"][0]
                + "/"
                + filter_params["end_date"][1]
                + "/"
                + filter_params["end_date"][2]
            )
            if start_date > end_date:
                ui_obj.set_warning(
                    texts.ERRORS["DATE_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
            else:
                params.append(['"' + start_date + '"', '"' + end_date + '"'])
                cols.append("date_")

        except:
            ui_obj.set_warning(
                texts.ERRORS["DATE_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []

    # check not wmpty
    if len(params) == 0 or len(cols) == 0:
        return "all", []

    # get from db

    # get from db
    if model_type == "binary":
        model_type = "binary_models"
    elif model_type == "classification":
        model_type = "classification_models"
    elif model_type == "localization":
        model_type = "localization_models"
    elif model_type == "yolo":
        model_type = "yolo_models"

    try:
        res, defects_list = db_obj.search_binary_model_by_filter(
            parms=params,
            cols=cols,
            limit=True,
            limit_size=limit_size,
            offset=offset,
            count=count,
            model_type=model_type,
        )
        if res:
            return "filtered", defects_list

        else:
            ui_obj.notif_manager.append_new_notif(
                message=texts.ERRORS["database_get_bmodels_failed"][ui_obj.language],
                level=4,
            )
            return "error", []

    except:
        return []


class Binary_model_train_worker(sQObject):
    """this class is worker for binary model training Qthred

    :param sQObject: _description_
    :type sQObject: _type_
    """

    finished = sSignal()
    warning = sSignal(str, str, str, int)
    reset_progressbar = sSignal(int, str)
    set_progressbar = sSignal()
    update_charts = sSignal(int, dict)

    def assign_parameters(self, b_parms, api_obj, ui_obj, db_obj, ds_obj):
        self.b_parms = b_parms
        self.api_obj = api_obj
        self.ui_obj = ui_obj
        self.db_obj = db_obj
        self.ds_obj = ds_obj

    def split_binary_dataset(self, paths, size):
        for i, path in enumerate(paths):
            if self.ds_obj.check_binary_dataset(path):
                self.ds_obj.create_split_folder(path)

                s_mask = os.path.join(
                    path, self.ds_obj.binary_folder, self.ds_obj.defect_mask_folder
                )
                s_defect = os.path.join(
                    path, self.ds_obj.binary_folder, self.ds_obj.defect_folder
                )
                d_defect = os.path.join(
                    path, self.ds_obj.binary_folder, self.ds_obj.defect_splitted_folder
                )

                s_perfect = os.path.join(
                    path, self.ds_obj.binary_folder, self.ds_obj.perfect_folder
                )
                d_perfect = os.path.join(
                    path, self.ds_obj.binary_folder, self.ds_obj.perfect_splitted_folder
                )

                imgs = os.listdir(s_defect)
                self.reset_progressbar.emit(
                    len(imgs) + len(os.listdir(s_perfect)),
                    "Splitting dataset {}".format(i + 1),
                )
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_defect, i), color="color")
                    mask = Utils.read_image(os.path.join(s_mask, i), color="color")
                    if img is None or mask is None:
                        continue
                    crops, _, _ = get_crops_random(img, mask, size)
                    self.ds_obj.save_to_defect_splitted(
                        crops, d_defect, name=i.split(".")[0]
                    )
                    self.set_progressbar.emit()

                imgs = os.listdir(s_perfect)
                if len(os.listdir(s_perfect)):
                    n_split = np.ceil(
                        (len(os.listdir(d_defect)) * 1.5) / (len(os.listdir(s_perfect)))
                    )
                else:
                    n_split = 0
                for i in imgs:
                    img = Utils.read_image(os.path.join(s_perfect, i), color="color")
                    if img is None:
                        continue
                    crops = get_crops_no_defect(img, n_split, size)
                    self.ds_obj.save_to_perfect_splitted(
                        crops, d_perfect, i.split(".")[0]
                    )
                    self.set_progressbar.emit()
            else:
                self.warning.emit(
                    texts.WARNINGS["DATASET_FORMAT"][self.language], "train", None, 2
                )

    def train_model(self):
        if self.b_parms[2]:
            self.split_binary_dataset(self.b_parms[-1], self.b_parms[1])

        self.reset_progressbar.emit(self.b_parms[3], "Training")
        bmodel_records = train_api.train_binary(
            *self.b_parms, self.api_obj.ds.weights_binary_path, self.api_obj
        )
        if not bmodel_records[0]:
            self.warning.emit(
                bmodel_records[1][0],
                bmodel_records[1][1],
                None,
                bmodel_records[1][2],
            )
        else:
            bmodel_records = bmodel_records[1]
            if bmodel_records:
                # notif
                self.ui_obj.notif_manager.append_new_notif(
                    message=texts.MESSEGES["bmodel_trained"][self.ui_obj.language],
                    level=1,
                )

                # add record to database
                self.api_obj.bmodel_train_result = save_new_binary_model_record(
                    ui_obj=self.ui_obj,
                    db_obj=self.db_obj,
                    bmodel_records=bmodel_records,
                )

                self.warning.emit(
                    texts.MESSEGES["train_successfuly"][self.api_obj.language],
                    "train",
                    None,
                    1,
                )
                # update ui

        # self.ui_obj.binary_train.setEnabled(True)
        # self.api_obj.running_b_model=False

        self.finished.emit()

    def assign_new_value_to_b_chart(self, last_epoch, logs):
        self.set_progressbar.emit()
        self.update_charts.emit(last_epoch, logs)

    def save_b_model(self, model, path, epoch):
        try:
            model.save(path)
            self.ui_obj.logger.create_new_log(
                message=texts.MESSEGES["SAVE_BMODEL_EPOCH"]["en"].format(epoch)
            )
        except:
            self.ui_obj.logger.create_new_log(
                message=texts.ERRORS["SAVE_BMODEL_EPOCH_FAILED"]["en"].format(epoch),
                level=5,
            )
            self.warning.emit(
                texts.ERRORS["SAVE_BMODEL_EPOCH_FAILED"][self.api_obj.language].format(
                    epoch
                ),
                "train",
                None,
                3,
            )

    def show_bmodel_train_result(self):
        self.reset_progressbar.emit(1, "")
        self.ui_obj.binary_train.setEnabled(True)
        self.api_obj.running_b_model = False
        return

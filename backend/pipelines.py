from cmath import pi
import json
import os
from tokenize import Name

from backend.Annotation import NAME

try:
    from backend import date_funcs
except:
    import date_funcs
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from PySide6.QtCore import QObject as sQObject
from PySide6.QtCore import Signal as sSignal

try:
    from backend import colors_pallete
except:
    import colors_pallete


from train_api import ALGORITHM_NAMES

# from binary_model_funcs import translate_binary_algorithm_id_to_name

# ____________________________________

PIPELINE_ROOT = "root_path"
PIPELINE_NAME = "name"
DATE_CREATED = "date_created"
TIME_CREATED = "time_created"
OWNER = "owner"
USE_YOLO = "use_yolo"
#
BINARY_MODEL = "binary_model"
CALSSIFICATION_MODEL = "classification_model"
LOCALIZATION_MODEL = "localization_model"
YOLO_MODEL = "yolo_model"
#
MODEL_ID = "id"
MODEL_WEIGHTS_PATH = "weights_path"
MODEL_ACCURACY = "accuracy"
MODEL_PRECISION = "precision"
MODEL_RECALL = "recall"
MODEL_F1 = "f1"
MODEL_LOSS = "loss"
MODEL_DICE = "dice"
MODEL_IOU = "iou"
MODEL_PERCLASSS_ACCURACY = "perclass_accuracy"
MODEL_BOXLOSS = "box_loss"
MODEL_OBJLOSS = "obj_loss"
MODEL_CLSLOSS = "cls_loss"
MODEL_MAP05 = "mAP_0.5"
MODEL_MAP0595 = "mAP_0.5:0.95"
#
TARGET_CLASSES = "target_classes"
#
EVALUATED_DATASETS = "evaluated_datasets"

SHAMSI_DATE = False


pipline_headers = [
    "name",
    "Date",
    "Time",
    "Owner",
    "Target Classes",
    "Evaluated Datasets",
    "Binary Model",
    "Binary Weights Path",
    "Binary accuracy",
    "Binary precision",
    "Binary recall",
    "Binary loss",
    "Binary f1",
    "Classification Model",
    "Classification Weights Path",
    "Classification accuracy",
    "Classification precision",
    "Classification recall",
    "Classification f1",
    "Classification perclass accuracy",
    "Classification confusion_matrix",
    "Classification confusion_matrix",
    "Localization Model",
    "Localization Weights Path",
    "Localization loss",
    "Localization f1",
    "Localization iou",
]
pipline_headers_fa = [
    "الگوریتم",
    "سایز ورودی",
    "نوع ورودی",
    "تعداد اپوک",
    "تعداد اپوک تنظیم",
    "سایز بچ",
    "نرخ یادگیری",
    "نسبت تقسیم",
    "خطا",
    "دقت",
    "پرسیژن",
    "ریکال",
    "خطای اعتبارسنجی",
    "دقت اعتبارسنجی",
    "پرسیژن اعتبارسنجی",
    "ریکال اعتبارسنجی",
    "آدرس دیتاست",
    "آدرس وزن ها",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
    "تاریخ ایجاد",
]


# headers in database
binary_headers_db = [
    "name",
    "date_created",
    "time_created",
    "owner",
    "target_classes",
    "evaluated_datasets",
    "binary_model",
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


# table number of rows and cols
pipline_table_ncols = len(pipline_headers)
pipline_table_nrows = 20


class Pipeline:
    def __init__(
        self,
        pipeline_root,
        pipeline_name,
        date_created=date_funcs.get_date(persian=SHAMSI_DATE, folder_path=True),
        time_created=date_funcs.get_time(folder_path=True),
    ):
        """this class is used to create an object containg all information belonging to a pipeline model

        :param pipeline_path: _description_
        :type pipeline_path: _type_
        :param pipeline_name: _description_
        :type pipeline_name: _type_
        """

        self.pipline_json = {}

        self.pipline_json[PIPELINE_NAME] = pipeline_name
        self.pipline_json[PIPELINE_ROOT] = pipeline_root
        self.pipline_json[DATE_CREATED] = date_created
        self.pipline_json[TIME_CREATED] = time_created
        self.pipline_json[OWNER] = None
        self.pipline_json[USE_YOLO] = None

        # target classes
        self.pipline_json[TARGET_CLASSES] = None

        # evaluated datasets
        self.pipline_json[EVALUATED_DATASETS] = None

        # binary model
        self.pipline_json[BINARY_MODEL] = {
            MODEL_ID: None,
            MODEL_WEIGHTS_PATH: None,
            MODEL_ACCURACY: None,
            MODEL_PRECISION: None,
            MODEL_RECALL: None,
            MODEL_LOSS: None,
            MODEL_F1: None,
        }

        # classification model
        self.pipline_json[CALSSIFICATION_MODEL] = {
            MODEL_ID: None,
            MODEL_WEIGHTS_PATH: None,
            MODEL_ACCURACY: None,
            MODEL_PRECISION: None,
            MODEL_RECALL: None,
            MODEL_LOSS: None,
            MODEL_F1: None,
            MODEL_PERCLASSS_ACCURACY: None,
        }

        # localization model
        self.pipline_json[LOCALIZATION_MODEL] = {
            MODEL_ID: None,
            MODEL_WEIGHTS_PATH: None,
            MODEL_LOSS: None,
            MODEL_F1: None,
            MODEL_DICE: None,
            MODEL_IOU: None,
        }

        # yolo model
        self.pipline_json[YOLO_MODEL] = {
            MODEL_ID: None,
            MODEL_WEIGHTS_PATH: None,
            MODEL_BOXLOSS: None,
            MODEL_OBJLOSS: None,
            MODEL_CLSLOSS: None,
            MODEL_PRECISION: None,
            MODEL_RECALL: None,
            MODEL_MAP05: None,
            MODEL_MAP0595: None,
        }

    def save_json(self):
        """this function is used to save pipeline json object to path as a file"""

        try:
            # print(self.pipline_json[PIPELINE_ROOT])
            json_path = os.path.join(
                self.pipline_json[PIPELINE_ROOT],
                "%s-%s-%s.json"
                % (
                    self.pipline_json[PIPELINE_NAME],
                    self.pipline_json[DATE_CREATED],
                    self.pipline_json[TIME_CREATED],
                ),
            )
            # print(json_path)
            with open(json_path, "w") as f:
                json.dump(self.pipline_json, f)
            f.close()

            # print(";" * 50)

        except:
            try:
                json_path = self.pipline_json[PIPELINE_ROOT]
                json_path += ".json" if json_path[-5:] != ".json" else ""
                #
                with open(json_path, "w") as f:
                    json.dump(self.pipline_json, f)
                f.close()

            except Exception as e:
                pass
                # print(e)

    def load_json(self):
        """this function is used to load pipline info from json file"""

        try:
            json_path = os.path.join(
                self.pipline_json[PIPELINE_ROOT],
                "%s_%s-%s.json"
                % (
                    self.pipline_json[PIPELINE_NAME],
                    self.pipline_json[DATE_CREATED],
                    self.pipline_json[TIME_CREATED],
                ),
            )
            if not os.path.isfile(json_path):
                json_path = self.pipline_json[PIPELINE_ROOT]
            #
            with open(json_path, "r") as f:
                self.pipline_json = json.load(f)
            f.close()

            return self.pipline_json

        except Exception as e:
            pass
            # print(e)

    def set(self, key, value):
        self.pipline_json[key] = value

    def get(self, key):
        return self.pipline_json[key]

    def set_binary_model(self, key, value):
        self.pipline_json[BINARY_MODEL][key] = value

    def get_binary_model(self, key):
        return self.pipline_json[BINARY_MODEL][key]

    def set_classification_model(self, key, value):
        self.pipline_json[CALSSIFICATION_MODEL][key] = value

    def set_yolo_model(self, key, value):
        self.pipline_json[YOLO_MODEL][key] = value

    def get_yolo_model(self, key):
        return self.pipline_json[YOLO_MODEL][key]

    def get_classification_model(self, key):
        return self.pipline_json[CALSSIFICATION_MODEL][key]

    def set_localization_model(self, key, value):
        self.pipline_json[LOCALIZATION_MODEL][key] = value

    def get_localization_model(self, key):
        return self.pipline_json[LOCALIZATION_MODEL][key]


def load_all_json_files(dir_path):
    res = []
    try:
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)) and path[-4:] == "json":
                # print(path)
                with open(os.path.join(dir_path, path), "r") as f:
                    res.append(json.load(f))
        return len(res), res
    except:
        return 0, None


MAIN_PARMS = [
    "date_created",
    "time_created",
    "owner",
    "target_classes",
    "evaluated_datasets",
]

# show/set models history to UI tabel
def set_piplines_on_ui_tabel(ui_obj, values):
    """this function is used to set binary models list on ui binary models list (binary history page)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param values: list of binary model params (in dict)
    :type values: list of dicts
    """

    # define table parameters
    ui_obj.pipline_history_tabel.resizeColumnsToContents()
    ui_obj.pipline_history_tabel.setColumnCount(pipline_table_ncols)

    if len(values) != 0:
        ui_obj.pipline_history_tabel.setRowCount(pipline_table_nrows)
    else:
        ui_obj.pipline_history_tabel.setRowCount(0)

    ui_obj.pipline_history_tabel.verticalHeader().setVisible(True)
    ui_obj.pipline_history_tabel.horizontalHeader().setSectionResizeMode(
        sQHeaderView.Stretch
    )
    ui_obj.pipline_history_tabel.setHorizontalHeaderLabels(
        pipline_headers if ui_obj.language == "en" else pipline_headers_fa
    )

    # text color
    text_color = colors_pallete.black

    # add users to table
    for row_idx, json_ in enumerate(values):
        iteration = 0
        table_item = sQTableWidgetItem(str(json_["name"]))
        ui_obj.pipline_history_tabel.setItem(row_idx, iteration, table_item)

        for itr, main_parm in enumerate(MAIN_PARMS):
            iteration += 1
            table_item = sQTableWidgetItem(str(json_[main_parm]))
            ui_obj.pipline_history_tabel.setItem(row_idx, iteration, table_item)

        for itr, parm in enumerate(list(json_["binary_model"].keys())):
            iteration += 1
            table_item = sQTableWidgetItem(str(json_["binary_model"][parm]))
            ui_obj.pipline_history_tabel.setItem(row_idx, iteration, table_item)

        for itr, parm in enumerate(list(json_["classification_model"].keys())):
            iteration += 1
            table_item = sQTableWidgetItem(str(json_["classification_model"][parm]))
            ui_obj.pipline_history_tabel.setItem(row_idx, iteration, table_item)

        for itr, parm in enumerate(list(json_["localization_model"].keys())):
            iteration += 1
            table_item = sQTableWidgetItem(str(json_["localization_model"][parm]))
            ui_obj.pipline_history_tabel.setItem(row_idx, iteration, table_item)

    try:
        ui_obj.pipline_history_tabel.setRowCount(row_idx + 1)

    except Exception as e:
        return


from pathlib import Path


def load_all_json_files_by_date(dir_path, reverse=False):
    """
    this function is used to get all files in a path, sorted by date (old to new)

    Args:
        dir_path (_type_): _description_
        reverse (bool, optional): a boolean to reverse sorting to new to old. Defaults to False.

    Returns:
        file_paths: list of file pathes
    """
    res = []
    try:
        file_paths = sorted(
            Path(dir_path).iterdir(), key=os.path.getmtime, reverse=True
        )
        # return len(file_paths),file_paths
    except:
        # return 0,[]
        file_paths = []

    for path in file_paths:

        path = os.path.normpath(path)
        if path[-4:] == "json":
            # #print(path)
            with open(path, "r") as f:
                res.append(json.load(f))
    return len(res), res


def set_combox_of_pipline_history_page(ui_obj, db_obj):
    ui_obj.cbBox_pipline_name_in_PBT_page.clear()
    ui_obj.cbBox_pipline_name_in_PBT_page.addItems([""] + db_obj.get_pipline_names())
    ui_obj.cbBox_binarry_model_in_PBT_page.clear()
    ui_obj.cbBox_binarry_model_in_PBT_page.addItems([""] + ALGORITHM_NAMES["binary"])
    ui_obj.cbBox_localization_model_in_PBT_page.clear()
    ui_obj.cbBox_localization_model_in_PBT_page.addItems(
        [""] + ALGORITHM_NAMES["localization"]
    )
    ui_obj.cbBox_classification_model_in_PBT_page.clear()
    ui_obj.cbBox_classification_model_in_PBT_page.addItems(
        [""] + ALGORITHM_NAMES["classification"]
    )


def get_pipline_info_from_ui(ui_obj):
    pipline_info = {}

    # pipline name
    if ui_obj.cbBox_pipline_name_in_PBT_page.currentText() != "":
        pipline_info[NAME] = ui_obj.cbBox_pipline_name_in_PBT_page.currentText()

    # TIME&DATE
    if (
        ui_obj.pipline_year_lineedit.text() != ""
        or ui_obj.pipline_month_lineedit.text() != ""
        or ui_obj.pipline_day_lineedit.text() != ""
    ):
        pipline_info[DATE_CREATED] = [
            ui_obj.pipline_year_lineedit.text(),
            ui_obj.pipline_month_lineedit.text(),
            ui_obj.pipline_day_lineedit.text(),
        ]
    if (
        ui_obj.pipline_hour_lineedit.text() != ""
        or ui_obj.pipline_minut_lineedit.text() != ""
    ):
        pipline_info[TIME_CREATED] = [
            ui_obj.pipline_hour_lineedit.text(),
            ui_obj.pipline_minut_lineedit.text(),
        ]

    # binary
    pipline_info[BINARY_MODEL] = {}
    if ui_obj.cbBox_binarry_model_in_PBT_page.currentText() != "":
        id = ui_obj.cbBox_binarry_model_in_PBT_page.currentText()
        id = ALGORITHM_NAMES["binary"].index(id)
        pipline_info[BINARY_MODEL][MODEL_ID] = id
    if (
        ui_obj.binary_acc_min_filter_lineedit_3.text() != ""
        or ui_obj.binary_acc_max_filter_lineedit_3.text() != ""
    ):
        pipline_info[BINARY_MODEL][MODEL_ACCURACY] = [
            ui_obj.binary_acc_min_filter_lineedit_3.text(),
            ui_obj.binary_acc_max_filter_lineedit_3.text(),
        ]
    if (
        ui_obj.binary_precision_min_filter_lineedit.text() != ""
        or ui_obj.binary_precision_max_filter_lineedit.text() != ""
    ):
        pipline_info[BINARY_MODEL][MODEL_PRECISION] = [
            ui_obj.binary_precision_min_filter_lineedit.text(),
            ui_obj.binary_precision_max_filter_lineedit.text(),
        ]
    if (
        ui_obj.binary_f1_min_filter_lineedit.text() != ""
        or ui_obj.binary_f1_max_filter_lineedit.text() != ""
    ):
        pipline_info[BINARY_MODEL][MODEL_F1] = [
            ui_obj.binary_f1_min_filter_lineedit.text(),
            ui_obj.binary_f1_max_filter_lineedit.text(),
        ]
    if (
        ui_obj.binary_recall_min_filter_lineedit.text() != ""
        or ui_obj.binary_recall_max_filter_lineedit.text() != ""
    ):
        pipline_info[BINARY_MODEL][MODEL_RECALL] = [
            ui_obj.binary_recall_min_filter_lineedit.text(),
            ui_obj.binary_recall_max_filter_lineedit.text(),
        ]

    # localization
    pipline_info[LOCALIZATION_MODEL] = {}
    if ui_obj.cbBox_localization_model_in_PBT_page.currentText() != "":
        id = ui_obj.cbBox_localization_model_in_PBT_page.currentText()
        id = ALGORITHM_NAMES["localization"].index(id)
        pipline_info[LOCALIZATION_MODEL][MODEL_ID] = id
    if (
        ui_obj.localization_dice_min_filter_lineedit.text() != ""
        or ui_obj.localization_dice_max_filter_lineedit.text() != ""
    ):
        pipline_info[LOCALIZATION_MODEL][MODEL_DICE] = [
            ui_obj.localization_dice_min_filter_lineedit.text(),
            ui_obj.localization_dice_max_filter_lineedit.text(),
        ]
    if (
        ui_obj.localization_iou_min_filter_lineedit.text() != ""
        or ui_obj.localization_iou_max_filter_lineedit.text() != ""
    ):
        pipline_info[LOCALIZATION_MODEL][MODEL_IOU] = [
            ui_obj.localization_iou_min_filter_lineedit.text(),
            ui_obj.localization_iou_max_filter_lineedit.text(),
        ]

    # classification
    pipline_info[CALSSIFICATION_MODEL] = {}
    if ui_obj.cbBox_classification_model_in_PBT_page.currentText() != "":
        id = ui_obj.cbBox_classification_model_in_PBT_page.currentText()
        id = ALGORITHM_NAMES["classification"].index(id)
        pipline_info[CALSSIFICATION_MODEL][MODEL_ID] = id
    if (
        ui_obj.classification_precision_min_filter_lineedit.text() != ""
        or ui_obj.classification_precision_max_filter_lineedit.text() != ""
    ):
        pipline_info[CALSSIFICATION_MODEL][MODEL_PRECISION] = [
            ui_obj.classification_precision_min_filter_lineedit.text(),
            ui_obj.classification_precision_max_filter_lineedit.text(),
        ]
    if (
        ui_obj.classification_acc_min_filter_lineedit.text() != ""
        or ui_obj.classification_acc_max_filter_lineedit.text() != ""
    ):
        pipline_info[CALSSIFICATION_MODEL][MODEL_ACCURACY] = [
            ui_obj.classification_acc_min_filter_lineedit().text(),
            ui_obj.classification_acc_max_filter_lineedit().text(),
        ]
    if (
        ui_obj.classification_f1_min_filter_lineedit.text() != ""
        or ui_obj.classification_f1_max_filter_lineedit.text() != ""
    ):
        pipline_info[CALSSIFICATION_MODEL][MODEL_F1] = [
            ui_obj.classification_f1_min_filter_lineedit.text(),
            ui_obj.classification_f1_max_filter_lineedit.text(),
        ]
    if (
        ui_obj.classification_recall_min_filter_lineedit.text() != ""
        or ui_obj.classification_recall_max_filter_lineedit.text() != ""
    ):
        pipline_info[CALSSIFICATION_MODEL][MODEL_RECALL] = [
            ui_obj.classification_recall_min_filter_lineedit.text(),
            ui_obj.classification_recall_max_filter_lineedit.text(),
        ]

    return pipline_info


def filter_piplines(all_content, param_filter):
    removeable_list = []
    overall_param = param_filter.keys()
    for pipline in all_content:
        # overall param
        if NAME in overall_param:
            if pipline[NAME] != param_filter[NAME]:
                # all_content.remove(pipline)
                removeable_list.append(pipline)
                continue

        if DATE_CREATED in overall_param:
            d = pipline[DATE_CREATED].split("-")
            d = [int(x) for x in d]
            if param_filter[DATE_CREATED][0] != "":
                y = d[0] == int(param_filter[DATE_CREATED][0])
            else:
                y = True

            if param_filter[DATE_CREATED][1] != "":
                m = d[1] == int(param_filter[DATE_CREATED][1])
            else:
                m = True

            if param_filter[DATE_CREATED][2] != "":
                d = d[2] == int(param_filter[DATE_CREATED][2])
            else:
                d = True

            if not (y and m and d):
                # all_content.remove(pipline)
                removeable_list.append(pipline)
                continue

        if TIME_CREATED in overall_param:
            t = pipline[DATE_CREATED].split("-")
            t = [int(x) for x in t]

            if param_filter[TIME_CREATED][0] != "":
                h = t[0] == int(param_filter[DATE_CREATED][0])
            else:
                h = True

            if param_filter[TIME_CREATED][1] != "":
                m = t[1] == int(param_filter[DATE_CREATED][1])
            else:
                m = True

            if not (h and m):
                # all_content.remove(pipline)
                removeable_list.append(pipline)
                continue

        #################################################
        check = filter_model(
            param_filter_model=param_filter[BINARY_MODEL], pipline=pipline[BINARY_MODEL]
        )
        if check:
            # all_content.remove(pipline)
            removeable_list.append(pipline)
            continue
        #################################################
        check = filter_model(
            param_filter_model=param_filter[LOCALIZATION_MODEL],
            pipline=pipline[LOCALIZATION_MODEL],
            localization=True,
        )
        if check:
            # all_content.remove(pipline)
            removeable_list.append(pipline)
            continue
        #################################################
        check = filter_model(
            param_filter_model=param_filter[CALSSIFICATION_MODEL],
            pipline=pipline[CALSSIFICATION_MODEL],
        )
        if check:
            # all_content.remove(pipline)
            removeable_list.append(pipline)
            continue

    for r in removeable_list:
        all_content.remove(r)

    # return all_content


def filter_model(param_filter_model, pipline, localization=False):
    param = param_filter_model.keys()
    if param != []:

        if MODEL_ID in param:
            if pipline[MODEL_ID] != param_filter_model[MODEL_ID]:
                return True

        if localization:
            if MODEL_DICE in param:
                check = filter_metrics_min_max(
                    min_filter_param=param_filter_model[MODEL_DICE][0],
                    max_filter_param=param_filter_model[MODEL_DICE][1],
                    value=pipline[MODEL_DICE],
                )
                if check:
                    return True

            if MODEL_IOU in param:
                check = filter_metrics_min_max(
                    min_filter_param=param_filter_model[MODEL_IOU][0],
                    max_filter_param=param_filter_model[MODEL_IOU][1],
                    value=pipline[MODEL_IOU],
                )
                if check:
                    return True
        else:
            if MODEL_ACCURACY in param:
                check = filter_metrics_min_max(
                    min_filter_param=param_filter_model[MODEL_ACCURACY][0],
                    max_filter_param=param_filter_model[MODEL_ACCURACY][1],
                    value=pipline[MODEL_ACCURACY],
                )
                if check:
                    return True
            if MODEL_PRECISION in param:
                check = filter_metrics_min_max(
                    min_filter_param=param_filter_model[MODEL_PRECISION][0],
                    max_filter_param=param_filter_model[MODEL_PRECISION][1],
                    value=pipline[MODEL_PRECISION],
                )
                if check:
                    return True

            if MODEL_RECALL in param:
                check = filter_metrics_min_max(
                    min_filter_param=param_filter_model[MODEL_RECALL][0],
                    max_filter_param=param_filter_model[MODEL_RECALL][1],
                    value=pipline[MODEL_RECALL],
                )
                if check:
                    return True
            if MODEL_F1 in param:
                check = filter_metrics_min_max(
                    min_filter_param=param_filter_model[MODEL_F1][0],
                    max_filter_param=param_filter_model[MODEL_F1][1],
                    value=pipline[MODEL_F1],
                )
                if check:
                    return True

        return False


def filter_metrics_min_max(min_filter_param, max_filter_param, value):
    if min_filter_param != "":
        min = int(min_filter_param)
    else:
        min = int(value)
    if max_filter_param != "":
        max = int(max_filter_param)
    else:
        max = int(value)

    if value == None:
        value = 0

    return not (value >= min and value <= max)


# def clear_filter():

# if __name__=='__main__':
#     # import cv2
#     # for i in range(100):
#     x=Pipeline('evaluated_jsons', 'evaluated_jsons')
#     #     cv2.waitKey(1000)
#     #     x.save_json()
#     # len_,file_paths=load_all_json_files_by_date('evaluated_jsons')
#     # #print(file_paths)
#     d=4
#     s='d;dv'
#     #print(type(x))
#     #print(type(d))
#     #print(type(s))

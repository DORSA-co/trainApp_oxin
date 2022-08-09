from itertools import count
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6 import QtCore as sQtCore
from PySide6.QtGui import QColor as sQColor
from pyparsing import col
from PySide6.QtWidgets import QHeaderView

from backend import colors_pallete
import train_api, texts


# table number of rows and cols
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
#
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
    bmodels_list = db_obj.get_binary_models(
        limit=True,
        count=count,
        limit_size=limit_size,
        offset=offset,
        type_model=model_type,
    )
    return bmodels_list


# translate binary model to id
def translate_binary_algorithm_id_to_name(algo_id, model_type="binary", reverse=False):
    if not reverse:
        return train_api.ALGORITHM_NAMES[model_type][int(algo_id)]
    else:
        try:
            return train_api.ALGORITHM_NAMES[model_type].index(algo_id)
        except:
            return -1


# show/set models history to UI tabel
def set_bmodels_on_ui_tabel(ui_obj, bmodels_list):
    # define table parameters
    # print(len(bmodels_list))
    ui_obj.binary_history_tabel.resizeColumnsToContents()
    ui_obj.binary_history_tabel.setColumnCount(binary_table_ncols)
    if len(bmodels_list) != 0:
        ui_obj.binary_history_tabel.setRowCount(binary_table_nrows)
    else:
        ui_obj.binary_history_tabel.setRowCount(0)
    ui_obj.binary_history_tabel.verticalHeader().setVisible(True)
    ui_obj.binary_history_tabel.horizontalHeader().setSectionResizeMode(
        sQHeaderView.Stretch
    )
    ui_obj.binary_history_tabel.setHorizontalHeaderLabels(binary_headers)
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
    except:
        return


# show/set models history to UI tabel
def set_bmodels_on_ui_tabel_edited_version(ui_obj, bmodels_list, model_type="binary"):
    # define table parameters
    # print(len(bmodels_list))
    ui_obj.table_of_binary_classifaction_in_PBT_page.resizeColumnsToContents()
    ui_obj.table_of_binary_classifaction_in_PBT_page.setColumnCount(binary_table_ncols)
    if len(bmodels_list) != 0:
        ui_obj.table_of_binary_classifaction_in_PBT_page.setRowCount(binary_table_nrows)
    else:
        ui_obj.table_of_binary_classifaction_in_PBT_page.setRowCount(0)
    ui_obj.table_of_binary_classifaction_in_PBT_page.verticalHeader().setVisible(True)
    ui_obj.table_of_binary_classifaction_in_PBT_page.horizontalHeader().setSectionResizeMode(
        sQHeaderView.Stretch
    )
    ui_obj.table_of_binary_classifaction_in_PBT_page.setHorizontalHeaderLabels(
        binary_headers
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
                    algo_id=bmodel[binary_headers_db[col_idx]], model_type=model_type
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
            ui_obj.table_of_binary_classifaction_in_PBT_page.setItem(
                row_idx, col_idx, table_item
            )

    try:
        ui_obj.table_of_binary_classifaction_in_PBT_page.setRowCount(row_idx + 1)
    except:
        return


# add new model training infoes to database
def add_new_binary_model_to_db(db_obj, new_bmodel_info):
    res = db_obj.add_binary_model_record(new_bmodel_info)
    return res


# add new defect
def save_new_binary_model_record(ui_obj, db_obj, bmodel_records):
    # # change defect-name to id
    # new_defect_info = defect_management_funcs.change_defect_group_id_to_name(db_obj=self.db, defects_list=new_defect_info, reverse=True)
    # add defect to database
    if (
        add_new_binary_model_to_db(db_obj=db_obj, new_bmodel_info=bmodel_records)
        == "True"
    ):
        # alert
        ui_obj.create_alert_message(
            title="Training Result",
            message="Model is Successfully Trained, Records are Saved to History",
        )

    else:
        ui_obj.create_alert_message(
            title="Training Result", message="Failed to Save Model Records to History"
        )


# get binary model information from UI filter section
def get_binary_model_filter_info_from_ui(ui_obj, wich_page, model_type="binary"):
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
                        algo_id=ui_obj.cbBox_of_multiClassification_model_in_PBT_page.currentText(),
                        model_type="classification",
                        reverse=True,
                    )
                ]
            elif model_type == "localization":
                bmodel_info["algo_name"] = [
                    translate_binary_algorithm_id_to_name(
                        algo_id=ui_obj.cbBox_of_localiztion_model_in_PBT_page.currentText(),
                        model_type="localization",
                        reverse=True,
                    )
                ]
            else:
                print("what the fuck!!!!!!!!1")

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
                texts.ERORS["EPOCH_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["EPOCH_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["TEPOCH_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["TEPOCH_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["BATCHSIZE_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["BATCHSIZE_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["SPLITRATIO_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["SPLITRATIO_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["LOSS_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["LOSS_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["ACCU_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["ACCU_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["PREC_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["PREC_FORMAT_INVALID"][ui_obj.language],
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
                texts.ERORS["RECA_RANGE_INCORRECT"][ui_obj.language],
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
            texts.ERORS["RECA_FORMAT_INVALID"][ui_obj.language],
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
                int(filter_params["start_date"][0]) < 1402
                or int(filter_params["start_date"][0]) > 1500
            ):
                ui_obj.set_warning(
                    texts.ERORS["YEAR_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERORS["YEAR_FORMAT_INVALID"][ui_obj.language],
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
                    texts.ERORS["MONTH_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERORS["MONTH_FORMAT_INVALID"][ui_obj.language],
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
                    texts.ERORS["DAY_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERORS["DAY_FORMAT_INVALID"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []
        #
        # end year
        try:
            if (
                int(filter_params["end_date"][0]) < 1402
                or int(filter_params["end_date"][0]) > 1500
            ):
                ui_obj.set_warning(
                    texts.ERORS["YEAR_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERORS["YEAR_FORMAT_INVALID"][ui_obj.language],
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
                    texts.ERORS["MONTH_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERORS["MONTH_FORMAT_INVALID"][ui_obj.language],
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
                    texts.ERORS["DAY_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
        except:
            ui_obj.set_warning(
                texts.ERORS["DAY_FORMAT_INVALID"][ui_obj.language],
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
                    texts.ERORS["DATE_RANGE_INCORRECT"][ui_obj.language],
                    "binary_model_history",
                    level=3,
                )
                return "error", []
            else:
                params.append(['"' + start_date + '"', '"' + end_date + '"'])
                cols.append("date_")
        except:
            print("date error")
            ui_obj.set_warning(
                texts.ERORS["DATE_RANGE_INCORRECT"][ui_obj.language],
                "binary_model_history",
                level=3,
            )
            return "error", []

    #
    print("-----------------------------------------------------------")
    print("params:", params)
    print("cols:", cols)
    print("-----------------------------------------------------------")
    # return

    # check not wmpty
    if len(params) == 0 or len(cols) == 0:
        return "all", []

    # get from db
    if model_type == "binary":
        model_type = "binary_models"
    elif model_type == "classification":
        model_type = "classification_models"
    elif model_type == "localization":
        model_type = "localiztion_models"
    else:
        print("what the fuck!!!!!!!!!!!!")

    try:
        defects_list = db_obj.search_binary_model_by_filter(
            parms=params,
            cols=cols,
            limit=True,
            limit_size=limit_size,
            offset=offset,
            count=count,
            model_type=model_type,
        )
        return "filtered", defects_list

    except:
        return []

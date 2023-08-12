import os
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6.QtGui import QStandardItem as sQStandardItem
from PySide6.QtGui import QColor as sQColor
from PySide6.QtWidgets import QLabel as sQlabel
from PySide6 import QtCore as sQtCore
import numpy as np
import colorsys
from persiantools.jdatetime import JalaliDate
import json

from backend import colors_pallete, dataset, Annotation
import texts
import dataset_utils


# table number of rows and cols
defect_table_ncols = 8
defect_table_nrows = 20
defect_group_table_ncols = 4
defect_group_table_nrows = 20

# UI table header names
headers = ['Defect Name', 'Defect Short-Name', 'Defect ID', 'Is Defect', 'Defect-Group', 'Defect Level', 'Defect Color Label', 'Created Date']
headers_fa = ['نام عیب', 'نام کوتاه عیب', 'آی دی عیب', 'عیب بودن', 'نام گروه عیب', 'سطح عیب', 'رنگ برچسب عیب', 'تاریخ ایجاد']
#
headers_train = ['Defect Name', 'Defect ID', 'Defect Level']
headers_train_fa = ['نام عیب', 'آی دی عیب', 'سطح عیب']
#
headers_defect_groups = ['Defect-Group Name', 'Defect-Group ID', 'Is Defect', 'Created Date']
headers_defect_groups_fa = ['نام گروه عیب', 'آی دی گروه عیب', 'عیب بودن', 'تاریخ ایجاد']

n_image_per_slide = 5

#---------------------------------------------------------------------------------------------------------------------------

# get users from database
def get_defects_from_db(db_obj, defect_groups=False):
    """this function is used to get defects list from dataabse

    :param db_obj: database object
    :type db_obj: _type_
    :param defect_groups: boolean determining whether to get defect groups, defaults to False
    :type defect_groups: bool, optional
    :return: boolean determininng result, defects/defect groups list
    :rtype: bool, list
    """

    if not defect_groups:
        res, defects_list = db_obj.load_defects()
        return res, defects_list

    else:
        defect_groups_list = db_obj.load_defect_groups()
        return defect_groups_list


# change defect group-id to name
def change_defect_group_id_to_name(db_obj, defects_list, reverse=False, single=False):
    """this function is used to translate defect group ids to group name

    :param db_obj: database object
    :type db_obj: _type_
    :param defects_list: list of defects
    :type defects_list: _type_
    :param reverse: boolean determining whther to reverse trnslating name to id, defaults to False
    :type reverse: bool, optional
    :param single: boolean determining if a single item is in input, defaults to False
    :type single: bool, optional
    :return: _description_
    :rtype: _type_
    """

    if not reverse:
        if not single:
            for i in range(len(defects_list)):
                res, defect_group_name = db_obj.search_defect_group_by_id(defects_list[i]['groupp'])

                if len(defect_group_name) != 0:
                    defects_list[i]['groupp'] = defect_group_name['defect_group_name']

        else:
            res, defect_group_name = db_obj.search_defect_group_by_id(defects_list['groupp'])
            if len(defect_group_name) != 0:
                defects_list['groupp'] = defect_group_name['defect_group_name']

    # reverse
    else:
        defect_group_id = db_obj.search_defect_by_name(defects_list['groupp'])
        if len(defect_group_id) != 0:
            defects_list['groupp'] = defect_group_id['defect_group_id']

    return defects_list


# load selected user from database to UI
def load_defects_from_db(db_obj, defect_id, defect_group=False, defect_group_id=False):
    """this function is used to load/search defects/defect groups from database

    :param db_obj: database object
    :type db_obj: _type_
    :param defect_id: defect id
    :type defect_id: str
    :param defect_group: boolean determiing wheather to get defect groups, defaults to False
    :type defect_group: bool, optional
    :param defect_group_id: boolean determinig wheather to search defect by defect group id, defaults to False
    :type defect_group_id: bool, optional
    :return: defect info
    :rtype: dict
    """

    # search defect
    if not defect_group:
        # search defect by defect if
        if not defect_group_id:
            defect_info = db_obj.search_defect_by_id(defect_id[0])
            return defect_info

        # search defect by defect group id
        else:
            defect_info = db_obj.search_defect_by_group_id(defect_id[0])
            return defect_info

    # defect-group
    else:
        res, defect_info = db_obj.search_defect_group_by_id(defect_id[0])
        return defect_info


# show/set user info to UI
def set_defects_on_ui(ui_obj, defects_list, defect_group_name='None'):
    """this function is used to set returned defects from database to UI defect tables

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param defects_list: list of defects
    :type defects_list: list of dicts
    :param defect_group_name: _description_, defaults to 'None'
    :type defect_group_name: str, optional
    """

    # definr table parameters
    ui_obj.classes_table.resizeColumnsToContents()
    ui_obj.classes_table.setColumnCount(defect_table_ncols)
    if len(defects_list) != 0:
        ui_obj.classes_table.setRowCount(defect_table_nrows)
    else:
        ui_obj.classes_table.setRowCount(0)
    ui_obj.classes_table.verticalHeader().setVisible(True)
    # ui_obj.classes_table.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.classes_table.setHorizontalHeaderLabels(headers if ui_obj.language=='en' else headers_fa)

    # add users to table
    for i, defect in enumerate(defects_list):
        # text color
        text_color = colors_pallete.failed_red if defect['groupp'] == defect_group_name else colors_pallete.black

        # set name
        table_item = sQTableWidgetItem(str(defect['name']))
        table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
        table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 0, table_item)

        # set short name
        table_item = sQTableWidgetItem(str(defect['short_name']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 1, table_item)
        
        # set defect_ID
        table_item = sQTableWidgetItem(str(defect['defect_ID']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 2, table_item)

        # set is_defect
        table_item = sQTableWidgetItem(str(defect['is_defect']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 3, table_item)

        # set group
        table_item = sQTableWidgetItem(str(defect['groupp']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 4, table_item)

        # set level
        table_item = sQTableWidgetItem(str(defect['level']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 5, table_item)

        # set color
        table_item = sQTableWidgetItem(str(defect['color']))
        icon = sQlabel('')
        icon.setStyleSheet("background-color: %s; margin-left:100px; margin-top:5px; margin-bottom:5px;" % str(defect['color']))
        ui_obj.classes_table.setCellWidget(i, 6, icon)
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 6, table_item)

        #ui_obj.tableWidget_defects.item(i, 6).setBackground(sQColor('#E22B2B'))
        # set date
        table_item = sQTableWidgetItem(str(defect['date']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.classes_table.setItem(i, 7, table_item)

    try:
        ui_obj.classes_table.setRowCount(i+1)

    except Exception as e:
        ui_obj.logger.create_new_log(message=texts.ERRORS['show_defefcts_on_ui_failed']['en'], level=5)
        return


def set_defects_on_train_ui(ui_obj, defects_list, defect_group_name='None'):
    """this function is used to set returned defects from database to UI defect tables

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param defects_list: list of defects
    :type defects_list: list of dicts
    :param defect_group_name: _description_, defaults to 'None'
    :type defect_group_name: str, optional
    """

    # definr table parameters
    ui_obj.table_classification_select_class.resizeColumnsToContents()
    ui_obj.table_classification_select_class.setColumnCount(len(headers_train))
    if len(defects_list) != 0:
        ui_obj.table_classification_select_class.setRowCount(defect_table_nrows)
    else:
        ui_obj.table_classification_select_class.setRowCount(0)
    ui_obj.table_classification_select_class.verticalHeader().setVisible(True)
    ui_obj.table_classification_select_class.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    ui_obj.table_classification_select_class.setHorizontalHeaderLabels(headers_train if ui_obj.language=="en" else headers_train_fa)

    # add users to table
    for i, defect in enumerate(defects_list):
        # text color
        text_color = colors_pallete.failed_red if defect['groupp'] == defect_group_name else colors_pallete.black

        # set short name
        table_item = sQTableWidgetItem(str(defect['short_name']))
        table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
        table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
        table_item.setForeground(sQColor(text_color))
        ui_obj.table_classification_select_class.setItem(i, 0, table_item)

        # set defect_ID
        table_item = sQTableWidgetItem(str(defect['defect_ID']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.table_classification_select_class.setItem(i, 1, table_item)

        # set level
        table_item = sQTableWidgetItem(str(defect['level']))
        table_item.setForeground(sQColor(text_color))
        ui_obj.table_classification_select_class.setItem(i, 2, table_item)

    try:
        ui_obj.table_classification_select_class.setRowCount(i+1)

    except:
        ui_obj.logger.create_new_log(message=texts.ERRORS['show_defefcts_on_ui_failed']['en'], level=5)
        return


# get selected users from user table in UI
def get_selected_defects(ui_obj):
    """this function is used to get selected 

    :param ui_obj: _description_
    :type ui_obj: _type_
    :return: selected defects list
    :rtype: list of dicts
    """

    list = []
    for i in range(ui_obj.classes_table.rowCount()):    
        if ui_obj.classes_table.item(i, 0).checkState() == sQtCore.Qt.Checked:
            list.append(ui_obj.classes_table.item(i, 2).text())

    return list


def get_selected_defects_for_train(ui_obj):
    """this function is used to get selected defects for model traning in ui classification model train page"""
    
    list = []
    for i in range(ui_obj.table_classification_select_class.rowCount()):    
        if ui_obj.table_classification_select_class.item(i, 0).checkState() == sQtCore.Qt.Checked:
            list.append(ui_obj.table_classification_select_class.item(i, 1).text())
    
    return list


#_______________________________________________________________________________________________________________
# load defect images from dataset(s) related to a defect class
def load_images_related_to_defect(ui_obj, datasets_list, defect_id):
    """this function is used to get image pathes list related to a defect, given selected datasets and defect

    :param datasets_list: list of datasets
    :type datasets_list: list of dicts
    :param defect_id: id of defect
    :type defect_id: _type_
    :return:
        annotation_list: list of annotation pathes for images
        image_list: list of image pathes
        binary_count: count of perfect and defect images on datasets
        classes_count: count of images related to each defects
    :rtype: _type_
    """

    annotation_list = []
    image_list = []
    binary_count = {dataset.DEFECT_FOLDER:0, dataset.PERFECT_FOLDER:0}
    classes_count = {}
    #
    for ds in datasets_list:
        ds_path = ds['path']

        # validationdataset_info_json_exists
        if validate_dataset(dataset_path=ds_path):
            # dataset main json file isnt available
            res, json_list, img_list, existed_binaries, existded_classes = dataset_info_json_exists(dataset_path=ds_path, dataset_name=ds['name'], defect_id=defect_id)

            if not res:
                related_annot_files, related_images_files, existded_classes = get_related_images_by_annotation(ui_obj=ui_obj, dataset_path=ds_path, defect_id=defect_id)
                existed_binaries = get_binary_count_by_filders(ui_obj=ui_obj, dataset_path=ds_path)
                annotation_list += related_annot_files
                image_list += related_images_files
            
            else:
                annotation_list += json_list
                image_list += img_list
        
        # add to count dicts
        binary_count = merge_classes_dictionaries(existded_classes_total=binary_count, existded_classes=existed_binaries)
        classes_count = merge_classes_dictionaries(existded_classes_total=classes_count, existded_classes=existded_classes)

    return annotation_list, image_list, binary_count, classes_count


# get image pathes realated to class using image annotations in annotation folder
def get_related_images_by_annotation(ui_obj, dataset_path, defect_id):
    """this function is used to get related images to a defect id, given dataset path and defect id

    :param dataset_path: path of dataset
    :type dataset_path: str
    :param defect_id: id of the defect
    :type defect_id: _type_
    :return: _description_
    :rtype: _type_
    """

    # annotations folder path
    annot_path = os.path.join(dataset_path, dataset.ANNOTATIONS_FOLDER)
    related_annot_files, related_images_files, existded_classes = get_jsons_related_to_defect(ui_obj=ui_obj, dirpath=annot_path, defect_id=defect_id, dataset_path=dataset_path)
    #
    return related_annot_files, related_images_files, existded_classes


def get_binary_count_by_filders(ui_obj, dataset_path):
    """this function is used to get count of defect and perfect images, by searching in dataset directory

    :param dataset_path: path of the dataset
    :type dataset_path: str
    :return: _description_
    :rtype: _type_
    """

    binary_count = {dataset.DEFECT_FOLDER:0, dataset.PERFECT_FOLDER:0}

    try:
        # len defect folder
        defect_path = os.path.join(dataset_path, dataset.BINARY_FOLDER, dataset.DEFECT_FOLDER)
        if os.path.exists(defect_path):
            binary_count[dataset.DEFECT_FOLDER] = len([s for s in os.listdir(defect_path) if os.path.isfile(os.path.join(defect_path, s)) and s[-3:]=='jpg'])
        
        # len perfect folder
        perfect_path = os.path.join(dataset_path, dataset.BINARY_FOLDER, dataset.PERFECT_FOLDER)
        if os.path.exists(perfect_path):
            binary_count[dataset.PERFECT_FOLDER] = len([s for s in os.listdir(perfect_path) if os.path.isfile(os.path.join(perfect_path, s)) and s[-3:]=='jpg'])
        
        return binary_count
    
    except Exception as e:
        ui_obj.logger.create_new_log(message=texts.ERRORS['get_binary_count_failed']['en'], level=5)
        return binary_count
        
    
# get files in a directory
def get_jsons_related_to_defect(ui_obj, dirpath, defect_id, dataset_path):
    """this function is used to get images related to a defect, by searching in each images json annotation file

    :param dirpath: directory to image json files
    :type dirpath: str
    :param defect_id: id of defect
    :type defect_id: _type_
    :param dataset_path: path of the dataset
    :type dataset_path: str
    :return:
        jsons_list: list of json pathes availebe in directory
        images_list: list of image pathes
        existded_classes_total: count of defects in dataset
    :rtype: _type_
    """

    jsons_list = []
    images_list = []
    existded_classes_total = {}
    
    try:
        a = [s for s in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, s)) and s[-4:]=='json']
        a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))

        for annot in a:
            # load json file
            try:
                with open(os.path.join(dirpath, annot)) as json_file:
                    annotations = json.load(json_file)
                json_file.close()

                # count existed defects in annotation
                existded_classes = get_existed_defects_in_image_annotation(json_annotation=annotations)
                existded_classes_total = merge_classes_dictionaries(existded_classes_total=existded_classes_total, existded_classes=existded_classes)

                # add to list if has defect class
                if check_annotation_related_to_defect(json_annotation=annotations, defect_id=defect_id):
                    # check image exist
                    image_name = annotations[Annotation.NAME]
                    # image directory
                    image_path = os.path.join(dataset_path, dataset.BINARY_FOLDER, dataset.DEFECT_FOLDER, image_name)

                    if check_image_exist_by_json(image_path=image_path):
                        jsons_list.append(os.path.join(dirpath, annot))
                        images_list.append(image_path)

            except:
                continue
        
        return jsons_list, images_list, existded_classes_total

    except Exception as e:
        ui_obj.logger.create_new_log(message=texts.ERRORS['get_images_related_to_defect_failed']['en'], level=5)
        return [], [], {}


def merge_classes_dictionaries(existded_classes_total, existded_classes):
    """this function is used to merge dictionaries

    :param existded_classes_total: _description_
    :type existded_classes_total: _type_
    :param existded_classes: _description_
    :type existded_classes: _type_
    :return: _description_
    :rtype: _type_
    """

    try:
        for cls in existded_classes.keys():
            if cls not in existded_classes_total.keys():
                existded_classes_total[cls] = existded_classes[cls]
            else:
                existded_classes_total[cls] += existded_classes[cls]
        
        return existded_classes_total
    
    except:
        return existded_classes


def check_annotation_related_to_defect(json_annotation, defect_id):
    """this function is used to check if a json annotation contating a defect

    :param json_annotation: json annotation dict
    :type json_annotation: dict
    :param defect_id: id of the defect
    :type defect_id: _type_
    :return: _description_
    :rtype: _type_
    """

    # check defect is in masks
    try:
        for obj_mask in json_annotation[Annotation.OBJ_MASKS_KEY]:
            if obj_mask[Annotation.CLASS_KEY] == str(int(defect_id)):
                return True

        #
        # for obj_bbox in json_annotation[Annotation.OBJ_BBOXS_KEY]:
        #     if obj_bbox[Annotation.CLASS_KEY] == str(int(defect_id)):
        #         return True

        #
        return False

    except:
        return False


def get_existed_defects_in_image_annotation(json_annotation):
    """this function is used to get existing defect in an image annotation

    :param json_annotation: json annotation dict
    :type json_annotation: dict
    :return: _description_
    :rtype: _type_
    """
    
    existded_classes = {}

    try:
        for obj_mask in json_annotation[Annotation.OBJ_MASKS_KEY]:
            if obj_mask[Annotation.CLASS_KEY] not in existded_classes.keys():
                existded_classes[obj_mask[Annotation.CLASS_KEY]] = 1
        
        #
        # for obj_bbox in json_annotation[Annotation.OBJ_BBOXS_KEY]:
        #     if obj_bbox[Annotation.CLASS_KEY] not in existded_classes.keys():
        #         existded_classes[obj_bbox[Annotation.CLASS_KEY]] = 1

        #
        return existded_classes
    except:
        return existded_classes


def check_image_exist_by_json(image_path):
    """this function is used to check if an image is existes

    :param image_path: path of image
    :type image_path: str
    :return: _description_
    :rtype: boolean determinin result
    """

    try:
        if os.path.exists(image_path):
            return True
        return False
        
    except:
        return False


def check_image_annotation_exist(annot_path):
    """this function is used to check if annotation exists 

    :param annot_path: path of annotation
    :type annot_path: str
    :return: boolean determining result
    :rtype: _type_
    """

    try:
        if os.path.exists(annot_path):
            return True

        return False

    except:
        return False


# dataset validation
def validate_dataset(dataset_path):
    """this function is used to vaidate a dataset folder to be in rigt format

    :param dataset_path: path of the dataset
    :type dataset_path: str
    :return: result
    :rtype: bool
    """

    # annotations
    if not os.path.exists(os.path.join(dataset_path, dataset.ANNOTATIONS_FOLDER)):
        return False

    # binary folder
    if os.path.exists(os.path.join(dataset_path, dataset.BINARY_FOLDER)):
        current_path = os.path.join(dataset_path, dataset.BINARY_FOLDER)
        # defect folder
        if os.path.exists(os.path.join(current_path, dataset.DEFECT_FOLDER)):
            return True
        else:
            return False
    else:
        
        return False


# check datasets main info json exists
def dataset_info_json_exists(dataset_path, dataset_name, defect_id):
    """this function is used to check if dataset info json is availabe, if available, return images list

    :param dataset_path: path of the dataset
    :type dataset_path: str
    :param dataset_name: name of dataset
    :type dataset_name: str
    :param defect_id: id of defect
    :type defect_id: _type_
    :return: _description_
    :rtype: _type_
    """

    jsons_list = []
    images_list = []
    #
    dataset_json_path = os.path.join(dataset_path, dataset_name+'.json')
    #
    if not os.path.exists(dataset_json_path):
        return False, jsons_list, images_list, {}, {}
    
    else:
        try:
            # open json
            with open(dataset_json_path) as json_file:
                annotations = json.load(json_file)
            json_file.close()

            # count defects
            binary_count, existded_classes = get_existed_defects_in_dataset_annotation(json_annotation=annotations)

            # check defect id is available in json file
            if str(defect_id) not in annotations[dataset_utils.CLASSIFICATION].keys():
                return True, jsons_list, images_list, binary_count, existded_classes

            else:
                for image_name in annotations[dataset_utils.CLASSIFICATION][str(defect_id)]:
                    # image directory
                    image_path = os.path.join(dataset_path, dataset.BINARY_FOLDER, dataset.DEFECT_FOLDER, image_name)

                    if check_image_exist_by_json(image_path=image_path):
                        images_list.append(image_path)

                        # annotation directory
                        annot_path = os.path.join(dataset_path, dataset.ANNOTATIONS_FOLDER, image_name[:-4]+'.json')
                        if check_image_annotation_exist(annot_path=annot_path):
                            jsons_list.append(annot_path)
                        else:
                            jsons_list.append('')
                        

            return True, jsons_list, images_list, binary_count, existded_classes

        except:
            return False, jsons_list, images_list, {}, {}


def get_existed_defects_in_dataset_annotation(json_annotation):
    """this function is used to get binary count (count of defect and perfect) and count of images related to each defect, from dataset json anootation file

    :param json_annotation: json annotation file
    :type json_annotation: _type_
    :return:
        binary_count
        existded_classes
    :rtype: _type_
    """

    existded_classes = {}
    binary_count = {dataset.DEFECT_FOLDER:0, dataset.PERFECT_FOLDER:0}
    #
    try:
        #
        for cls_id in json_annotation[dataset_utils.CLASSIFICATION].keys():
            if cls_id != dataset_utils.NONE_CLASS:
                existded_classes[cls_id] = len(json_annotation[dataset_utils.CLASSIFICATION][cls_id])
        
        #
        binary_count[dataset.DEFECT_FOLDER] = json_annotation[dataset_utils.BINARY][dataset_utils.COUNT_DEFECT]
        binary_count[dataset.PERFECT_FOLDER] = json_annotation[dataset_utils.BINARY][dataset_utils.COUNT_PERFECT]

        return binary_count, existded_classes

    except:
        return binary_count, existded_classes


        
    




import os
import shutil
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6.QtGui import QColor as sQColor
from PySide6.QtWidgets import QLabel as sQlabel
from PySide6 import QtCore as sQtCore

from backend import Annotation, colors_pallete
import string
import random
import cv2

IMAGES_TEMP_FOLDER = 'temp_images'
ANNOTATIONS_TEMP_FOLDER = 'temp_annotations'
IMAGE_FOLDERS = 'images'
ANNOTATIONS_FOLDER = 'annotations'
BINARY_FOLDER = 'binary'
DEFECT_FOLDER = 'defect'
PERFECT_FOLDER = 'perfect'
DEFECT_SPLITED_FOLDER = 'defect_splitted'
PERFECT_SPLITED_FOLDER = 'perfect_splitted'
FORMAT_IMAGE = '.jpg'
#
datasets_table_ncols = 3
datasets_table_nrows = 20
headers = ['Dataset Name', 'User Own', 'Dataset Path']


class Dataset:
    def __init__(self, dataset_path):
        self.images_temp_folder = 'temp_images'
        self.annotations_temp_folder = 'temp_annotations'
        self.images_folder = 'images'
        self.annotations_folder = 'annotations'
        self.binary_folder = 'binary'
        self.defect_folder = 'defect'
        self.perfect_folder = 'perfect'
        self.defect_mask_folder = 'defect_mask'
        self.defect_splitted_folder = 'defect_splitted'
        self.perfect_splitted_folder = 'perfect_splitted'
        self.weights = 'weights'
        self.weights_binary = 'binary'
        self.weights_localization = 'localization'
        self.weights_classification = 'classification'
        self.dataset_path = dataset_path
        self.format_image = '.png'

        # print(self.dataset_path)

        self.build_path()

    def __creat_path__(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def build_path(self, ):
        self.images_temp_path = os.path.join(self.dataset_path, self.images_temp_folder)
        self.annotations_temp_path = os.path.join(self.dataset_path, self.annotations_temp_folder)
        self.images_path = os.path.join(self.dataset_path, self.images_folder)
        self.annotations_path = os.path.join(self.dataset_path, self.annotations_folder)
        self.binary_path = os.path.join(self.dataset_path, self.binary_folder)
        self.defect_path = os.path.join(self.binary_path, self.defect_folder)
        self.defect_mask_path = os.path.join(self.binary_path, self.defect_mask_folder)
        self.perfect_path = os.path.join(self.binary_path, self.perfect_folder)
        self.defect_splitted_path = os.path.join(self.binary_path, self.defect_splitted_folder)
        self.perfect_splitted_path = os.path.join(self.binary_path, self.perfect_splitted_folder)
        self.weights_path = os.path.join(self.dataset_path, self.weights)
        self.weights_binary_path = os.path.join(self.weights_path, self.weights_binary)
        self.weights_localization_path = os.path.join(self.weights_path, self.weights_localization)
        self.weights_classification_path = os.path.join(self.weights_path, self.weights_classification)

        # print(self.annotations_folder)
        self.__creat_path__(self.dataset_path)
        self.__creat_path__(self.weights_path)
        self.__creat_path__(self.images_temp_path)
        self.__creat_path__(self.annotations_temp_path)
        self.__creat_path__(self.images_path)
        self.__creat_path__(self.annotations_path)
        self.__creat_path__(self.binary_path)
        self.__creat_path__(self.defect_path)
        self.__creat_path__(self.perfect_path)
        self.__creat_path__(self.defect_mask_path)
        self.__creat_path__(self.defect_splitted_path)
        self.__creat_path__(self.perfect_splitted_path)
        self.__creat_path__(self.weights_path)
        self.__creat_path__(self.weights_binary_path)
        self.__creat_path__(self.weights_localization_path)
        self.__creat_path__(self.weights_classification_path)

    def __random_name__(self, length):
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(length))

    def __file_name__(self, pos):
        name = ''
        pos = list(map(lambda x: str(x), pos))
        name = ''.join(pos)
        name = name.replace(',', '_')
        name = name.replace(' ', '')
        name = name.replace('(', '')
        name = name.replace(')', '')
        return name

    def save_to_temp(self, imgs_path, sheets, positions):
        for img_path, sheet, pos in zip(imgs_path, sheets, positions):
            image_name = self.__file_name__(pos) + self.format_image
            res_path = os.path.join(self.images_temp_path, image_name)
            shutil.copyfile(img_path, res_path)
            self.create_annotation_to_temp(sheet, image_name)

    def save(self, img_path, pos, sheet, masks):
        image_name = self.__file_name__(pos) + self.format_image
        res_path = os.path.join(self.images_path, image_name)
        shutil.copyfile(img_path, res_path)
        self.create_annotation_to_ds(sheet, masks, image_name, pos[-1])

    def create_annotation_to_temp(self, sheet, fname):
        image_path = os.path.join(self.images_temp_path, fname)

        json_name = fname.split('.')[0] + '.json'
        json_path = os.path.join(self.annotations_temp_path, json_name)

        annotation = Annotation.Annotation()
        annotation.set_fname(fname)
        annotation.set_sheet_id(sheet.get_id())
        annotation.set_date(sheet.get_date_string())
        annotation.set_time(sheet.get_time_string())
        annotation.set_user(sheet.get_user())
        annotation.set_pos('(,)')
        annotation.set_path(image_path)
        annotation.write(json_path)

    # def create_annotation_to_ds(self, sheet, masks, bboxes, fname, pos):
    #     image_path = os.path.join(self.images_path, fname)

    def create_annotation_to_ds(self, sheet, masks, fname, pos):
        image_path = os.path.join(self.images_path, fname)

        json_name = fname.split('.')[0] + '.json'
        json_path = os.path.join(self.annotations_path, json_name)

        annotation = Annotation.Annotation()
        annotation.set_fname(fname)
        annotation.set_sheet_id(sheet.get_id())
        annotation.set_date(sheet.get_date_string())
        annotation.set_time(sheet.get_time_string())
        annotation.set_user(sheet.get_user())
        annotation.set_pos(pos)
        annotation.set_path(image_path)
        annotation.set_masks(masks)
        annotation.write(json_path)

    # Miss Abtahi-------------------------------------

    def check_saved_defect(self, pos):
        image_name = self.__file_name__(pos) + self.format_image
        image_path = os.path.join(self.defect_path, image_name)
        if os.path.exists(image_path):
            return True
        return False

    def check_saved_perfect(self, pos):
        image_name = self.__file_name__(pos) + self.format_image
        image_path = os.path.join(self.perfect_path, image_name)
        if os.path.exists(image_path):
            return True
        return False

    def save_to_defect(self, img_path, pos, mask):
        image_name = self.__file_name__(pos) + self.format_image
        res_path = os.path.join(self.defect_path, image_name)
        mask_path = os.path.join(self.defect_mask_path, image_name)
        shutil.copyfile(img_path, res_path)
        cv2.imwrite(mask_path, mask)

    def delete_from_defect(self, pos):
        image_name = self.__file_name__(pos) + self.format_image
        path = os.path.join(self.defect_path, image_name)
        mask_path = os.path.join(self.defect_mask_path, image_name)
        os.remove(path)
        os.remove(mask_path)

    def save_to_perfect(self, img_path, pos):
        image_name = self.__file_name__(pos) + self.format_image
        res_path = os.path.join(self.perfect_path, image_name)
        shutil.copyfile(img_path, res_path)

    def delete_from_perfect(self, pos):
        image_name = self.__file_name__(pos) + self.format_image
        path = os.path.join(self.perfect_path, image_name)
        os.remove(path)

    def save_to_defect_splitted(self, crops, path='', pos='', name=''):
        if path == '': path = self.defect_splitted_path
        if pos != '':
            name = self.__file_name__(pos)
        for i in range(crops.shape[0]):
            image_name = name + '_(' + str(i) + ')' + self.format_image
            res_path = os.path.join(path, image_name)
            cv2.imwrite(res_path, crops[i])

    def delete_from_defect_splitted(self, pos):
        image_name = self.__file_name__(pos)
        imgs = os.listdir(self.defect_splitted_path)
        for img in imgs:
            if img.startswith(image_name):
                path = os.path.join(self.defect_splitted_path, img)
                os.remove(path)

    def save_to_perfect_splitted(self, crops, path='', pos='', name=''):
        if path == '': path = self.perfect_splitted_path
        if pos != '':
            name = self.__file_name__(pos)
        for i in range(crops.shape[0]):
            image_name = name + '_(' + str(i) + ')' + self.format_image
            res_path = os.path.join(path, image_name)
            cv2.imwrite(res_path, crops[i])

    def delete_from_perfect_splitted(self, pos):
        image_name = self.__file_name__(pos)
        imgs = os.listdir(self.perfect_splitted_path)
        for img in imgs:
            if img.startswith(image_name):
                path = os.path.join(self.perfect_splitted_path, img)
                os.remove(path)

    def check_binary_dataset(self, dataset_path):
        defect_path = os.path.join(dataset_path, self.defect_folder)
        perfect_path = os.path.join(dataset_path, self.perfect_folder)
        defect_mask_path = os.path.join(dataset_path, self.defect_mask_folder)
        return os.path.exists(defect_path) and os.path.exists(perfect_path)

    def create_split_folder(self, dataset_path):
        defect_splitted_path = os.path.join(dataset_path, self.defect_splitted_folder)
        perfect_splitted_path = os.path.join(dataset_path, self.perfect_splitted_folder)
        if os.path.exists(defect_splitted_path):
            shutil.rmtree(defect_splitted_path)
        if os.path.exists(perfect_splitted_path):
            shutil.rmtree(perfect_splitted_path)
        self.__creat_path__(defect_splitted_path)
        self.__creat_path__(perfect_splitted_path)
    # ---------------------------------------------------


# get datasets list from db
def get_datasets_list_from_db(db_obj):
    ds_list = db_obj.load_datasets()
    return ds_list


# set datasets on UI table
def set_datasets_on_ui(ui_obj, datasets_list, current_user='', default_dataset='', is_binarylist=False):
    # dataset object
    if is_binarylist:
        table_object = ui_obj.datasets_table_binarylist
    else:
        table_object = ui_obj.datasets_table
    #
    print('def', default_dataset)
    # definr table parameters
    table_object.resizeColumnsToContents()
    table_object.setColumnCount(datasets_table_ncols)
    print('len', len(datasets_list))
    if len(datasets_list) != 0:
        table_object.setRowCount(datasets_table_nrows)
    else:
        table_object.setRowCount(0)

    table_object.verticalHeader().setVisible(True)
    table_object.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    table_object.setHorizontalHeaderLabels(headers)

    # add users to table
    for i, dataset in enumerate(datasets_list):
        # text color
        text_color = colors_pallete.successfull_green if dataset['user_own'] == current_user else colors_pallete.black
        # set name
        table_item = sQTableWidgetItem(str(dataset['name']))
        table_item.setFlags(sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled)
        table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
        if str(dataset['name']) == default_dataset:
            table_item.setCheckState(sQtCore.Qt.CheckState.Checked)
        table_item.setForeground(sQColor(text_color))
        table_object.setItem(i, 0, table_item)
        # set user_own
        table_item = sQTableWidgetItem(str(dataset['user_own']))
        table_item.setForeground(sQColor(text_color))
        table_object.setItem(i, 1, table_item)
        # set path
        table_item = sQTableWidgetItem(str(dataset['path']))
        table_item.setForeground(sQColor(text_color))
        table_object.setItem(i, 2, table_item)

    try:
        table_object.setRowCount(i + 1)
    except:
        return


# get selected users from user table in UI
def get_selected_datasets(ui_obj, datasets_list, is_binarylist=False):
    # dataset object
    if is_binarylist:
        table_object = ui_obj.datasets_table_binarylist
    else:
        table_object = ui_obj.datasets_table
    #
    list = []
    for i in range(table_object.rowCount()):
        if table_object.item(i, 0).checkState() == sQtCore.Qt.Checked:
            #
            for dataset in datasets_list:
                if dataset['name'] == table_object.item(i, 0).text():
                    list.append(dataset)
    return list


if __name__ == '__main__':
    ds = Dataset('a')

    for i in range(100):
        print(ds.__random_name__(9))

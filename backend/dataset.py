import os
import shutil
from PySide6.QtWidgets import QHeaderView as sQHeaderView
from PySide6.QtWidgets import QTableWidgetItem as sQTableWidgetItem
from PySide6.QtGui import QColor as sQColor
from PySide6.QtWidgets import QLabel as sQlabel
from PySide6 import QtCore as sQtCore

from backend import Annotation, colors_pallete
import texts
import string
import random
import cv2

IMAGES_TEMP_FOLDER = "temp_images"
ANNOTATIONS_TEMP_FOLDER = "temp_annotations"
IMAGE_FOLDERS = "images"
ANNOTATIONS_FOLDER = "annotations"
BINARY_FOLDER = "binary"
DEFECT_FOLDER = "defect"
PERFECT_FOLDER = "perfect"
MASKS_FOLDER = "mask"
DEFECT_SPLITED_FOLDER = "defect_splitted"
PERFECT_SPLITED_FOLDER = "perfect_splitted"

#-------------------
WRONG_PREDICT_IMAGES='wrong_predict_images'
FP='false_positive'
FN='false_negative'
#-------------------

FORMAT_IMAGE = ".jpg"
#
datasets_table_ncols = 3
datasets_table_nrows = 20
headers = ["Dataset Name", "Owner User", "Dataset Path"]
headers_fa = ["نام مجموعه داده", "کاربر مالک", "آدرس مجموعه داده"]


class Dataset:
    def __init__(self, dataset_path):
        self.images_temp_folder = "temp_images"
        self.annotations_temp_folder = "temp_annotations"
        self.images_folder = "images"
        self.annotations_folder = "annotations"
        self.binary_folder = "binary"
        self.defect_folder = "defect"
        self.perfect_folder = "perfect"
        self.defect_mask_folder = "defect_mask"
        self.defect_splitted_folder = "defect_splitted"
        self.perfect_splitted_folder = "perfect_splitted"
        self.localization_folder = "localization"
        self.localization_folder_image = "image"
        self.localization_folder_label = "label"
        self.localization_folder_image_splitted = "image_splitted"
        self.localization_folder_label_splitted = "label_splitted"
        self.weights = "weights"
        self.weights_binary = "binary"
        self.weights_localization = "localization"
        self.weights_classification = "classification"
        self.dataset_path = dataset_path

        #--------------
        self.wrong_images_folder = 'wrong_predict_images'
        self.wrong_images_folder_fp = 'false_positive'
        self.wrong_images_folder_fn = 'false_negative'
        #--------------

        self.format_image = ".png"

        # print(self.dataset_path)

        self.build_path()

    def __creat_path__(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def build_path(
        self,
    ):
        self.images_temp_path = os.path.join(self.dataset_path, self.images_temp_folder)
        self.annotations_temp_path = os.path.join(
            self.dataset_path, self.annotations_temp_folder
        )
        self.images_path = os.path.join(self.dataset_path, self.images_folder)
        self.annotations_path = os.path.join(self.dataset_path, self.annotations_folder)
        self.binary_path = os.path.join(self.dataset_path, self.binary_folder)
        self.defect_path = os.path.join(self.binary_path, self.defect_folder)
        self.defect_mask_path = os.path.join(self.binary_path, self.defect_mask_folder)
        self.perfect_path = os.path.join(self.binary_path, self.perfect_folder)
        self.defect_splitted_path = os.path.join(
            self.binary_path, self.defect_splitted_folder
        )
        self.perfect_splitted_path = os.path.join(
            self.binary_path, self.perfect_splitted_folder
        )
        self.localization_path = os.path.join(
            self.dataset_path, self.localization_folder
        )
        self.localization_image_path = os.path.join(
            self.localization_path, self.localization_folder_image
        )
        self.localization_label_path = os.path.join(
            self.localization_path, self.localization_folder_label
        )
        self.localization_image_splitted_path = os.path.join(
            self.localization_path, self.localization_folder_image_splitted
        )
        self.localization_label_splitted_path = os.path.join(
            self.localization_path, self.localization_folder_label_splitted
        )
        self.weights_path = os.path.join(self.dataset_path, self.weights)
        self.weights_binary_path = os.path.join(self.weights_path, self.weights_binary)
        self.weights_localization_path = os.path.join(
            self.weights_path, self.weights_localization
        )
        self.weights_classification_path = os.path.join(
            self.weights_path, self.weights_classification
        )

        #-------------
        self.wrong_images_path = os.path.join(
            self.dataset_path, self.wrong_images_folder
        )
        # self.wrong_iamges_fp_path = os.path.join(
        #     self.wrong_iamges_path, self.wrong_images_folder_fp
        # )
        # self.wrong_iamges_fn_path = os.path.join(
        #     self.wrong_iamges_path, self.wrong_images_folder_fn
        # )
        #-------------
    

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
        self.__creat_path__(self.localization_path)
        self.__creat_path__(self.localization_image_path)
        self.__creat_path__(self.localization_label_path)
        self.__creat_path__(self.localization_image_splitted_path)
        self.__creat_path__(self.localization_label_splitted_path)
        self.__creat_path__(self.weights_path)
        self.__creat_path__(self.weights_binary_path)
        self.__creat_path__(self.weights_localization_path)
        self.__creat_path__(self.weights_classification_path)
        #--------------- 
        self.__creat_path__(self.wrong_images_path)
        # self.__creat_path__(self.wrong_iamges_fp_path)
        # self.__creat_path__(self.wrong_iamges_fn_path)
        #---------------
    #____________________________________JJ ZONE
    def creat_folder_structure_of_wrong_predict_images(self,pipline_name):
        
        #creat dirctory name
        pipline_wrong_result_path=os.path.join(self.wrong_images_path, pipline_name)
        self.pipline_wrong_result_fp_path=os.path.join(pipline_wrong_result_path,self.wrong_images_folder_fp)
        self.pipline_wrong_result_fn_path=os.path.join(pipline_wrong_result_path,self.wrong_images_folder_fn)

        #creat dirctory 
        self.__creat_path__(pipline_wrong_result_path)
        self.__creat_path__(self.pipline_wrong_result_fp_path)
        self.__creat_path__(self.pipline_wrong_result_fn_path)


    def write_image_in_fn_fp_folder(self,fn,img,file_name):
        if fn:
            cv2.imwrite(os.path.join(self.pipline_wrong_result_fn_path,file_name),img)
        else:
            cv2.imwrite(os.path.join(self.pipline_wrong_result_fp_path,file_name),img)
        
    #____________________________________JJ ZONE


    def __random_name__(self, length):
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return "".join(random.choice(letters) for i in range(length))

    def __file_name__(self, pos):
        name = ""
        pos = list(map(lambda x: str(x), pos))
        name = "".join(pos)
        name = name.replace(",", "_")
        name = name.replace(" ", "")
        name = name.replace("(", "")
        name = name.replace(")", "")
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

        json_name = fname.split(".")[0] + ".json"
        json_path = os.path.join(self.annotations_temp_path, json_name)

        annotation = Annotation.Annotation()
        annotation.set_fname(fname)
        annotation.set_sheet_id(sheet.get_id())
        annotation.set_date(sheet.get_date_string())
        annotation.set_time(sheet.get_time_string())
        annotation.set_user(sheet.get_user())
        annotation.set_pos("(,)")
        annotation.set_path(image_path)
        annotation.write(json_path)

    # def create_annotation_to_ds(self, sheet, masks, bboxes, fname, pos):
    #     image_path = os.path.join(self.images_path, fname)

    def create_annotation_to_ds(self, sheet, masks, fname, pos):
        image_path = os.path.join(self.images_path, fname)

        json_name = fname.split(".")[0] + ".json"
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

    def get_label_from_annotation(self, pos):
        fname = self.__file_name__(pos) + ".json"
        json_path = os.path.join(self.annotations_path, fname)
        if not os.path.exists(json_path):
            return []
        file = Annotation.Annotation().read(json_path)
        return file["obj_masks"]

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
        loc_image_path = os.path.join(self.localization_image_path, image_name)
        loc_label_path = os.path.join(self.localization_label_path, image_name)
        shutil.copyfile(img_path, res_path)
        shutil.copyfile(img_path, loc_image_path)
        cv2.imwrite(mask_path, mask)
        shutil.copyfile(mask_path, loc_label_path)

    def delete_from_defect(self, pos):
        image_name = self.__file_name__(pos) + self.format_image
        path = os.path.join(self.defect_path, image_name)
        mask_path = os.path.join(self.defect_mask_path, image_name)
        loc_image_path = os.path.join(self.localization_image_path, image_name)
        loc_label_path = os.path.join(self.localization_label_path, image_name)
        os.remove(path)
        os.remove(mask_path)
        os.remove(loc_image_path)
        os.remove(loc_label_path)

    def save_to_perfect(self, img_path, pos):
        image_name = self.__file_name__(pos) + self.format_image
        res_path = os.path.join(self.perfect_path, image_name)
        shutil.copyfile(img_path, res_path)

    def delete_from_perfect(self, pos):
        image_name = self.__file_name__(pos) + self.format_image
        path = os.path.join(self.perfect_path, image_name)
        os.remove(path)

    def save_to_defect_splitted(self, crops, path="", pos="", name=""):
        if path == "":
            path = self.defect_splitted_path
        if pos != "":
            name = self.__file_name__(pos)
        for i in range(crops.shape[0]):
            image_name = name + "_(" + str(i) + ")" + self.format_image
            res_path = os.path.join(path, image_name)
            cv2.imwrite(res_path, crops[i])

    def delete_from_defect_splitted(self, pos):
        image_name = self.__file_name__(pos)
        imgs = os.listdir(self.defect_splitted_path)
        for img in imgs:
            if img.startswith(image_name):
                path = os.path.join(self.defect_splitted_path, img)
                os.remove(path)

    def save_to_perfect_splitted(self, crops, path="", pos="", name=""):
        if path == "":
            path = self.perfect_splitted_path
        if pos != "":
            name = self.__file_name__(pos)
        for i in range(crops.shape[0]):
            image_name = name + "_(" + str(i) + ")" + self.format_image
            res_path = os.path.join(path, image_name)
            cv2.imwrite(res_path, crops[i])

    def delete_from_perfect_splitted(self, pos):
        image_name = self.__file_name__(pos)
        imgs = os.listdir(self.perfect_splitted_path)
        for img in imgs:
            if img.startswith(image_name):
                path = os.path.join(self.perfect_splitted_path, img)
                os.remove(path)

    def save_localization_splits(
        self, image_crops, label_crops, image_path, label_path, name=""
    ):
        for i in range(image_crops.shape[0]):
            image_name = name + "_(" + str(i) + ")" + self.format_image
            res_path = os.path.join(image_path, image_name)
            cv2.imwrite(res_path, image_crops[i])

            res_path = os.path.join(label_path, image_name)
            cv2.imwrite(res_path, label_crops[i])

    def check_binary_dataset(self, dataset_path):
        defect_path = os.path.join(dataset_path, self.defect_folder)
        perfect_path = os.path.join(dataset_path, self.perfect_folder)
        defect_mask_path = os.path.join(dataset_path, self.defect_mask_folder)
        return os.path.exists(defect_path) and os.path.exists(perfect_path)

    def check_localization_dataset(self, dataset_path):
        image_path = os.path.join(dataset_path, self.localization_folder_image)
        label_path = os.path.join(dataset_path, self.localization_folder_label)
        return os.path.exists(image_path) and os.path.exists(label_path)

    def create_split_folder(self, dataset_path):
        defect_splitted_path = os.path.join(dataset_path, self.defect_splitted_folder)
        perfect_splitted_path = os.path.join(dataset_path, self.perfect_splitted_folder)
        if os.path.exists(defect_splitted_path):
            shutil.rmtree(defect_splitted_path)
        if os.path.exists(perfect_splitted_path):
            shutil.rmtree(perfect_splitted_path)
        self.__creat_path__(defect_splitted_path)
        self.__creat_path__(perfect_splitted_path)

    def create_l_split_folder(self, dataset_path):
        image_splitted_path = os.path.join(
            dataset_path, self.localization_folder_image_splitted
        )
        label_splitted_path = os.path.join(
            dataset_path, self.localization_folder_label_splitted
        )
        if os.path.exists(image_splitted_path):
            shutil.rmtree(image_splitted_path)
        if os.path.exists(label_splitted_path):
            shutil.rmtree(label_splitted_path)
        self.__creat_path__(image_splitted_path)
        self.__creat_path__(label_splitted_path)

    # ---------------------------------------------------


# get datasets list from db
def get_datasets_list_from_db(db_obj):
    """this function is used to get datasets from database table

    :param db_obj: database object
    :type db_obj: _type_
    :return: datasets lits
    :rtype: _type_
    """

    res, ds_list = db_obj.load_datasets()
    return res, ds_list


# set datasets on UI table
def set_datasets_on_ui(
    ui_obj,
    datasets_list,
    current_user="",
    default_dataset="",
    is_binarylist=False,
    PBT_page=False,
):
    """this function is used to set datasets list on UI table

    :param ui_obj: main ui obj
    :type ui_obj: _type_
    :param datasets_list: datasets list from database
    :type datasets_list: list of dicts
    :param current_user: name of current user, this is used to highlight this users datasets, defaults to ''
    :type current_user: str, optional
    :param default_dataset: name of defeault database of this user, defaults to ''
    :type default_dataset: str, optional
    :param is_binarylist: boolean determining whether to refresh binarylist dataset table, defaults to False
    :type is_binarylist: bool, optional
    """

    PBT_option_list = []

    # dataset object
    if is_binarylist:
        table_object = ui_obj.datasets_table_binarylist
    else:
        table_object = ui_obj.datasets_table
    #
    # definr table parameters
    table_object.resizeColumnsToContents()
    table_object.setColumnCount(datasets_table_ncols)

    if len(datasets_list) != 0:
        table_object.setRowCount(datasets_table_nrows)
    else:
        table_object.setRowCount(0)

    table_object.verticalHeader().setVisible(True)
    # table_object.horizontalHeader().setSectionResizeMode(sQHeaderView.Stretch)
    table_object.setHorizontalHeaderLabels(
        headers if ui_obj.language == "en" else headers_fa
    )

    # add users to table
    for i, dataset in enumerate(datasets_list):
        # text color
        text_color = (
            colors_pallete.successfull_green
            if dataset["user_own"] == current_user
            else colors_pallete.black
        )
        # set name
        table_item = sQTableWidgetItem(str(dataset["name"]))
        if PBT_page:
            PBT_option_list.append(str(dataset["name"]))
        table_item.setFlags(
            sQtCore.Qt.ItemFlag.ItemIsUserCheckable | sQtCore.Qt.ItemFlag.ItemIsEnabled
        )
        table_item.setCheckState(sQtCore.Qt.CheckState.Unchecked)
        if str(dataset["name"]) == default_dataset:
            table_item.setCheckState(sQtCore.Qt.CheckState.Checked)
        table_item.setForeground(sQColor(text_color))
        table_object.setItem(i, 0, table_item)
        # set user_own
        table_item = sQTableWidgetItem(str(dataset["user_own"]))
        table_item.setForeground(sQColor(text_color))
        table_object.setItem(i, 1, table_item)
        # set path
        table_item = sQTableWidgetItem(str(dataset["path"]))
        table_item.setForeground(sQColor(text_color))
        table_object.setItem(i, 2, table_item)

    try:
        table_object.setRowCount(i + 1)
        if PBT_page:
            ui_obj.cbBox_of_dataset_in_PBT_page_load_dataset.clear()
            ui_obj.cbBox_of_dataset_in_PBT_page_load_dataset.addItems(PBT_option_list)
            return PBT_option_list
    except:
        return


# get selected users from user table in UI
def get_selected_datasets(ui_obj, datasets_list, is_binarylist=False):
    """this function is used to get selected datasets from UI table

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param datasets_list: list of all datasets
    :type datasets_list: list of dicts
    :param is_binarylist: boolean determining whether in binarylist page, defaults to False
    :type is_binarylist: bool, optional
    :return: selected datasets list
    :rtype: list of dicts
    """

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
                if dataset["name"] == table_object.item(i, 0).text():
                    list.append(dataset)

    return list


def get_selected_datasets_for_PBT_loadDataSet_page(datasetname, datasets_list):

    list = []
    for dataset in datasets_list:
        if dataset["name"] == datasetname:
            list.append(dataset)
    return list


if __name__ == "__main__":
    ds = Dataset("a")

    for i in range(100):
        print(ds.__random_name__(9))

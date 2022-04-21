import os
import shutil
from backend import Annotation
import string
import random
import cv2
class Dataset:


    def __init__(self, dataset_path, weights_path):
        self.images_temp_folder = 'temp_images'
        self.annotations_temp_folder = 'temp_annotations'
        self.images_folder = 'images'
        self.annotations_folder = 'annotations'
        self.binary_folder = 'binary'
        self.defect_folder = 'defect'
        self.perfect_folder = 'perfect'
        self.defect_splitted_folder = 'defect_splitted'
        self.perfect_splitted_folder = 'perfect_splitted'
        self.dataset_path = dataset_path
        self.weights_path = weights_path
        self.format_image = '.jpg'

        # print(self.dataset_path)

        self.build_path()
        



    def __creat_path__(self,path):
        if not os.path.exists(path):
            os.makedirs(path)


    def build_path(self,):
        self.images_temp_path = os.path.join( self.dataset_path, self.images_temp_folder )
        self.annotations_temp_path = os.path.join( self.dataset_path, self.annotations_temp_folder )
        self.images_path = os.path.join( self.dataset_path, self.images_folder )
        self.annotations_path = os.path.join( self.dataset_path, self.annotations_folder )
        self.binary_path = os.path.join( self.dataset_path, self.binary_folder )
        self.defect_path = os.path.join( self.binary_path, self.defect_folder )
        self.perfect_path = os.path.join( self.binary_path, self.perfect_folder )
        self.defect_splitted_path = os.path.join(self.binary_path, self.defect_splitted_folder)
        self.perfect_splitted_path = os.path.join(self.binary_path, self.perfect_splitted_folder)
        self.weights_binary_path = os.path.join(self.weights_path, self.binary_folder)
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
        self.__creat_path__(self.defect_splitted_path)
        self.__creat_path__(self.perfect_splitted_path)
        self.__creat_path__(self.weights_binary_path)


    def __random_name__(self, length):
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(length))


    def save_to_temp(self, imgs_path , sheets):
        for img_path, sheet in zip(imgs_path, sheets ):
            image_name = self.__random_name__(10) + self.format_image 
            res_path = os.path.join(  self.images_temp_path, image_name )
            shutil.copyfile(img_path, res_path )
            self.create_annotation_to_temp(sheet, image_name)



    def create_annotation_to_temp(self,sheet,fname):
        image_path = os.path.join(  self.images_temp_path, fname  )

        json_name = fname.split('.')[0] + '.json'
        json_path = os.path.join(self.annotations_temp_path, json_name)

        annotation=Annotation.Annotation()
        annotation.set_fname(fname)
        annotation.set_sheet_id(sheet.get_id())
        annotation.set_date(sheet.get_date_string())
        annotation.set_time(sheet.get_time_string())
        annotation.set_user(sheet.get_user())
        annotation.set_pos('(,)')
        annotation.set_path(image_path)
        annotation.write(json_path)


    def save_to_defect(self, img_path):
        # image_name = os.path.split(img_path)[-1]
        image_name = self.__random_name__(10) + self.format_image
        res_path = os.path.join(self.defect_path, image_name)
        shutil.copyfile(img_path, res_path)

    def save_to_perfect(self, img_path):
        # image_name = os.path.split(img_path)[-1]
        image_name = self.__random_name__(10) + self.format_image
        res_path = os.path.join(self.perfect_path, image_name)
        shutil.copyfile(img_path, res_path)

    def save_to_defect_splitted(self, crops, path=''):
        # name = os.path.split(img_path)[-1]
        if path == '': path = self.defect_splitted_path
        for i in range(crops.shape[0]):
            for j in range(crops.shape[1]):
                # image_name = name + '_' + str(i) + '_' + str(j)
                image_name = self.__random_name__(10) + self.format_image
                res_path = os.path.join(path, image_name)
                cv2.imwrite(res_path, crops[i, j])

    def save_to_perfect_splitted(self, crops, path=''):
        # name = os.path.split(img_path)[-1]
        if path == '': path = self.perfect_splitted_path
        for i in range(crops.shape[0]):
            for j in range(crops.shape[1]):
                # image_name = name.split('.')[0] + '_' + str(i) + '_' + str(j) + name.split('.')[1]
                image_name = self.__random_name__(10) + self.format_image
                res_path = os.path.join(path, image_name)
                cv2.imwrite(res_path, crops[i, j])

    def check_binary_dataset(self, dataset_path):
        defect_path = os.path.join(dataset_path, self.defect_folder)
        perfect_path = os.path.join(dataset_path, self.perfect_folder)
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

if __name__ == '__main__':
    ds = Dataset('a')

    for i in range(100):
        print(ds.__random_name__(9))
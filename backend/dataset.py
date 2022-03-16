import os
import shutil
from backend import Annotation
import string
import random
class Dataset:


    def __init__(self, dataset_path):
        self.images_temp_folder = 'temp_images'
        self.annotations_temp_folder = 'temp_annotations'
        self.images_folder = 'images'
        self.annotations_folder = 'annotations'
        self.dataset_path = dataset_path
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
        # print(self.annotations_folder)
        self.__creat_path__(self.dataset_path)
        self.__creat_path__(self.images_temp_path)
        self.__creat_path__(self.annotations_temp_path)
        self.__creat_path__(self.images_path)
        self.__creat_path__(self.annotations_path)




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



if __name__ == '__main__':
    ds = Dataset('a')

    for i in range(100):
        print(ds.__random_name__(9))
import os
import shutil
import Annotation

class Dataset:


    def __init__(self, dataset_path):
        self.images_temp_folder = 'temp_iamges'
        self.annotations_temp_folder = 'temp_annotations'
        self.images_folder = 'images'
        self.annotations_folder = 'annotations'
        self.dataset_path = dataset_path

        self.build_path()
        



    def __creat_path__(self,path):
        if not os.path.exists(path):
            os.makedirs(path)


    def build_path(self,):
        self.images_temp_path = os.path.join( self.dataset_path, self.images_temp_folder )
        self.annotations_temp_path = os.path.join( self.dataset_path, self.annotations_temp_folder )
        self.images_path = os.path.join( self.dataset_path, self.images_folder )
        self.annotations_path = os.path.join( self.dataset_path, self.annotations_folder )

        self.__creat_path__(self.images_temp_path)
        self.__creat_path__(self.annotations_temp_path)
        self.__creat_path__(self.images_path)
        self.__creat_path__(self.annotations_path)




    


    def save_to_temp(self, dataset_path, imgs_path):
        for img_path in imgs_path:
            res_path = os.path.join(  dataset_path, self.temp_folder )
            shutil.copyfile(img_path, res_path )

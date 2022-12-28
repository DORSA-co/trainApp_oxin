import os
import random
import sys
import shutil
import numpy as np

src_path = 'data/steel_defects/all/'
dst_path = 'data/steel_defects'
symlinkPath = 'SymLink'
split = 0.2

def bar(counter,n):
    percent = counter/n*100
    os.system('cls')
    print('percent={:.2f}%  |{}| n={} of {}'.format(percent, int(percent/2)*'◼' + int(50 - percent/2)*'-' ,int(counter), n))

def copy(src, dst):
    """This is function to copy images and symlinks

    :param src: Source path.
    :type src: str
    :param dst: Destination path.
    :type dst: str
    """
    if os.path.islink(src):
        if os.path.lexists(dst):
            os.unlink(dst)
        linkto = os.readlink(src)
        os.symlink(linkto, dst)
    else:
        shutil.copy(src, dst)

def create_localization_symlink(paths, image_folder='image', label_folder='label'):
    """This function is used to create symlinks of localization datasets.

    :param paths: Paths of localization datasets.
    :type paths: list
    :param image_folder: Image subfolder in symlink path, defaults to 'image'
    :type image_folder: str, optional
    :param label_folder: Label subfolder in symlink path, defaults to 'label'
    :type label_folder: str, optional
    """
    symlink_image_path = os.path.join(symlinkPath, image_folder)
    symlink_label_path = os.path.join(symlinkPath, label_folder)

    if os.path.exists(symlink_image_path):
        shutil.rmtree(symlink_image_path)
    os.makedirs(symlink_image_path)

    if os.path.exists(symlink_label_path):
        shutil.rmtree(symlink_label_path)
    os.makedirs(symlink_label_path)

    for path in paths:
        absPath = os.path.abspath(path)
        image_path = os.path.join(absPath, image_folder+'/*')
        os.system('ln -s ' + image_path + ' ' + symlink_image_path)

        label_path = os.path.join(absPath, label_folder+'/*')
        os.system('ln -s ' + label_path + ' ' + symlink_label_path)
       
def split_unet_dataset(paths, img_folder='image', label_folder='label', mulit_mask_class=False, split=0.2):
    """Split mask dataset into train and test.

    :param paths: Paths of localization datasets.
    :type paths: list
    :param img_folder: Image subfolder in symlink path, defaults to 'image'
    :type img_folder: str, optional
    :param label_folder: Label subfolder in symlink path, defaults to 'label'
    :type label_folder: str, optional
    :param mulit_mask_class: If label_folder contain some folder for each class it should be True, O.W if label folder 
    only contain images for one class it should be False, defaults to False
    :type mulit_mask_class: bool, optional
    :param split: Split percentage for Test, defaults to 0.2
    :type split: float, optional
    """
    create_localization_symlink(paths, img_folder, label_folder)

    src_path = os.path.abspath(symlinkPath)
    dst_path = os.path.abspath(symlinkPath)

    imgs_list = os.listdir( os.path.join( src_path, img_folder))
    #-------------------------------------
    #calc train and test count for split
    nimage = len(imgs_list)
    ntest = int(split * nimage)
    ntrain= nimage - ntest
    print("{} images split into {} train / {} test".format(nimage, ntrain, ntest))
    #-------------------------------------
    #obtain sources path for image and mask
    images_dir = os.path.join(src_path, img_folder)
    labels_dir = os.path.join(src_path, label_folder)
    #-------------------------------------
    folders_1 = ['train', 'test']
    folders_2 = ['image', 'label']
    if mulit_mask_class:
        folders_classes = os.listdir(labels_dir)
        folders_classes = list( filter ( lambda x:os.path.isdir(os.path.join(labels_dir,x)),
                                     folders_classes ))
        
        assert len(folders_classes)>0, 'multi_classes is True but Threre is no sub folder in {}'.format(os.path.join(src_path,label_folder))

            
    #-------------------------------------
    #remove dst contain folders if exist
    for f1 in folders_1:
        _path_ = os.path.join(dst_path,f1)
        if os.path.exists( _path_ ):
            shutil.rmtree( _path_ )
            
    
            
    #-------------------------------------
    __route__ = os.path.split(dst_path)
    for i in range(len(__route__)):
        __path__ = '//'.join(__route__[:i+1])
        if not os.path.exists(__path__):
            os.mkdir(__path__)
    #-------------------------------------
    
    #create all sub folders for dst
    for f1 in folders_1:
        _path_ = os.path.join( dst_path, f1)
        os.mkdir(_path_)
    
    for f1 in folders_1:
        for f2 in folders_2:
            _path_ = os.path.join( dst_path, f1,f2)
            os.mkdir(_path_)
    
    if mulit_mask_class:
        for f1 in folders_1:
            for f3 in folders_classes:  
                _path_ = os.path.join( dst_path, f1,folders_2[1],f3 )
                os.mkdir(_path_)

    #-------------------------------------
    #split images list into train and test
    random.shuffle(imgs_list)
    test_img_list = imgs_list[:ntest]
    train_img_list = imgs_list[ntest:]  
    lists_dict = {folders_1[0]:train_img_list, folders_1[1]:test_img_list}
    #-------------------------------------------------
    counter = 0
    for f1,fname_list in lists_dict.items():    
        for fname in fname_list:
            for f2 in folders_2:
                
                if f2 == 'image': #just copy image into corespond label
                    src = os.path.join(src_path, img_folder, fname )
                    dst = os.path.join(dst_path,f1, f2, fname )
                    copy( src, dst)
                
                else:
                    if not mulit_mask_class:
                        src = os.path.join(src_path, label_folder, fname )
                        dst = os.path.join(dst_path,f1, f2, fname )
                        copy( src, dst)
                    
                    else:
                        for f3 in folders_classes:
                            src = os.path.join(src_path, label_folder,f3, fname )
                            dst = os.path.join(dst_path,f1, f2, f3, fname )
                            copy( src, dst)

    return os.path.join(src_path, 'train'), os.path.join(dst_path, 'test'), ntrain, ntest
                            
                        
    #         counter+=1  
    #         if counter%5==0:
    #             bar(counter,nimage)
    # bar(counter,nimage)











if __name__ == '__main__':
    split_unet_dataset('data/allmc', 'data/mask_class', img_folder='image', label_folder='label', mulit_mask_class=True, split=0.2)



from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import copy
# import texts
import shutil
import cv2
import random
import segmentation_models as sm
import yaml

sm.set_framework("tf.keras")
sm.framework()

aug_dict = dict(rotation_range=15,
                width_shift_range=0.1,
                height_shift_range=0.1,
                shear_range=0.05,
                zoom_range=0.1,
                horizontal_flip=True,
                fill_mode='constant',
                )

symlinkMainPath = 'SymLink'
symlinkPath = 'SymLink/binary'
yolo_data_path = 'SymLink/localization_and_classification/data' #'/home/reyhane/.local/lib/python3.10/site-packages/yolov5/data'

def create_binary_symlink(paths, binary_folder, defect_folder, perfect_folder):
    """This function is used to create symlinks of binary datasets.

    :param paths: Path of binary datasets
    :type paths: list
    :param defect_folder: Subfolder for defective image.
    :type defect_folder: str
    :param perfect_folder: Subfolder for perfect image.
    :type perfect_folder: str
    """
    symlink_defect_path = os.path.join(symlinkPath, defect_folder)
    symlink_perfect_path = os.path.join(symlinkPath, perfect_folder)

    if os.path.exists(symlink_defect_path):
        shutil.rmtree(symlink_defect_path)
    os.makedirs(symlink_defect_path)

    if os.path.exists(symlink_perfect_path):
        shutil.rmtree(symlink_perfect_path)
    os.makedirs(symlink_perfect_path)

    for path in paths:
        path = os.path.join(path, binary_folder)
        absPath = os.path.abspath(path)
        defect_path = os.path.join(absPath, defect_folder)
        for i in os.listdir(defect_path):
            os.system('ln -s ' + os.path.join(defect_path, i) + ' ' + symlink_defect_path)

        perfect_path = os.path.join(absPath, perfect_folder)
        for i in os.listdir(perfect_path):
            os.system('ln -s ' + os.path.join(perfect_path, i) + ' ' + symlink_perfect_path)


def get_binarygenerator(paths, target_size, defective_folder, perfect_folder, aug_dict, api_obj, batch_size=8, validation_split=0.2):
    """return two binary generators (train and test).

    :param paths: A list of dataset paths.
    :type paths: list
    :param target_size: Target size of image.
    :type target_size: tuple
    :param defective_folder: Subfolder for defective image.
    :type defective_folder: str
    :param perfect_folder: Subfolder for perfect image.
    :type perfect_folder: str
    :param aug_dict: Dictionary for augmentation.
    :type aug_dict: dict
    :param api_obj: Dictionary for augmentation.
    :type api_obj: dict
    :param batch_size: Size of batch, defaults to 8.
    :type batch_size: int, optional
    :param validation_split: Validation split percentage, defaults to 0.2
    :type validation_split: float, optional
    :return: Two generator trainGen and testGen
    :rtype: tuple
    """
    binary_folder = api_obj.ds.binary_folder
    create_binary_symlink(paths, binary_folder, defective_folder, perfect_folder)
    path = symlinkPath

    # For path generate train and val generator
    trainGen = ImageDataGenerator(**aug_dict, validation_split=validation_split)
    # valGen = ImageDataGenerator(validation_split=validation_split)
    
    
    train_dataset = trainGen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        color_mode='grayscale',
        class_mode='binary',
        classes=[perfect_folder, defective_folder],
        seed=42,
        subset='training',
        follow_links=True) # set as training data

    val_dataset = trainGen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=batch_size,
        color_mode='grayscale',
        class_mode='binary',
        classes=[perfect_folder, defective_folder],
        seed=42,
        subset='validation',
        follow_links=True) # set as validation data

    return train_dataset, val_dataset


def maskGenerator(path,
                  image_folder,
                  mask_folder,
                  aug_dict,
                  subfolders_mask=None,
                  target_size=(256, 256),
                  batch_size=8,
                  seed=1,
                  image_color_mode="grayscale",
                  mask_color_mode="grayscale",
                  image_save_prefix="image",
                  mask_save_prefix="mask",
                  bg_idx=None):
    """Generator for mask. it can generate image and mask at the same time
    use the same seed for image_datagen and mask_datagen to ensure the transformation for image and mask is the same
    if you want to visualize the results of generator, set save_to_dir = "your path".

    :param path: Path of dataset.
    :type path: str
    :param image_folder: Subfolder for images.
    :type image_folder: str
    :param mask_folder: Subfolder for masks.
    :type mask_folder: str
    :param aug_dict: Dictionary for augmentation.
    :type aug_dict: dict
    :param subfolders_mask: If mask_folder contain Some folder for each mask's class it should be a list of class's subfolder 
    ( order is import ) another way it should be None ( for one class mask ). Defaults to None, defaults to None
    :type subfolders_mask: list, optional
    :param target_size: Target size of image, defaults to (256, 256)
    :type target_size: tuple, optional
    :param batch_size: Size of batch, defaults to 8
    :type batch_size: int, optional
    :param seed: Random seed, defaults to 1
    :type seed: int, optional
    :param image_color_mode: Color mode of image, defaults to "grayscale"
    :type image_color_mode: str, optional
    :param mask_color_mode: Color mode of mask, defaults to "grayscale"
    :type mask_color_mode: str, optional
    :param image_save_prefix: Prefix to use for filenames of saved images, defaults to "image"
    :type image_save_prefix: str, optional
    :param mask_save_prefix: Prefix to use for filenames of saved masks, defaults to "mask"
    :type mask_save_prefix: str, optional
    :param bg_idx: Defaults to None
    :type bg_idx: int, optional
    :yield: Tuple of batch of images and their masks.
    :rtype: tuple
    """
    # -----------------------------------------------------
    def adjustData(img, mask):
        """Normalize the img in range [0, 1] and convert the mask to a zero-one image.

        :param img: An image.
        :type img: array
        :param mask: A mask relative to img.
        :type mask: array
        :return: Tuple of image and its mask
        :rtype: tuple
        """
        if (np.max(img) > 1):
            img = img / 255.
            mask = mask / 255.
            mask[mask > 0.5] = 1
            mask[mask <= 0.5] = 0
            return (img, mask)

    # -----------------------------------------------------
    image_datagen = ImageDataGenerator(**aug_dict)
    mask_datagen = ImageDataGenerator(**aug_dict)
    # -----------------------------------------------------
    image_generator = image_datagen.flow_from_directory(
        path,
        classes=[image_folder],
        class_mode=None,
        color_mode=image_color_mode,
        target_size=target_size,
        batch_size=batch_size,
        save_prefix=image_save_prefix,
        seed=seed)
    # -----------------------------------------------------
    mask_generator = []
    if subfolders_mask is None:
        mask_generator = mask_datagen.flow_from_directory(
            path,
            classes=[mask_folder],
            class_mode=None,
            color_mode=mask_color_mode,
            target_size=target_size,
            batch_size=batch_size,
            save_prefix=mask_save_prefix,
            seed=seed)

    else:
        for subfolder in subfolders_mask:

            if bg_idx is not None:
                if subfolder == subfolders_mask[bg_idx]:
                    mask_datagen.cval = 255
                else:
                    mask_datagen.cval = 0

            mask_generator.append(
                copy.deepcopy(mask_datagen).flow_from_directory(
                    os.path.join(path, mask_folder),
                    classes=[subfolder],
                    class_mode=None,
                    color_mode=mask_color_mode,
                    target_size=target_size,
                    batch_size=batch_size,
                    save_prefix=mask_save_prefix,
                    seed=seed)
            )
    # -----------------------------------------------------
    if subfolders_mask is None:
        train_generator = zip(image_generator, mask_generator)
        for (img, mask) in train_generator:
            img, mask = adjustData(img, mask)
            yield (img, mask)

    else:
        mask_generator = tuple(mask_generator)
        train_generator = zip(*((image_generator,) + mask_generator))
        for (img, *mask) in train_generator:
            masks = np.concatenate(mask, axis=-1)
            img, masks = adjustData(img, masks)
            yield (img, masks)
    # -----------------------------------------------------


def create_yolo_yaml_file(train_images_path, val_images_path, class_name_to_id_mapping):
    d = {'train': train_images_path, 
    'val': val_images_path, 
    'nc': len(class_name_to_id_mapping),
    'names': list(class_name_to_id_mapping.keys())}

    name = 'oxin.yaml'
    if not os.path.exists(yolo_data_path):
        os.makedirs(yolo_data_path)
    path = os.path.join(yolo_data_path, name)
    with open(path, 'w') as f:
        yaml.dump(d, f)

    return path


class CustomDataGen(tf.keras.utils.Sequence):
    def __init__(
        self,
        path, 
        image_folder,
        mask_folder,
        batch_size,
        transforms=None,
        input_size=(224, 224),
        shuffle=True,
    ):

        self.batch_size = batch_size
        self.input_size = input_size
        self.shuffle = shuffle
        self.transforms = transforms

        self.image_path = os.path.join(path, image_folder)
        self.mask_path = os.path.join(path, mask_folder)

        self.image_list = os.listdir(self.image_path)
        self.n = len(self.image_list)

    def on_epoch_end(self):
        if self.shuffle:
            self.image_list = random.sample(self.image_list, self.n)

    def __get_input(self, path):
        image = cv2.imread(os.path.join(self.image_path, path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.input_size != (image.shape[0], image.shape[1]):
            image = cv2.resize(image, (self.input_size[1], self.input_size[0]))
        image = self.transforms(image)
        return image 

    def __get_output(self, path):
        mask = cv2.imread(os.path.join(self.mask_path, path), 0)
        if self.input_size != (mask.shape[0], mask.shape[1]):
            mask = cv2.resize(mask, (self.input_size[1], self.input_size[0]))
        return mask / (255.0)

    def __get_data(self, batches):
        # Generates data containing batch_size samples

        X_batch = np.array([self.__get_input(x) for x in batches])
        y_batch = np.array([self.__get_output(x) for x in batches])

        return X_batch, y_batch

    def __getitem__(self, index):
        batches = self.image_list[index * self.batch_size : (index + 1) * self.batch_size]
        X, y = self.__get_data(batches)
        return X, y

    def __len__(self):
        return (self.n//self.batch_size + 1) if ((self.n//self.batch_size) != (self.n/self.batch_size)) else (self.n//self.batch_size)


if __name__ == '__main__':
    # train, test = get_binarygenerator('data//binary',
    #                                   (128, 800),
    #                                   defective_folder='defective',
    #                                   perfect_folder='perfect',
    #                                   aug_dict=aug_dict,
    #                                   validation_split=0.2)

    # train_c = maskGenerator('data/mask_class/train',
    #                         'image',
    #                         'label',
    #                         aug_dict,
    #                         subfolders_mask=['0', '1', '2', '3', '4'],
    #                         batch_size=8,
    #                         target_size=(128, 800),
    #                         bg_idx=0)

    # train_nc = maskGenerator('SymLink/train',
    #                          'image',
    #                          'label',
    #                          aug_dict,
    #                          batch_size=13,
    #                          target_size=(256, 256))

    preprocess_input = sm.get_preprocessing("efficientnetb2")
    train_dataloader = CustomDataGen(
            path='/home/reyhane/PythonProjects/trainApp_oxin_new/SymLink/train',
            image_folder='image',
            mask_folder='label',
            batch_size=8,
            transforms=preprocess_input,
            input_size=(300, 800),
        )

    import cv2

    for x, ys in train_dataloader:
        print(len(x), len(ys))
        x = x[0]
        ys = ys[0]
        x = x * 255
        ys = ys * 255
        x = x.astype(np.uint8)
        ys = ys.astype(np.uint8)

        cv2.imshow('x', x)
        cv2.imshow('y', ys)
        # ys = np.moveaxis(ys, [-1], [0])
        # for i, y in enumerate(ys):
        #     cv2.imshow('y{}'.format(i), y)

        cv2.waitKey(0)

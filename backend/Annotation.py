import os
from turtle import pos
from typing_extensions import Annotated
import numpy as np
import cv2
from numpy.core.fromnumeric import reshape
from numpy.lib.shape_base import split
import random
from sys import getsizeof
import json
import math


CLASSIFICATION_TYPE = 1
BINARY_TYPE = 2
MASK_TYPE = 3
THRESH= 80
OBJ_BBOXS_KEY = 'obj_bboxes'
BBOX_KEY = 'bbox'
OBJ_MASKS_KEY = 'obj_masks'
MASK_KEY = 'mask'
CLASS_KEY = 'class'
NAME = 'name'


#______________________________________________________________________________________________________________________________________________
#explain:
#   a class for  masks of image. it contains maskes and their classes
#atribiut:
#   classes: array of classes Id
#   codedMaskes_: lists of points coordinate [[x1,y1], [x2,y2],...]
#______________________________________________________________________________________________________________________________________________
class Mask():

    def __init__(self, pts, class_id, refrenced_shape):
        self.class_id = class_id
        self.pts = pts
        self.refrenced_shape = refrenced_shape
        self.mask = self.draw_mask()

    #______________________________________________________________________________________________________________________________________________
    #explain:
    #   draw mask by its corners
    #
    #return:
    #   image_mask = a mask that shows the location of the certain defects
    #______________________________________________________________________________________________________________________________________________
    def draw_mask(self):
        mask = np.zeros( self.refrenced_shape, dtype=np.uint8)
        pts = np.array( pts ).astype(np.int32)
        pts = pts.reshape((-1,2,1)) #reshape to opencv contour shape
        return cv2.drawContours(mask, [pts], 0, color=255, thickness=-1)

    
    #______________________________________________________________________________________________________________________________________________
    #explain:
    #   give mask image
    #
    #return:
    #   mask image
    #______________________________________________________________________________________________________________________________________________
    def get_mask(self):
        return self.mask

    #______________________________________________________________________________________________________________________________________________
    #explain:
    #   give class id of mask
    #
    #return:
    #   class id integer
    #______________________________________________________________________________________________________________________________________________
    def get_class_id(self):
        return self.class_id

    def get_points(self):
        return self.pts






class BBOX():

    def __init__(
        self,
        bbox,
        class_id,
        refrenced_shape,
        pose = "Unspecified",
        truncated = '0',
        difficult = '0'
        ):
        
        self._bbox = bbox
        self._class_id = class_id
        self.refrenced_shape = refrenced_shape

        self._pose = pose
        self._truncated = truncated
        self._difficult = difficult

    
    def get_bbox(self):
        return self._bbox

    def get_class_id(self):
        return self._class_id

    def get_refrenced_shape(self):
        return self.refrenced_shape

    def get_pose(self):
        return self._pose

    def get_truncated(self):
        return self._truncated

    def get_difficult(self):
        return self._difficult






#______________________________________________________________________________________________________________________________________________
#explain:
#   a class for read json anntotion label
#
#atribiut:
#   annotation: dict of json file
#
#methods:
#
#   -------------------------------
#   __init__:
#       explain:
#           set the annotation atribiut
#       args:
#           path: path of json file
#       
#   -------------------------------
#   __read__:
#       explain:
#           read jason file and convert to dict
#       args:
#           path: path of json file
#       returns:
#          annotation: dictionary of json file
#   -------------------------------
#   get_fname:
#       explain:
#           return image file name image
#       returns:
#          fname: string of image's name
#   -------------------------------
#   get_path:
#       explain:
#           return path of image
#       returns:
#          fname: string of image's path
#   -------------------------------
#   get_fullpath:
#       explain:
#           return full path of image ( path + image_full_name)
#   -------------------------------
#   get_img_size:
#       explain:
#           return size of image in tuple (w,h)
#   -------------------------------
#   get_classes:
#       explain:
#           return classes id of all objects in image in np.array
#   -------------------------------
#   get_masks:
#       explain:
#           return list of objects label contain masks and classes in format of Label() class
#   -------------------------------
#   get_encoded_mask:
#       explain:
#           returns a list of masks object ( instance of Mask() class )
#   -------------------------------
#   get_bboxs:
#       TBD
#   -------------------------------
#   is_color:
#       explain:
#           return True, if image is colored
#   -------------------------------
#   is_gray:
#       explain:
#           return True, if image is gay
#   -------------------------------
#   is_mask:
#       explain:
#           return True, type of localisation's label is mask format
#   -------------------------------
#   is_lbl_bbox:
#       explain:
#           return True, type of localisation's label is bounding box format
#   -------------------------------
#   is_class_valid:
#       explain:
#           returns true if the mask class is available in the anotation. False if not.
#   --------------------------------
#______________________________________________________________________________________________________________________________________________
class Annotation():

    def read(self, path):
        with open(path) as jfile:
            file = json.load(jfile)
        return file
        

    def write(self,path):    
        with open(path, 'w') as f:
            json.dump(self.annotation, f)

    def __init__(self,):
        self.annotation = {}

    #--------------------------------------------------------
    #
    #--------------------------------------------------------
    def set_fname(self, name):
        self.annotation[NAME] = name

    def set_sheet_id(self, id):
        self.annotation['sheet_id'] = id

    def set_date(self, date):
        assert type(date) == str, "date should be string"
        self.annotation['date'] = date

    def set_time(self, time):
        assert type(time) == str, "date should be string"
        self.annotation['time'] = time

    def set_user(self, user):
        self.annotation['user'] = user

    def set_pos(self, pos):
        self.annotation['pos'] = list(pos)

    def set_path(self, path):
        self.annotation['path'] = path

    def set_img_size(self, size):
        self.annotation['size'] = size

    def set_masks(self, masks):
        ms = []
        for class_id,mask in masks:
            mask_dict = {}
            mask_dict[CLASS_KEY] = class_id
            mask_dict[MASK_KEY] = mask.tolist()
            ms.append( mask_dict)
        
        self.annotation[OBJ_MASKS_KEY] = ms


    def set_bboxes(self, bboxes):
        bs  = []
        for class_id,bbox in bboxes:
            box_dict = {}
            box_dict[CLASS_KEY] = class_id
            box_dict[BBOX_KEY] = bbox.tolist()
            bs.append( box_dict)
        
        self.annotation[OBJ_BBOXS_KEY] = bs

    #--------------------------------------------------------
    #
    #--------------------------------------------------------

    def get_fname(self):
        return self.annotation[NAME]

    def get_sheet_id(self):
        return self.annotation['sheet_id']

    def get_date(self):
        return self.annotation['date']

    def get_time(self):
        return self.annotation['time']

    def get_user(self):
        return self.annotation['user']

    def get_pos(self):
        return self.annotation['pos']

    def get_path(self):
        return self.annotation['path']

    def get_fullpath(self):
        return os.path.join(self.annotation['path'], self.annotation[NAME] )

    def get_img(self):
        return cv2.imread( self.get_fullpath() )

    def get_img_size(self):
        return tuple( self.annotation['size'] )

    def get_classes(self):
        assert self.have_object(), "There is no object"
        classes = []
        labels = self.annotation['labels']
        for lbl in labels:
            classes.append( int(lbl[CLASS_KEY]) )
        return np.array(classes)
    
    def get_masks(self):
        assert self.have_object(), "There is no object"
        assert self.is_lbl_mask(), "Label type is not mask"

        labels = self.annotation[OBJ_MASKS_KEY]
        mask_list = []
        for lbl in labels:
            refrenced_size = self.get_img_size()
            class_id = int(lbl[CLASS_KEY])
            coded_mask = np.array( lbl[MASK_KEY] ).reshape((-1,2)).astype(np.int32)
            mask_list.append( Mask( coded_mask, class_id, refrenced_size) )
        return mask_list

    
    def get_bboxs(self):
        assert self.have_object(), "There is no object"
        assert self.is_lbl_bbox(), "Label type is not bounding box"
        
        bbox_list = list()
        lables = self.annotation[OBJ_BBOXS_KEY]

        for label in lables:
            bbox = BBOX(
                bbox = tuple(label[BBOX_KEY]),
                class_id= label[CLASS_KEY],
                refrenced_size= self.get_img_size()
            )

            bbox_list.append(bbox)

        return bbox_list
        
    def is_class_valid(self , cls ):
        classes = self.get_classes()        
        if cls in classes:
            return True
        else:
            return False


    def is_color(self):
        return self.annotation['color_mode'] == 'COLOR'
    
    def is_gray(self):
        return self.annotation['color_mode'] == 'GRAY'

    def is_lbl_mask(self):  
        return self.annotation.get('label_type') == 'MASK'

    def is_lbl_bbox(self):  
        assert self.have_object(), "There is no object"
        return self.annotation['label_type'] == 'BBOX'

    def have_object(self): 
        return self.annotation['included_object'] == 'YES'


    def convert_mask_to_bbox(self):
        assert self.is_lbl_mask() , 'Your annotation is BBOX and cannot be converted.'
        assert self.have_object() , 'Your annotation dose not contatin an object'
        bboxes = list()

        for mask in self.get_masks():
            
            bbox_list = mask_to_bbox(mask.get_mask())
            
            for bbox in bbox_list:
                
                bbox = BBOX(
                    bbox=list( bbox ),
                    refrenced_size= self.get_img_size(),
                    class_id = mask.get_class_id()
                )

                bboxes.append(bbox)
    
        return bboxes

#______________________________________________________________________________________________________________________________________________
#explain:
#   filter annotation_name list base of filter_arg 
#
#arg:
#
#   path: path of annotations folder
#
#   filter_arg: it is a dictionay. it's key are same as annotation jason file, e.g "label_type", "color_mode" and etc, and
#   their values are a list of acceptabel values for related features. this Values are or by each other. it's also accept
#   the "class" key and don't accept "label" key for e.g if the filter_arg be { 'label_type':["MASK"], "class":[1,2] }
#   it pass annotations that their label_type are "MASK" and their object's class consist one of 1 or 2 class or both of them
#
#   annotation_name: list of annotation's name, if None, it read all the annonatons in the path
#   
#
#return:
#   filtered
#   filtered: list of annontions_file_name that pass filters
#______________________________________________________________________________________________________________________________________________
def filter_annotations(path,filter_arg, annotations_name=None):

    def filter_func(annotation_name):

        with open(os.path.join(path,annotation_name)) as jfile:
            annotation_dict = json.load(jfile)
        
        for filter_key, filter_values in filter_arg.items():
            if filter_key.lower() == CLASS_KEY:
                classes =[]
                labels = annotation_dict['labels']
                for lbl in labels:
                    classes.append( lbl[CLASS_KEY])

                flag = False
                for c in classes:
                    if c  in filter_values:
                        flag =  True
                if not flag:
                    return False                  
            else :
                if annotation_dict[filter_key.lower()] not in filter_values:
                    return False
        
        return True
    

    if annotations_name is None:
        assert os.path.isdir(path) , f"The following path is not available! \n {path} "
        annotations_name = os.listdir(path)
    
    annotations_name = list( filter( lambda x:x[-5:]=='.json' , annotations_name)) #just pass .json file


    filtered = list( filter( filter_func, annotations_name))
    return filtered




#______________________________________________________________________________________________________________________________________________
#explain:
#   get path of annotations and return list of annotations_name ( json file's name )
#
#arg:
#   path: path of json labels
#   shuffle: if True, the labels list shuffle
#
#return:
#   annotations_name_list
#   annotations_name_list: list of annontions_file_name ( jason file's name)
#______________________________________________________________________________________________________________________________________________
def get_annotation_name(path, shuffle=True):
    assert os.path.isdir(path) , f"The following path is not available! \n {path} "
    annotations_name_list = os.listdir(path)
    annotations_name_list = list( filter( lambda x:x[-5:]=='.json' , annotations_name_list))
    if shuffle:
        random.shuffle(annotations_name_list)
    return annotations_name_list


#______________________________________________________________________________________________________________________________________________
#explain:
#   get list of annotation_file_name ( jason file's name) and split into val and train annotation_file_name list
#
#arg:
#   annotations_name_list: list of an_file_name ( jason file's name)
#   split: a float number that determine amount of split
#   shuffle: if True, the labels list shuffle
#
#return:
#   annotations_train_list, annotations_val_list
#   annotations_train_list: list of list of lbl_file_name for validation_file_name for validation
#   annotations_val_list: list of annontions_file_name for validation
#______________________________________________________________________________________________________________________________________________
def split_annotations_name( annotations_name_list=None, split=0.2, shuffle=True ):
    lbls_count = len(annotations_name_list)
    annotations_val_list   = annotations_name_list[ : int(lbls_count * split)]
    annotations_train_list = annotations_name_list[ int(lbls_count * split) : ]
    return annotations_train_list, annotations_val_list



#______________________________________________________________________________________________________________________________________________
#explain:
#   get path of labels and a annotation_name and return annotation() class format
#
#arg:
#   annotations_path: path of folder of annotations 
#   annotation_name: name of specific annotation
#
#return:
#   labels
#   labels : a annoation of label in annotation() class format
#
#______________________________________________________________________________________________________________________________________________
def read_annotation(annotations_path, annotation_name):
    return  Annotation( os.path.join( annotations_path, annotation_name ) )


#______________________________________________________________________________________________________________________________________________
#explain:
#   return binary dataset extractor
#
#arg:
#
#return:
#   func: extractor function, that get an annotation ( Instance if annotation() class ) and return image, binary_lbl
#______________________________________________________________________________________________________________________________________________
def extact_binary():
    def func(annotation):
        lbl = int(annotation.have_object()) 
        img = annotation.get_img()
        return np.array(img),np.array(lbl )
    return func



#______________________________________________________________________________________________________________________________________________
#explain:
#   get an anonations( instance of Anonation() class ) and return its image and class label
#
#arg:
#   class_num, consider_no_object
#   class_num: number of class. no_object class shouldn't acount
#   consider_no_object: if True, it Allocates a new class to no object. it's class is 0 class. defuat is False
#
#return:
#   func: extractor function, that get an annotation ( Instance if annotation() class ) and return image, classificaiotn_label ( in one_hot_code format )
#______________________________________________________________________________________________________________________________________________
def extract_class( class_num, consider_no_object=False):

    def func(annotation):
        lbl =  np.zeros((class_num,))

        if annotation.have_object():
            classes = annotation.get_classes()
            classes - 1 #in json file class started ferm numer 1
            lbl[classes] = 1
        
        if consider_no_object:
            #if no defect, no_defect class value should be 1 else 0
            if np.sum(lbl) == 0:
                lbl = np.insert(lbl,0,1)
            else:
                lbl = np.insert(lbl,0,0)
        
        img = annotation.get_img()
        return np.array(img),np.array(lbl )
    return func







#______________________________________________________________________________________________________________________________________________
#explain:
#   get an anonations( instance of Anonation() class ) and return its image and mask label
#
#arg:
#   class_num, mask_size, consider_no_object
#   class_num: number of class. no_object class shouldn't acount
#   mask_size: size of results mask in format of (h,w)
#   consider_no_object: if True, it Allocates a new class to no object. it's class is 0 class. defuat is False
#
#return:
#   func: extractor function, that get an annotation ( Instance if annotation() class ) and return image, classificaiotn_label ( in one_hot_code format )
#______________________________________________________________________________________________________________________________________________
def extract_mask( class_num, mask_size, consider_no_object=False, class_id=None):
    def func(annotation):
        lbl = np.zeros(  mask_size + (class_num,) , dtype=np.uint8)
        if annotation.have_object():
            mask_objs = annotation.get_masks()
            if class_id is not None:
                for mask_obj in mask_objs:
                    if mask_obj.class_id == class_id:
                        mask = mask_obj.mask
                        mask = cv2.resize( mask, mask_size[::-1])
                        lbl =  np.expand_dims(mask, axis=-1)
                        break
                    else:
                        lbl = np.zeros( mask_size+(1,), dtype=np.uint8)
        

            else:
                for mask_obj in mask_objs:
                    msk = cv2.resize(mask_obj.mask , mask_size[::-1] )  #in json file class started ferm numer 1
                    _,msk = cv2.threshold(msk,THRESH, 255, cv2.THRESH_BINARY)
                    lbl[:,:,mask_obj.class_id] = msk
                     
        
        if consider_no_object:
            bg = np.sum( lbl, axis=-1 ).clip(0, 255)
            bg = 255 - bg
            bg =  np.expand_dims(bg , axis=-1).astype( np.uint8)
            lbl = np.concatenate((bg, lbl), axis=-1)
        
        img = annotation.get_img()
        return np.array(img),np.array(lbl )
    return func






#______________________________________________________________________________________________________________________________________________
#explain:
#   genreat inputs and labels batch
#
#
#arg:
#   annotations_path: path of annotations file
#   extractor_func: an exrtracor function that get an annotation and returns its image and label
#   annotations_name: list of file name of desire  annotations. if None , it load all the annotations in path
#   rescale: rescale value that images and masks divided on it (defualt = 255)
#   batch_size: size of batchs
#   aug: augmention object( instance of Augmention() class from augmention.py file. if None there is no augmention
#   resize: if not None, images resize to that. it is in format of (h,w)
#   featurs_extractor: list of feature_extractor functions that apply on images
# 
#
#return:
#   (batch_inputs , batch_lbls)
#   batch_inputs: batch of images that are ready for train
#   batch_lbls: batch of labels that are ready for train
#
#______________________________________________________________________________________________________________________________________________
def generator(annotations_path, extractor_func, annotations_name=None,rescale=255, batch_size = 32, aug = None, resize=None, reshape=None , featurs_extractor=None):
    
    batch_inputs = []
    batch_lbls = []
    if annotations_name is None:
        assert os.path.isdir(annotations_path) , f"The following path is not available! \n {annotations_path} "
        annotations_name = os.listdir(annotations_path)
    
    while True:
        for name in annotations_name:    
            annotation = read_annotation( annotations_path, name)
            img, lbl = extractor_func(annotation)
            if aug is not None:
                if len(lbl.shape) < 2: #binary or classification
                    img = aug.augment_single(img)
                    
                else: #Mask 
                    img, lbl = aug.augment_single_byMask(img, lbl)
                    
            
            if resize is not None:
                img = cv2.resize(img, resize[::-1])
            
            if reshape is not None:
                img = np.reshape(img , reshape)


            if featurs_extractor is None:
                img = img.astype(np.float32) / rescale
                if len(lbl.shape) > 2:
                    lbl = lbl.astype(np.float32) / rescale
                batch_inputs.append(img)

            else :
                feature_vestor=[]
                for featur_extractor in featurs_extractor:
                    f = featur_extractor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
                    feature_vestor.append(f)
                feature_vestor = np.concatenate(feature_vestor)
                batch_inputs.append( feature_vestor )

                if len(lbl.shape) > 2:
                    lbl = lbl.astype(np.float32) / rescale

            
            batch_lbls.append( lbl )
            

            if len(  batch_inputs) == batch_size:
                yield np.array(batch_inputs), np.array(batch_lbls)
                batch_inputs, batch_lbls = [] , []
        










if __name__ == '__main__':
    
    lbls_path = 'severstal-steel-defect-detection/annotations'
    imgs_path = 'severstal-steel-defect-detection/train_images'

    res_imgs_path = 'data/image'
    res_lbls_path = 'data/label'



    func = extract_mask(4, (256,1600), consider_no_object=False, class_id=None)
    # extractor_func1 = extact_binary()

    annotations_name = get_annotations_name(lbls_path, shuffle=False) 
    
    count = len(annotations_name)
    for i, nannotation in enumerate(annotations_name):
        #print(nannotation)
        annotation = read_annotation( lbls_path, nannotation)
        if annotation.have_object() == False:
            continue
        img, msks  = func(annotation)
        res_mask = np.sum(msks.astype(np.int32), axis=-1)

        res_mask = np.clip(res_mask,0,255).astype(np.uint8)
        #print(res_mask.shape)
        #cv2.imshow('msk', res_mask)
        #cv2.imshow('img', img)
        #cv2.waitKey(0)
        fname = nannotation[:-5] + '.jpg'
        
        cv2.imwrite(os.path.join(res_imgs_path, fname), img)
        cv2.imwrite(os.path.join(res_lbls_path, fname), res_mask)
        
        print(np.float16(i/count*100), '%')
        os.system('cls')
        

    end
    #print('Start filter by class 1')
    #annotations_name = filter_annotations( lbls_path, filter_arg={'class':[1]})
    #print('End filter')

    extractor_func1 = extact_binary()
    gen = generator( lbls_path, extractor_func1, annotations_name=annotations_name, batch_size=32, aug=None, rescale=255)
    x,y = next(gen)
    for i in range(len(x)):
        img = x[i]  * 255
        img = img.astype( np.uint8 )  
        cv2.imshow('img', img)
        cv2.waitKey(0)
        print('BINARY',y[i])





    extractor_func2 = extract_class(class_num=4, consider_no_object=True)
    gen = generator( lbls_path, extractor_func2, annotations_name=None, batch_size=32, aug=None, rescale=255)
    x,y = next(gen)
    for i in range(len(x)):
        img = x[i]  * 255
        img = img.astype( np.uint8 )  
        cv2.imshow('img', img)
        cv2.waitKey(0)
        print(y[i])







    extractor_func3 = extract_mask(4, (128,600), consider_no_object= True, class_id=None)
    gen = generator( lbls_path, extractor_func3, annotations_name=None, batch_size=32, aug=None, rescale=255)
    x,y = next(gen)
    for i in range(len(x)):
        img = x[i]  * 255
        img = img.astype( np.uint8 )  

        masks = np.moveaxis(y[i], [0,1,2], [1,2,0])

        cv2.imshow('img', img)
        for mask in masks:
            mask = mask * 255
            mask = mask.astype( np.uint8 )  
            cv2.imshow('mask', mask) 
            cv2.waitKey(0)
    # x2,y2 = next(gen)
    # filter_arg={'label_type':["BBOX","MASK"], 'class':[3]}
    # filtered = filter_annotations(annotations_name, path, filter_arg)
    # annontions_names = get_annotations_name(lbls_path)

    # annontions_names_train, annontions_names_val = split_annotations_name(annontions_names)
    # annotations = read_annotations(annontions_names_train,lbls_path)
    # imgs,lbls = get_class_datasets(annotations[:1000],4, consider_no_object=True)


def mask_to_bbox(enc_mask, image_size = (256 , 1600)):
    """Returns all the bounding boxes of a mask.

    Args:
        enc_mask (np.array): encoded_masks

    Returns:
        list: list of all bounding boxes in x_min , y_mix , x_max , y_max
    """
    kernel = np.ones((3,3),np.uint8)
    dilated = cv2.dilate(enc_mask,kernel,iterations = 3)

    contours , hir = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bbox_list = np.array(list(
        map(cv2.boundingRect , contours)
    ))

    bbox_list[:,2] += bbox_list[:,0]
    bbox_list[:,3] += bbox_list[:,1]

    return bbox_list

    

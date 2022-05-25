from functools import partial
from PySide6.QtWidgets import QLabel as sQLabel
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
import json
import os
import cv2
import numpy as np
from PIL import ImageColor

import texts
from neighbouring_UI import neighbouring
from backend import Annotation, classification_list_funcs



n_images_per_row = 6
n_images_per_row_classlist = 5
no_image_path = './images/no_image.png'
widjet_prefixes = {'perfect':'binary_list_perfect', 'defect':'binary_list_defect'}
image_list_object_names = {'perfect':'perfect_images', 'defect':'defect_images'}
language = 'en'
mask_color = '#FF0000' # BGR format
line_tickness = 4
mask_alpha = 0.5


# create image slider area on UI
def create_image_slider_on_ui(ui_obj, db_obj, frame_obj, prefix=widjet_prefixes['perfect'], image_per_row=n_images_per_row):
    # create layout
    try:
        layout = sQHBoxLayout()
        eval("exec('ui_obj.%s_layout = layout')" % prefix)
        
        # creat and assign labels to layout
        for i in range(image_per_row):
            label = sQLabel()
            label.setScaledContents(True)
            label.setWhatsThis('')
            # assign label to UI with name
            eval("exec('ui_obj.%s_label_%s = label')" % (prefix, i))
            # add to layout
            eval('ui_obj.%s_layout' % prefix).addWidget(eval('ui_obj.%s_label_%s' % (prefix, i)))
            # assign image
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, i)), image=None, no_image=True)

            # doble-click event for labels
            eval('ui_obj.%s_label_%s' % (prefix, i)).mouseDoubleClickEvent = partial(maximize_image_on_click, ui_obj, db_obj, eval('ui_obj.%s_label_%s' % (prefix, i)))

        # assign layout to frame
        frame_obj.setLayout(eval('ui_obj.%s_layout' % prefix))
        return True

    except:
        ui_obj.set_warning(texts.ERORS['BUILD_BINARYLIST_SLIDER_ERROR'][language], 'binarylist', level=3)
        return False


# maximize image label on click (open image in a window)
def maximize_image_on_click(ui_obj, db_obj, label, event):
    print('hi', label.whatsThis())
    pathes = label.whatsThis()
    #try:
    if pathes != '':
        pathes = pathes.split("#")
        if len(pathes) != 3:
            ui_obj.set_warning(texts.ERORS['MAXIMIZE_IMAGE_ERROR'][language], 'binarylist', level=3)
            return
        # load image
        if pathes[2] != 'fullpath':
            image = cv2.imread(os.path.join(pathes[0], pathes[1]))
            # mask (annotations) overlay
            annotation_path = os.path.join(pathes[2], pathes[1][:-4]+'.json')
        else:
            image = cv2.imread(pathes[0])
            # mask (annotations) overlay
            annotation_path = pathes[1]

        res, annotated_image = create_mask_from_annotation_file(db_obj=db_obj, image=image, annotation_path=annotation_path)
        if res:
            ui_obj.window = neighbouring(image, annotated_image=annotated_image, has_annotation=True)
            ui_obj.window.show()
        else:
            ui_obj.window = neighbouring(image, annotated_image=annotated_image, has_annotation=False)
            ui_obj.window.show()
    
    #except:
        #ui_obj.set_warning(texts.WARNINGS['BINARYLIST_MAXIMIZE_IMAGE_ERROR'][language], 'binarylist', level=2)
        

# set/update images to ui
def set_image_to_ui_slider(ui_obj, sub_directory, annot_sub_direcotory, image_path_list, prefix=widjet_prefixes['perfect'], image_per_row=n_images_per_row):
    try:
        # set dataset images on UI
        for i, image_path in enumerate(image_path_list):
            # load image
            image = cv2.imread(os.path.join(sub_directory, image_path))
            # set to UI label
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, i)), image=image, no_image=False)
            # update text (image url)
            whats_this_text = sub_directory + '#' + image_path + '#' + annot_sub_direcotory
            eval('ui_obj.%s_label_%s' % (prefix, i)).setWhatsThis(whats_this_text)
        # set last image labels on UI as empty
        try:
            i += 1
        except:
            i = 0
        for j in range(i, image_per_row):
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, j)), image=None, no_image=True)
            eval('ui_obj.%s_label_%s' % (prefix, j)).setWhatsThis('')
        
        return True

    except:
        return False


# set/update images to ui given full image and annoptation path
def set_image_to_ui_slider_full_path(ui_obj, image_path_list, annot_path_list, prefix=widjet_prefixes['perfect'], image_per_row=n_images_per_row):
    try:
        # set dataset images on UI
        for i, image_path in enumerate(image_path_list):
            # load image
            image = cv2.imread(image_path)
            # set to UI label
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, i)), image=image, no_image=False)
            # update text (image url)
            whats_this_text = image_path + '#' + annot_path_list[i] + '#' + 'fullpath'
            print('whatsthis:', whats_this_text)
            eval('ui_obj.%s_label_%s' % (prefix, i)).setWhatsThis(whats_this_text)
        # set last image labels on UI as empty
        try:
            i += 1
        except:
            i = 0
        for j in range(i, image_per_row):
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, j)), image=None, no_image=True)
            eval('ui_obj.%s_label_%s' % (prefix, j)).setWhatsThis('')
        
        return True

    except:
        return False

        

# get binarylist params from ui
def get_params_from_ui(ui_obj):
    params = {}
    try:
        params['dataset_path'] = ui_obj.binarylist_dataset_lineedit.text()
        return params
    except:
        return {}


# get image pathes in dataset directory
def get_image_pathes_list(ds_obj, dataset_path):
    # perfect
    perfect_check = True
    try:
        # perfect path
        perfect_path = os.path.join(dataset_path, ds_obj.perfect_folder)
        # get image pathes
        perfect_image_pathes = getfiles(perfect_path)

    except:
        perfect_check = False
        perfect_image_pathes = []
    
    # defect
    defect_check = True
    try:
        # defect path
        defect_path = os.path.join(dataset_path, ds_obj.defect_folder)
        # get image pathes
        defect_image_pathes = getfiles(defect_path)

    except:
        defect_check = False
        defect_image_pathes = []
    
    return perfect_check, perfect_image_pathes, defect_check, defect_image_pathes


# get files in a directory
def getfiles(dirpath):
    try:
        a = [s for s in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, s)) and s[-3:]=='jpg']
        a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
        return a
    except:
        return []


# set cameras imnages to UI
def set_image_to_ui(label_name, image, no_image=False):
    if no_image:
        image = cv2.imread(no_image_path)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    #
    h, w, ch = image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = sQImage(image.data, w, h, bytes_per_line, sQImage.Format_BGR888)
    label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))


# read annotation files and create mask
def create_mask_from_annotation_file(db_obj, image, annotation_path):

    print('annot:', annotation_path)
    # create image mask
    image_shape = image.shape
    image_mask = np.zeros((image_shape))
    image_mask2 = np.zeros((image_shape))

    # load json file
    try:
        with open(annotation_path) as json_file:
            annotations = json.load(json_file)
    except:
        return False, 'Annotation file doesnt exist/cant be loaded'
    
    # draw bbox and polygons on mask
    # polygons
    try:
        for obj_mask in annotations[Annotation.OBJ_MASKS_KEY]:
            # get defect color and name
            res, defect_info = get_defect_info(db_obj=db_obj, defect_id=obj_mask[Annotation.CLASS_KEY])

            # polygon points
            pts = np.array(obj_mask[Annotation.MASK_KEY] , np.int32)
            pts_center = centroid(vertexes=pts)
            pts = pts.reshape((-1, 1, 2))
            # Draw a line nofilled polygon
            # overlay_image = cv2.polylines(overlay_image, pts=[pts], isClosed=True, color=mask_color, thickness=8)
            # draw a filled polygon
            if res:
                #image_mask = cv2.fillPoly(image_mask, pts=[pts], color=html_to_bgr(defect_info['color']))
                image_mask = cv2.polylines(image_mask, [pts], isClosed=True, color=html_to_bgr(defect_info['color']), thickness=line_tickness)
                image_mask2 = cv2.putText(image_mask2, defect_info['short_name'], pts_center, cv2.FONT_HERSHEY_SIMPLEX, 1.5, html_to_bgr(defect_info['color']))
            else:
                #image_mask = cv2.fillPoly(image_mask, pts=[pts], color=html_to_bgr(mask_color))
                image_mask = cv2.polylines(image_mask, [pts], isClosed=True, color=html_to_bgr(mask_color), thickness=line_tickness)
        
        # masks
        for obj_bbox in annotations[Annotation.OBJ_BBOXS_KEY]:
            # get defect color and name
            res, defect_info = get_defect_info(db_obj=db_obj, defect_id=obj_bbox[Annotation.CLASS_KEY])

            # polygon points
            pts = np.array(obj_bbox[Annotation.BBOX_KEY] , np.int32)
            pts_center = centroid(vertexes=pts)
            
            # draw a filled bbox
            if res:
                image_mask = cv2.rectangle(image_mask, pts[0], pts[1], color=html_to_bgr(defect_info['color']), thickness=line_tickness)
                image_mask2 = cv2.putText(image_mask2, defect_info['short_name'], pts_center, cv2.FONT_HERSHEY_SIMPLEX, 1.5, html_to_bgr(defect_info['color']))
            else:
                image_mask = cv2.rectangle(image_mask, pts[0], pts[1], color=html_to_bgr(mask_color), thickness=line_tickness)

    except:
        return False, 'Cant laod masks from annotation file'
    
    try:
        baskground_image = image.copy()
        # Create a new np array
        shapes = np.zeros_like(image, np.uint8)
        shapes2 = np.zeros_like(image, np.uint8)
        # Put the overlay at the bottom-right corner
        shapes[0:, 0:] = image_mask
        shapes2[0:, 0:] = image_mask2
        # Change this into bool to use it as mask
        mask = shapes.astype(bool)
        mask2 = shapes2.astype(bool)
        
        # Create the overlay
        baskground_image[mask] = cv2.addWeighted(baskground_image, 1-mask_alpha, shapes, mask_alpha, 0)[mask]
        baskground_image[mask2] = cv2.addWeighted(baskground_image, 1-mask_alpha, shapes2, mask_alpha, 0)[mask2]
    except:
        return False, 'Cant annotation mask overlay on image'

    return True, baskground_image


# get defect name and color by id
def get_defect_info(db_obj, defect_id):
    try:
        defect_info = classification_list_funcs.load_defects_from_db(db_obj=db_obj, defect_id=[defect_id])
        if len(defect_id) > 0:
            return True, defect_info
        else:
            return False, 'Cant load defect info from database'

    except:
        return False, 'Cant load defect info from database'


def html_to_bgr(html_code):
    rgb = ImageColor.getcolor(html_code, "RGB")
    # convert to bgr
    bgr = (rgb[2], rgb[1], rgb[0])
    return bgr


# get centroid of polygon/box
def centroid(vertexes):
    _x_list = [vertex [0] for vertex in vertexes]
    _y_list = [vertex [1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return(int(_x)-30, int(_y)+20)


if __name__ == "__main__":
    html_to_bgr(mask_color)
    


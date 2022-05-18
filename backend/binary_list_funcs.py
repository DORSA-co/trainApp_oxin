from PySide6.QtWidgets import QLabel as sQLabel
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
import os
import cv2

import texts
from neighbouring_UI import neighbouring



n_images_per_row = 8
no_image_path = './images/no_image.png'
widjet_prefixes = {'perfect':'binary_list_perfect', 'defect':'binary_list_defect'}
image_list_object_names = {'perfect':'perfect_images', 'defect':'defect_images'}
language = 'en'


# create image slider area on UI
def create_image_slider_on_ui(ui_obj, frame_obj, prefix=widjet_prefixes['perfect']):
    # create layout
    try:
        layout = sQHBoxLayout()
        eval("exec('ui_obj.%s_layout = layout')" % prefix)
        
        # creat and assign labels to layout
        for i in range(n_images_per_row):
            label = sQLabel()
            label.setScaledContents(True)
            # assign label to UI with name
            eval("exec('ui_obj.%s_label_%s = label')" % (prefix, i))
            # add to layout
            eval('ui_obj.%s_layout' % prefix).addWidget(eval('ui_obj.%s_label_%s' % (prefix, i)))
            # assign image
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, i)), image=None, no_image=True)

            # doble-click event for labels
            #eval('ui_obj.%s_label_%s' % (prefix, i)).mouseDoubleClickEvent = maximize_image_on_click

        # assign layout to frame
        frame_obj.setLayout(eval('ui_obj.%s_layout' % prefix))
        return True

    except:
        ui_obj.set_warning(texts.WARNINGS['BUILD_BINARYLIST_SLIDER_ERROR'][language], 'binarylist', level=2)
        return False


# maximize image label on click (open image in a window)
def maximize_image_on_click(event, image_path):
    image = image = cv2.imread(image_path)
    window = neighbouring(image)
    window.show()


# set/update images to ui
def set_image_to_ui_slider(ui_obj, sub_directory, image_path_list, prefix=widjet_prefixes['perfect']):
    try:
        # set dataset images on UI
        i = 0
        for i, image_path in enumerate(image_path_list):
            # load image
            image = cv2.imread(os.path.join(sub_directory, image_path))
            # set to UI label
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, i)), image=image, no_image=False)
        # set last image labels on UI as empty
        for j in range(i+1, n_images_per_row):
            set_image_to_ui(label_name=eval('ui_obj.%s_label_%s' % (prefix, j)), image=None, no_image=True)
        
        return True

    except:
        return False

        

# get binarylist params from ui
def get_params_from_ui(ui_obj):
    params = {}
    try:
        params['dataset_path'] = ui_obj.binarylist_dataset_lineedit.toPlainText()
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
    convert_to_Qt_format = sQImage(image.data, w, h, bytes_per_line, sQImage.Format_RGB888)
    label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))


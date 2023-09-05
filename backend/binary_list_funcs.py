from functools import partial
from pickle import FALSE
from telnetlib import BINARY
from PySide6.QtWidgets import QLabel as sQLabel
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
import json
import os
import cv2
import numpy as np
from PIL import ImageColor

import texts, texts_codes
from neighbouring_UI import neighbouring
from backend import Annotation, classification_list_funcs, dataset


n_images_per_row = 4  # number of current images on binarylist page slider
n_images_per_row_classlist = (
    3  # number of current images on classification list page slider
)
no_image_path = (
    "./images/no_image.png"  # path for a raw image (using for labels default image)
)
widjet_prefixes = {"perfect": "binary_list_perfect", "defect": "binary_list_defect"}
image_list_object_names = {"perfect": "perfect_images", "defect": "defect_images"}
mask_color = "#FF0000"  # BGR format
line_tickness = 4  # this is the line width for drawing defect masks/bboxes on images
mask_alpha = 0.5  # alpha channel for image mask to make it transparent

# ______________________________________________________________________JJ
BINARY_PATH = "binary"
DEFCET_PATH = "defect"
PERFECT_PATH = "perfect"
DEFCET_MASK_PATH = "defect_mask"
ANNOTATION_PATH = "annotations"
PIPLINES_PATH = "evaluated_jsons"
WRONG_RIGHT_SYMBOL = {True: r"UI\images\true.jpg", False: r"UI\images\wrong.jpg"}

# ______________________________________________________________________JJ


# create image slider area on UI
def create_image_slider_on_ui(
    ui_obj,
    db_obj,
    frame_obj,
    prefix=widjet_prefixes["perfect"],
    image_per_row=n_images_per_row,
):
    """this function is used to create dataset image slider on ui binary list page, this slider is used to show dataset images

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param frame_obj: ui frame object to create slider in
    :type frame_obj: _type_
    :param prefix: _description_, defaults to widjet_prefixes['perfect']
    :type prefix: _type_, optional
    :param image_per_row: n images to show on each page of slider, defaults to n_images_per_row
    :type image_per_row: _type_, int
    :return: a boolean determining if the slider is initialized
    :rtype: boolean
    """

    try:
        # create layout
        layout = sQHBoxLayout()
        eval("exec('ui_obj.%s_layout = layout')" % prefix)

        # creat and assign labels to layout
        for i in range(image_per_row):
            label = sQLabel()
            label.setScaledContents(True)
            label.setWhatsThis("")
            # assign label to UI with name
            eval("exec('ui_obj.%s_label_%s = label')" % (prefix, i))
            # add to layout
            eval("ui_obj.%s_layout" % prefix).addWidget(
                eval("ui_obj.%s_label_%s" % (prefix, i))
            )
            # assign image
            set_image_to_ui(
                label_name=eval("ui_obj.%s_label_%s" % (prefix, i)),
                image=None,
                no_image=True,
            )

            # doble-click event for labels
            eval("ui_obj.%s_label_%s" % (prefix, i)).mouseDoubleClickEvent = partial(
                maximize_image_on_click,
                ui_obj,
                db_obj,
                eval("ui_obj.%s_label_%s" % (prefix, i)),
            )

        # assign layout to frame
        frame_obj.setLayout(eval("ui_obj.%s_layout" % prefix))

        ui_obj.logger.create_new_log(
            message=texts.MESSEGES["BINARYLIST_SLIDER_build"]["en"],
            code=texts_codes.SubTypes["BINARYLIST_SLIDER_build"],
            level=1,
        )
        return True

    except Exception as e:
        ui_obj.set_warning(
            texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"]["en"],
            "binarylist",
            texts_codes.SubTypes["BUILD_BINARYLIST_SLIDER_ERROR"],
            level=3,
        )
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"]["en"],
            code=texts_codes.SubTypes["BUILD_BINARYLIST_SLIDER_ERROR"],
            level=5,
        )
        return False


# maximize image label on click (open image in a window)
def maximize_image_on_click(ui_obj, db_obj, label, event):
    """this function is used to maximize an image lable on click (open new image viewer window)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param label: label name
    :type label: _type_
    :param event: _description_
    :type event: _type_
    """
    pathes = label.whatsThis()  # image path is set on its label whatsthis

    try:
        # path exists
        if pathes != "":
            pathes = pathes.split("#")
            # pathes invalid format
            if len(pathes) != 3:
                ui_obj.set_warning(
                    texts.ERRORS["MAXIMIZE_IMAGE_ERROR"][ui_obj.language],
                    "binarylist",
                    level=3,
                )
                ui_obj.logger.create_new_log(
                    message=texts.ERRORS["MAXIMIZE_IMAGE_ERROR"][ui_obj.language],
                    level=3,
                )
                return

            # load image
            if pathes[2] != "fullpath":
                image = cv2.imread(os.path.join(pathes[0], pathes[1]))
                # mask (annotations) overlay
                annotation_path = os.path.join(pathes[2], pathes[1][:-4] + ".json")

            else:
                image = cv2.imread(pathes[0])
                # mask (annotations) overlay
                annotation_path = pathes[1]

            res, annotated_image = create_mask_from_annotation_file(
                ui_obj=ui_obj,
                db_obj=db_obj,
                image=image,
                annotation_path=annotation_path,
            )

            if res:
                ui_obj.window = neighbouring(
                    image,
                    annotated_image=annotated_image,
                    has_annotation=True,
                    lang=ui_obj.language,
                )
                ui_obj.window.show()
            else:
                ui_obj.window = neighbouring(
                    image,
                    annotated_image=annotated_image,
                    has_annotation=False,
                    lang=ui_obj.language,
                )
                ui_obj.window.show()

    except Exception as e:
        ui_obj.set_warning(
            texts.WARNINGS["BINARYLIST_MAXIMIZE_IMAGE_ERROR"][ui_obj.language],
            "binarylist",
            level=2,
        )
        ui_obj.logger.create_new_log(
            message=texts.WARNINGS["BINARYLIST_MAXIMIZE_IMAGE_ERROR"][ui_obj.language],
            level=5,
        )


def set_image_on_loadDataSetSlider_in_PBT(
    ui_obj,
    db_obj,
    frame_obj,
    prefix="original",
    image_per_row=n_images_per_row,
    refersh_mode=False,
):
    # create layout
    try:
        # if not refersh_mode:
        layout = sQHBoxLayout()
        eval("exec('ui_obj.loadDataset_PBT_page_layout_%s = layout')" % prefix)

        # creat and assign labels to layout
        for i in range(image_per_row):
            # if not refersh_mode:
            label = sQLabel()
            label.setScaledContents(True)
            label.setWhatsThis("")
            # assign label to UI with name
            eval(
                "exec('ui_obj.loadDataset_PBT_page_label_%s_%s = label')" % (prefix, i)
            )
            # add to layout
            eval("ui_obj.loadDataset_PBT_page_layout_%s" % prefix).addWidget(
                eval("ui_obj.loadDataset_PBT_page_label_%s_%s" % (prefix, i))
            )
            # assign image
            set_image_to_ui(
                label_name=eval(
                    "ui_obj.loadDataset_PBT_page_label_%s_%s" % (prefix, i)
                ),
                image=None,
                no_image=True,
            )

            # # doble-click event for labels
            # eval(
            #     "ui_obj.loadDataset_PBT_page_label_%s_%s" % (prefix, i)
            # ).mouseDoubleClickEvent = partial(
            #     maximize_image_slider_on_click,
            #     ui_obj,
            #     eval("ui_obj.loadDataset_PBT_page_label_%s_%s" % (prefix, i)),
            # )

        # assign layout to frame
        frame_obj.setLayout(eval("ui_obj.loadDataset_PBT_page_layout_%s" % prefix))
        return True

    except:
        ui_obj.set_warning(
            texts.ERORS["BUILD_BINARYLIST_SLIDER_ERROR"][ui_obj.language],
            "binarylist",
            level=3,
        )
        return False


# set/update images to ui
def set_image_to_ui_slider(
    ui_obj,
    sub_directory,
    annot_sub_direcotory,
    image_path_list,
    prefix=widjet_prefixes["perfect"],
    image_per_row=n_images_per_row,
):
    """this function is used to set images on binarylist image sliders (using image names and subdirectory)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param sub_directory: subdirectory of images
    :type sub_directory: str
    :param annot_sub_direcotory: subdirectory of annotations
    :type annot_sub_direcotory: str
    :param image_path_list: images path/filenames list
    :type image_path_list: list of strings
    :param prefix: _description_, defaults to widjet_prefixes['perfect']
    :type prefix: _type_, optional
    :param image_per_row: n images in each page on slider, defaults to n_images_per_row
    :type image_per_row: int, optional
    :return: _description_
    :rtype: boolean determiing if done
    """

    try:
        # set dataset images on UI
        for i, image_path in enumerate(image_path_list):
            # load image
            image = cv2.imread(os.path.join(sub_directory, image_path))
            # set to UI label
            set_image_to_ui(
                label_name=eval("ui_obj.%s_label_%s" % (prefix, i)),
                image=image,
                no_image=False,
            )

            # update/set text (image url) on image label whatsthis
            whats_this_text = (
                sub_directory + "#" + image_path + "#" + annot_sub_direcotory
            )
            eval("ui_obj.%s_label_%s" % (prefix, i)).setWhatsThis(whats_this_text)

        # set last image labels on UI as empty
        try:
            i += 1
        except:
            i = 0
        for j in range(i, image_per_row):
            set_image_to_ui(
                label_name=eval("ui_obj.%s_label_%s" % (prefix, j)),
                image=None,
                no_image=True,
            )
            eval("ui_obj.%s_label_%s" % (prefix, j)).setWhatsThis("")

        return True

    except Exception as e:
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["set_image_to_slider_failed"][ui_obj.language], level=5
        )
        return False


# __________________________________________________JJ ZONE STARTS
def set_image_to_ui_slider_eidted_version(
    ui_obj,
    image_path_list,
    predict_eval,
    image_per_row=n_images_per_row,
):
    image_type = "noimage"

    # set dataset images on UI
    for i, image_path in enumerate(image_path_list):
        # load image
        image = cv2.imread(image_path)
        mask = cv2.imread(predict_eval[image_path])

        if image_path.find("perfect") != -1:
            image_type = "perfect"
        elif image_path.find("defect") != -1:
            image_type = "defect"
        else:
            image_type = "noimage"

        # set to UI label
        true_label = eval("ui_obj.loadDataset_PBT_page_label_%s_%s" % ("original", i))
        true_label.setWhatsThis(image_path)
        true_label.mouseDoubleClickEvent = partial(
            maximize_image_slider_on_click, ui_obj, true_label
        )
        set_image_to_ui_edited_version(
            label_name=true_label,
            image=image,
            no_image=False,
            image_type=image_type,
            use_color=True,
        )
        pred_label = eval("ui_obj.loadDataset_PBT_page_label_%s_%s" % ("evaluated", i))
        pred_label.setWhatsThis(predict_eval[image_path])
        pred_label.mouseDoubleClickEvent = partial(
            maximize_image_slider_on_click, ui_obj, pred_label
        )
        set_image_to_ui_edited_version(
            label_name=pred_label,
            image=mask,
            no_image=False,
            image_type=image_type,
            use_color=True,
        )
    image_type = "noimage"
    for j in range(image_per_row - len(image_path_list)):
        true_label = eval(
            "ui_obj.loadDataset_PBT_page_label_%s_%s"
            % ("original", j + len(image_path_list))
        )
        true_label.setWhatsThis("")
        set_image_to_ui_edited_version(
            label_name=true_label,
            image=image,
            no_image=True,
            image_type=image_type,
            use_color=True,
        )
        pred_label = eval(
            "ui_obj.loadDataset_PBT_page_label_%s_%s"
            % ("evaluated", j + len(image_path_list))
        )
        pred_label.setWhatsThis("")
        set_image_to_ui_edited_version(
            label_name=pred_label,
            image=mask,
            no_image=True,
            image_type=image_type,
            use_color=True,
        )


def maximize_image_slider_on_click(ui_obj, label, event):
    pathes = label.whatsThis()
    if pathes != "":
        image = cv2.imread(pathes)
        ui_obj.window = neighbouring(
            img=image,
            annotated_image=None,
            has_annotation=False,
            lang=ui_obj.language,
        )
        ui_obj.window.show()


# __________________________________________________JJ ZONE STOPS
# set/update images to ui given full image and annoptation path
def set_image_to_ui_slider_full_path(
    ui_obj,
    image_path_list,
    annot_path_list,
    prefix=widjet_prefixes["perfect"],
    image_per_row=n_images_per_row,
):
    """this function is used to set images on binarylist image sliders (using image full/relative pathes)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param image_path_list: image full pathes
    :type image_path_list: list of str
    :param annot_path_list: annotaions full pathes
    :type annot_path_list: list of str
    :param prefix: _description_, defaults to widjet_prefixes['perfect']
    :type prefix: _type_, optional
    :param image_per_row: n image in slider page, defaults to n_images_per_row
    :type image_per_row: int, optional
    :return: _description_
    :rtype: boolean determiing if done
    """

    try:
        # set dataset images on UI
        for i, image_path in enumerate(image_path_list):
            # load image
            image = cv2.imread(image_path)
            # set to UI label
            set_image_to_ui(
                label_name=eval("ui_obj.%s_label_%s" % (prefix, i)),
                image=image,
                no_image=False,
            )

            # update/set text (image url) on image label whatsthis
            whats_this_text = image_path + "#" + annot_path_list[i] + "#" + "fullpath"
            eval("ui_obj.%s_label_%s" % (prefix, i)).setWhatsThis(whats_this_text)

        # set last image labels on UI as empty
        try:
            i += 1
        except:
            i = 0
        for j in range(i, image_per_row):
            set_image_to_ui(
                label_name=eval("ui_obj.%s_label_%s" % (prefix, j)),
                image=None,
                no_image=True,
            )
            eval("ui_obj.%s_label_%s" % (prefix, j)).setWhatsThis("")

        return True

    except Exception as e:
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["set_image_to_slider_failed"][ui_obj.language], level=5
        )
        return False


# get binarylist params from ui
def get_params_from_ui(ui_obj):
    """this function is used to get selected binary dataset path form ui linedit

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :return: dataset path
    :rtype: dict
    """

    params = {}
    try:
        params["dataset_path"] = ui_obj.binarylist_dataset_lineedit.text()
        return params

    except:
        return {}


# get image pathes in dataset directory
def get_binarylist_image_pathes_list(ds_obj, dataset_pathes):
    """this function is used to get binarylist selected datasets image pathes

    :param ds_obj: dataset object
    :type ds_obj: _type_
    :param dataset_pathes: dataset info (including path) of selected datasets
    :type dataset_pathes: list of dicts
    :return:
        boolean determing if any perfect image exists
        list of perfect image pathes
        boolean determing if any defect image exists
        list of defect image pathes
        list of defect annotaton pathes
        dict containing n defect and perfect images ({dataset.DEFECT_FOLDER:n, dataset.PERFECT_FOLDER:m})
    :rtype: boolean, list of str, boolean, list of str, list of str, dict
    """

    # perfect
    perfect_image_pathes = []
    perfect_check = False
    defect_image_pathes = []
    defect_annot_pathes = []
    defect_check = False
    binary_count = {dataset.DEFECT_FOLDER: 0, dataset.PERFECT_FOLDER: 0}

    for ds_path in dataset_pathes:
        ds_path = ds_path["path"]
        # perfect path
        perfect_path = os.path.join(
            ds_path, dataset.BINARY_FOLDER, dataset.PERFECT_FOLDER
        )

        if os.path.exists(perfect_path):
            # get image pathes
            for img_path in getfiles(perfect_path):
                perfect_check = True
                perfect_image_pathes.append(os.path.join(perfect_path, img_path))
                binary_count[dataset.PERFECT_FOLDER] += 1

        # defect path
        defect_path = os.path.join(
            ds_path, dataset.BINARY_FOLDER, dataset.DEFECT_FOLDER
        )

        if os.path.exists(defect_path):
            # get image pathes
            for img_path in getfiles(defect_path):
                defect_check = True
                defect_image_pathes.append(os.path.join(defect_path, img_path))
                binary_count[dataset.DEFECT_FOLDER] += 1
                # annotation
                annot_path = os.path.join(
                    ds_path, dataset.ANNOTATIONS_FOLDER, img_path[:-4] + ".json"
                )

                if os.path.exists(annot_path):
                    defect_annot_pathes.append(annot_path)
                else:
                    defect_annot_pathes.append("")

    #
    return (
        perfect_check,
        perfect_image_pathes,
        defect_check,
        defect_image_pathes,
        defect_annot_pathes,
        binary_count,
    )


# get files in a directory
def getfiles(dirpath):
    """this function is used to get file pathes in a directory

    :param dirpath: directory path
    :type dirpath: str
    :return: list of file pathes
    :rtype: list of str
    """
    try:
        a = [
            s
            for s in os.listdir(dirpath)
            if os.path.isfile(os.path.join(dirpath, s))
            and (
                s[-3:] == "png"
                or s[-3:] == "jpg"
                or s[-4:] == "tiff"
                or s[-3:] == "bmp"
            )
        ]
        a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
        return a

    except:
        return []


def set_image_to_ui_edited_version(
    label_name, image, no_image=False, image_type="perfect", use_color=False
):
    if no_image:
        image = cv2.imread(no_image_path)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    image = cv2.resize(image, (224, 224))
    h, w, ch = image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = sQImage(
        image.data, w, h, bytes_per_line, sQImage.Format_BGR888
    )
    if use_color:
        if image_type == "perfect" and not (no_image):
            label_name.setStyleSheet("border: 4px solid green;")
        elif image_type == "defect" and not (no_image):
            label_name.setStyleSheet("border: 4px solid red;")
        else:
            label_name.setStyleSheet("border: 4px solid white;")
    else:
        label_name.setStyleSheet("border: 4px solid white;")

    label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))


# set cameras imnages to UI
def set_image_to_ui(label_name, image, no_image=False):
    """this function is used to set an image on ui label using label name

    :param label_name: name if the label
    :type label_name: _type_
    :param image: image in numpy format
    :type image: numpy array
    :param no_image: a boolean determinign wheater to assign defaults raw image to label. Defaults to False., defaults to False
    :type no_image: bool, optional
    """
    if no_image:
        image = cv2.imread(no_image_path)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    #
    h, w, ch = image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = sQImage(
        image.data, w, h, bytes_per_line, sQImage.Format_BGR888
    )
    label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))


# read annotation files and create mask
def create_mask_from_annotation_file(ui_obj, db_obj, image, annotation_path):
    """this function is used to create image defects mask from its json annotations file

    :param db_obj: database object
    :type db_obj: _type_
    :param image: main image
    :type image: numpy array
    :param annotation_path: json annotation file path
    :type annotation_path: str
    :return: a boolean determining if done, and the resualt image if task is done/ or error message
    :rtype: boolean(True), image or boolean(False), error string
    """

    # create image mask
    image_shape = image.shape
    image_mask = np.zeros((image_shape))
    image_mask2 = np.zeros((image_shape))

    # load json file
    try:
        with open(annotation_path) as json_file:
            annotations = json.load(json_file)
    except:
        return False, texts.ERRORS["annotation_not_exist"][ui_obj.language]

    # draw bbox and polygons on mask
    # polygons
    try:
        for obj_mask in annotations[Annotation.OBJ_MASKS_KEY]:
            # get defect color and name
            res, defect_info = get_defect_info(
                ui_obj=ui_obj, db_obj=db_obj, defect_id=obj_mask[Annotation.CLASS_KEY]
            )

            # polygon points
            pts = np.array(obj_mask[Annotation.MASK_KEY], np.int32)
            pts_center = centroid(vertexes=pts)
            pts = pts.reshape((-1, 1, 2))
            # Draw a line nofilled polygon
            # draw a filled polygon
            try:
                line_thickness = obj_mask["line_thickness"]
            except:
                line_thickness = 1
            if res:
                image_mask = cv2.polylines(
                    image_mask,
                    [pts],
                    isClosed=True,
                    color=html_to_bgr(defect_info["color"]),
                    thickness=line_thickness,
                )
                image_mask2 = cv2.putText(
                    image_mask2,
                    defect_info["defect_ID"]+' '+defect_info["short_name"],
                    pts_center,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    4,
                    html_to_bgr(defect_info["color"]),
                    2,
                )
            else:
                # image_mask = cv2.fillPoly(image_mask, pts=[pts], color=html_to_bgr(mask_color))
                image_mask = cv2.polylines(
                    image_mask,
                    [pts],
                    isClosed=True,
                    color=html_to_bgr(mask_color),
                    thickness=line_thickness,
                )

        # masks
        # for obj_bbox in annotations[Annotation.OBJ_BBOXS_KEY]:
        #     # get defect color and name
        #     res, defect_info = get_defect_info(
        #         ui_obj=ui_obj, db_obj=db_obj, defect_id=obj_bbox[Annotation.CLASS_KEY]
        #     )

        # # polygon points
        # pts = np.array(obj_bbox[Annotation.BBOX_KEY], np.int32)
        # pts_center = centroid(vertexes=pts)

        # # draw a filled bbox
        # if res:
        #     image_mask = cv2.rectangle(
        #         image_mask,
        #         pts[0],
        #         pts[1],
        #         color=html_to_bgr(defect_info["color"]),
        #         thickness=line_tickness,
        #     )
        #     image_mask2 = cv2.putText(
        #         image_mask2,
        #         defect_info["short_name"],
        #         pts_center,
        #         cv2.FONT_HERSHEY_SIMPLEX,
        #         1.5,
        #         html_to_bgr(defect_info["color"]),
        #     )
        # else:
        #     image_mask = cv2.rectangle(
        #         image_mask,
        #         pts[0],
        #         pts[1],
        #         color=html_to_bgr(mask_color),
        #         thickness=line_tickness,
        #     )

    except Exception as e:
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["load_masks_from_json_failed"][ui_obj.language],
            level=5,
        )
        return False, texts.ERRORS["load_masks_from_json_failed"][ui_obj.language]

    # add annotation mask as a transparent layer to main image
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
        baskground_image[mask] = cv2.addWeighted(
            baskground_image, 1 - mask_alpha, shapes, mask_alpha, 0
        )[mask]
        baskground_image[mask2] = cv2.addWeighted(
            baskground_image, 1 - mask_alpha, shapes2, mask_alpha, 0
        )[mask2]

    except Exception as e:
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["mask_overlay_to_image_failed"][ui_obj.language],
            level=5,
        )
        return False, texts.ERRORS["mask_overlay_to_image_failed"][ui_obj.language]

    return True, baskground_image


# get defect name and color by id
def get_defect_info(ui_obj, db_obj, defect_id):
    """this function is used to get defect infoes from database, using its id

    :param db_obj: database object
    :type db_obj: _type_
    :param defect_id: id of the defect
    :type defect_id: str
    :return: a boolean determining if defect info is recieved from database, and defect_info/error message
    :rtype: boolean(True), dict or boolean(False), str
    """

    try:
        defect_info = classification_list_funcs.load_defects_from_db(
            db_obj=db_obj, defect_id=[defect_id]
        )
        if len(defect_id) > 0:
            return True, defect_info
        else:
            ui_obj.logger.create_new_log(
                message=texts.ERRORS["database_load_defects_failed"][ui_obj.language],
                level=2,
            )
            return False, texts.ERRORS["database_load_defects_failed"][ui_obj.language]

    except Exception as e:
        ui_obj.logger.create_new_log(
            message=texts.ERRORS["database_load_defects_failed"][ui_obj.language],
            level=5,
        )
        return False, texts.ERRORS["database_load_defects_failed"][ui_obj.language]


def html_to_bgr(html_code):
    """this function is used to convert html color code to bgr code

    :param html_code: html color cole
    :type html_code: str
    :return: bgr color code
    :rtype: tupple
    """

    rgb = ImageColor.getcolor(html_code, "RGB")
    # convert to bgr
    bgr = (rgb[2], rgb[1], rgb[0])

    return bgr


# get centroid of polygon/box
def centroid(vertexes):
    """this function is used to get centroid if a polygan/bbox using its vertices

    :param vertexes: list of polygan vertices
    :type vertexes: _type_
    :return: centriod of the polygan
        x:
        y:
    :rtype: tupple
    """

    _x_list = [vertex[0] for vertex in vertexes]
    _y_list = [vertex[1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len

    return (int(_x) - 30, int(_y) + 20)

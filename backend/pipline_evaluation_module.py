import cv2
import os
import json
import torch
import numpy as np


from random_split import get_crops_normal
from PySide6.QtCore import QObject, QThread, Signal
from tensorflow.keras.losses import BinaryCrossentropy
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from yolov5.utils.general import (
    check_img_size,
    colorstr,
    TQDM_BAR_FORMAT,
    non_max_suppression,
    scale_boxes,
    xywh2xyxy,
)

DEFECT_FOLDER = "defect"
BINARY_FOLDER = "binary"
DEFECT_MASK_FOLDER = "defect_mask"
ANNOTATION_FOLDER = "annotations"
IMG_EXTENSION_PNG = ".png"
IMG_EXTENSION_JPG = ".jpg"
LABEL_EXTENSION_TXT = ".txt"
ANNOTATION_EXTENSION = ".json"
SPLITED_INPUT_TYPE = "splited"
RESIZED_INPUT_TYPE = "resized"


# _______Threading Management Class_______#
class Evaluation_worker(QObject):
    # vars for handling thread
    finished = Signal()
    progress = Signal(dict, dict)
    pgb_bar_signal = Signal(float)

    def set_params(
        self,
        data_path,
        pipline_obj,
        input_type,
        input_size,
        binary_model,
        binary_threshold,
        yolo_model,
        yolo_conf_thres,
        yolo_iou_thres,
        yolo_max_det,
    ):
        # _______block one_________#
        self.data_path = data_path
        self.pipline_obj = pipline_obj
        self.input_type = input_type
        self.input_size = input_size
        # ___________block two (binary)_______
        self.binary_model = binary_model
        self.binary_threshold = binary_threshold
        self.binary_pred = []
        self.binary_grandtruth = []
        # __________yolo three (yolo)_________
        self.yolo_model = yolo_model
        self.yolo_conf_thres = yolo_conf_thres
        self.yolo_iou_thres = yolo_iou_thres
        self.yolo_max_det = yolo_max_det

    # _______________________________

    def evaluate(self):
        # for i, image_path in enumerate(self.data_path):
        #     defect = True if image_path.find(DEFECT_FOLDER) != -1 else False
        #     self.Data2Binary(img_path=image_path, defect=defect)

        # self.finished.emit()
        pass

    # _____________________________________
    def Data2Binary(self, img_path, defect):
        # load input ------->img
        img = cv2.imread(img_path)
        # load output ------->label
        if self.input_type == SPLITED_INPUT_TYPE:
            if defect:
                mask_path = img_path.replace(DEFECT_FOLDER, DEFECT_MASK_FOLDER)
                mask = cv2.imread(mask_path)
                annotation_path = img_path.replace(
                    os.path.join(BINARY_FOLDER, DEFECT_FOLDER), ANNOTATION_FOLDER
                )
                annotation_path = annotation_path.replace(
                    IMG_EXTENSION_PNG, ANNOTATION_EXTENSION
                )
                with open(annotation_path) as f:
                    annotation = json.load(f)
            else:
                mask = np.zeros(shape=img.shape, dtype=np.uint8)
                annotation = None

            input2binary, crops_masks, crops_annotations = get_crops_normal(
                img=img,
                mask=mask,
                size=(self.input_size, self.input_size),
                annotation=annotation,
            )

        elif self.input_type == RESIZED_INPUT_TYPE:
            input2binary = np.array(
                [cv2.resize(img, (self.input_size, self.input_size))]
            )
            crops_annotations = [annotation]

        # ______model predicting_____#
        # set preds of model
        preds = self.binary_model.predict(input2binary)
        preds = (preds > self.binary_threshold).astype("float16")
        self.binary_pred.append(preds)
        # set grand truth of model
        grand_truth = np.zeros(preds.shape, dtype=np.float16)
        if defect:
            for index, crops_annotation in enumerate(crops_annotations):
                if crops_annotation["obj_masks"] != []:
                    grand_truth[index] = 1
        self.binary_grandtruth.append(grand_truth)

    # _____________________________________

    def create_yolo_dataloader(self, path, task="val"):
        stride = self.yolo_model.stride
        engine = self.yolo_model.engine
        if not (engine):
            yolo_device = self.yolo_model.device
        imgsz = check_img_size(self.input_size, s=stride)

    def Binary2Yolo(self, pbar, yolo_device):
        for batch_i, (im, targets, paths, shapes) in enumerate(pbar):
            im = im.to(yolo_device, non_blocking=True)
            im = im.float()
            targets = targets.to(yolo_device)
            nb, _, height, width = im.shape
            preds, train_out = self.yolo_model(im)
            targets[:, 2:] *= torch.tensor(
                (width, height, width, height), device=yolo_device
            )
            lb = [targets[targets[:, 0] == i, 1:] for i in range(nb)]
            preds = non_max_suppression(
                preds,
                self.yolo_conf_thres,
                self.yolo_iou_thres,
                labels=lb,
                multi_label=True,
                agnostic=False,
                max_det=self.yolo_max_det,
            )

    def PrepareBinaryOutputForYolo(self):
        pass

    # _____________________________________
    def Binary2Unet(self):
        pass

    def PrepareBinaryOutputForUnet(self):
        pass

    def Unet2Yolo(self):
        pass

    def PrepareUnetOutputForYolo(self):
        pass

    def Unet2Categorical(self):
        pass

    def PrepareUnetOutputForCategorical(self):
        pass

    # ___________________________________

    def ComputeMetrics(self):
        pass

    def create_dataset_folder_structure(self):
        pass

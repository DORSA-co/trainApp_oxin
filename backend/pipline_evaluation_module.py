import cv2
import os
import math
import shutil
import json
import torch
import itertools
import numpy as np
from PySide6.QtCore import QObject, Signal
from tensorflow.keras.losses import BinaryCrossentropy
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from tqdm import tqdm
from pathlib import Path
from yolov5.utils.metrics import ap_per_class, box_iou
from yolov5.utils.dataloaders import create_dataloader
from yolov5.utils.general import (
    check_img_size,
    colorstr,
    TQDM_BAR_FORMAT,
    non_max_suppression,
    scale_boxes,
    xywh2xyxy,
)
from backend import pipelines
from yolov5.utils.plots import Annotator, colors
from yolov5.utils.plots import output_to_target
from random_split import get_crops_normal

PERFECT_FOLDER = "perfect"
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
YOLO_TXT_FILE_DATA = "data"
YOLO_IMAGE_FOLDER = "images"
YOLO_LABEL_FOLDER = "labels"
LOCALIZATION_DATA_FOLDER = "localization"
YOLO_DATASET_PATH = "yolo_dataset"
SLIDER_PATH = "slider"
TRUE_IMAGE_SLIDER = "true"
PRED_IMAGE_SLIDER = "pred"


def plot_images(images, targets, paths=None, fname="images.jpg", names=None):
    # Plot image grid with labels
    if isinstance(images, torch.Tensor):
        images = images.cpu().float().numpy()
    if isinstance(targets, torch.Tensor):
        targets = targets.cpu().numpy()

    max_size = 1920  # max image size
    max_subplots = 16  # max image subplots, i.e. 4x4
    bs, _, h, w = images.shape  # batch size, _, height, width
    bs = min(bs, max_subplots)  # limit plot images
    ns = np.ceil(bs**0.5)  # number of subplots (square)
    if np.max(images[0]) <= 1:
        images *= 255  # de-normalise (optional)

    # Build Image
    mosaic = np.full((int(ns * h), int(ns * w), 3), 255, dtype=np.uint8)  # init
    for i, im in enumerate(images):
        if i == max_subplots:  # if last batch has fewer images than we expect
            break
        x, y = int(w * (i // ns)), int(h * (i % ns))  # block origin
        im = im.transpose(1, 2, 0)
        mosaic[y : y + h, x : x + w, :] = im

    # Resize (optional)
    scale = max_size / ns / max(h, w)
    if scale < 1:
        h = math.ceil(scale * h)
        w = math.ceil(scale * w)
        mosaic = cv2.resize(mosaic, tuple(int(x * ns) for x in (w, h)))

    # Annotate
    fs = int((h + w) * ns * 0.01)  # font size
    annotator = Annotator(
        mosaic, line_width=round(fs / 10), font_size=fs, pil=True, example=names
    )
    for i in range(i + 1):
        x, y = int(w * (i // ns)), int(h * (i % ns))  # block origin
        annotator.rectangle(
            [x, y, x + w, y + h], None, (255, 255, 255), width=2
        )  # borders
        if paths:
            annotator.text(
                (x + 5, y + 5), text=Path(paths[i]).name[:40], txt_color=(220, 220, 220)
            )  # filenames
        if len(targets) > 0:
            ti = targets[targets[:, 0] == i]  # image targets
            boxes = xywh2xyxy(ti[:, 2:6]).T
            classes = ti[:, 1].astype("int")
            labels = ti.shape[1] == 6  # labels if no conf column
            conf = (
                None if labels else ti[:, 6]
            )  # check for confidence presence (label vs pred)

            if boxes.shape[1]:
                if boxes.max() <= 1.01:  # if normalized with tolerance 0.01
                    boxes[[0, 2]] *= w  # scale to pixels
                    boxes[[1, 3]] *= h
                elif scale < 1:  # absolute coords need scale if image scales
                    boxes *= scale
            boxes[[0, 2]] += x
            boxes[[1, 3]] += y
            for j, box in enumerate(boxes.T.tolist()):
                cls = classes[j]
                color = colors(cls)
                cls = names[cls] if names else cls
                if labels or conf[j] > 0.25:  # 0.25 conf thresh
                    label = f"{cls}" if labels else f"{cls} {conf[j]:.1f}"
                    annotator.box_label(box, label, color=color)
    annotator.im.save(fname)  # save


# _______Threading Management Class_______#
class Evaluation_worker(QObject):
    # vars for handling thread
    finished = Signal()
    progress = Signal(dict, dict)
    pgb_bar_signal = Signal(float)
    pipline_signal = Signal(pipelines.Pipeline)

    def set_params(
        self,
        data_path,
        pipline_obj,
        input_type,
        input_size,
        data_nc,
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
        self.data_nc = data_nc
        # ___________block two (binary)_______
        self.binary_model = binary_model
        self.binary_threshold = binary_threshold
        # __________block three (yolo)_________
        self.yolo_model = yolo_model
        self.yolo_conf_thres = yolo_conf_thres
        self.yolo_iou_thres = yolo_iou_thres
        self.yolo_max_det = yolo_max_det
        # ______________block four (progress bar const)___________
        self.binary_evaluation_part = 40
        self.yolo_evaluation_data_preparation = 20
        self.yolo_evaluation_part = 30
        self.final_step = 10
        # ________________block five (slider param)__________
        self.dic_of_Cimag = {"true": {}, "pred": {}}
        self.dic_of_slider_image_path = {}

    def evaluate(self):
        loss, accuracy, precision, recall, f1, data2location = self.Data2Binary()

        bmetrics = [
            round(loss, 3),
            round(accuracy, 2),
            round(recall, 2),
            round(precision, 2),
            round(f1, 2),
        ]
        self.pipline_obj.set_binary_model(
            key=pipelines.MODEL_LOSS, value=int(round(loss, 3))
        )
        self.pipline_obj.set_binary_model(
            key=pipelines.MODEL_ACCURACY, value=int(round(accuracy, 2))
        )
        self.pipline_obj.set_binary_model(
            key=pipelines.MODEL_PRECISION, value=int(round(precision, 2))
        )
        self.pipline_obj.set_binary_model(
            key=pipelines.MODEL_RECALL, value=int(round(recall, 2))
        )
        self.pipline_obj.set_binary_model(
            key=pipelines.MODEL_F1, value=int(round(f1, 2))
        )
        self.pgb_bar_signal.emit(self.binary_evaluation_part)
        yolo_data_path = self.PrepareBinaryOutputForYolo(
            imgs=data2location["img"],
            annotions=data2location["annotation"],
            filenames=data2location["filename"],
        )
        self.pgb_bar_signal.emit(
            self.yolo_evaluation_data_preparation + self.binary_evaluation_part
        )
        mp, mr, map50, map, maps = self.Binary2Yolo(
            path=os.path.dirname(yolo_data_path)
        )

        ymetrics = [round(mp, 2), round(mr, 2), round(map50, 2), round(map, 2)]
        self.pipline_obj.set_yolo_model(
            key=pipelines.MODEL_PRECISION, value=(int(round(mp, 2)))
        )
        self.pipline_obj.set_yolo_model(
            key=pipelines.MODEL_RECALL, value=int(round(mr, 2))
        )
        self.pipline_obj.set_yolo_model(
            key=pipelines.MODEL_MAP05, value=int(round(map50, 2))
        )
        self.pipline_obj.set_yolo_model(
            key=pipelines.MODEL_MAP0595, value=int(round(map, 2))
        )
        metrics_info = {"binary": bmetrics, "yolo": ymetrics}

        self.pgb_bar_signal.emit(
            self.yolo_evaluation_part
            + self.binary_evaluation_part
            + self.yolo_evaluation_data_preparation
        )
        self.progress.emit(metrics_info, self.dic_of_slider_image_path)
        self.pgb_bar_signal.emit(
            self.yolo_evaluation_part
            + self.binary_evaluation_part
            + self.yolo_evaluation_data_preparation
            + self.final_step
        )
        self.pipline_signal.emit(self.pipline_obj)
        self.finished.emit()

    def Data2Binary(self):
        binary_pred = []
        binary_grandtruth = []
        defect_imgs = []
        defect_imgs_annotation = []
        defect_imgs_filename = []
        for i, img_path in enumerate(self.data_path):
            self.dic_of_Cimag["true"][
                os.path.splitext(os.path.basename(img_path))[0]
            ] = True
            self.dic_of_Cimag["pred"][
                os.path.splitext(os.path.basename(img_path))[0]
            ] = True
            # load input ------->img
            img = cv2.imread(img_path,0)
            # load output ------->label
            defect = True if img_path.find(DEFECT_FOLDER) != -1 else False
            if self.input_type == SPLITED_INPUT_TYPE or int(self.input_type) ==1:
                if defect:
                    mask_path = img_path.replace(DEFECT_FOLDER, DEFECT_MASK_FOLDER)
                    mask = cv2.imread(mask_path,0)
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

                input2binary, _, crops_annotations = get_crops_normal(
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
            binary_pred.append(preds)
            # set grand truth of model
            grand_truth = np.zeros(preds.shape, dtype=np.float16)
            if defect:
                for index, crops_annotation in enumerate(crops_annotations):
                    if crops_annotation["obj_masks"] != []:
                        grand_truth[index] = 1
            binary_grandtruth.append(grand_truth)

            defects_inx = np.where(preds[:] == 1)[0]
            for index in defects_inx:
                defect_imgs.append(input2binary[index])
                basename = os.path.basename(img_path)
                file_name, _ = os.path.splitext(basename)
                file_name = "{}_{}{}".format(file_name, index, IMG_EXTENSION_JPG)
                defect_imgs_filename.append(file_name)
                if defect:
                    if crops_annotations[index]["obj_masks"] != []:
                        defect_imgs_annotation.append(crops_annotations[index])
                    else:
                        defect_imgs_annotation.append("perfect")
                else:
                    defect_imgs_annotation.append("perfect")
            percentage = (self.binary_evaluation_part * (i + 1)) / len(self.data_path)
            self.pgb_bar_signal.emit(percentage)
        data2location = {
            "img": defect_imgs,
            "annotation": defect_imgs_annotation,
            "filename": defect_imgs_filename,
        }
        # ___compute metrics______
        y_pred = np.concatenate(binary_pred, dtype=np.float16)
        y_true = np.concatenate(binary_grandtruth, dtype=np.float16)

        bce = BinaryCrossentropy()
        f1 = f1_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        accuracy = accuracy_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        loss = bce(y_true, y_pred).numpy()

        return loss, accuracy, precision, recall, f1, data2location

    def makedir(self, path, remove_flag=False):
        if os.path.exists(path):
            if remove_flag:
                shutil.rmtree(path)
                os.mkdir(path)
        else:
            os.mkdir(path)

    def PrepareBinaryOutputForYolo(self, imgs, annotions, filenames):
        path = os.path.dirname(os.path.dirname(os.path.dirname(self.data_path[0])))
        path = os.path.join(path, LOCALIZATION_DATA_FOLDER, YOLO_DATASET_PATH)
        self.makedir(path, remove_flag=True)
        self.makedir(os.path.join(path, YOLO_IMAGE_FOLDER))
        self.makedir(os.path.join(path, YOLO_LABEL_FOLDER))
        all_image_path = []
        for i, (img, annotion, filename) in enumerate(zip(imgs, annotions, filenames)):
            ImagePath = os.path.join(path, YOLO_IMAGE_FOLDER, filename)
            cv2.imwrite(ImagePath, img)
            TextPath = os.path.join(
                path,
                YOLO_LABEL_FOLDER,
                filename.replace(IMG_EXTENSION_JPG, LABEL_EXTENSION_TXT),
            )
            all_image_path.append(TextPath)
            img_info = []
            if annotion != "perfect":  # if grand truth of split is defect
                for defect in annotion["obj_masks"]:
                    # proper data for label ,that saves on .txt file
                    classID = 0  # defect["class"]
                    cnt = np.array(defect["mask"])
                    (x, y, w, h) = cv2.boundingRect(cnt)
                    xc = (x + (w // 2)) / self.input_size
                    yc = (y + (h // 2)) / self.input_size
                    width = w / self.input_size
                    height = h / self.input_size
                    img_info.append([classID, xc, yc, width, height])
            else:
                img_info.append([""])

            with open(TextPath, "w") as f:
                for info in img_info:
                    for item in info:
                        f.write(str(item) + " ")
                    f.write("\n")
        percentage = (self.yolo_evaluation_data_preparation * (i + 1)) / len(imgs)
        self.pgb_bar_signal.emit(self.binary_evaluation_part + percentage)
        txt_label_path = os.path.join(
            path, "{}{}".format(YOLO_TXT_FILE_DATA, LABEL_EXTENSION_TXT)
        )
        with open(txt_label_path, "w") as f:
            for file in all_image_path:
                f.write(file)
                f.write("\n")

        return txt_label_path

    def create_yolo_dataloader(self, path, task="val"):
        stride = self.yolo_model.stride
        engine = self.yolo_model.engine
        yolo_device = "cpu"
        if not (engine):
            yolo_device = self.yolo_model.device
        imgsz = check_img_size(self.input_size, s=stride)
        pad, rect = 0, self.yolo_model.pt
        pred_dataloader = create_dataloader(
            path,
            imgsz,
            1,
            stride,
            False,
            pad=pad,
            rect=rect,
            workers=8,
            prefix=colorstr(f"{task}: "),
        )[0]
        true_dataloader = create_dataloader(
            path=path,
            imgsz=self.input_size,
            batch_size=1,
            stride=1,
            prefix=colorstr(f"{task}: "),
        )[0]
        s = ("%22s" + "%11s" * 6) % (
            "Class",
            "Images",
            "Instances",
            "P",
            "R",
            "mAP50",
            "mAP50-95",
        )
        pred_pbar = tqdm(pred_dataloader, desc=s, bar_format=TQDM_BAR_FORMAT)
        true_pbar = tqdm(true_dataloader, desc=s, bar_format=TQDM_BAR_FORMAT)
        return pred_pbar, true_pbar, yolo_device

    def points_creator(
        self, uper_band_i, uper_band_j, step, lower_band_i=0, lower_band_j=0
    ):
        jj = list(range(lower_band_i, uper_band_i, step))
        ii = list(range(lower_band_j, uper_band_j, step))
        points = list(itertools.product(jj, ii))
        points = sorted(points, key=lambda k: [k[0], k[1]])
        return points

    def save_true_and_pred_output_image(
        self,
        img,
        label,
        paths,
        save_path,
        names,
        batch_i,
        useing,
    ):
        save_path_ = os.path.join(
            save_path, "batch{}_{}".format(batch_i, IMG_EXTENSION_PNG)
        )
        plot_images(img, label, paths, save_path_, names)
        # load original image form source:
        # _____find name of file_________
        basename = os.path.basename(paths[0])
        filename, _ = os.path.splitext(basename)
        filename_components = filename.split("_")
        full_image_name = filename_components[0] + "_" + filename_components[1]
        # ________load raw image__________
        final_image_path = os.path.join(
            save_path, "{}{}".format(full_image_name, IMG_EXTENSION_JPG)
        )
        split = cv2.imread(save_path_)
        final_image_path = os.path.join(
            save_path, "{}{}".format(full_image_name, IMG_EXTENSION_JPG)
        )

        # if os.path.exists(final_image_path):

        if self.dic_of_Cimag[useing][full_image_name]:
            num1 = (self.target_size[0] // self.input_size) * split.shape[0]
            num2 = (self.target_size[1] // self.input_size) * split.shape[1]
            raw_image = np.zeros((num1, num2, 3))
            self.dic_of_Cimag[useing][full_image_name] = False
        else:
            raw_image = cv2.imread(final_image_path)
        if useing == "true":
            step1 = self.input_size
            step2 = self.input_size
            self.dic_of_slider_image_path[final_image_path] = final_image_path.replace(
                "true", "pred"
            )
        else:
            step1 = split.shape[0]
            step2 = split.shape[1]
        points = self.points_creator(
            uper_band_i=raw_image.shape[0], uper_band_j=raw_image.shape[1], step=step1
        )
        split_index = filename_components[2]
        split_index = int(split_index)
        j, i = points[split_index]
        raw_image[j : j + step1, i : i + step2, :] = split

        cv2.imwrite(final_image_path, raw_image)
        os.remove(save_path_)
    # else:
    #     print('Image not Exsit')
    def Binary2Yolo(self, path):
        # find points plot and target image size:
        temp_img = cv2.imread(self.data_path[0])
        temp_mask = cv2.cvtColor(temp_img, cv2.COLOR_BGR2GRAY)
        _, _, _, self.target_size = get_crops_normal(
            img=temp_img,
            mask=temp_mask,
            size=(self.input_size, self.input_size),
            annotation=None,
            number_output_flag=False,
        )
        # ______________________________________
        slider_dirctory = os.path.join(os.path.dirname(path), SLIDER_PATH)
        true_dirctory = os.path.join(slider_dirctory, TRUE_IMAGE_SLIDER)
        pred_dirctory = os.path.join(slider_dirctory, PRED_IMAGE_SLIDER)
        self.makedir(path=slider_dirctory, remove_flag=True)
        self.makedir(path=true_dirctory, remove_flag=True)
        self.makedir(path=pred_dirctory, remove_flag=True)
        # _____________________________________________________
        pred_pbar, true_pbar, yolo_device = self.create_yolo_dataloader(path=path)
        stats = []
        iouv = torch.linspace(0.5, 0.95, 10, device=yolo_device)
        niou = iouv.numel()
        names = (
            self.yolo_model.names
            if hasattr(self.yolo_model, "names")
            else self.yolo_model.module.names
        )
        # __________________________________________________
        for batch_i, (
            (im, targets, paths, shapes),
            (true_im, true_targets, true_paths, true_shapes),
        ) in enumerate(zip(pred_pbar, true_pbar)):
            # ____________one_______________________
            im = im.to(yolo_device, non_blocking=True)
            im = im.float()
            targets = targets.to(yolo_device)
            nb, _, height, width = im.shape
            preds, _ = self.yolo_model(im)
            targets[:, 2:] *= torch.tensor(
                (width, height, width, height), device=yolo_device
            )

            preds = non_max_suppression(
                preds,
                self.yolo_conf_thres,
                self.yolo_iou_thres,
                labels=[],
                multi_label=True,
                agnostic=False,
                max_det=self.yolo_max_det,
            )
            # ________________two________________
            true_im = true_im.to(yolo_device, non_blocking=True)
            true_im = true_im.float()
            true_targets = true_targets.to(yolo_device)
            _, _, true_height, true_width = true_im.shape
            true_targets[:, 2:] *= torch.tensor(
                (true_width, true_height, true_width, true_height), device=yolo_device
            )

            self.save_true_and_pred_output_image(
                img=true_im,
                label=true_targets,
                paths=true_paths,
                save_path=true_dirctory,
                names=names,
                batch_i=batch_i,
                useing="true",
            )
            self.save_true_and_pred_output_image(
                img=im,
                label=output_to_target(preds),
                paths=paths,
                save_path=pred_dirctory,
                names=names,
                batch_i=batch_i,
                useing="pred",
            )
            for si, pred in enumerate(preds):
                labels = targets[targets[:, 0] == si, 1:]
                nl, npr = (
                    labels.shape[0],
                    pred.shape[0],
                )  # number of labels, predictions
                path, shape = Path(paths[si]), shapes[si][0]
                correct = torch.zeros(
                    npr, niou, dtype=torch.bool, device=yolo_device
                )  # init

                if npr == 0:
                    if nl:
                        stats.append(
                            (
                                correct,
                                *torch.zeros((2, 0), device=yolo_device),
                                labels[:, 0],
                            )
                        )
                    continue

                # Predictions
                predn = pred.clone()
                scale_boxes(
                    im[si].shape[1:], predn[:, :4], shape, shapes[si][1]
                )  # native-space pred

                # Evaluate
                if nl:
                    tbox = xywh2xyxy(labels[:, 1:5])  # target boxes
                    scale_boxes(
                        im[si].shape[1:], tbox, shape, shapes[si][1]
                    )  # native-space labels
                    labelsn = torch.cat(
                        (labels[:, 0:1], tbox), 1
                    )  # native-space labels
                    correct = self.process_batch(predn, labelsn, iouv)
                stats.append(
                    (correct, pred[:, 4], pred[:, 5], labels[:, 0])
                )  # (correct, conf, pcls, tcls)
                percentage = (self.yolo_evaluation_part * (batch_i + 1)) / len(
                    pred_pbar
                )
                self.pgb_bar_signal.emit(
                    percentage
                    + self.binary_evaluation_part
                    + self.yolo_evaluation_data_preparation
                )
        # Compute metrics
        stats = [torch.cat(x, 0).cpu().numpy() for x in zip(*stats)]  # to numpy
        if len(stats) :#and stats[0].any():
            tp, fp, p, r, f1, ap, ap_class = ap_per_class(
                *stats, plot=False, save_dir="", names=names
            )
            ap50, ap = ap[:, 0], ap.mean(1)  # AP@0.5, AP@0.5:0.95
            mp, mr, map50, map = p.mean(), r.mean(), ap50.mean(), ap.mean()
        maps = np.zeros(self.data_nc) + map

        return mp, mr, map50, map, maps

    def process_batch(self, detections, labels, iouv):
        correct = np.zeros((detections.shape[0], iouv.shape[0])).astype(bool)
        iou = box_iou(labels[:, 1:], detections[:, :4])
        correct_class = labels[:, 0:1] == detections[:, 5]
        for i in range(len(iouv)):
            x = torch.where(
                (iou >= iouv[i]) & correct_class
            )  # IoU > threshold and classes match
            if x[0].shape[0]:
                matches = (
                    torch.cat((torch.stack(x, 1), iou[x[0], x[1]][:, None]), 1)
                    .cpu()
                    .numpy()
                )  # [label, detect, iou]
                if x[0].shape[0] > 1:
                    matches = matches[matches[:, 2].argsort()[::-1]]
                    matches = matches[np.unique(matches[:, 1], return_index=True)[1]]
                    # matches = matches[matches[:, 2].argsort()[::-1]]
                    matches = matches[np.unique(matches[:, 0], return_index=True)[1]]
                correct[matches[:, 1].astype(int), i] = True
        return torch.tensor(correct, dtype=torch.bool, device=iouv.device)

    # ________________For posterity....._____________________

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

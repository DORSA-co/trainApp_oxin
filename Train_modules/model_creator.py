import torch
from pathlib import Path
from backend.binary_model_funcs import *
from yolov5.utils.torch_utils import select_device
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.downloads import attempt_download
from Train_modules.models import (
    xception_cnn,
    resnet_cnn,
    base_unet,
    resnet_unet,
    low_unet,
    unet,
)


TENSORFLOW_MODEL_CREATOR = {
    "Xbc": xception_cnn,
    "Rbc": resnet_cnn,
    "Blu": base_unet,
    "Rleu": resnet_unet,
    "Ulnim": low_unet,
    "Ulnpr": unet,
    "Xcc": xception_cnn,
    "Rce": resnet_cnn,
}


class ModelCreator:
    def __init__(self, model_param, weights, model_type):
        self.model_param = model_param
        self.weights = weights
        self.model_type = model_type

    def yolo_creator(self):
        device = select_device(
            self.model_param["device"], batch_size=self.model_param["batch_size"]
        )
        model = DetectMultiBackend(
            weights=self.weights,
            device=device,
            dnn=False,
            fp16=False,
        )
        return model

    def tensorflow_model_creator(self):
        input_size = self.model_param["input_size"]
        num_class = self.model_param["num_class"]
        mode = self.model_param["mode"]
        function = TENSORFLOW_MODEL_CREATOR[
            translate_binary_algorithm_id_to_name(
                algo_id=self.model_param["algo_name"], model_type=self.model_type
            )
        ]
        model = function(
            input_size=input_size, num_class=num_class, mode=mode, weights=self.weights
        )

        return model


def get_model_type(weights_path, device):
    ckpt = torch.load(attempt_download(weights_path), map_location="cpu")  # load
    ckpt = (ckpt.get("ema") or ckpt["model"]).to(device).float()
    name = (
        Path(ckpt.yaml_file).stem.replace("yolov5", "YOLOv5")
        if hasattr(ckpt, "yaml_file")
        else "Model"
    )
    return name


def translate_model_database_info_to_modelOBJ(info_dict, weights_path, model_type):
    model_creator_OBJ = ModelCreator(
        model_param=info_dict, weights=weights_path, model_type=model_type
    )
    if model_type == "yolo":
        model = model_creator_OBJ.yolo_creator()
        return model

    model = model_creator_OBJ.tensorflow_model_creator()
    return model

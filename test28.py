import numpy as np
import torch

id2class = {1: '101', 2: '102', 3: '103', 4: '104'}
batch_size = 1
yolo_conf_thresh = 0.25

def create_random_yolo_output():
        pred = torch.tensor([[ 63.78859,  -2.85292, 178.54024, 256.59985,   0.33153,   1.00000],
                [ 17.03750,  -6.66229,  64.83273, 256.72855,   0.29511,   2.00000]])
        return pred
    
def yolo_batch_preds_post_processing(preds):
    if batch_size == 1:
        preds = [preds]
    preds = list(map(yolo_single_preds_post_processing, preds))
    print(preds)
    return preds

def yolo_single_preds_post_processing(preds):
    preds = preds[preds[:, 4] >= yolo_conf_thresh]
    preds[:, :-2] = torch.round(preds[:, :-2])
    preds[:, :-2] = torch.clamp(preds[:, :-2], min=0, max=256)
    bboxes = preds[:, :-2]
    classes = preds[:, -1].tolist()
    d = {0.0: '110', 1.0: '120', 2.0: '124'}
    classes = [d[key] for key in classes if key in d]
    areas = (bboxes[:, 2] - bboxes[:, 0]) * (bboxes[:, 3] - bboxes[:, 1])
    areas = areas.unsqueeze(1)
    bboxes = torch.cat((areas, bboxes), dim=1).tolist()
    return bboxes, classes


preds = create_random_yolo_output()
yolo_batch_preds_post_processing(preds)
from operator import itemgetter 
import cv2
import numpy as np
import os

IMAGE_SHAPE = (1200, 1920)

def get_selected_value(mylist , idxs):
    return np.array(mylist)[idxs].tolist()

def read_image(path, color='gray'):
    if not os.path.exists(path):
        return None
    if color == 'color':
        img = cv2.imread(path) 
    if color == 'gray':
        img = cv2.imread(path, 0)
    if img.shape != IMAGE_SHAPE:
        img = cv2.resize(img, (IMAGE_SHAPE[1], IMAGE_SHAPE[0]))
    return img

def add_layer_to_img(src_img, layer,opacity=0.7, compress=0.5):
    h,w = src_img.shape[:2]
    src_img = cv2.resize(src_img,None,fx=compress,fy=compress)
    layer = cv2.resize(layer,None,fx=compress,fy=compress)

    gray = cv2.cvtColor(layer, cv2.COLOR_BGR2GRAY)
    _,mask = cv2.threshold(gray,5,255, cv2.THRESH_BINARY)
    mask = (mask.astype(np.float32) / 255.)
    mask = np.expand_dims(mask, axis=-1)
    not_mask  = 1 - mask
    
    src_img = src_img.astype(np.float32)
    layer = layer.astype(np.float32)

    res = (src_img * not_mask ) +  (src_img + layer) * mask * opacity 
    res = np.clip(res, 0,255)
    return cv2.resize(res.astype(np.uint8),(w,h))





if __name__ == "__main__":
    l = [['a'], 'b', 2, 1, 5, 3,'g']
    idxs = [0]

    #print( get_selected_value(l,idxs))
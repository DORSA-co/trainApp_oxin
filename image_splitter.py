import os
import timeit
import numpy as np
import numba
import cv2


def ImageCrops(img, dim):
    img,rx,ry = ImageResize(img, dim)
    if len(img.shape) == 2:
        img = np.expand_dims(img, axis=-1)
    crops = np.array(ImageDivision(img, dim))
    return crops,rx,ry


def ImageResize(img, dim):
    xn,yn= round(img.shape[1] / dim[1]) * dim[1], round(img.shape[0] / dim[0]) * dim[0]
    ratio_x=xn/img.shape[1]
    ratio_y=yn/img.shape[0]
    res=cv2.resize(img,(xn, yn),)
    return res,ratio_x,ratio_y


# @numba.jit(cache=True)
def ImageDivision(img, dim):
    # Divide image into blocks with shape (dim, dim, d)

    # Find height and width and depth of image
    h, w, d = img.shape

    # Find number of blocks in x-axis and y-axis
    nx = int(np.ceil(h / dim[0]))
    ny = int(np.ceil(w / dim[1]))

    blocks = np.lib.stride_tricks.as_strided(img, (nx, ny, dim[0], dim[1], d),
                                             (img.strides[0] * dim[0], img.strides[1] * dim[1], img.strides[0],
                                              img.strides[1], img.strides[2]))
    return blocks

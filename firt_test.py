import os
import cv2
import time
import numpy as np
import math

def ImageEnhancement(img):
    # 1.
    imge = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, -1).astype('uint8')

    # 2.
    # gamma = 0.5
    # alpha = np.power(255, 1-gamma)
    # imge = (np.power(img, gamma)*alpha).astype('uint8')

    # 3.
    # imge = np.divide(np.multiply(img, 0.5), (np.add(cv2.GaussianBlur(img, (21, 21), 3.5, 3.5), math.pow(2, -25)))).astype('float32')
    # imge = cv2.normalize(imge, None, 0, 255, cv2.NORM_MINMAX, -1).astype('uint8')

    return imge

if __name__ == '__main__':
    # Define folder of images
    imgFolder = '/home/dorsa/Desktop/tset/'

    # List files in folder
    imgFiles = os.listdir(imgFolder)
    imgs = []

    for file in imgFiles:
        # Read images
        if file.split('.')[-1] == 'bmp' and not file.startswith('res'):
            img = cv2.imread(os.path.join(imgFolder, file))
            t = time.time()
            res = ImageEnhancement(img)
            print((time.time() - t)*1000)
            cv2.imshow('original', cv2.resize(img, (0, 0), fx=0.5, fy=0.5))
            cv2.imshow('result', cv2.resize(res, (0, 0), fx=0.5, fy=0.5))
            cv2.waitKey(0)
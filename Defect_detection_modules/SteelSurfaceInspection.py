import math
import timeit
import cv2
import os
import json
from skimage.filters import threshold_yen
import numpy as np
# calibrationCal\Preprocessing.py
try:
    from Defect_detection_modules.Preprocessing import ImageEnhancement
    from Defect_detection_modules.Variance import ImageBlockVariance, ThresholdCalculator
    from Defect_detection_modules.Noise import NoiseDetection
except:
    from Preprocessing import ImageEnhancement
    from Variance import ImageBlockVariance, ThresholdCalculator
    from Noise import NoiseDetection

DEFECT_BLOCKSIZE = {'Small': 21, 'Medium': 32, 'Large': 54}
NOISE_BLOCKSIZE = {'Small': 7, 'Medium': 8, 'Large': 9}

OVERLAP = 10


def SSI(img, block_size='Medium', defect_th=0, noise_th=7, noise=True, heatmap=False):
    """Return defective regions and heatmap of image.

    :param img: Input image (shape=(h, w, 3)).
    :type img: array (np.array, dtype = np.uint8)
    :param block_size: Block size of algorithm, defaults to 'Small'.
    :type block_size: str, optional
    :param defect_th: Threshold for defect detection in range [-1, 1], defaults to 0.
    :type defect_th: int, optional
    :param noise_th: Threshold for noise detection in range [0, 10], defaults to 7.
    :type noise_th: int, optional
    :param noise: If True, noise detection activate, defaults to True.
    :type noise: bool, optional
    :param heatmap: If True, the algorithm also returns heatmap of detected defects, defaults to False.
    :type heatmap: bool, optional
    :return: If heatmap=False, just returns original image with bounding box around defective regions. 
    If heatmap=True, returns original image with bounding box around defective regions and heatmap of detected defects.
    :rtype: array if heatmap=False, tuple if heatmap=true 
    """
    # start = timeit.default_timer()
    temp_img = img
    img = cv2.resize(img, (978, 528))

    # Crop 10px from left side
    img = img[:, 10:]

    # Convert image to grayscale format
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Divide image into 4 image with shape (132, 968, 3)
    imgs = [gray[0:132, :], gray[132:264, :], gray[264:396, :], gray[396:528, :]]
    t = list(map(FindDefectiveBlocks, imgs, [block_size]*4, [defect_th]*4, [noise_th]*4, [noise] * 4, [heatmap] * 4))

    df = np.concatenate([t[0]['mask'], t[1]['mask'], t[2]['mask'], t[3]['mask']])
    if heatmap:
        hm = np.concatenate([t[0]['heatmap'], t[1]['heatmap'], t[2]['heatmap'], t[3]['heatmap']])

    # Draw rectangle around defective regions
    res = temp_img.copy()
    df = cv2.resize(df, (temp_img.shape[1], temp_img.shape[0]))
    contours = cv2.findContours(df, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    df = np.zeros_like(df)
    bboxs = []
    for cntr in contours:
        x, y, w, h = cv2.boundingRect(cntr)
        x -= 5
        y -= 5
        h += 10
        w += 10
        cv2.rectangle(res, (x, y), (x + w, y + h), (205, 175, 33), 2)
        df[y:y+h, x:x+w] = 255
    #     bboxs.append([[x, y], [x+w, y+h]])

    # Improve heatmap based on defect mask
    # #print((timeit.default_timer() - start)*1000)
    if heatmap:
        hm = cv2.resize(hm, (temp_img.shape[1], temp_img.shape[0]))
        hm[:, :, 0] *= (df / 255).astype('uint8')
        hm[:, :, 1] *= (df / 255).astype('uint8')
        hm[:, :, 2] *= (df / 255).astype('uint8')
        return res, hm
    else:
        return res

def SSI_2(img, path, block_size='Medium', defect_th=0, noise_th=7, noise=True):
    """Return defective regions and heatmap of image.

    :param img: Input image (shape=(h, w)).
    :type img: array (np.array, dtype = np.uint8)
    :param block_size: Block size of algorithm, defaults to 'Small'.
    :type block_size: str, optional
    :param defect_th: Threshold for defect detection in range [-1, 1], defaults to 0.
    :type defect_th: int, optional
    :param noise_th: Threshold for noise detection in range [0, 10], defaults to 7.
    :type noise_th: int, optional
    :param noise: If True, noise detection activate, defaults to True.
    :type noise: bool, optional
    :return: Returns True and list of bounding box of defective regions if image was defective. otherwise returns False with empty list 
    If heatmap=True, returns original image with bounding box around defective regions and heatmap of detected defects.
    :rtype: array if heatmap=False, tuple if heatmap=true 
    """
    # start = timeit.default_timer()
    temp_img = img
    img = cv2.resize(img, (978, 528))

    # Crop 10px from left side
    img = img[:, 10:]

    # Divide image into 4 image with shape (132, 968, 3)
    imgs = [img[0:132, :], img[132:264, :], img[264:396, :], img[396:528, :]]
    t = list(map(FindDefectiveBlocks, imgs, [block_size]*4, [defect_th]*4, [noise_th]*4, [noise] * 4, [False] * 4))

    df = np.concatenate([t[0]['mask'], t[1]['mask'], t[2]['mask'], t[3]['mask']])

    # Draw rectangle around defective regions
    # res = temp_img.copy()
    df = cv2.resize(df, (temp_img.shape[1], temp_img.shape[0]))
    contours = cv2.findContours(df, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # df = np.zeros_like(df)
    bboxs = []
    for cntr in contours:
        x, y, w, h = cv2.boundingRect(cntr)
        x -= 5
        y -= 5
        h += 10
        w += 10
        bboxs.append([[x, y], [x+w, y+h]])

    if bboxs:
        with open(str(path), "w") as f:
            res_dict = {'status': 'True', 'bboxes':bboxs}
            json.dump(res_dict, f, indent=4, sort_keys=True)
    else:
        with open(str(path), "w") as f:
            res_dict = {'status': 'False', 'bboxes':bboxs}
            json.dump(res_dict, f, indent=4, sort_keys=True)

    # #print((timeit.default_timer() - start)*1000)
    # if bboxs:
    #     return True, bboxs
    # else:
    #     return False, bboxs

def FindDefectiveBlocks(gray, block_size='Medium', defect_th=0, noise_th=7, noise=True, heatmap=False):
    """Return defective mask and heatmap of image

    :param gray: Steel gray image (shape=(132, 968)).
    :type gray: array (np.array, dtype = np.uint8)
    :param block_size: Block size of algorithm, defaults to 'Small'.
    :type block_size: str, optional
    :param defect_th: Threshold for defect detection in range [-1, 1], defaults to 0.
    :type defect_th: int, optional
    :param noise_th: Threshold for noise detection in range [0, 10], defaults to 7.
    :type noise_th: int, optional
    :param noise: If True, noise detection activate, defaults to True.
    :type noise: bool, optional
    :param heatmap: If True, the algorithm also returns heatmap of detected defects, defaults to False.
    :type heatmap: bool, optional
    :return: If heatmap=False, just returns dictionary contains zero-one mask of defects. 
    If heatmap=True, returns dictionary contains zero-one mask of defects and heatmap of detected defects.
    :rtype: dict
    """
    # Enhance image for better defect detection
    imge = ImageEnhancement(gray)
    dim = DEFECT_BLOCKSIZE[block_size]
    ndim = NOISE_BLOCKSIZE[block_size]

    # Find defective blocks

    # Find variance of each block
    variance = ImageBlockVariance(imge, dim, OVERLAP)

    # Compute mean of blocks variance
    m_v = variance.mean()

    # Compute threshold v_th for image
    v_th = ThresholdCalculator(variance)

    # Find number of blocks in x-axis and y-axis
    h, w = imge.shape
    ny = int(w / (dim - OVERLAP))

    # Detect defective blocks based on variance and threshold
    # Decide about defect threshold and noise threshold based on average variance of blocks
    defectiveBlocks = 0
    th = -1
    # defect_th = defect_th/10
    if m_v >= 300:
        defectiveBlocks = np.where(variance > (4+defect_th) * v_th)[0]

    elif 300 > m_v >= 200:
        defectiveBlocks = np.where(variance > (3+defect_th) * v_th)[0]
        if noise:
            th = noise_th*5

    elif 200 > m_v >= 100:
        defectiveBlocks = np.where(variance > (2+defect_th) * v_th)[0]
        if noise:
            th = (noise_th+1)*5

    elif m_v < 100:
        defectiveBlocks = np.where(variance > (1.5+defect_th) * v_th)[0]
        if noise:
            th = (noise_th+1)*5 + 2

    # Find noisy blocks based on defined thresholds
    defectMask = np.zeros_like(imge, dtype='uint8')
    for c in defectiveBlocks:
        d = math.floor(c / ny) * (dim - OVERLAP)
        m = (c % ny) * (dim - OVERLAP)

        if th < 0:
            defectMask[d:d + dim, m:m + dim] = 255

        elif NoiseDetection(imge[d:d + dim, m:m + dim], dim, ndim) >= th:
            defectMask[d:d + dim, m:m + dim] = 255
    # Create heatmap of gray image
    if heatmap:
        heatmap = CreateHeatmap(gray, imge)

        # Return heatmap and mask of defects
        return {'mask': defectMask, 'heatmap': heatmap}
    else:
        return {'mask': defectMask}

def CreateHeatmap(gray, img):
    """Return heatmap of image.

    :param gray: Gray scale steel image (shape=(h, w)).
    :type gray: array (np.array, dtype = np.uint8)
    :param img: Steel image after enhancement (shape=(h, w)).
    :type img: array (np.array, dtype = np.float64)
    :return: heatmap of image (shape=(h, w, 3)).
    :rtype: array
    """
    # Image thresholding based on yen thresholding
    th = threshold_yen(img)
    imgt = cv2.threshold(img.astype('uint8'), th, 1, cv2.THRESH_BINARY, None)[1]

    # Normalize binary image multiply by gray image between [0, 255]
    t = cv2.normalize((imgt * gray).astype('uint8'), None, 0, 255, cv2.NORM_MINMAX, -1, None)

    # Create heatmap of image
    heatmap = cv2.applyColorMap(255 - t, cv2.COLORMAP_AUTUMN)

    # Multiply heatmap with binary image to remove background
    heatmap[:, :, 0] *= imgt.astype('uint8')
    heatmap[:, :, 1] *= imgt.astype('uint8')
    heatmap[:, :, 2] *= imgt.astype('uint8')

    return heatmap

# def CreateHeatmap(gray, mask):
#     imge = ImageEnhancement(gray)
#
#     th = threshold_yen(imge)
#     imgt = cv2.threshold(imge.astype('uint8'), th, 1, cv2.THRESH_BINARY, None)[1]
#
#     # Normalize binary image multiply by gray image between [0, 255]
#     t = cv2.normalize((imgt * gray).astype('uint8'), None, 0, 255, cv2.NORM_MINMAX, -1, None)
#
#     # Create heatmap of image
#     heatmap = cv2.applyColorMap(255 - t, cv2.COLORMAP_AUTUMN)
#
#     # Multiply heatmap with binary image to remove background
#     heatmap[:, :, 0] *= imgt.astype('uint8')
#     heatmap[:, :, 1] *= imgt.astype('uint8')
#     heatmap[:, :, 2] *= imgt.astype('uint8')
#
#     heatmap[:, :, 0] *= (mask / 255).astype('uint8')
#     heatmap[:, :, 1] *= (mask / 255).astype('uint8')
#     heatmap[:, :, 2] *= (mask / 255).astype('uint8')
#
#     return heatmap


if __name__ == '__main__':
    sheetID = '996'
    mainPath = '/home/reyhane/PycharmProjects/trainApp_oxin8/oxin_image_grabber'
    jsonMainPath = '/home/reyhane/PycharmProjects/trainApp_oxin8/oxin_image_grabber_imgProcessing'
    img_format = '.png'
    json_format = '.json'
    for s in ['BOTTOM', 'TOP']:
        for c in range(1, 13):
            if not os.path.exists(os.path.join(jsonMainPath, sheetID, s, str(c))):
                os.makedirs(os.path.join(jsonMainPath, sheetID, s, str(c)))
            for f in range(1, 200):
                img = cv2.imread(os.path.join(mainPath, sheetID, s, str(c), str(f)+img_format), 0)
                df = SSI_2(img, path=os.path.join(jsonMainPath, sheetID, s, str(c), str(f)+json_format) ,block_size='Medium', defect_th=0, noise_th=7, noise=True)
                # #print(df)
                # # cv2.imshow('', img)
                # cv2.waitKey(0)
import os
import random
import time
import timeit
import cv2
import numpy as np
# import numba as nb

MASK = True
SIZE = (300, 300)


def FindRegions(img):
    # make image grayscale
    if len(img.shape) != 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # if image is zero-one mask remove pixels with gray value between 0 and 255
    if MASK:
        img = ((img > 100) * 255).astype('uint8')

    # define a list for regions
    regions = []

    # find contours in image
    contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # shuffle contours
    contours = list(contours)
    random.shuffle(contours)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        block = {'x': round(x + w / 2), 'y': round(y + h / 2), 'h': h, 'w': w}
        f = 0
        for region in regions:
            f = 1
            for bl in region:
                diffx = abs(bl['x'] - block['x']) + bl['w'] / 2 + block['w'] / 2
                diffy = abs(bl['y'] - block['y']) + bl['h'] / 2 + block['h'] / 2
                if diffx > SIZE[1] or diffy > SIZE[0]:
                    f = 0
                    break
            if f == 1:
                region.append(block)
                break
        if f == 0:
            regions.append([block])
    return regions


def FindCrops(img, mask, regions):
    # img_res = img.copy()
    # mask_res = mask.copy()
    img_crops = []
    mask_crops = []
    points = []
    for region in regions:
        if len(region) == 1 and region[0]['h'] > SIZE[0] or region[0]['w'] > SIZE[1]:
            minx = min(round(bl['x'] - bl['w'] / 2) for bl in region)
            miny = min(round(bl['y'] - bl['h'] / 2) for bl in region)
            maxx = max(round(bl['x'] + bl['w'] / 2) for bl in region)
            maxy = max(round(bl['y'] + bl['h'] / 2) for bl in region)

            for i in range(minx, maxx, SIZE[1]):
                for j in range(miny, maxy, SIZE[0]):
                    if i < 0:
                        i = 0

                    if j < 0:
                        j = 0

                    if i + SIZE[1] > img.shape[1]:
                        i = img.shape[1] - SIZE[1]

                    if j + SIZE[0] > img.shape[0]:
                        j = img.shape[0] - SIZE[0]
                    points.append([j, i])

        else:
            minx = min(round(bl['x'] - bl['w'] / 2) for bl in region) + 20
            miny = min(round(bl['y'] - bl['h'] / 2) for bl in region) + 20
            maxx = max(round(bl['x'] + bl['w'] / 2) for bl in region) - 20
            maxy = max(round(bl['y'] + bl['h'] / 2) for bl in region) - 20

            r = random.randint(0, 10)

            if random.randint(0, 1):
                meanx = round((r * minx + (10 - r) * maxx) / 10) - round((10 - r) * SIZE[1] / 10)
                meany = round((r * miny + (10 - r) * maxy) / 10) - round((10 - r) * SIZE[0] / 10)
            else:
                meanx = round((r * minx + (10 - r) * maxx) / 10) - round((10 - r) * SIZE[1] / 10)
                meany = round((r * maxy + (10 - r) * miny) / 10) - round(r * SIZE[0] / 10)

            if meanx < 0:
                meanx = 0

            if meany < 0:
                meany = 0

            if meanx + SIZE[1] > img.shape[1]:
                meanx = img.shape[1] - SIZE[1]

            if meany + SIZE[0] > img.shape[0]:
                meany = img.shape[0] - SIZE[0]

            points.append([meany, meanx])

    points = sorted(points, key=lambda k: [k[0], k[1]])

    for j, i in points:
        if mask[j:j + SIZE[0], i:i + SIZE[1]].max() > 100:
            img_crops.append(img[j:j + SIZE[0], i:i + SIZE[1]])
            mask_crops.append(mask[j:j + SIZE[0], i:i + SIZE[1]])
            # cv2.rectangle(img_res, (i, j), (i + SIZE[1], j + SIZE[0]), (205, 175, 33), 2)
            # cv2.rectangle(mask_res, (i, j), (i + SIZE[1], j + SIZE[0]), (205, 175, 33), 2)
            # cv2.imshow('img', img_res)
            # cv2.imshow('mask', mask_res)
            # cv2.waitKey(0)

    img_crops = np.array(img_crops)
    mask_crops = np.array(mask_crops)

    return img_crops, mask_crops


def get_crops(img, mask, size):
    global SIZE
    SIZE = size
    reg = FindRegions(mask)
    img_crops, mask_crops = FindCrops(img, mask, reg)
    return img_crops, mask_crops


def get_crops_no_defect(img, n_split, size):
    # img_res = img.copy()
    global SIZE
    SIZE = size
    points = []
    img_crops = []
    n = 0
    while n < n_split:
        i = np.random.randint(0, img.shape[1] - SIZE[1])
        j = np.random.randint(0, img.shape[0] - SIZE[0])
        for y, x in points:
            if np.abs(x - i) < SIZE[1] / 2 and np.abs(y - j) < SIZE[0] / 2:
                break
        else:
            points.append([j, i])
            n += 1

    points = sorted(points, key=lambda k: [k[0], k[1]])
    for j, i in points:
        img_crops.append(img[j:j + SIZE[0], i:i + SIZE[1]])
        # cv2.rectangle(img_res, (i, j), (i + SIZE[1], j + SIZE[0]), (205, 175, 33), 2)
        # cv2.imshow('img', img_res)
        # cv2.waitKey(0)

    img_crops = np.array(img_crops)

    return img_crops


def get_crops_no_defect2(img, n_split, size):
    global SIZE
    SIZE = size
    mask = np.ones_like(img) * 255
    temp_img_crops, _ = get_crops(img, mask)
    img_crops = []
    crops = list(range(temp_img_crops.shape[0]))
    n_crops = []
    n = 0
    while n < n_split:
        i = np.random.randint(0, len(crops))
        n_crops.append(crops[i])
        crops.remove(crops[i])
        n += 1

    n_crops = sorted(n_crops)
    for i in n_crops:
        img_crops.append(temp_img_crops[i])
    # #print(n_crops)
    img_crops = np.array(img_crops)

    return img_crops


if __name__ == '__main__':
    imgFolder = 'default_dataset/binary/defect'
    maskFolder = 'default_dataset/binary/defect_mask'

    # List files in folder
    imgFiles = os.listdir(imgFolder)
    maskFiles = os.listdir(maskFolder)
    imgs = []
    masks = []

    for imgFile, maskFile in zip(imgFiles, maskFiles):
        # Read images
        img = cv2.imread(os.path.join(imgFolder, imgFile), 0)
        img = cv2.resize(img, (1920, 1200))
        mask = cv2.imread(os.path.join(maskFolder, maskFile), 0)
        # img = cv2.resize(img, dsize=None, fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST_EXACT)
        # mask = cv2.resize(mask, dsize=None, fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST_EXACT)
        imgs.append(img)
        masks.append(mask)

    for img, mask in zip(imgs, masks):
        t = time.time()
        img_crops, mask_crops = get_crops(img, mask)
        # img_crops = get_crops_no_defect(img, 10)
        # img_crops = get_crops_no_defect2(img, 10)
        #print((time.time() - t) * 1000)
        # for ic, mc in zip(img_crops, mask_crops):
        #     cv2.imshow('img', ic)
        #     cv2.imshow('mask', mc)
        #     cv2.waitKey(0)

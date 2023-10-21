import os
import random
import time
import timeit
import cv2
import numpy as np
import json
import itertools

# import numba as nb

SIZE = (224, 224)
TH = 50


def ImageResize(img, size):
    return cv2.resize(
        img,
        (
            int(np.floor(img.shape[1] / size[1]) * size[1]),
            int(np.floor(img.shape[0] / size[0]) * size[0]),
        ),
    )


def FindNormalCrops(img, mask, size, annotation, number_output_flag):
    img = ImageResize(img, size)
    mask = ImageResize(mask, size)

    img_res = img.copy()
    mask_res = mask.copy()
    img_crops = []
    mask_crops = []
    crops_annotations = []
    points = []
    jj = list(range(0, img.shape[0], size[0]))
    ii = list(range(0, img.shape[1], size[1]))
    points = list(itertools.product(jj, ii))
    points = sorted(points, key=lambda k: [k[0], k[1]])
    for j, i in points:
        # if np.count_nonzero(mask[j:j + size[0], i:i + size[1]]) > TH:
        img_crops.append(img[j : j + size[0], i : i + size[1]])
        mask_crops.append(mask[j : j + size[0], i : i + size[1]])
        if annotation:
            crops_annotations.append(
                create_crops_annotations(mask, (j, i), size, annotation)
            )
        # cv2.rectangle(img_res, (i, j), (i + size[1], j + size[0]), (205, 175, 33), 2)
        # cv2.rectangle(mask_res, (i, j), (i + size[1], j + size[0]), (205, 175, 33), 2)
        # cv2.imshow('img', img_res)
        # cv2.imshow('mask', mask_res)
        # print(crops_annotations[-1])
        # cv2.waitKey(0)

    img_crops = np.array(img_crops)
    mask_crops = np.array(mask_crops)
    if number_output_flag:
        return img_crops, mask_crops, crops_annotations
    else:
        return img_crops, mask_crops, crops_annotations, (img.shape)[0:2]


def FindRegions(img, size):
    # define a list for regions
    regions = []

    # find contours in image
    contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # shuffle contours
    contours = list(contours)
    random.shuffle(contours)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        block = {"x": round(x + w / 2), "y": round(y + h / 2), "h": h, "w": w}
        f = 0
        for region in regions:
            f = 1
            for bl in region:
                diffx = abs(bl["x"] - block["x"]) + bl["w"] / 2 + block["w"] / 2
                diffy = abs(bl["y"] - block["y"]) + bl["h"] / 2 + block["h"] / 2
                if diffx > size[1] or diffy > size[0]:
                    f = 0
                    break
            if f == 1:
                region.append(block)
                break
        if f == 0:
            regions.append([block])

    return regions


def FindCrops(img, mask, regions, size, annotation):
    img_res = img.copy()
    mask_res = mask.copy()
    img_crops = []
    mask_crops = []
    crops_annotations = []
    points = []
    for region in regions:
        if len(region) == 1 and region[0]["h"] > size[0] or region[0]["w"] > size[1]:
            minx = min(round(bl["x"] - bl["w"] / 2) for bl in region)
            miny = min(round(bl["y"] - bl["h"] / 2) for bl in region)
            maxx = max(round(bl["x"] + bl["w"] / 2) for bl in region)
            maxy = max(round(bl["y"] + bl["h"] / 2) for bl in region)

            for i in range(minx, maxx, size[1]):
                for j in range(miny, maxy, size[0]):
                    if i < 0:
                        i = 0

                    if j < 0:
                        j = 0

                    if i + size[1] > img.shape[1]:
                        i = img.shape[1] - size[1]

                    if j + size[0] > img.shape[0]:
                        j = img.shape[0] - size[0]
                    points.append([j, i])

        else:
            minx = min(round(bl["x"] - bl["w"] / 2) for bl in region) + 20
            miny = min(round(bl["y"] - bl["h"] / 2) for bl in region) + 20
            maxx = max(round(bl["x"] + bl["w"] / 2) for bl in region) - 20
            maxy = max(round(bl["y"] + bl["h"] / 2) for bl in region) - 20

            r = random.randint(0, 10)

            if random.randint(0, 1):
                meanx = round((r * minx + (10 - r) * maxx) / 10) - round(
                    (10 - r) * size[1] / 10
                )
                meany = round((r * miny + (10 - r) * maxy) / 10) - round(
                    (10 - r) * size[0] / 10
                )
            else:
                meanx = round((r * minx + (10 - r) * maxx) / 10) - round(
                    (10 - r) * size[1] / 10
                )
                meany = round((r * maxy + (10 - r) * miny) / 10) - round(
                    r * size[0] / 10
                )

            if meanx < 0:
                meanx = 0

            if meany < 0:
                meany = 0

            if meanx + size[1] > img.shape[1]:
                meanx = img.shape[1] - size[1]

            if meany + size[0] > img.shape[0]:
                meany = img.shape[0] - size[0]

            points.append([meany, meanx])

    points = sorted(points, key=lambda k: [k[0], k[1]])

    for j, i in points:
        if np.count_nonzero(mask[j : j + size[0], i : i + size[1]]) > TH:
            img_crops.append(img[j : j + size[0], i : i + size[1]])
            mask_crops.append(mask[j : j + size[0], i : i + size[1]])
            if annotation:
                crops_annotations.append(
                    create_crops_annotations(mask, (j, i), size, annotation)
                )
            # cv2.rectangle(img_res, (i, j), (i + size[1], j + size[0]), (205, 175, 33), 2)
            # cv2.rectangle(mask_res, (i, j), (i + size[1], j + size[0]), (205, 175, 33), 2)
            # cv2.imshow('img', img_res)
            # cv2.imshow('mask', mask_res)
            # print(crops_annotations[-1])
            # cv2.waitKey(0)

    img_crops = np.array(img_crops)
    mask_crops = np.array(mask_crops)
    return img_crops, mask_crops, crops_annotations


def create_crops_annotations(mask, point, size, annotation):
    split_annotation = {"obj_masks": []}
    j, i = point
    contours = cv2.findContours(
        mask[j : j + size[0], i : i + size[1]],
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )[0]
    contours = list(contours)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < TH:
            continue
        cls = test_point_in_contours(cnt, annotation, point, size)
        split_annotation["obj_masks"].append({"class": cls, "mask": cnt.tolist()})
    return split_annotation


def test_point_in_contours(contour, annotation, point, size):
    x, y = get_contour_center(contour, size)
    x += point[1]
    y += point[0]
    classes = list(
        map(
            lambda d: d["class"]
            if (
                cv2.pointPolygonTest(np.array(d["mask"]), (x, y), True)
                + d["line_thickness"]
            )
            > 0
            else -1,
            annotation["obj_masks"],
        )
    )
    cls = list(filter(lambda x: x != -1, classes))
    if len(cls) > 0:
        cls = cls[0]
    else:
        cls = -1
        # img = np.zeros((SIZE[0], SIZE[1], 3))
        # cv2.drawContours(img, [contour], -1, (255, 255, 255), -1)
        # img = cv2.circle(img, (x-point[1], y-point[0]), 2, (0, 0, 255), -1)
        # cv2.imshow('', img)
        # cv2.waitKey(0)
    return cls


def get_contour_center(contour, size):
    mask = np.zeros(size)
    cv2.drawContours(mask, [contour], -1, 1, -1)
    coordinates = np.where(mask)
    l = coordinates[0].shape[0]
    x = int(coordinates[1][l // 2])
    y = int(coordinates[0][l // 2])
    while cv2.pointPolygonTest(contour, (x, y), False) < 0:
        i = np.random.randint(0, l)
        x = int(coordinates[1][i])
        y = int(coordinates[0][i])
    return (x, y)


def get_contour_center2(contour, size):
    m = cv2.moments(contour)
    x = int(m["m10"] / m["m00"])
    y = int(m["m01"] / m["m00"])
    return (x, y)


def get_crops_random(img, mask, size, annotation=None):
    # make image grayscale
    if len(mask.shape) != 2:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # if image is zero-one mask remove pixels with gray value between 0 and 255
    mask = ((mask > 100) * 255).astype("uint8")

    reg = FindRegions(mask, size)
    img_crops, mask_crops, crops_annotations = FindCrops(
        img, mask, reg, size, annotation
    )
    return img_crops, mask_crops, crops_annotations


def get_crops_normal(img, mask, size, annotation=None, number_output_flag=True):
    # make image grayscale
    if len(mask.shape) != 2:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # if image is zero-one mask remove pixels with gray value between 0 and 255
    mask = ((mask > 100) * 255).astype("uint8")

    if number_output_flag:
        img_crops, mask_crops, crops_annotations = FindNormalCrops(
            img, mask, size, annotation, number_output_flag
        )
        return (
            img_crops,
            mask_crops,
            crops_annotations,
        )
    else:
        (
            img_crops,
            mask_crops,
            crops_annotations,
            target_shape,
        ) = FindNormalCrops(img, mask, size, annotation, number_output_flag)
        return img_crops, mask_crops, crops_annotations, target_shape


def get_crops_no_defect(img, n_split, size):
    # img_res = img.copy()
    points = []
    img_crops = []
    n = 0
    while n < n_split:
        i = np.random.randint(0, img.shape[1] - size[1])
        j = np.random.randint(0, img.shape[0] - size[0])
        for y, x in points:
            if np.abs(x - i) < size[1] / 2 and np.abs(y - j) < size[0] / 2:
                break
        else:
            points.append([j, i])
            n += 1

    points = sorted(points, key=lambda k: [k[0], k[1]])
    for j, i in points:
        img_crops.append(img[j : j + size[0], i : i + size[1]])
        # cv2.rectangle(img_res, (i, j), (i + size[1], j + size[0]), (205, 175, 33), 2)
        # cv2.imshow('img', img_res)
        # cv2.waitKey(0)

    img_crops = np.array(img_crops)

    return img_crops


def get_crops_no_defect2(img, n_split, size):
    mask = np.ones_like(img) * 255
    temp_img_crops, _ = get_crops_random(img, mask, size)
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
    img_crops = np.array(img_crops)

    return img_crops

def ImageResize(img, dim):
    fx, fy = get_resize_ratio(img.shape, dim)
    return cv2.resize(img, dsize=(0, 0), fx=fx, fy=fy)

def get_resize_ratio(shape, dim):
    fx = int(np.floor(shape[1] / dim[1]) * dim[1]) / shape[1]
    fy = int(np.floor(shape[0] / dim[0]) * dim[0]) / shape[0]
    return fx, fy

def get_crops_no_defect3(img, size):
    img = ImageResize(img, size)

    height, width = img.shape
    window_height, window_width = size

    num_windows_height = height // window_height
    num_windows_width = width // window_width

    windows = img.reshape(
        num_windows_height, window_height, num_windows_width, window_width
    ).transpose(0, 2, 1, 3)

    windows = windows.reshape(-1, window_height, window_width)

    return windows


def main():
    imgFolder = "/home/reyhane/PythonProjects/trainApp_oxin_new/default_dataset/localization/image"
    maskFolder = "/home/reyhane/PythonProjects/trainApp_oxin_new/default_dataset/localization/label"
    annotFolder = (
        "/home/reyhane/PythonProjects/trainApp_oxin_new/default_dataset/annotations"
    )

    # List files in folder
    imgFiles = os.listdir(imgFolder)
    maskFiles = os.listdir(maskFolder)

    for imgFile, maskFile in zip(imgFiles, maskFiles):
        # Read images
        img = cv2.imread(os.path.join(imgFolder, imgFile))
        # img = cv2.resize(img, (1792, 1200))
        mask = cv2.imread(os.path.join(maskFolder, maskFile))
        # Read annotation
        with open(os.path.join(annotFolder, imgFile.split(".")[0]) + ".json") as f:
            annotation = json.load(f)

        t = time.time()
        # img_crops, mask_crops, crops_annotations = get_crops_random(img, mask, SIZE, annotation)
        img_crops, mask_crops, crops_annotations = get_crops_normal(
            img, mask, SIZE, annotation
        )
        print(len(img_crops))
        # print((time.time() - t)*1000)
        # img_crops = get_crops_no_defect(img, 10)
        # img_crops = get_crops_no_defect2(img, 10)

        # for ic, mc in zip(img_crops, mask_crops):
        #     cv2.imshow('img', ic)
        #     cv2.imshow('mask', mc)
        #     cv2.waitKey(0)


if __name__ == "__main__":
    main()

import os

import cv2

import numpy as np

# list_side=[delattr]
ncam = 13
nframe = 50
for cnt in range(1001, 1030):
    path = "oxin_image_grabber/{}".format(cnt)
    if not os.path.exists(path):
        os.makedirs(path)
    for side in ["TOP", "BOTTOM"]:
        if not os.path.exists(os.path.join(path, side)):
            os.makedirs(os.path.join(path, side))
        for n in range(1, ncam):
            if not os.path.exists(os.path.join(path, side, str(n))):
                os.makedirs(os.path.join(path, side, str(n)))
            for f in range(1, nframe):
                img = np.zeros((1200, 1920), dtype=np.uint8)
                img[:, :] = np.random.randint(0, 150)
                res_path = os.path.join(path, side, str(n))
                h, w = img.shape
                img = cv2.putText(
                    img,
                    "{}_{}_{}_{}".format(cnt, side, n, f),
                    (w // 4, h // 2),
                    2,
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    255,
                )
                # print(res_path)
                cv2.imwrite(os.path.join(res_path, str(f) + ".png"), img)

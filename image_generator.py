import os

import cv2

import numpy as np

# list_side=[delattr]
ncam = 13
nframe=50
for cnt in range(18):
    path = 'G:\oxin_image_grabber/{}'.format(cnt)
    for side in ['UP', 'DOWN']:
        for n in range(ncam):
            for f in range(nframe):
                img = np.zeros((1200,1920), dtype=np.uint8)
                img[:,:] = np.random.randint(0,150)
                res_path = os.path.join( path, side, str(n))
                h,w = img.shape
                img = cv2.putText( img,
                            '{}_{}_{}_{}'.format(cnt,side,n,f),
                            (w//4,h//2),
                            2,
                            cv2.FONT_HERSHEY_COMPLEX_SMALL,255)
                # print(res_path)
                cv2.imwrite(os.path.join(res_path, str(f)+'.jpg'), img)
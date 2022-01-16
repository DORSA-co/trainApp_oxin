import os

import cv2

import numpy as np

list_side=[delattr]
ncam = 10
nframe=20
path = 'G:\oxin_image_grabber/001'
for side in ['UP', 'DOWN']:
    for n in range(ncam):
        for f in range(nframe):
            img = np.zeros((1920,1200), dtype=np.uint8)
            img[:,:] = np.random.randint(0,150)
            res_path = os.path.join( path, side, str(n))
            h,w = img.shape
            img = cv2.putText( img,
                        '{}_{}_{}'.format(side,n,f),
                        (w//2,h//2),
                        1,
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,255)

            cv2.imwrite(os.path.join(res_path, str(f)+'.jpg'), img)
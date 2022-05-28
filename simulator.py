import os
import cv2
import numpy as np
import time
import threading

PATH = 'MyDS\c.jpg'
coil_number = 889
side = 'TOP'
n = 1
f = 1


def camera_simulator():
    global coil_number
    global f

    grab = open('grab.txt', 'w',encoding='Utf-8')
    grab.write('True')
    grab.close()

    img = np.zeros((1200, 1920), dtype=np.uint8)
    img[:, :] = np.random.randint(0, 150)
    h, w = img.shape
    img = cv2.putText(img,
                      '{}_{}_{}_{}'.format(coil_number, side, n, f),
                      (w // 4, h // 2),
                      2,
                      cv2.FONT_HERSHEY_COMPLEX_SMALL, 255)
    f += 1
    time.sleep(0.1)

    grab = open('grab.txt', 'w', encoding='Utf-8')
    grab.write('False')
    grab.close()

    cv2.imwrite(PATH, img)

    threading.Timer(1, camera_simulator).start()


def plc_simulator():
    global coil_number
    global f
    coil_number += 1
    f = 1
    plc = open('plc.txt', 'w', encoding='Utf-8')
    plc.write(str(coil_number))
    plc.close()

    threading.Timer(12, plc_simulator).start()

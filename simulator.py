import json
import os
import cv2
import numpy as np
import time
import threading

PATH = '/home/reyhane/camera'
coil_number = 889
f = 1
coil_dict = {'sheet_id': 996, 'heat_id': '0', 'ps_number': '1111', 'pdl_number': '2222.0', 'length': 1000.0,
             'width': 480.0, 'thickness': None}


def cameras_simulator(cameras_numbers):
    global f
    for i in cameras_numbers:
        camera_simulator(int(i))
    f += 1
    threading.Timer(0.09, cameras_simulator, args=(cameras_numbers,)).start()


def camera_simulator(i):
    global coil_number
    global f
    if i <= 12:
        c = i
        side = 'TOP'
    else:
        c = i - 12
        side = 'BOTTOM'

    with open('grab' + str(i) + '.txt', 'w', encoding='Utf-8') as grab:
        grab.write('True')

    img = np.zeros((1200, 1920), dtype=np.uint8)
    img[:, :] = np.random.randint(0, 150)
    h, w = img.shape
    img = cv2.putText(img,
                      '{}_{}_{}_{}'.format(coil_number, side, c, f),
                      (w // 4, h // 2),
                      2,
                      cv2.FONT_HERSHEY_COMPLEX_SMALL, 255)
    time.sleep(0.01)

    with open('grab' + str(i) + '.txt', 'w', encoding='Utf-8') as grab:
        grab.write('False')

    file_name = str(i) + '.png'
    cv2.imwrite(os.path.join(PATH, file_name), img)


def plc_simulator():
    global coil_number
    global f
    coil_number += 1
    f = 1
    coil_dict['sheet_id'] = coil_number
    with open('plc.txt', 'w', encoding='Utf-8') as plc:
        plc.write(str(coil_dict))

    threading.Timer(12, plc_simulator).start()


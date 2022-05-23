import cv2
from backend import camera_connection


def save_camera_images(cameras):
    cnt = 0
    while 1:
        print(cnt, ': new process')
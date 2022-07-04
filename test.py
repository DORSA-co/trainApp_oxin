# from multiprocessing import Process, Array
# import scipy
# import numpy as np
# import cv2
# import os
# import time
#
#
# def f(a):
#     path = '/home/reyhane/Desktop/Images/'
#     file = os.listdir(path)
#     for f in file:
#         img = cv2.imread(os.path.join(path, f), 0)
#         img = cv2.resize(img, (1920, 1200))
#         # cv2.imshow('t', img)
#         # cv2.waitKey(0)
#         a[:] = img.flatten()
#         # cv2.imshow('a', np.reshape(np.array(a[:], dtype=np.uint8), (1200, 1920)))
#         # cv2.waitKey()
#
#
# if __name__ == '__main__':
#     # Create the array
#     N = int(10)
#     arr = Array('d', np.zeros((1920, 1200)).flatten())
#
#     p = Process(target=f, args=(arr,))
#     p.start()
#     # p.join()
#
#     # Printing out the changed values
#     while 1:
#         img = np.reshape(np.array(arr[:], dtype=np.uint8), (1200, 1920))
#         # cv2.imwrite('/home/reyhane/Desktop/test1/test.png', img)
#         cv2.imshow('', img)
#         cv2.waitKey()
#

def squareNum(a):
    print('test', a)


listt = [0, -1, 3, 4.5, 99, .08]
x = map(squareNum, listt)
print(list(x))


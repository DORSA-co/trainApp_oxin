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

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

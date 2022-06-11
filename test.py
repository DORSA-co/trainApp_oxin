from multiprocessing import Process, Array
import scipy
import numpy as np
import cv2
import os


def f(a):
    path = '/home/reyhane/Desktop/Images/'
    file = os.listdir(path)
    for f in file:
        b = cv2.imread(os.path.join(path, f), 0)
        c = cv2.resize(b, (1200, 1920))
        a[:] = c.flatten()


if __name__ == '__main__':
    # Create the array
    N = int(10)
    unshared_arr = np.zeros((1920, 1200))
    arr = Array('d', unshared_arr.flatten())
    print("Originally, the first two elements of arr = %s" % (arr[:1]))

    # Create, start, and finish the child processes
    p = Process(target=f, args=(arr,))
    p.start()
    # p.join()

    # Printing out the changed values
    while 1:
        print("Now, the first two elements of arr = %s" % arr[:1])
        img = np.array(arr[:])
        cv2.imshow('', img)
        cv2.waitKey()

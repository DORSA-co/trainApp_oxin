# from threading import Thread
# import time

# class thread_test:
#     def __init__(self):
#         self.threads = []
#         self.n_threads = 1

#     def thread_func(self):
#         for i in range(10):
#             a = 5
#             b = 4
#             print(a+b)
#         return True

#     def create_threads(self):
#         self.threads = []
#         for n in range(self.n_threads):
#             self.threads.append(Thread(target=self.thread_func)) 

#     def start_threads(self):
#         for t in self.threads:
#             t.start()

#     def stop_threads(self):
#         for t in self.threads:
#             t.join()

#     def start(self):
#         self.create_threads()
#         self.start_threads()

#     def stop(self):
#         self.stop_threads()

# if __name__=='__main__':
#     cls = thread_test()
#     # t = time.time()
#     # for i in range(10):
#     #     cls.start()
#     #     cls.stop()
#     # print((time.time() - t)*1000)

#     t = time.time()
#     cls.start()
#     cls.stop()
#     print((time.time() - t)*1000)


# import cv2
# img = cv2.imread('oxin_image_grabber/2023/05/27/900o7/TOP/6/12.png')
# img = cv2.flip(img, 1)
# cv2.imshow('a',img)
# cv2.waitKey(0)

import os
def find_mount_point(path):
    path = os.path.abspath(path)
    orig_dev = os.stat(path).st_dev

    while path != '/':
        dir = os.path.dirname(path)
        if os.stat(dir).st_dev != orig_dev:
            # we crossed the device border
            break
        path = dir
    return path


def find_mount_point2(path):
    path = os.path.abspath(path)
    while not os.path.ismount(path):
        path = os.path.dirname(path)
    return path

path = '/media/reyhane/782F28BD242E495A/oxin_image_grabber'
print(find_mount_point2(path))

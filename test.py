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
# img = cv2.imread('oxin_image_grabber/2023/05/19/989m7/TOP/6/12.png')
# img = cv2.flip(img, 1)
# cv2.imshow('a',img)
# cv2.waitKey(0) 


ret_dict = {24: (True, 'start grabbing ok'), 12: (True, 'start grabbing ok'), 4: (False, 'start grabbing ok'), 2: (True, 'start grabbing ok'), 15: (True, 'start grabbing ok'), 13: (True, 'start grabbing ok'), 20: (True, 'start grabbing ok'), 16: (True, 'start grabbing ok'), 3: (True, 'start grabbing ok'), 17: (True, 'start grabbing ok'), 6: (True, 'start grabbing ok'), 7: (True, 'start grabbing ok'), 22: (True, 'start grabbing ok'), 1: (True, 'start grabbing ok'), 23: (True, 'start grabbing ok'), 9: (True, 'start grabbing ok'), 19: (True, 'start grabbing ok'), 21: (True, 'start grabbing ok'), 5: (True, 'start grabbing ok'), 8: (True, 'start grabbing ok'), 18: (True, 'start grabbing ok'), 10: (True, 'start grabbing ok'), 14: (True, 'start grabbing ok'), 11: (True, 'start grabbing ok')}


myKeys = list(ret_dict.keys())
myKeys.sort()
sorted_dict = {i: ret_dict[i] for i in myKeys}

print(sorted_dict)


for cam_id, value in zip(sorted_dict.keys(),sorted_dict.values()):
    print(value)
    if value[0]:
        print(cam_id)


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

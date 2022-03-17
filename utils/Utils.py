from operator import itemgetter 
import cv2
import numpy as np

def get_selected_value(mylist , idxs):
    return np.array(mylist)[idxs].tolist()

def read_image(path, color='gray'):
    if color == 'color':
        return cv2.imread(path)
    if color == 'color':
        return cv2.imread(path, 0)





if __name__ == "__main__":
    l = [['a'], 'b', 2, 1, 5, 3,'g']
    idxs = [0]

    print( get_selected_value(l,idxs))
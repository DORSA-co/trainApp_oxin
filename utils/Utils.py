from operator import itemgetter 
import numpy as np

def get_selected_value(mylist , idxs):
    return np.array(mylist)[idxs].tolist()








if __name__ == "__main__":
    l = [['a'], 'b', 2, 1, 5, 3,'g']
    idxs = [0]

    print( get_selected_value(l,idxs))
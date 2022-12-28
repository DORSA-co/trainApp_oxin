import numpy as np
import numba


# @numba.jit()
def ImageDivision(img, dim, ol):
    """Divide image into square blocks and return them.

    :param img: Gray image (shape=(h, w)).
    :type img: array (np.array, dtype = np.float64)
    :param dim: Dimension of blocks.
    :type dim: int
    :param ol: Overlap between blocks.
    :type ol: int
    :return: Array of blocks (shape(int(h / (dim - ol)), int(w / (dim - ol)), dim, dim)).
    :rtype: array 
    """
    # Divide image into blocks with shape (dim, dim) and ol pixel overlap
    # Find height and width of image
    h, w = img.shape

    # Find number of blocks in x-axis and y-axis
    nx = int(h / (dim - ol))
    ny = int(w / (dim - ol))

    # Find each block and return as 4d array with shape (nx, ny, dim, dim)
    blocks = np.lib.stride_tricks.as_strided(img, (nx, ny, dim, dim),
                                             (img.strides[0] * (dim - ol), img.strides[1] * (dim - ol), img.strides[0],
                                              img.strides[1]))
    return blocks

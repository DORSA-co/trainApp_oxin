import numpy as np
from Defect_detection_modules.Division import ImageDivision


def NoiseDetection(img, dim, ndim):
    """Return a number for noise detection.

    :param img: A Block of image.
    :type img: array
    :param dim: Dimension of img.
    :type dim: int
    :param ndim: Dimension of noise blocks.
    :type ndim: int
    :return: Number used for noise detection.
    :rtype: int
    """
    
    if img.shape[0] != dim:
        img = np.pad(img, [(0, dim - img.shape[0]), (0, 0)], mode='constant')
    if img.shape[1] != dim:
        img = np.pad(img, [(0, 0), (0, dim - img.shape[1])], mode='constant')

    # blocks = np.swapaxes(img.reshape(4, 8, 4, -1), 1, 2)

    # Divide img into (ndim, ndim) sub-blocks
    blocks = ImageDivision(img, ndim, 0)

    # Find maximum of each sub-block and save in 1-d array x
    x = ((blocks.max(axis=3)).max(axis=2)).flatten()

    # For each coordinate i in x compute:
    # abs(x[i] - x[i - 1]) + abs(x[i] - x[i + 1])
    # and save in 1-d array y
    y = np.zeros(x.shape[0], dtype=np.float64)
    y[0] = abs(x[1] - x[0])
    y[x.shape[0] - 1] = abs(x[x.shape[0] - 1] - x[x.shape[0] - 2])
    for i in range(1, x.shape[0] - 1): y[i] = abs(x[i] - x[i - 1]) + abs(x[i] - x[i + 1])

    # Find standard deviation of y
    num = round(y.std())
    return num

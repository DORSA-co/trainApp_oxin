import numpy as np
from Defect_detection_modules.Division import ImageDivision


def ImageBlockVariance(img, dim, ol):
    """Return variance of image blocks.

    :param img: Gray image (shape=(h, w)).
    :type img: array (np.array, dtype = np.float64)
    :param dim: Dimension of blocks.
    :type dim: int
    :param ol: Overlap between blocks.
    :type ol: int
    :return: Variance of image blocks (shape(int(h / (dim - ol)) * int(w / (dim - ol)), )).
    :rtype: array
    """
    # Add ol columns of zero in right side and ol rows of zero in bottom of image for better division
    img = np.pad(img, [(0, ol), (0, ol)], mode='constant')

    # Divide image into blocks with shape (dim, dim) and ol pixel overlap
    blocks = ImageDivision(img, dim, ol)

    # Calculate variance for each block
    variance = VarianceCalculator(blocks, dim)
    return variance.flatten()


def VarianceCalculator(blocks, dim):
    """Return variance of blocks.

    :param blocks: 4-d array of blocks (shape=(nx, ny, dim, dim)).
    :type blocks: array (np.array, dtype = np.float64)
    :param dim: Dimension of blocks.
    :type dim: int
    :return: Variance of each block (shape(nx * ny, )).
    :rtype: array
    """
    # Compute Variance of img
    return ((((blocks ** 2).sum(axis=3)).sum(axis=2)) / (dim**2)) - ((((blocks.sum(axis=3)).sum(axis=2)) / (dim**2)) ** 2)

def ThresholdCalculator(variance):
    """Return threshold based on variance for detect defective blocks.

    :param variance: Variance of blocks (shape(nx * ny, )).
    :type variance: array (np.array, dtype = np.float64)
    :return: Number used for defect detection.
    :rtype: int
    """
    # Compute threshold based on blocks variance
    sen_v = 0.0125
    max_v = variance.max(initial=0)
    m_v = variance.mean()
    v_th = m_v + (max_v - m_v) * sen_v
    return v_th


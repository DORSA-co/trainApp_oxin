import timeit

import cv2
import math
import numpy as np

def ImageEnhancement(img):
    """Return an enhanced version of steel image.

    :param img: Gray image (shape=(h, w)).
    :type img: array (np.array, dtype = np.uint8)
    :return: Enhanced image (shape(w, h)).
    :rtype: array
    """
    # Enhance image for better defect detection
    # Apply GaussianBlur with (5, 5) kernel size
    imge = cv2.GaussianBlur(img, (5, 5), 1.1, 1.1)

    # Smooth image
    imge = ImageSmoothness(imge)

    # Remove small noise
    imge = SmallNoiseRemoval(imge)

    # Detect edges
    imge = EdgeDetection(imge)

    # Normalize image in range [0, 255]
    imge = cv2.normalize(imge, None, 0, 255, cv2.NORM_MINMAX, -1)

    return imge

def ImageSmoothness(img):
    """Return a smoothed version of steel image.

    :param img: Gray image (shape=(h, w)).
    :type img: array (np.array, dtype = np.uint8)
    :return: Smoothed image (shape(w, h)).
    :rtype: array
    """
    # Apply smoothness with following equation:l
    # SmoothedImage = (OriginalImage * 0.5) / (OriginalImage after applying GaussianBlur with (21, 21) kernel size)
    imge = np.divide(np.multiply(img, 0.5), (np.add(cv2.GaussianBlur(img, (21, 21), 3.5, 3.5), math.pow(2, -25))))
    return imge.astype('float32')

def SmallNoiseRemoval(img):
    """Remove small noise from image.

    :param img: Gray image (shape=(h, w)).
    :type img: array (np.array, dtype = np.float64)
    :return: Image with small noise removal (shape(w, h)).
    :rtype: array
    """
    # Apply morphology to remove small noise

    # Define ellipse structuring element with size (3, 3)
    element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)

    # Apply first erosion on img
    imge = cv2.erode(img, element, iterations=1)

    # Apply dilation on img
    imge = cv2.dilate(imge, element, iterations=1)

    # Apply second erosion on img
    imge = cv2.erode(imge, element)
    return imge


def EdgeDetection(img):
    """Detect edges in image.

    :param img: gray image (shape=(h, w)).
    :type img: array (np.array, dtype = np.float64)
    :return: Image with edges detected (shape(w, h)).
    :rtype: array
    """
    # Detect edges with sobel edge detection

    # Find edges in x-axis
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)

    # Find edges in y-axis
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

    # Calculates the magnitude 2D vectors
    imge = np.sqrt(gx**2 + gy**2)

    return imge

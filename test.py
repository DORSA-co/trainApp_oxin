# import numpy as np
# import cv2
# import torch
# import time

# img = np.random.rand(1, 256, 256)

# preds = torch.tensor([[ 63.78859,  -2.85292, 178.54024, 256.59985,   0.33153,   1.00000],
#                 [ 17.03750,  -6.66229,  64.83273, 256.72855,   0.29511,   2.00000]])

# t = time.time()
# # Round the tensor
# preds = preds[preds[:, 4] >= 0.25]
# preds[:, :-2] = torch.round(preds[:, :-2])

# # Clamp the tensor to 0 for negative values
# preds = np.array(torch.clamp(preds, min=0, max=256))
# print((time.time() - t)*1000)

# print(preds)
# img = img[0].astype('uint8')
# for pred in preds:
#     x1, y1, x2, y2, conf, clss = pred
#     cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color=255, thickness=1)

#     # cv2.imshow('', img)
#     # cv2.waitKey(0)


import numpy as np

# Create a NumPy array
arr = np.zeros((1000, 1000))

# Get the size of the array in GB
size_gb = arr.nbytes / (1024**3)

# Print the size of the array in GB
print(f"Size of array: {size_gb:.2f} GB")

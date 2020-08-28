# from matplotlib import pyplot as plt
# plt.imshow(plt.imread('C:\\Users\\18587\\Desktop\\Paper 1 Data\\b22_p64-65.jpg'))
# plt.show()

import cv2
img = cv2.imread('C:\\Users\\18587\\Desktop\\Paper 1 Data\\seg_b22_p64-65.png')
crop_img = img[190:2750, 0:3895]
cv2.imwrite('C:\\Users\\18587\\Desktop\\Paper 1 Cropped\\seg_b22_p64-65_cropped.png', crop_img)
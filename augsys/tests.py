import codecs
import math
import json
import glob
import cv2
import os
import random
import matplotlib.pyplot as plt
import numpy as np
import time

f1 = [74.4,70.29]
f2 =[58.01,35.24]
f3=[47.49,28.04]

x=['SegNet','HRNet']
x_len =np.arange(len(x))
plt.savefig('/Users/zhangshijie/Desktop/Q1.png')

# img = '/Users/zhangshijie/Desktop/imageOriginal.png'
# img1 = cv2.imread(img)
# print(img1.shape[1],img1.shape[0])
# # 2.2 相对尺寸
# dst = cv2.GaussianBlur(img1, (5,5), 0, 0)
# cv2.imwrite('/Users/zhangshijie/Desktop/imageBlur.png', dst)
# img ='/Users/zhangshijie/Desktop/people_42.png'
# img1 = cv2.imread(img)
# for m in range(img1.shape[0]):
#     for n in range(img1.shape[1]):
#         if((img1[m][n] == [0,0,0]).all()):
#             img1[m][n] = [255,255,255]
# cv2.imwrite('/Users/zhangshijie/Desktop/people_42.png', img1)
#
# newImagename = '/Users/zhangshijie/Desktop/instlbl.png'
# img = cv2.imread(newImagename)
# # cv2.imwrite('/Users/zhangshijie/Desktop/111111.png', img)
#
# for m in range(img.shape[0]):
#     for n in range(img.shape[1]):
#             # print(img[m][n])
#         if ((img[m][n] == [7, 7, 7]).all()):
#             img[m][n] = [128, 64, 128]
#         elif ((img[m][n] == [8, 8, 8]).all()):
#             img[m][n] = [232, 35, 244]
#         elif ((img[m][n] == [11, 11, 11]).all()):
#             img[m][n] = [70, 70, 70]
#         elif ((img[m][n] == [12, 12, 12]).all()):
#             img[m][n] = [156, 102, 102]
#         elif ((img[m][n] == [13, 13, 13]).all()):
#             img[m][n] = [153, 153, 190]
#         elif ((img[m][n] == [17, 17, 17]).all()):
#             img[m][n] = [153, 153, 153]
#         elif ((img[m][n] == [19, 19, 19]).all()):
#             img[m][n] = [30, 170, 250]
#         elif ((img[m][n] == [20, 20, 20]).all()):
#             img[m][n] = [0, 220, 220]
#         elif ((img[m][n] == [21, 21, 21]).all()):
#             img[m][n] = [35, 142, 107]
#         elif ((img[m][n] == [22, 22, 22]).all()):
#             img[m][n] = [152, 251, 152]
#         elif ((img[m][n] == [23, 23, 23]).all()):
#             img[m][n] = [180, 130, 70]
#         elif ((img[m][n] == [24, 24, 24]).all()):
#             img[m][n] = [60, 20, 220]
#         elif ((img[m][n] == [25, 25, 25]).all()):
#             img[m][n] = [255, 0, 0]
#         elif ((img[m][n] == [26, 26, 26]).all()):
#             img[m][n] = [142, 0, 0]
#         elif ((img[m][n] == [27, 27, 27]).all()):
#             img[m][n] = [70, 0, 0]
#         elif ((img[m][n] == [28, 28, 28]).all()):
#             img[m][n] = [100, 60, 0]
#         elif ((img[m][n] == [31, 31, 31]).all()):
#             img[m][n] = [100, 80, 0]
#         elif ((img[m][n] == [32, 32, 32]).all()):
#             img[m][n] = [230, 0, 0]
#         elif ((img[m][n] == [33, 33, 33]).all()):
#             img[m][n] = [32, 11, 119]
# cv2.imwrite('/Users/zhangshijie/Desktop/instlblCor.png', img)

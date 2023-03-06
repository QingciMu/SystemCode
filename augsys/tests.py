import cv2
import os
import glob
import numpy as np
from augsys.generalMethod import *
def transSegNetResult(setPath,resultPath):
    test_predict = sorted(glob.glob(setPath + '/*'))
    pos = len(test_predict[0].split('/'))-1
    for i in range(len(test_predict)):
        img = cv2.imread(test_predict[i])
        fileName = getImgName(test_predict[i],pos)
        for m in range(img.shape[0]):
            for n in range(img.shape[1]):
                if ((img[m][n] == [29,29,29]).all() or (img[m][n] == [30,30,30]).all() or (
                        img[m][n] == [24,24,24]).all() or (img[m][n] == [25,25,25]).all() or (
                        img[m][n] == [26,26,26]).all() or (img[m][n] == [27,27,27]).all() or (
                        img[m][n] == [28,28,28]).all() or (img[m][n] == [31,31,31]).all() or (
                        img[m][n] == [32,32,32]).all() or (img[m][n] == [33,33,33]).all()):
                    img[m][n] = [255, 255, 255]
                else:
                    img[m][n] = [0,0,0]
        cv2.imwrite(resultPath + fileName + '.png', img)
    return True

path = '/Users/zhangshijie/Desktop/SegTest-Data/AugResult/Test0306/label'
res_path='/Users/zhangshijie/Desktop/SegTest-Data/labelAfter/Test0306/'
transSegNetResult(path,res_path)
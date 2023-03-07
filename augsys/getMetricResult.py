import cv2
import os
import glob
import numpy as np
def getErrorResult(resultPath,labelPath,min_use,min_ose):
    res = sorted(glob.glob(resultPath + '/*'))
    lbl = sorted(glob.glob(labelPath + '/*'))
    num = len(res)
    errorUse =0
    errorOse = 0
    for i in range(num):
        lostPixels = 0
        matchedPixels = 0
        extraPixels = 0
        res_img = cv2.imread(res[i])
        lbl_img = cv2.imread(lbl[i])
        lbl_img = cv2.resize(lbl_img,(res_img.shape[1],res_img.shape[0]))
        for j in range(res_img.shape[0]):
            for k in range(res_img.shape[1]):
                if (all(lbl_img[j][k] == [255, 255, 255]) and all(
                        res_img[j][k] == [255, 255, 255])):
                    matchedPixels += 1
                elif (all(res_img[j][k] == [255, 255, 255]) and any(
                        lbl_img[j][k] != [255, 255, 255])):
                    extraPixels += 1
                elif (all(lbl_img[j][k] == [255, 255, 255]) and any(
                        res_img[j][k] != [255, 255, 255])):
                    lostPixels += 1
        USE = round((extraPixels) / (matchedPixels + lostPixels),2)
        OSE = round((lostPixels) / (matchedPixels + lostPixels),2)
        if(USE < min_use):
            errorUse += 1
        if(OSE < min_ose):
            errorOse += 1
    USERate = round(errorUse/num,2)
    OSERate = round(errorOse/num,2)
    return USERate,OSERate
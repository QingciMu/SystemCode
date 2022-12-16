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
                # print(img[m][n])
                if ((img[m][n] == [60, 20, 220]).all() or (img[m][n] == [0, 0, 255]).all() or (
                        img[m][n] == [142, 0, 0]).all() or (img[m][n] == [70, 0, 0]).all() or (
                        img[m][n] == [100, 60, 0]).all() or (img[m][n] == [90, 0, 0]).all() or (
                        img[m][n] == [110, 0, 0]).all() or (img[m][n] == [100, 80, 0]).all() or (
                        img[m][n] == [230, 0, 0]).all() or (img[m][n] == [32, 11, 119]).all()):
                    img[m][n] = [255, 255, 255]
                else:
                    img[m][n] = [0,0,0]
        cv2.imwrite(resultPath + fileName + '.png', img)
    return True

def transSegNetLabel(setPath,resultPath):
    lblList = sorted(glob.glob(setPath + '/*'))
    pos = len(lblList[0].split('/'))-1
    for i in range(len(lblList)):
        lbl = cv2.imread(lblList[i])
        fileName = getImgName(lblList[i],pos)
        for m in range(lbl.shape[0]):
            for n in range(lbl.shape[1]):
                if (all(lbl[m][n] == [24, 24, 24]) or all(lbl[m][n] == [25, 25, 25]) or all(lbl[m][n] == [26, 26, 26]) or all(lbl[m][n] == [27, 27, 27]) or all(lbl[m][n] == [28, 28, 28]) or all(lbl[m][n] == [31, 31, 31]) or all(lbl[m][n] == [32,32,32]) or all(lbl[m][n] == [33,33,33])):
                    lbl[m][n] = [255, 255, 255]
                else:
                    lbl[m][n] = [0,0,0]
        cv2.imwrite(resultPath + fileName + '.png', lbl)
    return True


def processResult(setPath):
    return 0



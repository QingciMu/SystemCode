import cv2
import os
import glob
import numpy as np
from augsys.generalMethod import *


def getMetaResult(taskName,rawSet,augSet,num):
    rawPath = '/Users/zhangshijie/Desktop/SegTest-Data/predictResult/'+taskName+'/'+rawSet
    augPath = '/Users/zhangshijie/Desktop/SegTest-Data/predictResult/'+taskName+'/'+augSet
    augList = glob.glob(augPath+'/*')
    print(augList)
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(len(augList)):
        count =0
        augImg = cv2.imread(augList[i])
        name = getRawName(augList[i])
        raw_img = rawPath +'/'+name+'.png'
        print(raw_img)
        rawImg = cv2.imread(raw_img)
        for j in range(augImg.shape[0]):
            for k in range(augImg.shape[1]):
                if ((augImg[j][k] == rawImg[j][k]).all()):
                    count += 1
        # print(count)
        res = ((256 * 512) - count) / (256 * 512)
        res = ('%.2f' % res)
        # print(res)
        if (res >= '0.05'):
            c0 += 1
        if (res >= '0.1'):
            c1 += 1
        if (res >= '0.15'):
            c2 += 1
        if (res >= '0.2'):
            c3 += 1
    # print(c0,c1,c2,c3)
    c0 = c0 / num
    c0 = ('%.2f' % c0)
    c1 = c1 / num
    c1 = ('%.2f' % c1)
    c2 = c2 / num
    c2 = ('%.2f' % c2)
    c3 = c3 / num
    c3 = ('%.2f' % c3)
    return c0,c1,c2,c3

def getRawName(augpath):
    augName = getImgName(augpath,8)
    lst = augName.split('_')
    return lst[0]



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
from augsys import models
from augsys.generalMethod import *




def objectInsertion(labelName,imageName,obj,insertpoint,times,method,taskName):
    image_name = getImgName(imageName,8)
    newImagename = '/Users/zhangshijie/Desktop/SegTest-Data/AugResult/'+taskName+'/image/'+image_name+'_'+method+'_'+str(times)+'.png'
    newLabelname = '/Users/zhangshijie/Desktop/SegTest-Data/AugResult/'+taskName+'/label/'+image_name+'_'+method+'_'+str(times)+'.png'
    img = cv2.imread(imageName)
    label = cv2.imread(labelName)
    img = cv2.resize(img,(512,256))
    label = cv2.resize(label,(512,256))
    objimg = cv2.imread(obj)
    objimg = cv2.resize(objimg,(int(objimg.shape[1]/4),int(objimg.shape[0]/4)))
    centroid = (int(objimg.shape[0]/2),int(objimg.shape[1]/2))
    realinsertpoint = (insertpoint[0]-centroid[0],insertpoint[1]-centroid[1])
    for i in range(min(objimg.shape[0],img.shape[0]-realinsertpoint[0])):
        for j in range(min(objimg.shape[1],img.shape[1]-realinsertpoint[1])):
            if (i+realinsertpoint[0] < 0 or j+realinsertpoint[1] < 0):
                continue
            if any(objimg[i][j] != [0,0,0]):
                img[i+realinsertpoint[0]][j+realinsertpoint[1]] = objimg[i][j]
                if('car' in obj):
                    label[i+realinsertpoint[0]][j+realinsertpoint[1]] = [13,13,13]
                else:
                    label[i + realinsertpoint[0]][j + realinsertpoint[1]] = [11, 11, 11]
    cv2.imwrite(newImagename, img)
    cv2.imwrite(newLabelname, label)
    return newImagename,newLabelname


# starttime = time.time()  # 开始记录
# endtime = time.time() # 结束记录
# dtime = endtime - starttime
# print("程序运行时间：%.4s s" % dtime)  # 显示到微秒
def getFormInfo(data):
    name = data['taskName']
    desc = data['taskDesc']
    dataset = data['dataset']
    times = data['fold']
    instance = data['instances']
    methods =data['methods']
    head_path = '/Users/zhangshijie/Desktop/SegTest-Data/dataset'
    raw_img = os.path.join(head_path,dataset,'image/*')
    img_list = sorted(glob.glob(raw_img))
    file_num = len(methods) * times * len(img_list)
    new_task = models.AugTask(name=name, desc=desc, fileType='Image', dataset=dataset, times=times, num=file_num,
                              augType='SegTest', status='Running')
    new_task.save()
    return name,desc,dataset,times,instance,methods

def getInsAndPos(instance):
    posLst = []
    for i in range(256):
        for j in range(512):
            dist = min(i, j, 255 - i, 511 - j)
            weight = 1
            if dist < 50:
                weight = weight * 2
            for k in range(weight):
                posLst.append((i, j))
    instLst = []
    head_path = '/Users/zhangshijie/Desktop/SegTest-Data/InstancePool'
    for i in range(len(instance)):
        path = os.path.join(head_path,instance[i][1]+'/*')
        instLst += glob.glob(path)
    return instLst,posLst




def segtestAug(data):
    name,desc,dataset,times,instance,methods = getFormInfo(data)
    aug_path = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult',name)
    aug_img_path = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult',name,'image')
    aug_label_path = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult', name, 'label')
    if not os.path.exists(aug_path):
        os.mkdir((aug_path))
    if not os.path.exists(aug_img_path):
        os.mkdir(aug_img_path)
    if not os.path.exists(aug_label_path):
        os.mkdir(aug_label_path)
    imageLst = glob.glob(os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/Dataset',dataset +'/image/*'))
    labelLst = glob.glob(os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/Dataset',dataset +'/label/*'))
    methodName = ['Random','RandomInst','RandomPos','NoRandom']
    instLst,posLst = getInsAndPos(instance)
    randomPos = []
    for i in range(256):
        for j in range(512):
            randomPos.append((i, j))
    if 'Random' in methods:
        models.Methods(taskName=name,method='Random').save()
        for i in range(len(imageLst)):
            for j in range(times):
                obj = random.choice(instLst)
                pos = random.choice(randomPos)
                objectInsertion(labelLst[i],imageLst[i],obj,pos,j,methodName[0],name)
    if 'RandomInstance' in methods:
        models.Methods(taskName=name,method='Random Instance').save()
        for i in range(len(imageLst)):
            for j in range(times):
                obj = random.choice(instLst)
                pos = random.choice(posLst)
                objectInsertion(labelLst[i],imageLst[i],obj,pos,j,methodName[1],name)
    if 'RandomInsertion' in methods:
        models.Methods(taskName=name,method='Random Insertion').save()
        for i in range(len(imageLst)):
            for j in range(times):
                obj = random.choice(instLst)
                pos = random.choice(randomPos)
                objectInsertion(labelLst[i],imageLst[i],obj,pos,j,methodName[2],name)
    if 'SegTest' in methods:
        models.Methods(taskName=name,method='No Random').save()
        for i in range(len(imageLst)):
            for j in range(times):
                obj = random.choice(instLst)
                pos = random.choice(posLst)
                objectInsertion(labelLst[i],imageLst[i],obj,pos,j,methodName[3],name)
    task_data = models.AugTask.objects.get(name=name)
    task_data.status = 'Success'
    task_data.save()
    return True

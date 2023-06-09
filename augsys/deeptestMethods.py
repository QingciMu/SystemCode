import glob

import cv2
import os
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from augsys import models
from augsys.generalMethod import *


def translation(imgName,tx,ty,times,fileName,aug_img_path):
    # 1. 读取图片
    img1 = cv2.imread(imgName)
    img1 = cv2.resize(img1,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_translation'+'_'+str(times)+'.png')
    # 2. 图像平移
    rows, cols = img1.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])  # 平移矩阵
    dst = cv2.warpAffine(img1, M, (cols, rows))
    cv2.imwrite(newimgName,dst)


    return 0

def scale(imgName,sx,sy,times,fileName,aug_img_path):
    # 1. 读取图片
    img1 = cv2.imread(imgName)
    img1 = cv2.resize(img1,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_scale'+'_'+str(times)+'.png')
    # 2.图像缩放
    # 2.1 绝对尺寸
    rows, cols = img1.shape[:2]
    res = cv2.resize(img1, (2 * cols, 2 * rows), interpolation=cv2.INTER_CUBIC)
    # 2.2 相对尺寸
    res1 = cv2.resize(img1, None, fx=sx, fy=sy)
    cv2.imwrite(newimgName,res1)

    return 0

def shear(imgName,sx,sy,times,fileName,aug_img_path):
    # 1. 读取图片
    img1 = cv2.imread(imgName)
    img1 = cv2.resize(img1,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_shear'+'_'+str(times)+'.png')
    # 2 仿射变换
    rows, cols = img1.shape[:2]
    # 2.1 创建变换矩阵
    M = np.float32([[1, sx, 0], [sy, 1, 0]])  # 平移矩阵
    dst = cv2.warpAffine(img1, M, (cols, rows))
    cv2.imwrite(newimgName,dst)

def rotation(imgName,degree,times,fileName,aug_img_path):
    # 1. 读取图片
    img1 = cv2.imread(imgName)
    img1 = cv2.resize(img1,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_rotation'+'_'+str(times)+'.png')
    # 2 图像旋转
    rows, cols = img1.shape[:2]
    # 2.1 生成旋转矩阵
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)
    # 2.2 进行旋转变换
    dst = cv2.warpAffine(img1, M, (cols, rows))
    cv2.imwrite(newimgName,dst)
    return 0

def contrast(imgName,gain,times,fileName,aug_img_path):
    img = cv2.imread(imgName)
    img = cv2.resize(img,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_contrast'+'_'+str(times)+'.png')
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + beta * blank
    dst = cv2.addWeighted(img, gain, blank, gain, 0)
    cv2.imwrite(newimgName,dst)
    return 0

def brightness(imgName,bias,times,fileName,aug_img_path):
    img = cv2.imread(imgName)
    img = cv2.resize(img,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_brightness'+'_'+str(times)+'.png')
    blank = np.zeros(img.shape, img.dtype)
    dst = cv2.addWeighted(img, 1, blank, 0, bias)
    cv2.imwrite(newimgName,dst)
    return 0

def blur(imgName,strategy,times,fileName,aug_img_path):
    img = cv2.imread(imgName)
    img = cv2.resize(img,(512,256))
    newimgName = os.path.join(aug_img_path,fileName+'_blur'+'_'+str(times)+'.png')
    if strategy == 'Averaging':
        dst = cv2.blur(img, (5,5))
    if strategy == 'Gaussian':
        dst = cv2.GaussianBlur(img, (5,5), 0, 0)
    if strategy == 'Median':
        dst = cv2.medianBlur(img, 3)
    if strategy == 'Bilateral Filter':
        dst = cv2.bilateralFilter(img,25,100,100)
    cv2.imwrite(newimgName,dst)
    return 0


def deeptestAug(data):
    dataset = data['dataset']
    taskName = data['taskName']
    taskDesc = data['taskDesc']
    fold = int(data['fold'])
    methods =data['methods']
    head_path = '/Users/zhangshijie/Desktop/SegTest-Data/dataset'
    raw_img = os.path.join(head_path,dataset,'*')
    aug_path = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult',taskName)
    zip_path =os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult',taskName+'.zip')
    aug_img_path = os.path.join(aug_path)
    img_list = sorted(glob.glob(raw_img))
    file_num = len(methods) * fold * len(img_list)
    #  任务开始后对任务的数据进行保存 任务状态为Running
    new_task = models.AugTask(name=taskName,desc=taskDesc,fileType='Image',dataset=dataset,times=fold,num=file_num,augType='DeepTest',status='Running')
    new_task.save()
    d1=d2=d3=d4=d5=d6=d7 = False
    models.DeeptestParams(taskName = taskName,tranXmin=0,tranXmax=0,tranYmin=0,tranYmax=0,scaleXmin=0,scaleXmax=0,scaleYmin=0,scaleYmax=0,degreeMin=0,degreeMax=0,biasMin=0,biasMax=0).save()
    if('translation' in  methods):
        d1 = True
        tranXmin = int(data['trans_x']['min'])
        tranXmax = int(data['trans_x']['max'])
        tranYmin = int(data['trans_y']['min'])
        tranYmax = int(data['trans_y']['max'])
        models.Methods(taskName=taskName,method='translation').save()
        models.DeeptestParams.objects.filter(taskName=taskName).update(tranXmin=tranXmin,tranXmax=tranXmax,tranYmin=tranYmin,tranYmax=tranYmax)
    if('scale' in methods):
        d2 = True
        scaleXmin = int(data['scale_x']['min'])
        scaleXmax = int(data['scale_x']['max'])
        scaleYmin = int(data['scale_y']['min'])
        scaleYmax = int(data['scale_y']['max'])
        models.Methods(taskName=taskName,method='scale').save()
        models.DeeptestParams.objects.filter(taskName=taskName).update(scaleXmin=scaleXmin,scaleXmax=scaleXmax,scaleYmin=scaleYmin,scaleYmax=scaleYmax)
    if('shear' in methods):
        d3 = True
        models.Methods(taskName=taskName,method='shear').save()
    if ('rotation' in methods):
        d4 = True
        degreeMin = int(data['degree']['min'])
        degreeMax = int(data['degree']['max'])
        models.Methods(taskName=taskName,method='rotation').save()
        models.DeeptestParams.objects.filter(taskName=taskName).update(degreeMin=degreeMin,degreeMax=degreeMax)
    if ('contrast' in methods):
        d5 = True
        models.Methods(taskName=taskName,method='contrast').save()
    if ('brightness' in methods):
        d6 = True
        biasMin = int(data['bias']['min'])
        biasMax = int(data['bias']['max'])
        models.Methods(taskName=taskName,method='brightness').save()
        models.DeeptestParams.objects.filter(taskName=taskName).update(biasMin=biasMin,biasMax=biasMax)
    if ('blur' in methods):
        d7 = True
        strategy = data['strategy']
        models.Methods(taskName=taskName,method='blur').save()
        for i in range(len(strategy)):
            models.Strategy(taskName=taskName,strategy=strategy[i]).save()
    if not os.path.exists(aug_path):
        os.mkdir((aug_path))
    if not os.path.exists(aug_img_path):
        os.mkdir(aug_img_path)
    for i in range(fold):
        for j in range(len(img_list)):
            imgPath = img_list[j]
            imgName = getImgName(imgPath,7)
            if(d1):
                p1 = random.randint(tranXmin,tranXmax)
                p2 = random.randint(tranYmin,tranYmax)
                translation(imgPath,p1,p2,i,imgName,aug_img_path)
            if(d2):
                p1 = random.randint(scaleXmin,scaleXmax)
                p2 = random.randint(scaleYmin,scaleYmax)
                scale(imgPath,p1,p2,i,imgName,aug_img_path)
            if(d3):
                p1 = -0.1 * random.randint(-5, 5)
                p2 = 0
                shear(imgPath,p1,p2,i,imgName,aug_img_path)
            if(d4):
                degree = random.randint(degreeMin,degreeMax)
                rotation(imgPath,degree,i,imgName,aug_img_path)
            if(d5):
                p = random.randint(2,3)
                contrast(imgPath,p,i,imgName,aug_img_path)
            if(d6):
                p = random.randint(biasMin,biasMax)
                brightness(imgPath,p,i,imgName,aug_img_path)
            if(d7):
                strategy_now = random.choice(strategy)
                blur(imgPath,strategy_now,i,imgName,aug_img_path)
    zipDir(aug_path,zip_path)
    task_data = models.AugTask.objects.get(name=taskName)
    task_data.status = 'Success'
    task_data.save()
    return 0




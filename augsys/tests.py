# import cv2
# import os
# import glob
# import numpy as np
# from augsys.generalMethod import *
# def transSegNetResult(setPath,resultPath):
#     test_predict = sorted(glob.glob(setPath + '/*'))
#     pos = len(test_predict[0].split('/'))-1
#     for i in range(len(test_predict)):
#         img = cv2.imread(test_predict[i])
#         fileName = getImgName(test_predict[i],pos)
#         for m in range(img.shape[0]):
#             for n in range(img.shape[1]):
#                 if ((img[m][n] == [29,29,29]).all() or (img[m][n] == [30,30,30]).all() or (
#                         img[m][n] == [24,24,24]).all() or (img[m][n] == [25,25,25]).all() or (
#                         img[m][n] == [26,26,26]).all() or (img[m][n] == [27,27,27]).all() or (
#                         img[m][n] == [28,28,28]).all() or (img[m][n] == [31,31,31]).all() or (
#                         img[m][n] == [32,32,32]).all() or (img[m][n] == [33,33,33]).all()):
#                     img[m][n] = [255, 255, 255]
#                 else:
#                     img[m][n] = [0,0,0]
#         cv2.imwrite(resultPath + fileName + '.png', img)
#     return True
#
# path = '/Users/zhangshijie/Desktop/SegTest-Data/AugResult/Test0306/label'
# res_path='/Users/zhangshijie/Desktop/SegTest-Data/labelAfter/Test0306/'
# transSegNetResult(path,res_path)
import glob
import os
import zipfile

import numpy as np
import matplotlib.pyplot as plt
def drawPicture(useIOU,useOSE,useUSE,IOU,OSE,USE,taskName,dataset):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x_data =[]
    y_data = []
    if(useIOU ==1):
        x_data.append('IOU')
        y_data.append(IOU)
    if(useOSE == 1):
        x_data.append('OSE')
        y_data.append(OSE)
    if(useUSE == 1):
        x_data.append('USE')
        y_data.append(USE)
    for i in range(len(x_data)):
        plt.bar(x_data[i], y_data[i])
    # 设置图片名称
    plt.title("测试结果",fontname = 'SimHei')
    # 设置x轴标签名
    plt.xlabel("评价指标",fontname = 'SimHei')
    # 设置y轴标签名
    plt.ylabel("致错率",fontname = 'SimHei')
    # 显示
    plt.savefig('/Users/zhangshijie/Desktop/SegTest-Data/fig/%s.png'%(taskName+'-'+dataset))
    return True

drawPicture(1,1,1,0,1,0.71,'testall','Test0306')
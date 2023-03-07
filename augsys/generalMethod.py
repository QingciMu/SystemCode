import glob
import os
import zipfile

import numpy as np
import matplotlib.pyplot as plt


def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))

    zip.close()

#获取测试集中的测试用例数
def getFileNum(path):
    return len(glob.glob(path))

def getImgName(imgPath,i):
    img = (imgPath.split('/'))[i]
    return (img.split('.'))[0]

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
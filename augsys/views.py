import os.path

from django.shortcuts import render
from django.db import connection

# Create your views here.
# 需要导入相关的模块
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from augment.wsgi import *
from augsys import models
# Create your views here.
from django.http import HttpResponse
from django.core.files import File
import zipfile
import glob
from augsys.deeptestMethods import *
from augsys.segtestMethods import *
from augsys.getFileSize import *
from augsys.uploadInstance import *
import shutil
from augsys.generalMethod import *
from augsys.predictSegNet import *
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph,Table,TableStyle
from augsys.generateReport import *




def datasetDetail(request):
    response = {}
    try:
        datasetDetail = models.dataset.objects.raw('select * from dataset')
        response['code'] = 200
        response['data'] = json.loads(serializers.serialize("json", datasetDetail))
        response['msg'] = 'success'
    except  Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

def getModel(request):
    response = {}
    try:
        modelDetail = eval(serializers.serialize("json", models.Model.objects.all()))
        response['code'] = 200
        result=[]
        for i in range(len(modelDetail)):
            temp = {}
            temp['id'] = modelDetail[i]['pk']
            temp['name'] = modelDetail[i]['fields']['name']
            temp['modelType'] = modelDetail[i]['fields']['modelType']
            temp['uploadTime'] = modelDetail[i]['fields']['uploadTime']
            result.append(temp)
        response['data'] = result
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

def uploadSegModel(request):
    response = {}
    try:
        if request.method == 'POST':
            file_obj = request.FILES.get('file',None)
            head_path = '/Users/zhangshijie/Desktop/SegTest-Data/model'
            if not os.path.exists(head_path):
                os.mkdir((head_path))

            file_path = os.path.join(head_path,file_obj.name)
            with open(file_path,'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            new_model = models.Model(name=file_obj.name,modelType="SegNet")
            new_model.save()
            response['code'] = 200
            response['data'] = file_obj.name
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def uploadHrModel(request):
    response = {}
    try:
        if request.method == 'POST':
            file_obj = request.FILES.get('file',None)
            head_path = '/Users/zhangshijie/Desktop/SegTest-Data/model'
            if not os.path.exists(head_path):
                os.mkdir((head_path))

            file_path = os.path.join(head_path,file_obj.name)
            with open(file_path,'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            new_model = models.Model(name=file_obj.name,modelType="HRNet")
            new_model.save()
            response['code'] = 200
            response['data'] = file_obj.name
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def deleteModel(request):
    response = {}
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            modelId = data['id']
            name = data['name']
            modelPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/Model',name)
            os.remove(modelPath)
            models.Model.objects.filter(modelId = modelId).delete()
            cursor = connection.cursor()
            cursor.execute('alter table Model drop modelId')
            cursor.execute('alter table Model add modelId int not null primary key auto_increment first')
            response['code'] = 200
            response['data'] = True
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def file_iterator(file_path, chunk_size = 512):
    with open(file_path, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c :
                yield c
            else:
                break

def uploadDataset(request):
    response = {}
    try:
        if request.method == 'POST':
            file_obj = request.FILES.get('file',None)
            head_path = '/Users/zhangshijie/Desktop/SegTest-Data/dataset'
            zip_file = zipfile.ZipFile(file_obj)
            if not os.path.exists(head_path):
                os.mkdir((head_path))
            zip_file.extractall(path=head_path)

            file_path = os.path.join(head_path,file_obj.name)
            with open(file_path,'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            fileName = str(file_obj.name).split('.')[0]
            num = len(glob.glob(os.path.join(head_path,fileName,'image/*')))
            new_dataset = models.dataset(name=fileName,num=num)
            new_dataset.save()
            response['code'] = 200
            response['data'] = fileName
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def deleteDataset(request):
    response = {}
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            id = data['id']
            name = data['name']
            models.dataset.objects.filter(id = id).delete()
            dirPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/Dataset',name)
            shutil.rmtree(dirPath)
            zipPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/Dataset',name+'.zip')
            os.remove(zipPath)
            cursor = connection.cursor()
            cursor.execute('alter table dataset drop id')
            cursor.execute('alter table dataset add id int not null primary key auto_increment first')
            response['code'] = 200
            response['data'] = True
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def getInstance(request):
    response = {}
    try:
        head_path = '/Users/zhangshijie/Desktop/SegTest-Data/InstancePool'
        car_path = os.path.join(head_path,'car/*')
        person_path = os.path.join(head_path,'person/*')
        car_list = sorted(glob.glob(car_path))
        person_list = sorted(glob.glob(person_path))
        lst = []
        for i in range(len(car_list)):
            row = {}
            filePath = car_list[i]
            fileName = getImgName(filePath,7)
            fileSize = getFileSize(filePath)
            row['name'] = fileName
            row['type'] = 'Car'
            row['size'] = str(fileSize) + 'KB'
            lst.append(row)
        for i in range(len(person_list)):
            row = {}
            filePath = person_list[i]
            fileName = getImgName(filePath,7)
            fileSize = getFileSize(filePath)
            row['name'] = fileName
            row['type'] = 'Person'
            row['size'] = str(fileSize) + 'KB'
            lst.append(row)
        response['code'] = 200
        response['data'] = lst
        response['msg'] = 'success'
    except Exception as e:
        response['data'] = []
        response['msg'] = str(e)
    return JsonResponse(response)

def getInstanceList(request):
    response = {}
    try:
        instanceDetail = eval(serializers.serialize("json", models.Instance.objects.all()))
        response['code'] = 200
        result={}
        car=[]
        person=[]
        for i in range(len(instanceDetail)):
            temp = {}
            temp['value'] = instanceDetail[i]['pk']
            temp['label'] = instanceDetail[i]['pk']
            type = instanceDetail[i]['fields']['type']
            if(type == 'Car'):
                car.append(temp)
            else:
                person.append(temp)
        result['car'] = car
        result['person'] = person
        response['data'] = result
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

def uploadCar(request):
    response = {}
    try:
        if request.method == 'POST':
            file_obj = request.FILES.get('file',None)
            uploadInstance(file_obj)
            fileName = str(file_obj.name).split('.')[0]
            response['code'] = 200
            response['data'] = fileName
            response['msg'] = 'success'
            models.Instance(name=fileName,type='Car').save()
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def uploadPerson(request):
    response = {}
    try:
        if request.method == 'POST':
            file_obj = request.FILES.get('file',None)
            uploadInstance(file_obj)
            fileName = str(file_obj.name).split('.')[0]
            response['code'] = 200
            response['data'] = fileName
            response['msg'] = 'success'
            models.Instance(name=fileName,type='Person').save()
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def downloadInstance(request):
    response = {}
    try:
        raw_file = '/Users/zhangshijie/Desktop/SegTest-Data/InstancePool'
        zip_path = '/Users/zhangshijie/Desktop/SegTest-Data/InstancePool.zip'
        if(os.path.exists(zip_path)):
            os.remove(zip_path)
        zipDir(raw_file,zip_path)
        response['code'] = 200
        response['data'] =True
        response['msg'] ='success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)


def deepTask(request):
    data = json.loads(request.body.decode('utf-8'))
    response = {}
    try:
        deeptestAug(data)
        response['data'] = True
        response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def segTask(request):
    data = json.loads(request.body.decode('utf-8'))
    response = {}
    try:
        segtestAug(data)
        response['data'] = True
        response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def getTask(request):
    response = {}
    try:
        modelDetail = eval(serializers.serialize("json", models.AugTask.objects.all()))
        response['code'] = 200
        result=[]
        for i in range(len(modelDetail)):
            temp = {}
            temp['taskName'] = modelDetail[i]['pk']
            temp['fileType'] = modelDetail[i]['fields']['fileType']
            temp['fileNum'] = modelDetail[i]['fields']['num']
            temp['Method'] = modelDetail[i]['fields']['augType']
            temp['Status'] = modelDetail[i]['fields']['status']
            temp['createTime'] = modelDetail[i]['fields']['startTime']
            result.append(temp)
        response['data'] = result
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


def getAugDetail(request):
    response = {}
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            taskName = data['taskName']
            type = data['type']
            result = {}
            taskResult = {}
            paramsResult = {}
            taskInfo = eval(serializers.serialize("json", models.AugTask.objects.filter(name=taskName)))
            if(type == 'DeepTest'):
                paramsInfo = eval(serializers.serialize("json", models.DeeptestParams.objects.filter(taskName=taskName)))
                paramsLst = ['tranXmin','tranXmax','tranYmin','tranYmax','scaleXmin','scaleXmax','scaleYmin','scaleYmax','degreeMin','degreeMax','biasMin','biasMax']
                for s in paramsLst:
                    paramsResult[s] = paramsInfo[0]['fields'][s]
                strategy = []
                strategyinfo = eval(serializers.serialize("json", models.Strategy.objects.filter(taskName=taskName)))
                for i in range(len(strategyinfo)):
                    strategy.append(strategyinfo[i]['fields']['strategy'])
                result['strategy'] = strategy
            methodInfo = eval(serializers.serialize("json", models.Methods.objects.filter(taskName=taskName)))
            lstMethod = []
            for i in range(len(methodInfo)):
                lstMethod.append(methodInfo[i]['fields']['method'])
            taskResult['taskName'] = taskInfo[0]['pk']
            taskResult['taskDesc'] = taskInfo[0]['fields']['desc']
            taskResult['dataset'] = taskInfo[0]['fields']['dataset']
            taskResult['type'] = taskInfo[0]['fields']['augType']
            taskResult['times'] = taskInfo[0]['fields']['times']
            taskResult['lstMethod'] = lstMethod
            result['taskInfo'] = taskResult
            result['paramsInfo'] = paramsResult
            response['code'] = 200
            response['data'] = result
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

# 删除扩增任务
def deleteAugTask(request):
    response = {}
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            taskName =data['taskName']
            type = data['type']
            dirPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult',taskName)
            shutil.rmtree(dirPath)
            zipPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult',taskName+'.zip')
            os.remove(zipPath)
            cursor = connection.cursor()
            if(type == 'DeepTest'):
                models.AugTask.objects.filter(name=taskName).delete()
                models.Methods.objects.filter(taskName=taskName).delete()
                models.DeeptestParams.objects.filter(taskName=taskName).delete()
                models.Strategy.objects.filter(taskName=taskName).delete()
                cursor.execute('alter table Methods drop id')
                cursor.execute('alter table Methods add id int not null primary key auto_increment first')
                cursor.execute('alter table strategy drop id')
                cursor.execute('alter table strategy add id int not null primary key auto_increment first')
            response['code'] = 200
            response['data'] = True
            response['msg'] = 'success'
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)

def getTestTask(request):
    response = {}
    try:
        modelDetail = eval(serializers.serialize("json", models.PredictTask.objects.all()))
        response['code'] = 200
        result=[]
        for i in range(len(modelDetail)):
            temp = {}
            temp['taskName'] = modelDetail[i]['pk']
            temp['fileType'] = modelDetail[i]['fields']['fileType']
            temp['fileNum'] = modelDetail[i]['fields']['num']
            temp['Method'] = modelDetail[i]['fields']['augType']
            temp['Status'] = modelDetail[i]['fields']['status']
            temp['createTime'] = modelDetail[i]['fields']['startTime']
            result.append(temp)
        response['data'] = result
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


#创建测试任务时 获取测试数据集 包括原始数据集和扩增数据集
def getTestCase(request):
    response = {}
    try:
        dataset = eval(serializers.serialize("json", models.dataset.objects.all()))
        augResult = eval(serializers.serialize("json", models.AugTask.objects.filter(status = 'Success')))
        dataLst = []
        augLst = []
        for i in range(len(dataset)):
            temp = {}
            temp['value']=temp['label'] = dataset[i]['fields']['name']
            dataLst.append(temp)
        for i in range(len(augResult)):
            temp = {}
            temp['value']=temp['label'] = augResult[i]['pk']
            augLst.append(temp)
        data = {}
        data['dataSet'] = dataLst
        data['augResult'] = augLst
        response['code'] = 200
        response['data'] = data
        response['msg'] = 'Success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)

def startTest(request):
    response = {}
    try:
        if request.method == 'POST':
            # 获取所有的表单数据
            data = json.loads(request.body.decode('utf-8'))
            taskName = data['taskName']
            taskDesc = data['taskDesc']
            modelName = data['model']
            testCase = data['testCase']
            testSet = []
            dataset = ""
            num= 0
            testSetNum = len(testCase)
            colorResult = '/Users/zhangshijie/Desktop/SegTest-Data/predictResult/' +taskName
            resultPathLst = []
            # 获取模型的类型 根据模型类型执行不同的预测任务
            type = eval(serializers.serialize("json", models.Model.objects.filter(name=modelName)))[0]['fields'][
                'modelType']
            if not os.path.exists(colorResult):
                os.mkdir(colorResult)
            for i in range(testSetNum):
                resultPath = colorResult +'/'+ testCase[i][0]
                if not os.path.exists(resultPath):
                    os.mkdir(resultPath)
                resultPath = resultPath + '/' + testCase[i][1]
                if not os.path.exists(resultPath):
                    os.mkdir(resultPath)
                resultPathLst.append(resultPath)
                if(i != len(testCase)):
                    testStr = testCase[i][0] + '/'+ testCase[i][1]
                    # 保存测试用例集信息
                    # models.TestCase(taskName=taskName,testCase=testStr).save()
                    if(i != len(testCase) -1):
                        testStr += ' '
                    dataset += testStr
                setPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data',testCase[i][0],testCase[i][1])
                testSet.append(setPath)
                path = os.path.join(setPath,'image/*')
                num += getFileNum(path)

            models.PredictTask(taskName=taskName,taskDesc=taskDesc,dataset=dataset,num=num,model=modelName,status='Running').save()
            doc = SimpleDocTemplate("%s.pdf" %taskName)
            story = []
            addTaskInfo(taskName,story)
            if(type == 'SegNet'):
                for i in range(testSetNum):
                    loss,iou = startSegNetPredict(testSet[i],resultPathLst[i],modelName)
                    story = addTestResult(testSet[i],story,loss,iou)
            task_data = models.PredictTask.objects.get(taskName=taskName)
            task_data.status = 'Success'
            task_data.save()
            doc.build(story)
            response['code'] = 200
            response['data'] = True
    except Exception as e:
        response['data'] = False
        response['msg'] = str(e)
    return JsonResponse(response)


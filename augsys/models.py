from django.db import models

# Create your models here.
class dataset(models.Model):
    id=models.AutoField(primary_key=True,null=False,unique=True)
    name = models.CharField(max_length=255,null=False)
    num = models.IntegerField(null=False)
    uploadTime = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'dataset'

class Model(models.Model):
    modelId=models.AutoField(primary_key=True,null=False,unique=True)
    name = models.CharField(max_length=255,null=False)
    modelType = models.CharField(max_length=255,null=False)
    uploadTime = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'Model'

class AugTask(models.Model):
    name = models.CharField(primary_key=True,max_length=255,null=False)
    desc = models.CharField(max_length=500,null=True)
    dataset = models.CharField(max_length=255, null=False)
    fileType = models.CharField(max_length=255,null=False)
    times = models.IntegerField(null=False)
    num = models.IntegerField(null=True)
    augType = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)
    startTime =models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'AugTask'

class Methods(models.Model):
    id=models.AutoField(primary_key=True,null=False,unique=True)
    taskName = models.CharField(max_length=255,null=False)
    method = models.CharField(max_length=255,null=False)
    class Meta:
        db_table = 'Methods'
class DeeptestParams(models.Model):
    taskName = models.CharField(primary_key=True,max_length=255,null=False)
    tranXmin = models.IntegerField(null=True)
    tranXmax = models.IntegerField(null=True)
    tranYmin = models.IntegerField(null=True)
    tranYmax = models.IntegerField(null=True)
    scaleXmin = models.IntegerField(null=True)
    scaleXmax = models.IntegerField(null=True)
    scaleYmin = models.IntegerField(null=True)
    scaleYmax = models.IntegerField(null=True)
    degreeMin = models.IntegerField(null=True)
    degreeMax = models.IntegerField(null=True)
    biasMin = models.IntegerField(null=True)
    biasMax = models.IntegerField(null=True)

    class Meta:
        db_table = 'DeepParams'

class Strategy(models.Model):
    id=models.AutoField(primary_key=True,null=False,unique=True)
    taskName = models.CharField(max_length=255,null=False)
    strategy = models.CharField(max_length=255,null=False)

    class Meta:
        db_table = 'strategy'

class Instance(models.Model):
    name = models.CharField(primary_key=True,max_length=255,null=False)
    type = models.CharField(max_length=255, null=False)
    uploadTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'instance'

class PredictTask(models.Model):
    taskName = models.CharField(primary_key=True,max_length=255,null=False)
    taskDesc = models.CharField(max_length=500,null=True)
    dataset = models.CharField(max_length=255,null=False)
    num = models.IntegerField(null=False)
    model = models.CharField(max_length=255,null=False)
    status = models.CharField(max_length=255,null=False)
    createTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'predictTask'

class TestCase(models.Model):
    id=models.AutoField(primary_key=True,null=False,unique=True)
    taskName = models.CharField(max_length=255,null=False)
    setType = models.CharField(max_length=255,null=False)
    testCase = models.CharField(max_length=255,null=False)

    class Meta:
        db_table = 'testCase'


class Threshold(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    taskName = models.CharField(max_length=255,null=False)
    metric = models.CharField(max_length=255,null=False)
    threshold = models.CharField(max_length=255,null=False)

    class Meta:
        db_table = 'threshold'

class TestResult(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    taskName = models.CharField(max_length=255,null=False)
    dataset = models.CharField(max_length=255,null=False)
    IOU = models.CharField(max_length=255,null=True)
    OSE = models.CharField(max_length=255,null=True)
    USE = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'testResult'
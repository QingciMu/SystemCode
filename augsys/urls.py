from django.urls import path , re_path

from . import views

urlpatterns = [
    re_path(r'uploadDataset',views.uploadDataset),
    re_path(r'deleteDataset',views.deleteDataset),
    re_path(r'dataset', views.datasetDetail),
    re_path(r'uploadSegModel',views.uploadSegModel),
    re_path(r'getModel',views.getModel),
    re_path(r'deleteModel',views.deleteModel),
    re_path(r'uploadHrModel',views.uploadHrModel),
    re_path(r'deepTask',views.deepTask),
    re_path(r'segTask',views.segTask),
    re_path(r'getTask',views.getTask),
    re_path(r'getAugDetail',views.getAugDetail),
    re_path(r'deleteAugTask',views.deleteAugTask),
    re_path(r'getInstance$',views.getInstance),
    re_path(r'uploadCar',views.uploadCar),
    re_path(r'uploadPerson',views.uploadPerson),
    re_path(r'getInstanceList$',views.getInstanceList),
    re_path(r'downloadInstance',views.downloadInstance)
]
import glob
import os.path

import cv2
import torch
from django.test import TestCase

# Create your tests here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from augment.wsgi import *
from augsys import models
import ast
lst = {}
taskName = 'test1'
s = 'tranXmin'
paramsInfo = eval(serializers.serialize("json", models.DeeptestParams.objects.filter(taskName=taskName)))
lst['tranXin'] = paramsInfo[0]['fields']['tranXmin']
print(lst)
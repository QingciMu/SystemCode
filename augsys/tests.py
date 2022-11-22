import glob
import os.path
import shutil

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

dirPath = os.path.join('/Users/zhangshijie/Desktop/SegTest-Data/AugResult', 'test1.zip')
os.remove(dirPath)
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
from augsys.getFileSize import *
from augsys.uploadInstance import *
import shutil


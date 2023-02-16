from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from augsys import models
from django.core import serializers


styles = getSampleStyleSheet()
pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  #注册字体
# 设置标题和正文字体
styles.add(ParagraphStyle(fontName='SimSun', name='SongTitle', leading=50, fontSize=20,alignment=1))  #自己增加新注册的字体
styles.add(ParagraphStyle(fontName='SimSun', name='Song', leading=20, fontSize=10,alignment=1))  #自己增加新注册的字体
styles.add(ParagraphStyle(fontName='SimSun', name='SubTitle', leading=20, fontSize=15,alignment=0))  #自己增加新注册的字体

def addTaskInfo(taskName,story):
       taskData = models.PredictTask.objects.get(taskName=taskName)
       story.append(Paragraph("测试任务%s测试报告" %taskName, styles['SongTitle']))
       story.append(Paragraph("任务名称:  %s" %taskData.taskName, styles['Song']))
       story.append(Paragraph("任务描述:  %s" %taskData.taskDesc, styles['Song']))
       story.append(Paragraph("测试模型:  %s" %taskData.model, styles['Song']))
       story.append(Paragraph("测试数据集:  %s" %taskData.dataset, styles['Song']))

       # 初始化表格内容
       data= [['标识', '对应扩增方法'],
              ['ST1','Translation'],
              ['ST2','Scale'],
              ['ST3','Shear'],
              ['ST4','Rotation'],
              ['ST5','Contrast'],
              ['ST6','Brightness'],
              ['ST7','Blur'],
              ['ST0,0','Random'],
              ['ST0,1','Random Instance'],
              ['ST1,0','Random Position'],
              ['St1,1','No Random']]

       # 根据内容创建表格
       t = Table(data)
       t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'SimSun'), ('LEADING',(0,0),(-1,-1),10), ('FONTSIZE',(0,0),(-1,-1),12),('GRID',(0,0),(-1,-1),0.5,colors.grey)]))
       # 将表格添加到内容中
       story.append(t)
       return story
def addTestResult(dataset,story,loss,IoU):
       story.append(Paragraph("数据集%s"%dataset, styles['SubTitle']))
       story.append(Paragraph("Loss:  %s" %loss, styles['Song']))
       story.append(Paragraph("IoU:  %s" %IoU, styles['Song']))
       return story

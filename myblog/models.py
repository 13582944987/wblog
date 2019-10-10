from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


class Blogtypes(models.Model):
    """类型"""
    types = models.CharField(verbose_name='类型', max_length=24)

class Blog(models.Model):
    """内容"""
    title = models.CharField(max_length=64)
    add_time = models.DateTimeField(verbose_name="创建时间",default=datetime.now)
    categorie = models.ForeignKey(Blogtypes,on_delete=models.CASCADE, null=False, verbose_name='类别')
    content = UEditorField(verbose_name='内容',
    						width = 700,
    						height = 400,
    						toolbars = "full",
    						imagePath='',
    						filePath='',
    						upload_settings={'imageMaxSizing':1024000},
    						default=''
    	)
    def __str__(self):
        return '标题:{},时间:{},概要:{}'.format(self.title,self.add_time,self.content)


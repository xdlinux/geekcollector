#-*- coding: UTF-8 -*-
from django.db import models

class OS(models.Model):
    """不同操作系统的展示信息"""
    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=140)
    image = models.ImageField(upload_to='./', max_length=100)
    def __unicode__(self):
        return self.name


#-*- coding: UTF-8 -*-
from django.db import models

class OS(models.Model):
    """不同操作系统的展示信息"""
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=140)
    image = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name


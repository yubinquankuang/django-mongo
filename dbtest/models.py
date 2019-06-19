import mongoengine

import datetime

from django.db import models

#mongo数据库，存储xml以及解析后的json数据
class XmlData(mongoengine.Document):
    anareport = mongoengine.IntField()
    xml = mongoengine.DictField()
    file = mongoengine.FileField()
    wave = mongoengine.DictField()
    file_name = mongoengine.StringField()
    #
    # class Meta:
    #     collection = "xmldata"

    def __str__(self):
        return self.anareport


class AnaReport(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    device = models.ForeignKey(to = "dbtest.Device",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=15,null=True,blank = True)

    def __str__(self):
        return self.name



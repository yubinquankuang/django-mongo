# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/6/14 15:06'
import django_filters
from .models import XmlData,Device,AnaReport

class XmlReadFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = XmlData
        fields = ("anareport",)
# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/6/13 13:53'

from django.conf.urls import url,include
from dbtest.views import DeviceViewSet,XmlReadViewSet,AnaReportViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
#连接xmlData
route.register(r"xml",XmlReadViewSet,base_name="xml")
#连接anaRepot
route.register(r"anaReport",AnaReportViewSet,base_name="anaReport")
#连接device
route.register(r"device",DeviceViewSet,base_name="device")

urlpatterns = [
    url(r"^", include(route.urls)),
]
# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/6/19 16:09'

import urllib
import requests
http = "http://10.140.22.253/"
a = "data/faultfile/山东省/潍坊/20160530 103534#1变/云湖站/本侧第二套保护/677_4027.cfg"


b = urllib.parse.quote(a)
s = http + b
print(s)
# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/6/13 15:48'
import random,os
from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers

from .models import XmlData,AnaReport,Device
from tools.readXml import parseXml
from tools.readWave import jarinput


def m2d_exclude(obj, *args):
    """
    排除mongo文档中args中的相关字段
    :param obj:
    :param args:
    :return:
    """
    model_dict = obj.to_mongo().to_dict()
    if args:
        list(map(model_dict.pop, list(args)))
    if "_id" in model_dict.keys():
        #将ObjectID转换为str类型
        model_dict["_id"] = str(model_dict["_id"])
        if "file" in model_dict:
            # model_dict["file"] = obj.file.read()
            del model_dict["file"]
            # model_dict["file_name"] = obj.file.get("filename")
    return model_dict


def getXmlData():
    """
    获取一个随机xml的json数据
    :return:
    """
    index = random.randint(0, 4)
    file_name = parseXml.XMLs[index]
    file_path = os.path.join(parseXml.xml_path, file_name)
    try:
        result = parseXml.delXml1(file_path)
    except:
        result = parseXml.delXml2(file_path)
    return result

# class XmlReadSerializer(serializers.ModelSerializer):
#     ana = serializers.SerializerMethodField(read_only=True)
#
#     def get_ana(self,obj):
#         xml = XmlData.objects.all()
#         anaReport = xml.item_frequecies("anareport")
#         return anaReport
#     id = serializers.SerializerMethodField(read_only=True)
#
#     def get_id(self,obj):
#         id = str(obj._id)
#         return id
#
#     class Meta:
#         model = XmlData
#         fields = ("id","ana")
class XmlReadSerializer(DocumentSerializer):
    class Meta:
        model = XmlData
        fields = "__all__"


class AnaReportSerializer(serializers.ModelSerializer):
    xmldata = serializers.SerializerMethodField(read_only=True)
    # file = serializers.FileField(write_only=True)
    def get_xmldata(self,obj):
        try:
            data = XmlData.objects.get(anareport = obj.id)
        except:
            return {}
        lis = ["wave"]
        xml_data = m2d_exclude(data,*lis)
        return xml_data

    def create(self, validated_data):
        # file = self.context["request"].FILES

        # file = validated_data["file"]
        file = open(r"I:\teamproject\djangodb\data\xml\00002_00003_00000.xml","rb")
        result = getXmlData()
        # del validated_data['file']
        ana = AnaReport.objects.create(**validated_data)
        wave = r"I:\teamproject\djangodb\data\wave\3628080_comtrade"
        xml = jarinput.ReadXml()
        wave = xml.get_wave(wave, "[80,0]", {})
        xml = XmlData.objects.create(anareport = ana.id,xml = result,wave = wave,file = file,file_name = file.name)
        file.close()
        return ana

    def update(self, instance, validated_data):
        result = getXmlData()
        ana = AnaReport.objects.filter(id = instance.id).update(**validated_data)
        print(ana)
        xml = XmlData.objects.filter(anareport = instance.id).update(xml = result)
        return AnaReport.objects.get(id = instance.id)

    class Meta:
        model = AnaReport
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"

# _*_ coding: utf-8 _*_
__author__ = 'yubinquan'
__date__ = '2019/5/29 15:46'

import os, re,types

from xml.dom.minidom import parse
from djangodb.settings import BASE_DIR,MEDIA_ROOT


class parseXml(object):
    def __init__(self, path):
        self.path = path
        self.root = parse(self.path).documentElement

    def tag(self, name):
        return self.root.getElementsByTagName(name)

    def tagParent(self, tag, name):
        return tag.getElementsByTagName(name)

    def tagAttr(self, name, attr="value"):
        """
        传入标签名称和attr值，如果找到一个，则返回对应的值，早到找到多个对应标签，返回对应值的列表
        :param name: 标签名称
        :param attr: 属性名称
        :return: 对应属性的值
        """
        if len(self.tag(name)) == 1:
            if self.tag(name)[0].hasAttribute(attr):
                return self.tag(name)[0].getAttribute(attr)
            else:
                return "未找到该attr"
        elif len(self.tag(name)) > 1:
            attrs = []
            for tag in self.tag(name):
                if tag.hasAttribute(attr):
                    attrs.append(tag.getAttribute(attr))
                else:
                    break
            return attrs

    def tagAttrIndex(self, name, index, attr="value"):
        if self.tag(name)[index].hasAttribute(attr):
            return self.tag(name)[index].getAttribute(attr)
        else:
            return "未找到该attr"

def t_float(charList):
    """
    判断传入数据的类型，将百分数转换为float，将数字字符串转换为float，其他直接返回
    :param charList:
    :return:
    """
    rule = re.compile(r"\D")
    if type(charList) == type([]):
       charList = charList[0]
    if charList == "" or charList == None:
        return None
    elif rule.findall(charList):
        result = float(charList.split(" ")[0])
        if "%" in charList:
            result = result / 100
            result = round(result,7)
        return result

def t_bool(charList):
    """
    将bool字符串转换为对应的bool值
    :param charList:
    :return:
    """
    if charList:
        if charList == "False" or charList == "false":
            return False
        else:
            return True
    else:
        return False

def delXml1(path):
    """
    解析xml文件
    :param path: xml文件绝对路径
    :return: 读取指定元素的字典
    """
    dic = {}
    x = parseXml(path)
    bay = x.tagAttr("Bay")
    dic["Bay"] = bay
    bay_type = x.tagAttr("Bay", "type")
    dic["Bay_type"] = bay_type
    faultINo = x.tagAttr("FaultINo")
    dic["FaultINo"] = faultINo
    faultUNo = x.tagAttr("FaultUNo")
    dic["FaultUNo"] = faultUNo
    faultDNo = x.tagAttr("FaultDNo")
    dic["FaultDNo"] = faultDNo
    phase = x.tagAttr("Phase")[0]
    dic["Phase_x"] = phase
    jpt = x.tagAttr("JPT")
    dic["JPT"] = int(jpt)
    position = x.tagAttr("Position")
    dic["Position"] = t_float(position)
    percentage = x.tagAttr("Percentage")
    dic["Percentage"] = t_float(percentage)
    dic["FaultTime"] = x.tagAttr("FaultTime")
    dic["SampleNo"] = int(x.tagAttr("SampleNo"))
    dic["RelayActTime"] = t_float(x.tagAttr("RelayActTime"))
    dic["BreakerJumpTime"] = t_float(x.tagAttr("BreakerJumpTime"))
    dic["FaultClearTime"] = t_float(x.tagAttr("FaultClearTime"))
    dic["CHZTime"] = t_float(x.tagAttr("CHZTime"))
    dic["BreakerShutTime"] = t_float(x.tagAttr("BreakerShutTime"))
    dic["WaveClosetTime"] = t_float(x.tagAttr("WaveClosetTime"))
    dic["RelayActAgainTime"] = t_float(x.tagAttr("RelayActAgainTime"))
    dic["BreakerJumpAgainTime"] = t_float(x.tagAttr("BreakerJumpAgainTime"))
    dic["FaultClearAgainTime"] = t_float(x.tagAttr("FaultClearAgainTime"))
    dic["Duration"] = t_float(x.tagAttr("Duration"))
    dic["Result_x"] = t_bool(x.tagAttr("Result"))
    primary = x.tag("Primary")[0]
    dic["Primary_I"] = t_float(x.tagParent(primary, "I")[0].getAttribute("value"))
    dic["Primary_Ia"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ia"))
    dic["Primary_Ib"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ib"))
    dic["Primary_Ic"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ic"))
    dic["Primary_I0"] = t_float(x.tagParent(primary, "I")[0].getAttribute("I0"))
    dic["Primary_U"] = t_float(x.tagParent(primary, "U")[0].getAttribute("value"))
    dic["Primary_Ua"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Ua"))
    dic["Primary_Ub"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Ub"))
    dic["Primary_Uc"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Uc"))
    dic["Primary_U0"] = t_float(x.tagParent(primary, "U")[0].getAttribute("U0"))
    secondary = x.tag("Secondary")[0]
    dic["Secondary_I"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("value"))
    dic["Secondary_Ia"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ia"))
    dic["Secondary_Ib"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ib"))
    dic["Secondary_Ic"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ic"))
    dic["Secondary_I0"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("I0"))
    dic["Secondary_U"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("value"))
    dic["Secondary_Ua"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Ua"))
    dic["Secondary_Ub"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Ub"))
    dic["Secondary_Uc"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Uc"))
    dic["Secondary_U0"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("U0"))
    dic["UPercentage"] = t_float(x.tagAttr("UPercentage"))
    return dic

def delXml2(path):
    """
    解析xml文件
    :param path: xml文件绝对路径
    :return: 读取指定元素的字典
    """
    dic = {}
    x = parseXml(path)
    bay = x.tagAttr("Bay")[0]
    dic["Bay"] = bay
    bay_type = x.tagAttr("Bay", "type")[0]
    dic["Bay_type"] = bay_type
    faultINo = x.tagAttr("FaultINo")[0]
    dic["FaultINo"] = faultINo
    faultUNo = x.tagAttr("FaultUNo")[0]
    dic["FaultUNo"] = faultUNo
    faultDNo = x.tagAttr("FaultDNo")[0]
    dic["FaultDNo"] = faultDNo
    phase = x.tagAttr("Phase")[0]
    dic["Phase_x"] = phase
    jpt = x.tagAttr("JPT")[0]
    dic["JPT"] = int(jpt)
    position = x.tagAttr("Position")[0]
    dic["Position"] = t_float(position)
    percentage = x.tagAttr("Percentage")[0]
    dic["Percentage"] = t_float(percentage)
    dic["FaultTime"] = x.tagAttr("FaultTime")[0]
    dic["SampleNo"] = int(x.tagAttr("SampleNo")[0])
    dic["RelayActTime"] = t_float(x.tagAttr("RelayActTime")[0])
    dic["BreakerJumpTime"] = t_float(x.tagAttr("BreakerJumpTime")[0])
    dic["FaultClearTime"] = t_float(x.tagAttr("FaultClearTime")[0])
    dic["CHZTime"] = t_float(x.tagAttr("CHZTime")[0])
    dic["BreakerShutTime"] = t_float(x.tagAttr("BreakerShutTime")[0])
    dic["WaveCloseTime"] = t_float(x.tagAttr("WaveClosetTime")[0])
    dic["RelayActAgainTime"] = t_float(x.tagAttr("RelayActAgainTime")[0])
    dic["BreakerJumpAgainTime"] = t_float(x.tagAttr("BreakerJumpAgainTime")[0])
    dic["FaultClearAgainTime"] = t_float(x.tagAttr("FaultClearAgainTime")[0])
    dic["Duration"] = t_float(x.tagAttr("Duration")[0])
    dic["Result_x"] = t_bool(x.tagAttr("Result")[0])
    primary = x.tag("Primary")[0]
    dic["Primary_I"] = t_float(x.tagParent(primary, "I")[0].getAttribute("value"))
    dic["Primary_Ia"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ia"))
    dic["Primary_Ib"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ib"))
    dic["Primary_Ic"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ic"))
    dic["Primary_I0"] = t_float(x.tagParent(primary, "I")[0].getAttribute("I0"))
    dic["Primary_U"] = t_float(x.tagParent(primary, "U")[0].getAttribute("value"))
    dic["Primary_Ua"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Ua"))
    dic["Primary_Ub"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Ub"))
    dic["Primary_Uc"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Uc"))
    dic["Primary_U0"] = t_float(x.tagParent(primary, "U")[0].getAttribute("U0"))
    secondary = x.tag("Secondary")[0]
    dic["Secondary_I"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("value"))
    dic["Secondary_Ia"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ia"))
    dic["Secondary_Ib"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ib"))
    dic["Secondary_Ic"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ic"))
    dic["Secondary_I0"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("I0"))
    dic["Secondary_U"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("value"))
    dic["Secondary_Ua"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Ua"))
    dic["Secondary_Ub"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Ub"))
    dic["Secondary_Uc"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Uc"))
    dic["Secondary_U0"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("U0"))
    dic["UPercentage"] = t_float(x.tagAttr("UPercentage"))

    bay = x.tagAttr("Bay")[1]
    dic["iBay"] = bay
    bay_type = x.tagAttr("Bay", "type")[1]
    dic["iBay_type"] = bay_type
    faultINo = x.tagAttr("FaultINo")[1]
    dic["iFaultINo"] = faultINo
    faultUNo = x.tagAttr("FaultUNo")[1]
    dic["iFaultUNo"] = faultUNo
    faultDNo = x.tagAttr("FaultDNo")[1]
    dic["iFaultDNo"] = faultDNo
    phase = x.tagAttr("Phase")
    l = int(len(phase)/2)
    phase = phase[l]
    dic["iPhase_x"] = phase
    jpt = x.tagAttr("JPT")[1]
    dic["iJPT"] = int(jpt)
    position = x.tagAttr("Position")[1]
    dic["iPosition"] = t_float(position)
    percentage = x.tagAttr("Percentage")[1]
    dic["iPercentage"] = t_float(percentage)
    dic["iFaultTime"] = x.tagAttr("FaultTime")[1]
    dic["iSampleNo"] = int(x.tagAttr("SampleNo")[1])
    dic["iRelayActTime"] = t_float(x.tagAttr("RelayActTime")[1])
    dic["iBreakerJumpTime"] = t_float(x.tagAttr("BreakerJumpTime")[1])
    dic["iFaultClearTime"] = t_float(x.tagAttr("FaultClearTime")[1])
    dic["iCHZTime"] = t_float(x.tagAttr("CHZTime")[1])
    dic["iBreakerShutTime"] = t_float(x.tagAttr("BreakerShutTime")[1])
    dic["iWaveCloseTime"] = t_float(x.tagAttr("WaveClosetTime")[1])
    dic["iRelayActAgainTime"] = t_float(x.tagAttr("RelayActAgainTime")[1])
    dic["iBreakerJumpAgainTime"] = t_float(x.tagAttr("BreakerJumpAgainTime")[1])
    dic["iFaultClearAgainTime"] = t_float(x.tagAttr("FaultClearAgainTime")[1])
    dic["iDuration"] = t_float(x.tagAttr("Duration")[1])
    dic["iResult_x"] = t_bool(x.tagAttr("Result")[1])
    primary = x.tag("Primary")[1]
    dic["iPrimary_I"] = t_float(x.tagParent(primary, "I")[0].getAttribute("value"))
    dic["iPrimary_Ia"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ia"))
    dic["iPrimary_Ib"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ib"))
    dic["iPrimary_Ic"] = t_float(x.tagParent(primary, "I")[0].getAttribute("Ic"))
    dic["iPrimary_I0"] = t_float(x.tagParent(primary, "I")[0].getAttribute("I0"))
    dic["iPrimary_U"] = t_float(x.tagParent(primary, "U")[0].getAttribute("value"))
    dic["iPrimary_Ua"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Ua"))
    dic["iPrimary_Ub"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Ub"))
    dic["iPrimary_Uc"] = t_float(x.tagParent(primary, "U")[0].getAttribute("Uc"))
    dic["iPrimary_U0"] = t_float(x.tagParent(primary, "U")[0].getAttribute("U0"))
    secondary = x.tag("Secondary")[1]
    dic["iSecondary_I"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("value"))
    dic["iSecondary_Ia"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ia"))
    dic["iSecondary_Ib"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ib"))
    dic["iSecondary_Ic"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("Ic"))
    dic["iSecondary_I0"] = t_float(x.tagParent(secondary, "I")[0].getAttribute("I0"))
    dic["iSecondary_U"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("value"))
    dic["iSecondary_Ua"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Ua"))
    dic["iSecondary_Ub"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Ub"))
    dic["iSecondary_Uc"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("Uc"))
    dic["iSecondary_U0"] = t_float(x.tagParent(secondary, "U")[0].getAttribute("U0"))
    dic["iUPercentage"] = t_float(x.tagAttr("UPercentage"))

    thisSide = x.tagAttr("ThisSide")
    dic["ThisSide"] = t_float(thisSide)
    remoteSide = x.tagAttr("RemoteSide")
    dic["RemoteSide"] = t_float(remoteSide)
    thisSide1 = x.tagAttr("ThisSide1")
    dic["ThisSide1"] = t_float(thisSide1)
    remoteSide1 = x.tagAttr("RemoteSide1")
    dic["RemoteSide1"] = t_float(remoteSide1)
    trans_r = x.tagAttr("TransientImpedance","R")
    dic["TransientImpedance_R"] = t_float(trans_r)
    trans_x = x.tagAttr("TransientImpedance","X")
    dic["TransientImpedance_X"] = t_float(trans_x)
    return dic

xml_path = os.path.join(MEDIA_ROOT,"xml")
XMLs = os.listdir(xml_path)

if __name__  == "__main__":
    xmls = os.listdir(xml_path)
    for xml in xmls:
        path = os.path.join(xml_path,xml)
        if len(xml) < 10:
            result = delXml2(path)
        else:
            result = delXml1(path)
        print(result)
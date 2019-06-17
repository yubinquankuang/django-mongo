import time as ti
import os

from xml.dom.minidom import parse
from fault_maintenance.settings import BASE_DIR


class expperiment:
    def idedit(self, head):
        time1 = ti.strftime('%Y%m%d%H%M%S', ti.localtime(ti.time()))
        return "%s%s" % (head, time1)





class parseXml(object):
    def __init__(self, path):
        self.path = path
        self.root = parse(self.path).documentElement

    def tag(self, name):
        return self.root.getElementsByTagName(name)

    def tagAttr(self, name, attr):
        if len(self.tag(name)) == 1:
            if self.tag(name)[0].hasAttribute(attr):
                return self.tag(name)[0].getAttribute(attr)
            else:
                return "未找到该attr"
        elif len(self.tag(name) > 1):
            attrs = []
            for tag in self.tag(name):
                if tag.hasAttribute(attr):
                    attrs.append(tag.getAttribute(attr))
                else:
                    break
            return attrs

    def tagAttrIndex(self, name, attr, index):
        if self.tag(name)[index].hasAttribute(attr):
            return self.tag(name)[index].getAttribute(attr)
        else:
            return "未找到该attr"


path = r"I:\test\vue110\data\fault\1.xml"
path = os.path.join(BASE_DIR,"data","fault","1.xml")
x = parseXml(path)
startTime = x.tagAttr("StartTime", "value")
desc1 = x.tagAttr("Bay", "value") + x.tagAttr("JPT", "desc")[:-2]
desc2 = x.tagAttrIndex("Phase","value",0) + "相故障"
desc3 = "重合失败，主保护未动作"
faultEvent = "%s %s，%s，%s"%(startTime,desc1,desc2,desc3)
chn = x.tag("Chn")
faultLocParams = []
diclist = []
dictotal = {}
for c in chn:
    name = c.getAttribute("Name")[:-1]
    dictotal[name] ={}
    if name not in diclist:
        diclist.append(name)
print(diclist)
for c in chn:
    name = c.getAttribute("Name")[:-1]
    deviceName = c.getAttribute("BayName")
    ph = c.getAttribute("Ph")
    rate = c.getAttribute("Percentage")
    before = c.getElementsByTagName("Cyc1Before")[0].getAttribute("Primary")
    after = c.getElementsByTagName("Cyc1After")[0].getAttribute("Primary")
    dictotal[name]["deviceName"] = deviceName
    if ph == "A":
        dictotal[name]["phaseA"] = {"before":before,"after":after,"rate":rate}
    if ph == "B":
        dictotal[name]["phaseB"] = {"before": before, "after": after, "rate": rate}
    if ph == "C":
        dictotal[name]["phaseC"] = {"before": before, "after": after, "rate": rate}
for i in diclist:
    faultLocParams.append(dictotal[i])

print(faultLocParams)
    # print(c.getAttribute("Name")[:-1])
    # print(c.getAttribute("BayName"))
    # print(c.getAttribute("Ph"))
    # print(c.getAttribute("Percentage"))
    # print(c.getElementsByTagName("Cyc1Before")[0].getAttribute("Primary"))
    # print(c.getElementsByTagName("Cyc1After")[0].getAttribute("Primary"))



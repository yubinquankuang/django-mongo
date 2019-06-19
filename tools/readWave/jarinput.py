import jpype
import os
import json
from djangodb.settings import BASE_DIR


class ReadXml(object):
    def __init__(self):
        self.result = ""

    def get_xml(self, path,return_dict):
        """
        调用java jar包，对入参进行rsa签名
        :param sign_raw:待签名字符串
        :return:signature:签名后的加密字符串
        """
        # 启动JVM

        jvmPath = jpype.getDefaultJVMPath()
        jar = os.path.join(BASE_DIR, "tools", "readWave","jar","readXML.jar")
        # 加载jar
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=" + jar)
        # 指定main class
        JDClass = jpype.JClass("com.lwl.main.ReadXML")
        # 创建类实例对象
        # jd = JDClass()
        # 引用jar包类中的方法 rsa_sign
        result = JDClass.read(path)
        # 关闭JVM
        # jpype.shutdownJVM()
        result = eval(result)
        return_dict["result"] = result
        return result

    def get_wave(self, path,attr,return_dict):
        """
        获取波形文件展示数据
        :param path: cfg dat dmf 文件地址
        :param attr: 信道参数
        :param return_dict: 公共返回数据
        :return:
        """
        # 启动JVM
        jvmPath = jpype.getDefaultJVMPath()
        jar = os.path.join(BASE_DIR, "tools","readWave","jar", "readXML.jar")
        # 加载jar
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=" + jar)
        # 指定main class
        JDClass = jpype.JClass("com.lwl.main.ReadXML")
        # 引用jar包类中的方法 rsa_sign，attr代表对应的通道号"[1,2,3]"
        result = JDClass.showWave(path,attr)
        result = json.loads(result)
        # result = json.dumps(result)
        # 关闭JVM
        # jpype.shutdownJVM()
        return_dict["result"] = result
        return result

    def get_dmf(self):
        jar = os.path.join(BASE_DIR, "tools", "readWave","jar","FileChooserDmfMain.jar")
        a = os.popen(jar)



if __name__ == "__main__":

    xml = ReadXml()
    # xml.get_dmf()
    # show = r"I:\test\fault_maintenance\data\fault\3628080_6X100000.xml"
    wave = r"I:\teamproject\djangodb\data\wave\3628080_comtrade"
    waveShow = xml.get_wave(wave,"[80,0]",{})
    print(waveShow)
    # show = xml.get_xml(show)
    # print(show)
    # with open("show.txt","w") as f:
    #     f.write(str(waveShow))

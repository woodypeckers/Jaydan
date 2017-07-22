# -*- coding:utf-8 -*-  
# author:Jaydan

import os
import ConfigParser



iniFileUrl="ini.ini"
conf = ConfigParser.ConfigParser()
conf.read(iniFileUrl)

def read_config_file():
    """
    sections:配置文件中[]的值
    options：每组中的键
    items：键-值得列表形式
    """
    sections = conf.sections()
    print "---conf.ini文件中的section内容有：", sections
    print "---conf.ini文件中的键内容有：", conf.options("section1")
    print "---conf.ini文件中的键-值内容有：", conf.items("section1")
    print "---section1组的processnum值为：", conf.get("section1", "processnum")

def write_config_file():
    """
    根据分组名、键名修改为新键值
    @param sections: section分组名
    @param key: 分组中的key
    @param newvalue: 需要修改后的键值
    """
    conf.set("section1", "processnum", "new3")  # 指定section和option则更新value
    conf.set("section1", "mood", "happy")  # 指定section，则增加option和value
    conf.add_section("section2")  # 添加section组
    conf.set("section2", "sex", "female")  # 给添加的section组增加option-value

    # 写回配置文件
    conf.write(open(iniFileUrl, "wb"))



if __name__ == '__main__':
    # read_config_file()
    write_config_file()
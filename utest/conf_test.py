# coding:utf-8

#Conf 类测试
import sys
sys.path.append("..")
from conf import Conf
import sys,os
import ConfigParser

#global_conf = Conf("../conf/diffPy.conf")
cf = ConfigParser.ConfigParser()  
cf.read("../conf/diffPy.conf") 
sections = cf.sections()
#print 'sections: ', sections
o = cf.options("diff_args") 
#print 'options:', o
v = cf.items("diff_args")  
print  v 
# coding:utf-8

#Conf 类测试
import sys
sys.path.append("..")
import conf
import sys,os

conf = conf.Conf("../conf/diffPy.conf")
tp1 = 'offline_env', 'online_env', 'host', 'qps'
tp2 = 'is_from_online', 'machine', 'log_path', 'filters'
for ele in tp1:
    print conf.get('diff_args', ele) 
for ele in tp2:
    if ele == 'filters':
        strlist = conf.get('dict', ele).split(',')
        for s in strlist:
            print s.strip()
    else:
        print conf.get('dict', ele) 

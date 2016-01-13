# -*- coding:utf-8 -*-
import ConfigParser

class Conf:
    '''配置文件类'''
    
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)
    def get(self, field, key):
        '''获取某个key值'''
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result
    def set(self, filed, key, value):
        '''设置某个key值'''
        try:
            self.cf.set(field, key, value)
            cf.write(open(self.path,'w'))
        except:
            return False
        return True
    def get_field(self):
        pass


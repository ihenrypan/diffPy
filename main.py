# coding:utf-8

from conf import Conf 

if __name__ == '__main__':
    global_conf = Conf('./conf/diffPy.conf')
    print global_conf.get('diff_args', 'offline_env')
    print 'main'
# -*- encoding:utf-8 -*-

__author__ = 'dumingtan'

'''
Created on Nov 22, 2011

@author: Gino
'''
import os

#配置
DIR = 'd:\cygwin'

def release(obj):
    #print(os.getcwd())
    if os.path.isfile(obj):
        return
    cmd = 'cacls ' + obj + '\*.* /g everyone:f'
    print(cmd)
    #os.system(cmd)
    p = os.popen(cmd, "w") #auto confirm
    p.write('y\n')
    subobjs = os.path.os.listdir(obj)
    if subobjs == [] :
        return
    else:
        for temp in subobjs:
            tempobj = os.path.join(obj, temp)
            release(tempobj)

if __name__ == '__main__':
    release( DIR )
    rmcmd = 'rmdir ' + DIR + ' /s /q'
    #print(rmcmd)
    os.system(rmcmd)
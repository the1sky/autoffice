# -*- encoding:utf-8 -*-

__author__ = 'dumingtan'

import config

#判断'#admaker'标识的存在性
def judgeAlreadyExist():
    exist = False
    p = open( config.HOST_FILE, 'r')
    lines = p.readlines()
    for i in range( len( lines ) ):
        lineStr = lines[i]
        if lineStr.strip() == '#admaker':
            exist = True
    p.close()
    return exist

#写配置到host文件
def writeHost(content):
    p = open( config.HOST_FILE, 'a+')
    p.write( content )
    p.close()

str = '\n\n#admaker\n'\
      '10.81.7.80 mycas.baidu.com\n'\
      '10.81.20.120 admaker.baidu.com\n'\
      '10.81.12.166 caspq.baidu.com\n'\
      '10.81.54.65 beidoulocal.baidu.com\n'\
      '10.81.22.89 kehutest.baidu.com\n'\
      '10.81.14.247 caslt.baidu.com\n'\
      '10.81.14.247 ult.baidu.com\n'\
      '172.22.230.215 chuangyi-test.baidu.com'

if not judgeAlreadyExist():
    writeHost( str )

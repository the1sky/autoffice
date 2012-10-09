# -*- encoding:utf-8 -*-

__author__ = 'dumingtan'

import os, stat
from stat import *

def changeMod():
    cmd = 'cacls ' + HOST_DIR + '*.* /G everyone:f'
    print(cmd)
    print( oct(os.stat( HOST_DIR )[ST_MODE])[-3:] )
    p = os.popen(cmd, "w")
    p.write( 'y\n' )

def writeHost(content):
    p = open( HOST_FILE, 'a+')
    p.write( content )
    p.close()

#配置
HOST_DIR = 'c:\\windows\\system32\\drivers\\etc\\'
HOST_FILE = HOST_DIR + 'hosts'

#优酷
youkuStr = '\n\n#youku \n' \
           '127.0.0.1 atm.youku.com\n' \
           '127.0.0.1 Fvid.atm.youku.com\n' \
           '127.0.0.1 html.atm.youku.com\n' \
           '127.0.0.1 valb.atm.youku.com\n' \
           '127.0.0.1 valf.atm.youku.com\n' \
           '127.0.0.1 valo.atm.youku.com\n' \
           '127.0.0.1 valp.atm.youku.com\n' \
           '127.0.0.1 lstat.youku.com\n' \
           '127.0.0.1 speed.lstat.youku.com\n' \
           '127.0.0.1 urchin.lstat.youku.com\n' \
           '127.0.0.1 stat.youku.com'

#执行
changeMod()
writeHost( youkuStr )



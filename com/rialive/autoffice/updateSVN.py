# -*- coding: gbk -*

__author__ = 'dumingtan'

import subprocess
from log import Log

def run(path):
    x = subprocess.call( 'svn cleanup ' + path )
    subprocess.call( 'svn up ' + path )
    log.log( path + '�Ѹ���' )

    #��ʱ��ⲻ�����º��״̬

#����
LOG_FILE = 'c:\\log\\autoffice.log'

#ִ��
log = Log()
log.config( LOG_FILE )

run( 'C:\\projs\\python\\autoffice' )
run( 'C:\\projs\\admaker' )

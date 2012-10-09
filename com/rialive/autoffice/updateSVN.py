# -*- coding: gbk -*

__author__ = 'dumingtan'

import subprocess
from log import Log

def run(path):
    x = subprocess.call( 'svn cleanup ' + path )
    subprocess.call( 'svn up ' + path )
    log.log( path + '已更新' )

    #暂时检测不到更新后的状态

#配置
LOG_FILE = 'c:\\log\\autoffice.log'

#执行
log = Log()
log.config( LOG_FILE )

run( 'C:\\projs\\python\\autoffice' )
run( 'C:\\projs\\admaker' )

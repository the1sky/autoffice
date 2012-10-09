# -*- encoding:GBK -*-

__author__ = 'dumingtan_nant'

import time

class Log:
    _logfile = ''
    _msg = ''

    def config(self,logfile):
        if logfile != '':
            self._logfile = logfile
        else:
            self._logfile = 'run.log'
    def log(self,msg):
        now = time.time()
        strtime = str( time.localtime( now )[0] ) + '-' +\
                  str( time.localtime( now )[1] ) + '-' +\
                  str( time.localtime( now )[2] ) + ' ' +\
                  str( time.localtime( now )[3] ) + ':' +\
                  str( time.localtime( now )[4] ) + ':' +\
                  str( time.localtime( now )[5] )

        _msg = strtime + ' ' + msg + '\n'
        try:
            logfilehandle = open( self._logfile, 'a+' )
            logfilehandle.write( _msg )
            logfilehandle.close()
            print( self._logfile )
        except:
            exit( 0 )
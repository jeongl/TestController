import os
import time
from subprocess import *
import sys
import signal
import ctypes
import datetime

class TestRunner (object):
        def __init__ (self):
            self.test_handle=object
            self.test_status=object
            print "You have initialized the TestRunner"
        def start_test(self, ip, port, directory):
            print "running test"
            self.test_status_IP=ip
            self.test_status_PORT=port
            self.test_status_DIRECTORY=directory            
            time_date = " "+str(datetime.datetime.now()).split(".")[0].replace(':','.')+'.xml'
            SQUISH_DIR = "c:\\Users\\UserName\\Documents\\squish-5.0.0-qt47x-win64-msvc9\\squish-5.0.0-qt47x-win64-msvc9\\bin\\"
            SAVE_DIR="xml2.1,c:\\Users\UserName\\Documents\\results\\"+ip+time_date
            if ip=="UserDefinedApp":
                self.test_handle = Popen([directory],stdout=PIPE,stderr=PIPE)
            else:
                self.test_handle = Popen([SQUISH_DIR+"squishrunner.exe","--host", ip, "--port", port, "--testsuite", directory, "--reportgen",SAVE_DIR],shell=True)
            self.test_status=self.test_handle
        def check_testStatus(self):
            return self.test_status.poll()
        def stop_Test(self):
            Popen("taskkill /F /T /PID %i"%self.test_status.pid , shell=True)
        def gatherINFO(self,input, i):
            if input=="True":
                print str(i)+" -- "+time.strftime("%c")+" -- Running---  "+self.test_status_IP,self.test_status_PORT,self.test_status_DIRECTORY
            else:
                print str(i)+" -- "+time.strftime("%c")+" -- Failed--    "+self.test_status_IP,self.test_status_PORT,self.test_status_DIRECTORY
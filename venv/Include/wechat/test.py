# -*- coding:utf-8 -*-
# Author: zww
import _thread

def print_time( threadName):
   print(threadName)

try:
   _thread.start_new_thread( print_time, ("Thread-1", ) )
   _thread.start_new_thread( print_time, ("Thread-2", ) )
except:
   print ("Error: 无法启动线程")

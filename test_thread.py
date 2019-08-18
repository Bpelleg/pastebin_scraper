# -*- coding: utf-8 -*-

import threading 
import time


class TestThread(threading.Thread):

    
    def __init__(self,name="Test thread"):
        super(TestThread, self).__init__()
        self.stop_event=threading.Event() 
        
    def run(self):

        self.running()
        
        i=0
               
        
        while not self.stopped() :
            time.sleep(4)
            i=i+1
            print(i)
            
            
        print("stopped")
        return 0
        
        
    
    def stop(self):
        self.stop_event.set()
        
    def stopped(self):
        return self.stop_event.is_set()
    
    def running(self):
        self.stop_event.clear()
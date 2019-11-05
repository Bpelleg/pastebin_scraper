#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:37:13 2019

@author: pellegrini
"""

# -*- coding: utf-8 -*-

import params
import threading 
import pastebin_scraper
import time
import stats
import json

class ScrapingThread(threading.Thread):

    
    def __init__(self,regexps,name="Scraping thread",  path=params.DEFAULT_PATH):
        super(ScrapingThread, self).__init__()
        self.stop_event=threading.Event() 
        self.root_path=path
        self.name=name
        self.scraper=pastebin_scraper.PastebinScraper()
        self.stats=stats.Stats()
        print("initialize thread")
        for re in regexps :
            self.scraper.add_re(re)
        
    def run(self):
        print("running !")
        self.running()
        
        i=0
               
        try :
            while not self.stopped() :
                i=i+1
                print(i)
                """for re in self.scraper.get_rexps():
                print(re)"""
                
                results=self.scraper.combined_scraping()
                self.store_results(results)
                self.update_stats(results)
                time.sleep(params.WAITING_TIME)
            
        except Exception as e:
            print(e,e.with_traceback)
        finally :
            pass
        
        print("stopped")
        return self.get_stats()
        
        
    
    def stop(self):
        self.stop_event.set()
        
    def stopped(self):
        return self.stop_event.is_set()
    
    def running(self):
        self.stop_event.clear()
        
    def store_results(self, results):
        import time;
        with open('result'+str(time.time())+'.json', 'w') as f:
            json.dump(results, f)
        
        
    def get_stats(self):
        return self.stats
    
    def update_stats(self,results):
        self.stats.update(len(results["matches"]),len(results["patterns"]))
        
        
        
if __name__ == '__main__':
    regexps=["[A-Z][a-z][0-9]\s","[a-zA-Z0-9.!#$%&*+=?^_~-]+@[a-zA-Z0-9]{1,63}\.[a-zA-Z0-9]{1,63}[\.]{0,1}[a-zA-Z0-9]{0,63}[:|]{1}\S{1,63}","<\S{1,10}>"]
    thread=ScrapingThread(regexps)
    thread.start() 
    thread.join()


"""
import json

with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)

# elsewhere...

with open('my_dict.json') as f:
    my_dict = json.load(f)
"""
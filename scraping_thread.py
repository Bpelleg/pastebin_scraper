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
import csv

class ScrapingThread(threading.Thread):

    
    def __init__(self,regexps,name="Scraping thread",  path=params.DEFAULT_PATH):
        super(ScrapingThread, self).__init__()
        self.stop_event=threading.Event() 
        self.root_path=path
        self.name=name
        self.scraper=pastebin_scraper.PastebinScraper()
        self.stats=stats.Stats()
        print("initialize thread")
        #self.load_regexps_file(file)
        for re in regexps :
            self.scraper.add_re(re)
        
    def run(self):
        print("running !")
        self.running()
 
        try :
            while not self.stopped() :
                results=self.scraper.combined_scraping()
                self.store_results(results)
                self.update_stats(results)
                print(self.get_stats().serialize())
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
        timestamp=time.time()
        with open('./results/matches'+str(timestamp)+'.json', 'w') as f:
            json.dump(results["matches"], f)
        self.store_patterns(results["patterns"],timestamp)
        
    def store_patterns(self,patterns,timestamp):
        formatted_patterns=[]
        for key,values in patterns.items():      
            for value in values:
                dictionary=dict()
                dictionary["timestamp"]=timestamp
                dictionary["regexp"]=key
                dictionary["pattern"]=value
                formatted_patterns.append(dictionary)
            
        with open('./results/patterns'+str(timestamp)+'.csv', 'w') as f:
            writer=csv.DictWriter(f,fieldnames=['timestamp','regexp','pattern'])
            writer.writeheader()
            for data in formatted_patterns:
                writer.writerow(data)
        
            
        
        
    def get_stats(self):
        return self.stats
    
    def update_stats(self,results):
        if len(results["matches"])>-1 and len(results["patterns"])>-1:
            self.stats.update(len(results["matches"]),len(results["patterns"]))
        
    def load_regexps_file(self,filename):
        """ TODO implement 
        for re in regexps :
            self.scraper.add_re(re)
        """
        
if __name__ == '__main__':
    regexps=["[A-Z][a-z][0-9]\s","[a-zA-Z0-9.!#$%&*+=?^_~-]+@[a-zA-Z0-9]{1,63}\.[a-zA-Z0-9]{1,63}[\.]{0,1}[a-zA-Z0-9]{0,63}[:|]{1}\S{1,63}","<\S{1,10}>"]
    thread=ScrapingThread(regexps)
    #thread=ScrapingThread("./regexps.txt")
    thread.start() 
    thread.join(2000)
    thread.stop()


"""
import json

with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)

# elsewhere...

with open('my_dict.json') as f:
    my_dict = json.load(f)
"""
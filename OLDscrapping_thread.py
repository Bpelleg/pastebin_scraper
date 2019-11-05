# -*- coding: utf-8 -*-

import params
import threading 
import pastebin_scraper
import time
import stats


class ScrapingThread(threading.Thread):
    """ Thread chargé de lancer les méthodes de scraping 
    et  de stocker les résultats """
    
    def __init__(self,res,name="Scraping thread", path=params.DEFAULT_PATH):
        super(ScrapingThread, self).__init__()
        self.root_path=path
        self.name=name
        self.stop_event=threading.Event()
        self.scraper=pastebin_scraper.PastebinScraper()
        self.stats=stats.Stats()
        
        for re in res :
            self.scraper.add_re(re)
        
        
    def run(self):
        """TODO implement"""
        
        self.running()
        
        self.init_stats()
        
        while not self.stopped() :
            results=self.scraper.combined_scraping()
            self.store_results(results)
            self.update_stats(results)
            time.sleep(params.WAITING_TIME)
            
            
            
        return self.stats()
        
        
    
    def stop(self):
        self.stop_event.set()
        
    def stopped(self):
        return self.stop_event.is_set()
    
    def running(self):
        self.stop_event.clear()
    
    def store_results(self):
        """TODO implement
            store results in files in a specific folder
        """
        
    def stats(self):
        return self.stats.serialize()
    
    def update_stats(self,results):
        self.stats.update(results["matches"].len(),results["patterns"].len())
       
        

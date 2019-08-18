# -*- coding: utf-8 -*-

import params
import threading 
import pastebin_scraper


class ScrapingThread(threading.Thread):
    """ Thread chargé de lancer les méthodes de scraping 
    et  de stocker les résultats """
    
    def __init__(self,res,name="Scraping thread", path=params.DEFAULT_PATH):
        super(ScrapingThread, self).__init__()
        self.root_path=path
        self.name=name
        self.stop_event=threading.Event()
        self.scraper=pastebin_scraper.PastebinScraper()
        
        for re in res :
            self.scraper.add_re(re)
        
        
    def run(self):
        """TODO implement"""
        
        self.running()
        
        self.init_stats()
        
        while not self.stopped() :
            res_patterns=scraper.scrape_find_patterns()
            time.sleep(params.WAITING_TIME)            
            scraped_pastes=scraper.get_scraped_pastes()
            time.sleep(params.WAITING_TIME)
            self.stats()
            
            
            
        return self.stats()
        
        
    
    def stop(self):
        self.stop_event.set()
        
    def stopped(self):
        return self.stop_event.is_set()
    
    def running(self):
        self.stop_event.clear()
    
    def save_patterns(self):
        """TODO implement 
        save and update stats"""
        
        
    def save_pastes(self):
        """TODO implement
        save and update stats"""
        
    def stats(self):
        """TODO implement)
    stats: 
            - nb patterns
            - nb pastes
            - nb de "round" de scraping
            - temps d'exécution"""
    
    def update_stats(self):
        """TODO implement"""
        
    def init_stats(self):
        """TODO implement"""
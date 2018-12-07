#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:34:32 2018

@author: pellegrini

Pastebin scraping utility methods
"""


from pastebin_wrapper import Pastebin
import requests
import time
import re

class PastebinScraper(object):
    def __init__(self):
        self.pastebin=Pastebin()
        self.rexps=[]
        self.scrape_limit='50'
        
        
    def scrape(self,lang='none'):
        """Return a list of paste objects created from the most recent pastes
            Do not call this several times without delay
           :returns: a list of Paste objects
           :rtype: list
        """
        if lang=='none':
            parameter = {'limit': self.scrape_limit}
        else:
            parameter = {'limit': self.scrape_limit,'lang':lang}
            
        #print(str(parameter))
        response = requests.get('https://scrape.pastebin.com/api_scraping.php',params=parameter)

        return response.json()

    def scrape_raw(self,lang='none'):
        """ Return the raw texts of the most recents pastes
        """
        pastes_json=self.scrape(lang);
        time.sleep(1)
        raw_pastes=[]
        
        for paste in pastes_json:
            key=paste['key']
            raw_paste=self.scrape_paste(key)
            raw_pastes.append(raw_paste)
            time.sleep(1)
            
        return raw_pastes
            
        
       
    def scrape_paste(self,paste_id):
        """Return raw string of given paste_id.
           :type paste_id: string
           :param paste_id: The ID key of the paste
           :returns: the text of the paste
           :rtype: string
        """
        parameter = {'i': paste_id}
        r = requests.get('https://scrape.pastebin.com/api_scrape_item.php',params=parameter)
        return r.text
    
    def scrape_metadata(self,paste_id):
        """scrape_paste_metadata(paste_key)
            Return a dictionary containing the metadata of the paste.
            :param paste_key: the unique key of the paste you want to scrape
            :type paste_key: string
            :returns: dictionary containing the metadata of the paste
            :rtype: dictionary
        """
        parameter = {'i': paste_id}
        r = requests.get('https://scrape.pastebin.com/api_scrape_item_meta.php', params=parameter)
        return r.json()
    
    def add_re(self,rexp):
        """ add a regular expressions to the list of regular expressions
            that are used while scraping (with regExp)
        """
        crexp=re.compile(rexp)
        self.rexps.append(crexp)
        
    def clear_res(self):
        """ Removes all regexps
        """
        self.rexps.clear()
        
    def pop_re(self):
        """ remove the last regexp added and returns it
        """
        return self.rexps.pop()
    
    
    def find_matching_pastes(self,raw_pastes):
        """ find the pastes in the input list that contains on of the patterns
            at least once
        """

        matching_pastes=[]
        
        for rp in raw_pastes :
            for rex in self.rexps :
                if rex.search(rp) :
                    matching_pastes.append(rp)
                    break      
        return matching_pastes  
 
    
    def scrape_matching(self,lang='none'):
        """ Return the raw texts of the most recents pastes that contains 
            one of the patterns
        """
        raw_pastes=self.scrape_raw(lang)
        
        return self.find_matching_pastes(raw_pastes)  

 
    def find_all_patterns(self, raw_pastes):
        """ find all the patterns in the input pastes
            returns a dictionary (regexp -> list of results)
        """
        
        patterns=dict()
        
        for rex in self.rexps :
            patterns[rex.pattern]=[]
            for rp in raw_pastes :
                (patterns[rex.pattern]).extend(rex.findall(rp))
                
        return patterns
            
        
        
        
        
    
    def scrape_find_patterns(self, lang='none'):
        """ Find all the patterns in the most recent pastes
        """      
        raw_pastes=self.scrape_raw(lang)
        
        return self.find_all_patterns(raw_pastes)
        
    
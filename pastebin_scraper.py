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

class PastebinScraper(object):
    def __init__(self):
        self.pastebin=Pastebin()
        
        
    def scrape(self,lang='none'):
        """Return a list of paste objects created from the most recent pastes
            Do not call this several times without delay
           :returns: a list of Paste objects
           :rtype: list
        """
        if lang=='none':
            parameter = {'limit': '50'}
        else:
            parameter = {'limit': '50','lang':lang}
            
        #print(str(parameter))
        response = requests.get('https://scrape.pastebin.com/api_scraping.php',params=parameter)

        return response.json()

    def scrape_raw(self,lang='none'):
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
        parameter = {'i': paste_key}
        r = requests.get('https://scrape.pastebin.com/api_scrape_item_meta.php', params=parameter)
        return r.json()
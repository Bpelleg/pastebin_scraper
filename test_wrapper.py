#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:34:24 2018

@author: pellegrini
Test module for the pastebin api wraper
"""
"""
import sys
sys.path.insert(0, '/path/to/application/app/folder')
"""


from pastebin_wrapper import Pastebin

p=Pastebin()
print(p.api_dev_key,p.api_user_key)


pastes=p.get_trending_raw_pastes()
  
text="Hi, I'm testing the API"
#url=p.create_paste(text,1,"Test API")
#print(url)
    
paste=p.get_raw_paste("YqyeULEe")

#meta=p.scrape_paste_metadata("YqyeULEe")
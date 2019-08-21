#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:14:17 2018

@author: pellegrini
test module for the pastebin scraping module
"""

"""
import sys
sys.path.insert(0, '/path/to/application/app/folder')
"""
from pastebin_scraper import PastebinScraper
import time

email_regexp="[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
pwd_leak_regexp="[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*[:|]{1}\S{1,63}"

#https://www.regextester.com/19
simple_mail_regexp="[a-zA-Z0-9.!#$%&*+=?^_~-]+@[a-zA-Z0-9]{1,63}\.[a-zA-Z0-9]{1,63}[\.]{0,1}[a-zA-Z0-9]{0,63}"
simple_pwd_leak_regexp="[a-zA-Z0-9.!#$%&*+=?^_~-]+@[a-zA-Z0-9]{1,63}\.[a-zA-Z0-9]{1,63}[\.]{0,1}[a-zA-Z0-9]{0,63}[:|]{1}\S{1,63}"



scraper=PastebinScraper()

#scraped_pastes=scraper.scrape_raw();
#time.sleep(10)
#scraped_pastes_java=scraper.scrape_raw('java');

scraper.add_re(email_regexp)
scraper.add_re("<\S{1,10}>")
scraper.add_re("[a-zA-Z][0-9]a-zA-Z][0-9]")
scraper.add_re(pwd_leak_regexp)
scraper.add_re(simple_mail_regexp)
scraper.add_re(simple_pwd_leak_regexp)

res_patterns=scraper.scrape_find_patterns()

time.sleep(10)

scraped_pastes=scraper.get_scraped_pastes()
time.sleep(10)
res_match=scraper.scrape_matching()

time.sleep(10)

dic=scraper.combined_scraping()


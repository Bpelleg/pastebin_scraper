#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:31:41 2018

@author: pellegrini
inspired by https://github.com/Mikts/pbwrap

Wrapper module for the pastebin API
"""

import re
import requests

class Pastebin(object):
    def __init__(self):
        self.load_api_key()
        self.authenticate()
        
        
        
    def load_api_key(self):
        api_file=open('../api_key.txt','r')
        self.api_key=api_file.readline()
        self.api_key=re.sub(r'[^a-zA-Z0-9]','',self.api_key)
        api_file.close()
        
    def authenticate(self):
        creds_file=open('../creds.txt','r')
        
        username=creds_file.readline()
        username=re.sub(r'[^a-zA-Z0-9]','',username)
        
        password=creds_file.readline()
        password=re.sub(r'[^a-zA-Z0-9]','',password)
        
        creds_file.close()
        
        
        data = {'api_dev_key': self.api_key,
                'api_user_name': username,
                'api_user_password': password}
        

        response = requests.post('https://pastebin.com/api/api_login.php', data)

        self.api_user_key = response.text

        return self.api_user_key
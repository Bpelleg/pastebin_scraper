#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:31:41 2018

@author: pellegrini
inspired by https://github.com/Mikts/pbwrap

Wrapper module for the pastebin API
"""

import re
import os
import requests
import formatter
import constants

class Pastebin(object):
    def __init__(self):
        self.load_api_key()
        self.authenticate()
        
        
        
    def load_api_key(self):
        api_file=open('../api_key.txt','r')
        self.api_dev_key=api_file.readline()
        self.api_dev_key=re.sub(r'[^a-zA-Z0-9]','',self.api_dev_key)
        api_file.close()
        
    def authenticate(self):
        creds_file=open('../creds.txt','r')
        
        username=creds_file.readline()
        username=re.sub(r'[^a-zA-Z0-9]','',username)
        
        password=creds_file.readline()
        password=re.sub(r'[^a-zA-Z0-9]','',password)
        
        creds_file.close()
        
        
        data = {'api_dev_key': self.api_dev_key,
                'api_user_name': username,
                'api_user_password': password}
        

        response = requests.post('https://pastebin.com/api/api_login.php', data)

        self.api_user_key = response.text

        return self.api_user_key
    
    def get_user_details(self):
        """Return user details in a dictionary.
           Can only be user after authenticating with get_user_id(username, password).
           :returns: dictionary containing user details
           :rtype: dictionary
        """
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key}

        response = requests.post('https://pastebin.com/api/api_post.php', data)

        return formatter.user_from_xml(response.text)
    
    def get_trending(self):
        """Return a list of paste objects created from the most trending pastes
           :returns: a list of Paste objects
           :rtype: list
        """
        data = {
            'api_dev_key': self.api_dev_key,
            'api_option': constants.API_OPTIONS['TREND']}

        response = requests.post('https://pastebin.com/api/api_post.php', data)

        return formatter.paste_list_from_xml(response.text)
    
    def get_trending_raw_pastes(self):
        trending_raw_pastes=[]
        for paste_elt in self.get_trending():
            raw_paste=self.get_raw_paste(paste_elt.key)
            trending_raw_pastes.append(raw_paste)
        return trending_raw_pastes
    
    
    def create_paste(self, api_paste_code, api_paste_private=0, api_paste_name=None, api_paste_expire_date=None,
                     api_paste_format=None):
        """Create a new paste if succesfull return it's url.
           :type api_paste_code: string
           :param api_paste_code: your paste text
           :type api_paste_private: int
           :param api_paste_private: valid values=0(public),1(unlisted),2(private)
           :type api_paste_name: string
           :param api_user_name: your paste name
           :type api_paste_expire_date: string
           :param api_paste_expire_date: check documentation for valid values
           :type api_paste_format: string
           :param api_paste_format: check documentation for valid values
           :returns: new paste url
           :rtype: string
        """
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_paste_code': api_paste_code,
                'api_paste_private': api_paste_private,
                'api_paste_name': api_paste_name,
                'api_paste_expire_date': api_paste_expire_date,
                'api_paste_format': api_paste_format,
                'api_option': constants.API_OPTIONS['PASTE']}

        # Filter data and remove dictionary None keys.
        filtered_data = {k: v for k, v in data.items() if v is not None}

        r = requests.post('https://pastebin.com/api/api_post.php', filtered_data)

        return r.text

    def create_paste_from_file(self, filepath, api_paste_private=0, api_paste_name=None,
                               api_paste_expire_date=None, api_paste_format=None):
        """Create a new paste from file if succesfull return it's url.
            :type filepath: string
            :param filepath: the path of the file
            :type api_paste_private: int
            :param api_paste_private: valid values=0(public),1(unlisted),2(private)
            :type api_paste_name: string
            :param api_user_name: your paste name
            :type api_paste_expire_date: string
            :param api_paste_expire_date: check documentation for valid values
            :type api_paste_format: string
            :param api_paste_format: check documentation for valid values
            :returns: new paste url
            :rtype: string
            """
        if os.path.exists(filepath):
            api_paste_code = open(filepath).read()
            return self.create_paste(api_paste_code, api_paste_private, api_paste_name,
                                     api_paste_expire_date, api_paste_format)
        print('File not found')
        return None

    
    @staticmethod
    def get_archive():
        """Return archive paste link list.Archive contains 25 most recent pastes.
           :returns: a list of url strings
           :rtype: list
        """
        r = requests.get('https://pastebin.com/archive')

        return formatter.archive_url_format(r.text)


    @staticmethod
    def get_raw_paste(paste_id):
        """Return raw string of given paste_id.
           get_raw_paste(pasted_id)
           :type paste_id: string
           :param paste_id: The ID key of the paste
           :returns: the text of the paste
           :rtype: string
        """
        r = requests.get('https://pastebin.com/raw/' + paste_id)
        return r.text
    
    @staticmethod
    def get_paste(paste_id):
        """Return raw string of given paste_id.
           get_raw_paste(pasted_id)
           :type paste_id: string
           :param paste_id: The ID key of the paste
           :returns: the text of the paste
           :rtype: string
        """
        r = requests.get('https://pastebin.com/api/api_raw.php' + paste_id)
        return r.text
    
    
    @staticmethod
    def scrape_paste_metadata(paste_key):
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
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:34:24 2018

@author: pellegrini
Test module for the pastebin api wraper
"""

from pastebin_wrapper import Pastebin

p=Pastebin()
print(p.api_key,p.api_user_key)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stats():
    
    
    def __init__(self):
        self.loops=0;
        self.matching=0;
        self.patterns=0;
        
        
    def update(self, nb_m, nb_p):
        self.loops=self.loops+1
        self.matching=self.matching+nb_m
        self.patterns=self.patterns+nb_p
        
    def serialize(self):
        serialized='LOOPS='+str(self.loops)+'\nNB MATCHES='+str(self.matching)+'\nNB PATTERNS='+str(self.patterns)
        return serialized

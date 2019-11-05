#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple web server in Flask for launching, managing the scraper 
as well as fetching its results

@author: pellegrini
"""
from flask import Flask
from scraping_thread import ScrapingThread

thread=ScrapingThread([])

def create_app():
    
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello World! TODO should return the available commands"


    @app.route('/launch')
    def launch():
        """stop an already existing thread then create a new one each time"""
        global thread
        if(thread.running):
            return "already running"
        regexps=["[A-Z][a-z][0-9]\s","[a-zA-Z0-9.!#$%&*+=?^_~-]+@[a-zA-Z0-9]{1,63}\.[a-zA-Z0-9]{1,63}[\.]{0,1}[a-zA-Z0-9]{0,63}[:|]{1}\S{1,63}","<\S{1,10}>"]
        thread=ScrapingThread(regexps)
        thread.start()
        return "TODO dev this part : launching the scraping if not running yet"
    
    
    @app.route('/stop')
    def stop():      
        thread.stop()
        stats=thread.get_stats()
        return stats.serialize()


    @app.route('/stats')
    def stats():
        return "TODO dev this part : get stats about the scraping process and its results"


    @app.route('/patterns')
    def get_patterns():
        return "TODO dev this part : get the current patterns as text that can be edited and then posted back "


    @app.route('/postpatterns')
    def post_patterns():
        return "TODO dev this part : upload patterns via a form//use only when the scraper isn't running"



    @app.route('/results')
    def get_matching():
        return "TODO dev this part : returns a list of the result files with their IDs"


    @app.route('/results/<id>')
    def get_results(name):
        return "TODO dev this part : return results as JSON for the given result file ID {}!".format(id)

    app.debug=True
    app.run()

if __name__ == '__main__':
    create_app()    

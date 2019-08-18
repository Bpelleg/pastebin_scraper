#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple web server in Flask for launching, managing the scraper 
as well as fetching its results

@author: pellegrini
"""

from flask import Flask
from test_thread import TestThread
app = Flask(__name__)

thread=TestThread()


@app.route('/')
def index():
    return "Hello World! TODO should return the available commands"


@app.route('/launch')
def launch():
    """create a new thread each time"""
    thread.start()
    return "TODO dev this part : launching the scraping if not running yet"


@app.route('/stop')
def stop():
    thread.stop()
    return "TODO dev this part : stop the scraper"


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
    return "TODO dev this part : returns a list of the patterns in use with their IDs"


@app.route('/results/<id>')
def hello_name(name):
    return "TODO dev this part : return results as JSON for the given pattern ID {}!".format(id)





if __name__ == '__main__':
    app.run()
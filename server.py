#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple web server in Flask for launching, managing the scraper 
as well as fetching its results

@author: pellegrini
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World! TODO should return the available commands"


@app.route('/launch')
def launch():
    return "TODO dev this part : launching the scraping if not running yet"


@app.route('/stop')
def stop():
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
def get_results(name):
    return "TODO dev this part : return results as JSON for the given pattern ID {}!".format(id)


@app.route('/postresult', methods=['GET', 'POST'])
def post_result():
    return "TODO dev this part : add result to the DB thanks to a POST request"


if __name__ == '__main__':
    app.run()

#coding=utf-8
import flask_helpers as a
import os
import schedule
import time

from pymongo import MongoClient
db = MongoClient('mongodb://master:1234@ds129374.mlab.com:29374/kylestinder')

import urllib
from flask_cors import CORS

from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/matches')
def match():
    tinder_matches = a.matches()
    print(tinder_matches)
    return jsonify(tinder_matches)



@app.route('/setstatus', methods=['POST'])
def like(): 


    
    data = request.get_json()
    url = data['url']
    status = data['status']

    if status == 'like':
        images = db.kylestinder.images
        image_data = {
            'url': url
        }

        result = images.insert(image_data)
        
        
        return jsonify(
            status = 200,
            msg = 'done'
        )
        
    else:

        images = db.kylestinder.badimages
        image_data = {
            'url': url
        }

        result = images.insert(image_data)
        
        
        return jsonify(
            status = 200,
            msg = 'done'
        )
        



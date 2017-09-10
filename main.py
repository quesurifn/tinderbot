import flask_helpers as a
import cv2
import numpy as np

from pymongo import MongoClient
db = MongoClient('mongodb://master:1234@ds129374.mlab.com:29374/kylestinder')

import urllib
import pymongo

from flask_cors import CORS

from flask import Flask, jsonify, request
app = Flask(__name__)
CORS(app)

@app.route('/')
def open():
    faceCascade = cv2.CascadeClassifier('./helpers/config/classify.xml')
    image = a.url_to_image('http://facefacts.scot/images/science/Q2_high_health_f.jpg')
    cv2.imshow("Image", image)
    cv2.waitKey(0)


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
        



# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:11:21 2019

@author: ekans
"""

import Airtelgeolocator
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class geolocation(Resource):
    def get(self, lat, long):
        coordinates = (lat,long)
        return{'data': Airtelgeolocator.reverseGeocode(coordinates)}


    
api.add_resource(geolocation, '/Geolocation/<lat>/<long>')

if __name__ == 'main':
    app.run()
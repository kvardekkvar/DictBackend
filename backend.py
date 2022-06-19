# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:58:21 2022

@author: beelzebub
"""

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful

from flask import Flask
from flask import request
from flask_restx import Api, Resource, reqparse, Namespace, fields

import xml.dom.minidom

app = Flask(__name__)
api = Api(app)


print('You are not authorized to make changes in dict. \n Headers recieved: ')




def upload_xml(d):
        
        f = open("/var/www/html/dic/xml/dictest.xml",'wb')
        f.write(d)
        f.close
        
class Dic(Resource):
    @api.doc(description="Test method. Have fun.", params={}, namespace='XML')
    def get(self):
        return "Api running", 200
        
    @api.doc(security='apikey', description="Method for updating dictionary. Takes xml file as body.", params={'authorization': 'An authorization token'}, responses = {401:"Not authorized", 400: "Body is not an XML file", 200:"XML dictionary was successfully updated"})
    def post(self):
        if request.headers.get('authorization') != 'BlimpEaterDict':
            return 'You are not authorized to make changes in dict.', 401
        data =  request.get_data()  
        try: 
            xml.dom.minidom.parseString(data)
        except xml.parsers.expat.ExpatError:
            return "Your request body is not a valid XML file", 400
            
        upload_xml(data)
        
        return 'XML dictionary was successfully updated', 200
    
api.add_resource(Dic, "/dic/xml")


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5001)
    app.run()


#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request

from pymongo import MongoClient
import pymongo as pm


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://asciienjoyers:Flanki123@cluster0.fbab8.mongodb.net/test"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['SubsEnjoyers']

db = get_database()

app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/add_user/',  methods=['GET', 'POST'])
def incrementer():
    json_user_email_password = request.get_json()
    print(json_user_email_password['email'])
    print(json_user_email_password['login'])
    print(json_user_email_password['password'])
    return "Email Password Correct"


@app.route('/subscribtion/', methods=['GET', 'POST'])
def get_subscribtion_from_firm():
    """
    This request gets name of the firm from json and return json file with subscribtion types

    """
    subscribition_json = request.get_json()
    firm_name = subscribition_json['firm_name']
    # get_associated_subscribtion()
    return "Possible subscribtion"

@app.route('/auth/', methods=['GET', 'POST'])
def check_authentication():
    """
    Function return True or False, depends on login and password is stored in database
    :return:
    json: #TODO specify
    """
    user_password = request.get_json()
    print(user_password)
    # search users database for key login and check correctness of password
    # Authenticate_User_Password
    return "Possible subscribtion"

@app.route('/add_sub/', methods=['GET', 'POST'])
def add_subscriprtion():
    """
    Function return True or False, depends on login and password is stored in database
    :return:
    json: #TODO specify
    """
    global db
    subscribed_services = db['subscribed_services']
    user_data = request.get_json()
    services_array = subscribed_services.find({"email": user_data["email"]})['services']
    services_array = services_array + user_data['services']
    subscribed_services.inventory.updateOne( 
        {"email": user_data["email"]},\
        {
            {"$set": {"services": services_array}}
        }
    )

    return "Subscription addded"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request

from pymongo import MongoClient
import pymongo as pm

import pandas as pd

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

@app.route('/get_subscriptions/', methods=['GET', 'POST'])
def get_user_subscribtions():
    user_email = request.get_json()["email"]
    user_services_collection = db["subscribed_services"]
    users_details = user_services_collection.find_one({"email": user_email})["services"]
    # user_services = pd.DataFrame(users_details)
    # user_services = user_services[user_services["email"] == user_email]["services"]
    # print("USER SERVICES KURWA")
    # print(user_services.head())
    list_of_user_services = list()

    for i, service in enumerate(users_details):

        service_dict = dict()
        service_dict["id"] = i
        service_dict["company"] = service["name"]
        service_dict["amount"] = service["price"]
        service_dict["period"] = db["plans_descriptions"].find_one({"name": service["subs_model"]})["payment_interval"]
        service_dict["link"] = db["available_services"].find_one({"name": service["name"]})["link"]
        
        list_of_user_services.append(service_dict)

    return {"lista": list_of_user_services}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
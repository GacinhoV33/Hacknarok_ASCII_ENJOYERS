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


def get_user_subscribtions():
    users = db["users"]
    users_details = collection.find()
    df = pd.DataFrame(users_details)
    print(df.head())
    # for user in users_details:
    #     print(user["email"])

get_user_subscribtions()
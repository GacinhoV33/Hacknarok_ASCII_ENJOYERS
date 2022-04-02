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

collection = db["users"]
users_details = collection.find()

print(users_details)
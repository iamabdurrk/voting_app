from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["voting_db"]
votes_collection = db["votes"]

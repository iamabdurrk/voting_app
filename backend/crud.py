from .database import votes_collection
from .models import Vote

def submit_vote(vote: Vote):
    votes_collection.insert_one(vote.dict())

def get_results():
    results = votes_collection.aggregate([
        {"$group": {"_id": "$candidate", "count": {"$sum": 1}}}
    ])
    return {r["_id"]: r["count"] for r in results}

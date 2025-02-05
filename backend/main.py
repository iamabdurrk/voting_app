from fastapi import FastAPI
from .models import Vote
from .crud import submit_vote, get_results

app = FastAPI()

@app.post("/vote/")
def vote(vote: Vote):
    submit_vote(vote)
    return {"message": "Vote submitted!"}

@app.get("/results/")
def results():
    return get_results()

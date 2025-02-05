from pydantic import BaseModel

class Vote(BaseModel):
    candidate: str

from pydantic import BaseModel

class RequestChange(BaseModel):
    patch: str
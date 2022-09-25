from pydantic import BaseModel

class Role(BaseModel):
    id: str
    permissions: str
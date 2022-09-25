from ast import List
from pydantic import BaseModel

class TechnicalData(BaseModel):
    roles: List[str]
    permissions: List[str]
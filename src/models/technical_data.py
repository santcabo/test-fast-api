from typing import List
from pydantic import BaseModel
from .role import Role

class TechnicalData(BaseModel):
    roles: List[Role]
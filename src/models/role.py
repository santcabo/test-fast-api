from typing import List
from pydantic import BaseModel

class PermissionType(BaseModel):
    READ: bool
    WRITE: bool

class Role(BaseModel):
    id: str
    permissions: List[PermissionType]
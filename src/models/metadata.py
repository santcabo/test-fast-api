from pydantic import BaseModel

class Metadata(BaseModel):
    name: str
    owner: str
    configuration_manager: str
from pydantic import BaseModel

from .metadata import Metadata
from .technical_data import TechnicalData

class ApplicationConfiguration(BaseModel):
    metadata: Metadata
    technical_data: TechnicalData
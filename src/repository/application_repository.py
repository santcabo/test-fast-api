from typing import List
from pydantic import BaseModel
from .application_item import ApplicationItem

class ApplicationRepository(BaseModel):
    _memory: List[ApplicationItem] = []
        
    def get_applications(self):      
        return self._memory
    
    def add_application(self, application_item: ApplicationItem):
        self._memory.append(application_item)
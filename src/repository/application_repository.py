from typing import List
from pydantic import BaseModel
from .application_item import ApplicationItem

class ApplicationRepository(BaseModel):
    _memory: List[ApplicationItem] = []
    _repo: dict[str, List[ApplicationItem]] = dict()
        
    def get_applications(self):      
        return self._repo
    
    def get_application_updates(self, application_id: str):      
        return self._repo[application_id]
    
    def create_application(self, application_item: ApplicationItem):
        self._repo[application_item.guid] = []
        self._repo[application_item.guid].append(application_item)
    
    def add_application_update(self, application_update: ApplicationItem):
        self._repo[application_update.guid].append(application_update)
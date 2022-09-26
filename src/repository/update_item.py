from time import time
from uuid import uuid4
from ..models.application_configuration import ApplicationConfiguration

class UpdateItem():
    guid: str
    application_id: str
    request_date: str
    processed_date: str | None
    request_change: str
    status: str
    
    def __init__(self, application_id: str, request_change: str):
        self.guid = str(uuid4())
        self.application_id = application_id
        self.request_date = round(time())
        self.processed_date = None
        self.request_change = request_change
        self.status = 'pending'
    
    def approve(self):
        self.processed_date = round(time())      
        self.status = 'approved'
        
    def approve(self):
        self.processed_date = round(time())      
        self.status = 'rejected'
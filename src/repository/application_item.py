from time import time
from uuid import uuid4
from ..models.application_configuration import ApplicationConfiguration

class ApplicationItem():
    guid: str
    request_date: str
    application_configuration: ApplicationConfiguration | None
    approval_date: str | None
    requested_change: str | None
    status: str
    
    def __init__(self, application_configuration: ApplicationConfiguration = None, requested_change: str = None):
        self.guid = str(uuid4())
        self.request_date = round(time())
        self.application_configuration = application_configuration
        
        if application_configuration:
            self.approval_date = self.request_date
            self.requested_change = None
            self.status = 'approved'
            return
        
        if requested_change:
            self.approval_date = None
            self.requested_change = requested_change
            self.status = 'pending'
            return
    
    def approve(self):
        self.approval_date = round(time())
        self.status = 'approved'
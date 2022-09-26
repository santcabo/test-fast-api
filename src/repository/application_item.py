from time import time
from uuid import uuid4
from ..models.application_configuration import ApplicationConfiguration

class ApplicationItem():
    guid: str
    creation_date: str
    application_configuration: ApplicationConfiguration
    
    def __init__(self, application_configuration: ApplicationConfiguration):
        self.guid = str(uuid4())
        self.creation_date = round(time())
        self.application_configuration = application_configuration
        
        if application_configuration:
            self.approval_date = self.creation_date
            self.requested_change = None
            self.status = 'approved'
            return
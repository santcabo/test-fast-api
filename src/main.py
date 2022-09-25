from fastapi import FastAPI

from .models.application_configuration import ApplicationConfiguration
from .repository.application_repository import ApplicationRepository, ApplicationItem	

repo = ApplicationRepository()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Mission Control Center (MCC)"}

@app.get("/applications/")
def read_applications():
    return {"applications": repo.get_applications()}

@app.get("/application/{application_id}")
def read_application(application_id: int):
    return {"application_id": application_id}


@app.post("/application/")
async def create_application(application: ApplicationConfiguration):
    app = ApplicationItem(application)
    repo.add_application(app)
    return {"result:": "Success", "application_id": app.guid, "application_configuration": app.application_configuration}
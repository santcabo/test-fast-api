from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
import jsonpatch

from .models.application_configuration import ApplicationConfiguration
from .models.request_change import RequestChange
from .repository.application_repository import ApplicationRepository, ApplicationItem
from .repository.update_item import UpdateItem


repo = ApplicationRepository()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Mission Control Center (MCC)"}


@app.get("/applications/")
def read_applications():
    return {"applications": repo.get_applications()}


@app.get("/application/{application_id}")
def read_application(application_id: str):
    return repo.get_application(application_id)


@app.post("/application/", status_code=status.HTTP_200_OK)
async def create_application(application: ApplicationConfiguration):
    app = ApplicationItem(application)
    repo.create_application(app)
    return {"result:": "Success", "application_id": app.guid, "application": app}


@app.get("/update/{update_id}")
async def read_update(update_id: str):
    update = repo.get_update(update_id)
    return {"update": update}
    
    
@app.get("/application/{application_id}/updates/")    
async def read_application_updates(application_id: str):
    updates = repo.get_application_updates(application_id)
    return {"updates": updates}


@app.post("/application/{application_id}/update/", status_code=status.HTTP_200_OK)
async def create_application(application_id: str, request_change: RequestChange):
    update = UpdateItem(application_id, request_change.patch)
    print(update)
    repo.create_update(update)
    return {"result:": "Success", "update_id": update.guid, "update": update}
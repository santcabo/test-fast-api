from fastapi import FastAPI

from .models.application_configuration import ApplicationConfiguration


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Mission Control Center (MCC)"}


@app.get("/application/{application_id}")
def read_application(application_id: int):
    return {"application_id": application_id}


@app.post("/application/")
async def create_application(application: ApplicationConfiguration):
    return {"result:": "Success", "application": application}
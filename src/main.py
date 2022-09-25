from fastapi import FastAPI
from pydantic import BaseModel

from .models.metadata import Metadata
# from .models.technical_data import TechnicalData


class Application(BaseModel):
    metadata: Metadata
    technical_data: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Mission Control Center (MCC)"}


@app.get("/application/{application_id}")
def read_application(application_id: int):
    return {"application_id": application_id}


@app.post("/application/")
async def create_application(application: Application):
    return {"result:": "Success", "application": application}

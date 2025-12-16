from fastapi import FastAPI,HTTPException,Path
from pydantic import BaseModel,EmailStr,Field
from typing import Annotated,Literal
from typing_extensions import Literal
import json

app=FastAPI()

class Patient(BaseModel):
    patient_id:str
    name:str
    age:int
    gender:Literal['male','female']
    height:int




def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'Hello World'}

@app.get("/about")
def about():
   return {'message':'My name is Khushwant'}

@app.get('/view')
def view():
    data=load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error':'patient is not found'}

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str=Path(...,description='ID OF THE PATIENT IN THE DB',example='P001')):
    return {"patient_id": patient_id}

@app.post("/patient/{patient_id}")
def update_patient(
    patient_id: str = Path(..., example="P001"),
    patient: Patient = ...
):
    return {"id": patient_id, **patient.dict()}
    





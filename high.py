from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Literal
import json

app = FastAPI()

class Patient(BaseModel):
    patient_id: str
    name: str
    age: int
    gender: Literal['Male', 'Female']
    height: int

FILE_NAME = "patient.json"

def load_data():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., example="P001")):
    data = load_data()
    for patient in data:
        if patient["patient_id"] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail="Patient not found")


@app.post("/patient")
def add_patient(patient: Patient):
    data = load_data()

    for p in data:
        if p["patient_id"] == patient.patient_id:
            raise HTTPException(status_code=400, detail="Patient already exists")

    data.append(patient.dict())
    save_data(data)
    return {"message": "Patient added successfully", "data": patient}


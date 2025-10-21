from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
app = FastAPI(title="Simple FastAPI App", version="1.0.0")


data = [{"name": "Sam Larry", "age": 20, "track": "AI Developer"},
        {"name": "Bahubili", "age": 21, "track": "Backend developer"},
        {"name": "John Doe", "age": 22, "track": "Frontend Developer"}]


class Item(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Perpetual"})
    age: int = Field(..., json_schema_extra={"example": 25})
    track: str = Field(..., json_schema_extra={
                       "example": "Fullstack developer"})


@app.get("/", description="This endpoint just returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}


@app.get("/get-data")
def get_data():
    return data


@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"Message": "Data Received", "Data": data}


@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)

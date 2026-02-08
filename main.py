from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def read_root():
    return {"Message": "Hello world vikas"}

@app.get('/about')
def read_about():
    return {"Message": "Hello about"}

@app.get('/about/{name}')
def read_about_name(name:str, age:Optional[int]=None):
    return {"Message": f"Hello {name} and you are {age} years old"}


class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create student") 
def create_student(student: Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll":student.roll
    }
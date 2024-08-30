from fastapi import FastAPI, HTTPException
from models import Toy
from utils import move_toy, turn_toy

app = FastAPI()

class ToyDetails:
    details = {}

toy_db = ToyDetails()

@app.post("/place/")
def place(toy: Toy):
    toy_db.details = toy.dict()
    return toy_db.details

@app.post("/move/")
def move():
    if not toy_db.details:
        return
    move_toy(toy_db.details)

@app.post("/left/")
def turn_left():
    if not toy_db.details:
        return
    turn_toy(toy_db.details, "left")

@app.post("/right/")
def turn_right():
    if not toy_db.details:
        return
    turn_toy(toy_db.details, "right")

@app.get("/report/")
def report():
    return toy_db.details
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Mentorama"}

class Resp(BaseModel):
    valor1: int
    valor2: int
    operação: str

@app.post("/outrarota")
async def outrarota(resp: Resp):
    return resp

# 11/19/26
# Alex Vu
# api.py

from fastapi import FastAPI
from parser import getInfo

app = FastAPI()

@app.get("/getentries")
async def getentries():
    return getInfo()

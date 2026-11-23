# 11/19/26
# Alex Vu
# api.py

import utils.session
from fastapi import FastAPI
from parser import getFirstN, getByClass
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # restrict this in a real project
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getentries/")
async def getentries(n : int | None, category : str | None):
    if type(n) == int and n >= 0:
        if category:
            return getByClass(n, category)
        return getFirstN(n)
        

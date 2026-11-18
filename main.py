# 11/19/26
# Alex Vu
# api.py

from fastapi import FastAPI
from parser import getFirstN, getByClass

app = FastAPI()

@app.get("/getentries/")
async def getentries(n : int | None, category : str | None):
    if n:
        if category:
            return getByClass(n, category)
        return getFirstN(n)
    else:
        return "Invalid query structure!"

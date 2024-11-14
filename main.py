from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from typing import Union

# FastAPI instance
app = FastAPI()

# Input Schema
class CalculatorRequest(BaseModel):
    input1: float
    input2: float


#Function Start
# Addition
def add(addInput1: float, addInput2: float) -> float:
    return addInput1 + addInput2

#Subtract
def subtract(subInput1: float, subInput2: float) -> float:
    return subInput1 - subInput2

#Multiplication
def multiply(mulInput1: float, mulInput2: float) -> float:
    return mulInput1 * mulInput2

#Division
def division(divInput1: float, divInput2: float) -> float:
    return divInput1 / divInput2

#Function End

# API Link Start
# Health check API
@app.get("/healthcheck")
async def health_check():
    return {"status": "Application Running"}

#Addition API
@app.post("/add")
async def add_endpofloat(request: CalculatorRequest):
    if request is None:
        return HTTPException(status_code=404, detail="Input Not Valid")
    return {"result": add(request.input1, request.input2)}

# Subtraction API
@app.post("/subtract")
async def subtract_endpofloat(request: CalculatorRequest):
    if request is None:
        return HTTPException(status_code=404, detail="Input Not Valid")
    return {"result": subtract(request.input1, request.input2)}

# Multiplication API
@app.post("/multiply")
async def multiply_endpofloat(request: CalculatorRequest):
    if request is None:
        return HTTPException(status_code=404, detail="Input Not Valid")
    return {"result": multiply(request.input1, request.input2)}

# Division API
@app.post("/division")
async def divide_endpofloat(request: CalculatorRequest):
    if request is None:
        return HTTPException(status_code=404, detail="Input Not Valid")
    return {"result": division(request.input1, request.input2)}

#API Link End
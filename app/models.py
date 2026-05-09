from fastapi import FastAPI
from pydantic import BaseModel
# Expense Model
class Expense(BaseModel):
    title: str
    amount: float
    category: str
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
from bson import ObjectId
from .database import expense_collection
from .models import Expense

app = FastAPI(title="Expense Tracker API")

# Home Route
@app.get("/")
async def home():
    return {"message": "Expense Tracker API Running"}


# Add Expense
@app.post("/expenses")
async def add_expense(expense: Expense):

    result = await expense_collection.insert_one(expense.dict())

    return {
        "message": "Expense added",
        "id": str(result.inserted_id)
    }


# Get Expenses
@app.get("/expenses")
async def get_expenses():

    expenses = []

    async for expense in expense_collection.find():

        expense["_id"] = str(expense["_id"])
        expenses.append(expense)

    return expenses


# Update Expense
@app.put("/expenses/{expense_id}")
async def update_expense(expense_id: str, expense: Expense):

    await expense_collection.update_one(
        {"_id": ObjectId(expense_id)},
        {"$set": expense.dict()}
    )

    return {"message": "Expense updated"}


# Delete Expense
@app.delete("/expenses/{expense_id}")
async def delete_expense(expense_id: str):

    await expense_collection.delete_one(
        {"_id": ObjectId(expense_id)}
    )

    return {"message": "Expense deleted"}


# Upload CSV
@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    data = df.to_dict(orient="records")

    if data:
        await expense_collection.insert_many(data)

    return {
        "message": f"{len(data)} expenses uploaded"
    }
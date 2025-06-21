# app/routes/transactions.py

from fastapi import APIRouter
import pandas as pd

router = APIRouter()

# Sample transaction data (Replace with actual data)
transaction_data = pd.read_csv("data/transactions.csv")

@router.get("/transactions/report")
async def get_transactions_report(date: str = None, class_type: str = None, payment_type: str = None):
    """
    Retrieve filtered transaction data based on date, class, and payment type.
    """
    filtered_data = transaction_data
    
    if date:
        filtered_data = filtered_data[filtered_data['date'] == date]
    if class_type:
        filtered_data = filtered_data[filtered_data['class_type'] == class_type]
    if payment_type:
        filtered_data = filtered_data[filtered_data['payment_type'] == payment_type]

    return filtered_data.head(10)  # Returning first 10 rows as a demo

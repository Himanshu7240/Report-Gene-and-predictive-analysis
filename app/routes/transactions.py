# app/routes/transactions.py

from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()

@router.get("/transactions/report")
async def get_transactions_report(
    date: str = Query(None, description="Transaction date in YYYY-MM-DD format"),
    class_type: str = Query(None, description="Class type (e.g., Science, Arts)"),
    payment_type: str = Query(None, description="Payment method (e.g., Cash, Card)")
):
    """
    Retrieve filtered transaction data based on date, class, and payment type.
    """
    # Load transaction data on each request (optional: cache or use a DB in production)
    transaction_data = pd.read_csv("data/transactions.csv")

    # Apply filters
    filtered_data = transaction_data.copy()
    if date:
        filtered_data = filtered_data[filtered_data['date'] == date]
    if class_type:
        filtered_data = filtered_data[filtered_data['class_type'] == class_type]
    if payment_type:
        filtered_data = filtered_data[filtered_data['payment_type'] == payment_type]

    # Return as list of dictionaries to ensure JSON serializability
    return filtered_data.head(10).to_dict(orient="records")

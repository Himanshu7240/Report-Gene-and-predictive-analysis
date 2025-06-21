import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Function to preprocess student data
def preprocess_student_data(df):
    """Preprocess student data for performance forecasting"""
    # Example of how data could be preprocessed (you can adapt this for your own data)
    df['attendance'] = df['attendance'] / 100  # Normalize attendance to a range of 0-1
    df['behavior'] = df['behavior'] / 100      # Normalize behavior to a range of 0-1
    return df

# 1. Student Performance Forecasting Model (Random Forest Regressor)
def train_student_performance_model(df):
    """
    Train a Random Forest Regressor to predict student performance (score).
    """
    # Preprocessing data
    df = preprocess_student_data(df)
    
    # Define features (attendance, behavior) and target (score)
    X = df[['attendance', 'behavior']]
    y = df['score']

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest Regressor
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X_train, y_train)

    # Predict on the test data
    y_pred = rf_regressor.predict(X_test)

    # Calculate performance (Mean Squared Error)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print(f"Student Performance Model - RMSE: {rmse}")
    
    return rf_regressor

# 2. Dropout Risk Prediction Model (Random Forest Classifier)
def train_dropout_risk_model(df):
    """
    Train a Random Forest Classifier to predict dropout risk (0 = no, 1 = yes).
    """
    # Preprocessing data
    df = preprocess_student_data(df)

    # Define features and target (binary: dropout = 1, no dropout = 0)
    X = df[['attendance', 'behavior', 'score']]
    y = df['dropout']  # Assuming 'dropout' column exists in the dataset

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Predict on the test data
    y_pred = rf_classifier.predict(X_test)

    # Calculate performance (Accuracy)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Dropout Risk Prediction Model - Accuracy: {accuracy}")

    return rf_classifier

# 3. School Revenue Projection Model (Linear Regression)
def train_school_revenue_projection(df):
    """
    Train a Linear Regression model to forecast school revenue based on historical data.
    """
    # Assuming 'date' and 'revenue' columns exist in the dataset
    df['ds'] = pd.to_datetime(df['date'])  # 'ds' is the column name Prophet expects for date
    df['y'] = df['revenue']  # 'y' is the column name Prophet expects for the target variable

    # Feature engineering: Create numerical features for Linear Regression (e.g., month, year)
    df['month'] = df['ds'].dt.month
    df['year'] = df['ds'].dt.year

    # Define features and target
    X = df[['year', 'month']]  # Features: Year and Month
    y = df['y']  # Target: Revenue

    # Initialize the Linear Regression model
    linear_model = LinearRegression()
    linear_model.fit(X, y)

    # Make future predictions (for next 12 months)
    future_dates = pd.date_range(start=df['ds'].max(), periods=13, freq='M')[1:]  # Next 12 months
    future_df = pd.DataFrame({'ds': future_dates, 'month': future_dates.month, 'year': future_dates.year})

    # Predict the revenue for future dates
    future_df['predicted_revenue'] = linear_model.predict(future_df[['year', 'month']])

    # Plot the forecast
    plt.figure(figsize=(10, 6))
    plt.plot(df['ds'], df['y'], label='Historical Revenue')
    plt.plot(future_df['ds'], future_df['predicted_revenue'], label='Predicted Revenue', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.title('School Revenue Forecast')
    plt.legend()
    plt.show()

    print(f"School Revenue Projection - Forecast for the next 12 months:\n{future_df[['ds', 'predicted_revenue']]}")
    
    return linear_model

# Example Usage
if __name__ == "__main__":
    # Load sample data (ensure you replace this with actual data)
    student_data = pd.read_csv("data/students.csv")
    student_data['dropout'] = np.random.choice([0, 1], size=len(student_data))  # For demo purposes, creating a random 'dropout' column

    # 1. Train the student performance model (Random Forest Regressor)
    student_model = train_student_performance_model(student_data)
    
    # 2. Train the dropout risk prediction model (Random Forest Classifier)
    dropout_model = train_dropout_risk_model(student_data)
    
    # 3. Train the school revenue projection model (Linear Regression)
    revenue_data = pd.read_csv("data/transactions.csv")  # Assuming this file has date and revenue columns
    revenue_model = train_school_revenue_projection(revenue_data)

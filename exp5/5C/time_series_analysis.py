"""
Experiment 5C: Time Series Analysis

AIM:
To perform Time Series Analysis on diabetes-related datasets, identifying trends, seasonality, and
patterns in glucose levels over time.

NOTE ON THE DATA:
The lab manual uses 'diabetes9.csv' (768 records) with a seasonal period of 30. That file is not
part of this repository, so the analysis runs on the UCI Diabetes glucose series (100 records)
available here, with the decomposition period reduced to 12 so that several full cycles still fit
within the series. The dataset carries no timestamp column, so the record index is treated as the
time axis - the ordering is sequential, not calendar-based.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

SEASONAL_PERIOD = 12
MOVING_AVERAGE_WINDOW = 7

def run_experiment_5c():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load the Dataset
    diabetes_data = pd.read_csv(os.path.join(base_dir, "uci_diabetes.csv"))

    # Check and Preview the Data
    print(diabetes_data.head())

    # 1. Plot Time Series Data
    plt.figure(figsize=(12, 5))
    plt.plot(diabetes_data['Glucose'], label="Glucose Level", color='blue')
    plt.xlabel("Index")
    plt.ylabel("Glucose Level")
    plt.title("Time Series of Glucose Levels")
    plt.legend()
    plt.savefig(os.path.join(base_dir, "glucose_time_series.png"), bbox_inches='tight')
    plt.close()
    print("\nSaved time series plot to 'glucose_time_series.png'")

    # 2. Decompose Time Series into Trend, Seasonality, and Residuals
    decomposition = seasonal_decompose(diabetes_data['Glucose'], model='additive',
                                       period=SEASONAL_PERIOD)
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))
    decomposition.trend.plot(ax=axes[0], title="Trend Component")
    decomposition.seasonal.plot(ax=axes[1], title="Seasonal Component")
    decomposition.resid.plot(ax=axes[2], title="Residual Component")
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, "seasonal_decomposition.png"), bbox_inches='tight')
    plt.close()
    print("Saved decomposition plot to 'seasonal_decomposition.png'")

    # 3. Apply Moving Average for Smoothing
    diabetes_data['Glucose_MA'] = diabetes_data['Glucose'].rolling(
        window=MOVING_AVERAGE_WINDOW).mean()
    plt.figure(figsize=(12, 5))
    plt.plot(diabetes_data['Glucose'], label="Original", alpha=0.5)
    plt.plot(diabetes_data['Glucose_MA'],
             label=f"{MOVING_AVERAGE_WINDOW}-point Moving Average", color='red')
    plt.legend()
    plt.title("Moving Average Smoothing")
    plt.savefig(os.path.join(base_dir, "moving_average.png"), bbox_inches='tight')
    plt.close()
    print("Saved moving average plot to 'moving_average.png'")

    # 4. Build ARIMA Model for Forecasting
    train_size = int(len(diabetes_data) * 0.8)
    train = diabetes_data['Glucose'][:train_size]
    test = diabetes_data['Glucose'][train_size:]

    model = ARIMA(train, order=(5, 1, 0))  # ARIMA(p,d,q) where p=5, d=1, q=0
    fitted_model = model.fit()

    # Forecast Future Glucose Levels
    forecast = fitted_model.forecast(steps=len(test))

    # Plot Forecast vs Actual Data
    plt.figure(figsize=(12, 5))
    plt.plot(range(len(test)), test, label="Actual", color="blue")
    plt.plot(range(len(test)), forecast, label="Forecast", color="red")
    plt.xlabel("Index")
    plt.ylabel("Glucose Level")
    plt.title("ARIMA Model Forecasting")
    plt.legend()
    plt.savefig(os.path.join(base_dir, "arima_forecast.png"), bbox_inches='tight')
    plt.close()
    print("Saved ARIMA forecast plot to 'arima_forecast.png'")

if __name__ == "__main__":
    run_experiment_5c()

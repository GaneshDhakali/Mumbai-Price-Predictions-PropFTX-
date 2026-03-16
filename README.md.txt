# Mumbai Property Price Prediction – EDA, ML & FastAPI

## Overview

This project focuses on analysing real estate pricing trends using the provided Mumbai property dataset.  
The solution prioritises structured data understanding, logical preprocessing, and creation of a simple yet functional ML inference pipeline.

---

## Dataset Understanding

The dataset represents aggregated property pricing trends across different Mumbai localities and time periods.

Key attributes include:

- **Locality** –  area name  
- **Quarter** – Time period  
- **Price Range** – Interval showing minimum and maximum pricing levels  
- **Average Price** – Mean price (used it as prediction target)  
- **Q-o-Q Growth** – Quarter-on-quarter pricing change  
- **City / Type / Growth Type** – Additional categorical indicators  

The data reflects locality-level market behaviour rather than individual property listings.

---

## Data Cleaning & Preparation

Applied Several preprocessing steps to improve dataset usability:

- Removed the Records corresponding to Hyderabad due to structural column inconsistencies and low representation (~2% of data).
- Dropped Columns with extremely high missing values.
- Removed the rows missing the target variable (Average Price).
- Excluded Non-informative columns with no variability.
- Encoded the Categorical features such as Locality and Quarter using one-hot encoding.

---

## Target Variable Selection

Selected the **Average Price** column as the prediction target because it provides a single continuous numerical representation of locality-level pricing trends, making it suitable for regression modelling.

---

## Exploratory Data Analysis Insights

- Property pricing shows significant variation across localities..
- Feature importance analysis highlights locality and time period as key predictors.

---

## Model

Used a **Random Forest Regressor** as a baseline model due to its ability to capture non-linear relationships and handle high-dimensional encoded categorical features.

### Evaluation Metric

The model achieved an RMSE of approximately **3744**, indicating moderate prediction error given the variability in real estate pricing patterns.

---

## FastAPI Prediction Service

Implemented a minimal FastAPI application to serve predictions.

### 
-------
### API FORMAT

## Running the FastAPI Service

### 1. Install Dependencies

pip install -r Dependencies

### 2. Start the API Server

uvicorn main: app --reload

### 3. Test the Endpoint

Open the following URL in your browser:

http://127.0.0.1:8000/docs


Use the interactive Swagger UI to test the `/predict` endpoint by providing values for **Locality** and **Quarter**.

### Example Input

```json
{
  "Locality": "90 Feet Road",
  "Quarter": "Jul-Sep 2024"
}

Note: Ensure that the input values match the categorical values seen during model training (e.g., valid locality names and quarter formats).

### Example output
{
  "predicted_price": 22500.34
}

## Note on Input Features

The assignment description included example prediction inputs such as `area_sqft`, `bedrooms`, `bathrooms`, and `furnishing`.  
However, these structural property-level attributes were not available in the provided dataset.

Since the dataset represents aggregated locality-level pricing trends rather than individual property listings, the prediction interface was adapted to use the available predictors — **Locality** and **Quarter**.

### END POINT
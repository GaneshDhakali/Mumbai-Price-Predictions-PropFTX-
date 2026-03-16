from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

#Loading trained model
model = pickle.load(open("price_model.pkl","rb"))

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    # Align columns with training features
    model_features = model.feature_names_in_
    df = df.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(df)

    return {"predicted_price": float(prediction[0])}











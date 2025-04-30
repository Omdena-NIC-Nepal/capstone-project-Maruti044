import streamlit as st
import pandas as pd
from models.classification.random_forest import load_random_forest_model, predict_zone
from models.regression.linear_regression import predict_impact

def show_predictions():
    st.title("🌍 Climate Change Predictions")

    df = pd.read_csv("data/processed_climate_data.csv")

    if not {'Temperature', 'Precipitation', 'Season'}.issubset(df.columns):
        st.error("Missing required columns in data.")
        return

    X = df[['Temperature', 'Precipitation', 'Season']]

    st.subheader("1️⃣ Climate Zone Prediction")
    try:
        model = load_random_forest_model()
        predicted_zones = predict_zone(model, X)
        st.write("Predicted Zones (sample):")
        st.dataframe(predicted_zones[:10])
    except Exception as e:
        st.error(f"Error loading model: {e}")

    st.subheader("2️⃣ Climate Impact Prediction")
    try:
        impact_prediction = predict_impact(X)
        st.write("Impact Predictions (sample):")
        st.dataframe(impact_prediction[:10])
    except Exception as e:
        st.error(f"Error predicting impact: {e}")

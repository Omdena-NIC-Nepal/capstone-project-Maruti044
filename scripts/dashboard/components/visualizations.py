import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def plot_temperature_trends(region):
    df = pd.read_csv("data/processed/temperature_trends.csv")
    if region != "All":
        df = df[df['Region'] == region]
    fig, ax = plt.subplots()
    for reg in df['Region'].unique():
        sub = df[df['Region'] == reg]
        ax.plot(sub['Year'], sub['Temperature'], label=reg)
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    st.pyplot(fig)

def plot_precipitation_changes(region):
    df = pd.read_csv("data/processed/precipitation_trends.csv")
    if region != "All":
        df = df[df['Region'] == region]
    fig, ax = plt.subplots()
    for reg in df['Region'].unique():
        sub = df[df['Region'] == reg]
        ax.plot(sub['Year'], sub['Precipitation'], label=reg)
    ax.set_xlabel("Year")
    ax.set_ylabel("Precipitation (mm)")
    ax.legend()
    st.pyplot(fig)

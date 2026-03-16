import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("XGBR.pkl", "rb"))

st.set_page_config(page_title="California Housing Price Predictor")

st.title("🏠 California Housing Price Prediction")
st.write("Enter housing details to predict the price.")

# Input fields
medinc = st.number_input("Median Income", min_value=0.0)
houseage = st.number_input("House Age", min_value=0.0)
averooms = st.number_input("Average Rooms", min_value=0.0)
avebedrms = st.number_input("Average Bedrooms", min_value=0.0)
population = st.number_input("Population", min_value=0.0)
aveoccup = st.number_input("Average Occupancy", min_value=0.0)
latitude = st.number_input("Latitude", value=34.0)
longitude = st.number_input("Longitude", value=-118.0)

# Prediction button
if st.button("Predict House Price"):

    input_data = np.array([[medinc, houseage, averooms, avebedrms,
                            population, aveoccup, latitude, longitude]])

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ${prediction[0]*100000:.2f}")

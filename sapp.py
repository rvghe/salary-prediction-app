import streamlit as st
import joblib
import numpy as np

# Load saved model
model = joblib.load("salary_model.pkl")

st.title("Salary Prediction App")

# User input
experience = st.number_input("Enter Years of Experience", min_value=0.0)

if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")


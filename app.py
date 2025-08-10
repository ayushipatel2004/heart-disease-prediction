import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title("Heart stroke prediction by ayushii<3")
st.markdown("Provide the following details to predict the heart stroke")

age = st.slider("Age", 18, 100, 25, 1)
sex = st.selectbox("Sex", ["Male", "Female"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure", 60, 200, 120, 1)
cholesterol = st.number_input("Cholesterol", 100, 500, 200, 1)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST" , "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 200, 150, 1)
exercise_angina = st.selectbox("Exercise Angina", ["Yes", "No"])
oldpeak = st.slider("Old Peak", 0.0, 10.0, 1.0, 0.1)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])


if st.button("Predict"):
    raw_input = {
        "Age": age,
        "Sex_"+ sex : 1,
        "chest_pain_type"+chest_pain : 1,
        "resting_blood_pressure":resting_bp,
        "cholesterol": cholesterol,
        "fasting_blood_sugar": fasting_bs,
        "resting_ecg"+resting_ecg : 1,
        "max_heart_rate": max_hr,
        "exercise_angina"+ exercise_angina : 1,
        "oldpeak": oldpeak,
        "st_slope"+st_slope: 1
    }
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Heart stroke is possible")
    else:
        st.success("Heart stroke is not possible")


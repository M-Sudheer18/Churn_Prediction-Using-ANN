import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# model 
model = tf.keras.models.load_model("ann_model.h5")
sc = joblib.load("scaler.pkl")


st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Customer Churn Prediction")
st.markdown("Enter the customer's details below to predict whether they are likely to leave the bank.")

st.divider()

# Customer Details
credit_score = st.slider(
    "Credit Score",
    min_value=350,
    max_value=850,
    value=650
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

gender = 1 if gender == "Male" else 0

age = st.slider(
    "Age",
    min_value=18,
    max_value=92,
    value=35
)

tenure = st.slider(
    "Tenure (Years)",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Account Balance",
    min_value=0.0,
    max_value=250898.09,
    value=75000.0
)

num_products = st.selectbox(
    "Number of Products",
    [1, 2, 3, 4]
)

has_card = st.selectbox(
    "Has Credit Card",
    ["Yes", "No"]
)
has_card = 1 if has_card == "Yes" else 0


active_member = st.selectbox(
    "Is Active Member",
    ["Yes", "No"]
)
active_member = 1 if active_member == "Yes" else 0


estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=11.58,
    max_value=199992.48,
    value=100000.0
)



# Button 
if st.button("Predict", use_container_width=True):
    
    input_data = np.array([[
    credit_score,
    gender,
    age,
    tenure,
    balance,
    num_products,
    has_card,
    active_member,
    estimated_salary
    ]])

    input_data = sc.transform(input_data)
    prediction = model.predict(input_data)

    st.write(f"Prediction Probability: {prediction[0][0]:.4f}")

    if prediction[0][0] > 0.5:
        st.error("⚠️ Customer is likely to leave the bank.")
    else:
        st.success("✅ Customer is likely to stay with the bank.")





















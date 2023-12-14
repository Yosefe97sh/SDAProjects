import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the XGBoost model
xgb_model = pickle.load(open("xgb", "rb"))

# Load the label encoder
label_encoder = pickle.load(open("encoder", "rb"))

def predict_churn(features):
    # Convert features to a DataFrame
    features_df = pd.DataFrame([features], columns=["satisfaction_level", "last_evaluation", "number_project", "average_montly_hours", "time_spend_company", "Work_accident", "promotion_last_5years", "Departments", "salary"])

    # One-hot encode the categorical features
    departments_encoded = pd.get_dummies(features_df["Departments"], prefix="Departments")
    salary_encoded = pd.get_dummies(features_df["salary"], prefix="salary")

    # Concatenate the encoded features
    encoded_features = pd.concat([departments_encoded, salary_encoded], axis=1)

    # Drop the original categorical columns
    features_df.drop(["Departments", "salary"], axis=1, inplace=True)

    # Concatenate the original features with the encoded ones
    features_df = pd.concat([features_df, encoded_features], axis=1)

    # Make predictions using the XGBoost model
    predicted_churn = xgb_model.predict(features_df.values)

    return predicted_churn[0]

def main():
    st.set_page_config(
        page_title="Customer Churn Prediction App",
        page_icon="📉",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title("Customer Churn Prediction 📉")

    st.write("### Enter customer details:")
    satisfaction_level = st.slider("Satisfaction Level", min_value=0.0, max_value=1.0, value=0.5)
    last_evaluation = st.slider("Last Evaluation", min_value=0.0, max_value=1.0, value=0.5)
    number_project = st.slider("Number of Projects", min_value=1, max_value=10, value=5)
    average_monthly_hours = st.slider("Average Monthly Hours", min_value=0, max_value=500, value=250)
    time_spend_company = st.slider("Time Spent in Company", min_value=1, max_value=10, value=3)
    work_accident = st.checkbox("Work Accident")
    promotion_last_5years = st.checkbox("Promotion in Last 5 Years")
    department = st.selectbox("Department", ["sales", "accounting", "hr", "technical", "support", "management", "IT", "product_mng", "marketing", "RandD"])
    salary = st.selectbox("Salary", ["low", "medium", "high"])

    # Convert boolean values to integers
    work_accident = int(work_accident)
    promotion_last_5years = int(promotion_last_5years)

    features = [satisfaction_level, last_evaluation, number_project, average_monthly_hours, time_spend_company, work_accident, promotion_last_5years, department, salary]

    # Create features_df for visualizations
    features_df = pd.DataFrame([features], columns=["satisfaction_level", "last_evaluation", "number_project", "average_montly_hours", "time_spend_company", "Work_accident", "promotion_last_5years", "Departments", "salary"])

    # Make predictions using the XGBoost model
    predicted_churn = predict_churn(features)

    if st.button("Predict Churn", key="predict_button"):
        predicted_result = "Churn" if predicted_churn == 1 else "Not Churn"
        st.success(f"Prediction: {predicted_result}")

if __name__ == "__main__":
    main()













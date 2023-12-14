import streamlit as st
import pickle
import pandas as pd

# Load the XGBoost model
xgb_model = pickle.load(open("xgb (1)", "rb"))

def predict_fraud(features):
    # Convert features to a DataFrame
    features_df = pd.DataFrame([features], columns=["Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"])

    # Make predictions using the XGBoost model
    predicted_churn = xgb_model.predict(features_df.values)

    return predicted_churn[0]

def main():
    st.set_page_config(
        page_title="Fraud Detection App",
        page_icon="🔍",
        layout="wide",  # Adjusted layout to "wide" for better spacing
        initial_sidebar_state="collapsed",
    )

    st.title("Fraud Detection 🔍")

    st.write("### Enter Transaction details:")
    
    # Use st.columns for better layout
    col1, col2 = st.columns(2)

    # Create sliders in two columns for better layout
    with col1:
        Time = st.slider("Time Level", min_value=0.0, max_value=1.0, value=0.5)
        V1 = st.slider("V1", min_value=-10, max_value=10, value=5)
        V3 = st.slider("V3", min_value=-10, max_value=10, value=5)
        V5 = st.slider("V5", min_value=-10, max_value=10, value=5)
        V7 = st.slider("V7", min_value=-10, max_value=10, value=5)
        V9 = st.slider("V9", min_value=-10, max_value=10, value=5)
        V11 = st.slider("V11", min_value=-10, max_value=10, value=5)
        V13 = st.slider("V13", min_value=-10, max_value=10, value=5)
        V15 = st.slider("V15", min_value=-10, max_value=10, value=5)
        V17 = st.slider("V17", min_value=-10, max_value=10, value=5)
        V19 = st.slider("V19", min_value=-10, max_value=10, value=5)
        V21 = st.slider("V21", min_value=-10, max_value=10, value=5)
        V23 = st.slider("V23", min_value=-10, max_value=10, value=5)
        V25 = st.slider("V25", min_value=-10, max_value=10, value=5)
        V27 = st.slider("V27", min_value=-10, max_value=10, value=5)

    with col2:
        V2 = st.slider("V2", min_value=-10, max_value=10, value=5)
        V4 = st.slider("V4", min_value=-10, max_value=10, value=5)
        V6 = st.slider("V6", min_value=-10, max_value=10, value=5)
        V8 = st.slider("V8", min_value=-10, max_value=10, value=5)
        V10 = st.slider("V10", min_value=-10, max_value=10, value=5)
        V12 = st.slider("V12", min_value=-10, max_value=10, value=5)
        V14 = st.slider("V14", min_value=-10, max_value=10, value=5)
        V16 = st.slider("V16", min_value=-10, max_value=10, value=5)
        V18 = st.slider("V18", min_value=-10, max_value=10, value=5)
        V20 = st.slider("V20", min_value=-10, max_value=10, value=5)
        V22 = st.slider("V22", min_value=-10, max_value=10, value=5)
        V24 = st.slider("V24", min_value=-10, max_value=10, value=5)
        V26 = st.slider("V26", min_value=-10, max_value=10, value=5)
        V28 = st.slider("V28", min_value=-10, max_value=10, value=5)
        Amount = st.slider("Amount", min_value=0, max_value=100, value=50)

    features = [Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]

    # Create features_df for visualizations
    features_df = pd.DataFrame([features], columns=["Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"])

    # Make predictions using the XGBoost model
    predicted_churn = predict_fraud(features)

    if st.button("Predict Fraud", key="predict_button"):
        predicted_result = "Fraud" if predicted_churn == 1 else "Not Fraud"
        st.success(f"Prediction: {predicted_result}")

if __name__ == "__main__":
    main()














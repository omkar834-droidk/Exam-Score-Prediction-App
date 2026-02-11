import streamlit as st
import pickle
import pandas as pd

# Load model
try:
    with open('best_xgboost_model.pkl', 'rb') as f:
        xgb_tuned = pickle.load(f)
    st.success("XGBoost model loaded successfully!")
except FileNotFoundError:
    st.error("Model file not found!")
    st.stop()

# Load label encoders
try:
    with open('label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    st.success("Label encoders loaded successfully!")
except FileNotFoundError:
    st.error("Label encoder file not found!")
    st.stop()

st.title("📊 Exam Score Prediction App")

# -------- Numerical Inputs --------
study_hours = st.slider("Study Hours", 0.0, 10.0, 4.0, 0.1)
class_attendance = st.slider("Class Attendance (%)", 0.0, 100.0, 75.0, 0.1)
sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0, 0.1)

# -------- Categorical Inputs --------
sleep_quality = st.selectbox(
    "Sleep Quality",
    label_encoders['sleep_quality'].classes_
)

study_method = st.selectbox(
    "Study Method",
    label_encoders['study_method'].classes_
)

facility_rating = st.selectbox(
    "Facility Rating",
    label_encoders['facility_rating'].classes_
)

exam_difficulty = st.selectbox(
    "Exam Difficulty",
    label_encoders['exam_difficulty'].classes_
)

# -------- Prediction --------
if st.button("Predict Exam Score"):

    # Encode
    encoded_sleep_quality = label_encoders['sleep_quality'].transform([sleep_quality])[0]
    encoded_study_method = label_encoders['study_method'].transform([study_method])[0]
    encoded_facility_rating = label_encoders['facility_rating'].transform([facility_rating])[0]
    encoded_exam_difficulty = label_encoders['exam_difficulty'].transform([exam_difficulty])[0]

    # Create dataframe (IMPORTANT: Same order as training)
    input_data = pd.DataFrame([{
        'study_hours': study_hours,
        'class_attendance': class_attendance,
        'sleep_hours': sleep_hours,
        'sleep_quality': encoded_sleep_quality,
        'study_method': encoded_study_method,
        'facility_rating': encoded_facility_rating,
        'exam_difficulty': encoded_exam_difficulty
    }])

    prediction = xgb_tuned.predict(input_data)[0]

    st.success(f"🎯 Predicted Exam Score: {prediction:.2f}")

st.write("---")
st.write("Built with XGBoost + Streamlit 🚀")

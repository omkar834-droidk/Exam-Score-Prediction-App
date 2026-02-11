📊 Exam Score Prediction App

🚀 Live App:
👉 https://exam-score-prediction-app-gz4a6dvoetibpmqzn5p7zz.streamlit.app/

🎯 Project Overview

This is an end-to-end Machine Learning web application that predicts a student's exam score based on study habits, attendance, sleep patterns, and exam difficulty.

The project demonstrates the complete ML lifecycle:

Data preprocessing

Feature engineering

Label encoding

Hyperparameter tuning with GridSearchCV

Model training using XGBoost

Model serialization using Pickle

Deployment using Streamlit Cloud

Version control using Git & GitHub

This is a production-ready ML deployment project.

🧠 Machine Learning Details

Model: XGBoost Regressor
Tuning: GridSearchCV
Problem Type: Regression
Target Variable: Exam Score

Input Features:

Study Hours

Class Attendance (%)

Sleep Hours

Sleep Quality

Study Method

Facility Rating

Exam Difficulty

🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

XGBoost

Streamlit

Git

GitHub

Streamlit Cloud (Deployment)

🌐 Live Application

You can test the deployed model here:

👉 Live Demo:
https://exam-score-prediction-app-gz4a6dvoetibpmqzn5p7zz.streamlit.app/

No installation required.

📂 Project Structure
Exam-Score-Prediction-App/
│
├── main.py
├── best_xgboost_model.pkl
├── label_encoders.pkl
├── requirements.txt
└── README.md

▶️ Run Locally
1️⃣ Clone the Repository
git clone https://github.com/omkar834-droidk/Exam-Score-Prediction-App.git
cd Exam-Score-Prediction-App

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
streamlit run main.py

📈 What This Project Demonstrates

✔ End-to-End Machine Learning Pipeline
✔ Feature Encoding Handling in Deployment
✔ Model Serialization & Loading
✔ Feature Schema Alignment
✔ Cloud Deployment
✔ Version Control Best Practices

🚀 Future Improvements

Add feature importance visualization

Add performance metrics dashboard

Replace Label Encoding with One-Hot Encoding

Add data validation layer

Improve UI styling with custom themes

👨‍💻 Author

Omkar Salunke
Aspiring Data Scientist | Machine Learning Engineer

If you like this project, consider giving it a ⭐ on GitHub.

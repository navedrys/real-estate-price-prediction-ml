# 🏠 California Housing Price Prediction (XGBoost + Streamlit)

A Machine Learning web application that predicts **California housing prices** using an **XGBoost Regressor** trained on the *California Housing Dataset*.
The model is deployed as an **interactive Streamlit web app** where users can input housing features and get real-time price predictions.

---

## 🌐 Live Demo

👉 **Streamlit App:**
[[https://your-streamlit-app-link.streamlit.app/]([https://real-estate-price-ml.streamlit.app/](https://real-estate-price-prediction-ml-mcfrmsdwe3lngdmqgggswy.streamlit.app/))](https://real-estate-price-prediction-ml-mcfrmsdwe3lngdmqgggswy.streamlit.app/)

---

## 📌 Project Overview

This project demonstrates an **end-to-end Machine Learning workflow**, including:

* Data preprocessing
* Model training using **XGBoost Regressor**
* Model serialization using **Pickle**
* Deployment using **Streamlit**

The application allows users to enter housing details such as income, house age, rooms, and location to estimate the **median house value**.

---

## ⚙️ Features

* Interactive **Streamlit UI**
* Real-time house price prediction
* Clean and simple user interface
* Fast predictions using a trained **XGBoost model**
* Easily deployable ML application

---

## 🧠 Machine Learning Model

**Algorithm Used**

* XGBoost Regressor

**Dataset**

* California Housing Dataset (from Scikit-learn)

**Input Features**

* Median Income
* House Age
* Average Rooms
* Average Bedrooms
* Population
* Average Occupancy
* Latitude
* Longitude

**Target Variable**

* Median House Value

---

## 🖥️ Tech Stack

* Python
* Scikit-learn
* XGBoost
* NumPy
* Streamlit
* Pickle

---

## 📂 Project Structure

```
california-housing-price-predictor
│
├── app.py                # Streamlit application
├── model.pkl             # Trained ML model
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🚀 Installation & Run Locally

Clone the repository

```
git clone https://github.com/yourusername/california-housing-price-predictor.git
```

Navigate to the project folder

```
cd california-housing-price-predictor
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit app

```
streamlit run app.py
```

---

## 📊 How the App Works

1. User enters housing features.
2. The input data is passed to the trained **XGBoost model**.
3. The model predicts the **estimated house price**.
4. The result is displayed instantly on the Streamlit interface.

---

## 🎯 Future Improvements

* Add model evaluation metrics
* Feature importance visualization
* Data visualization dashboard
* SHAP explainability integration

---

## 👨‍💻 Author

**Naved Shaikh**


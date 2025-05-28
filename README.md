
# 🚗 Car Price Prediction Web App

A simple and intuitive web application built using **Streamlit** that predicts the price of a car based on various input features such as car name, model, fuel type, kilometers driven, and more.

**Developed by [Suraj](https://github.com/your-github-username)**

---

## 📌 Features

- Predict car prices using a trained **Linear Regression** model.
- Real-time prediction based on user input.
- Handles data preprocessing:
  - One-Hot Encoding (Car Name)
  - Label Encoding (Model)
  - Feature Scaling (All features except Price)
- Clean and interactive UI with **Streamlit**.
- Easily deployable and lightweight.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas, NumPy** – Data Handling
- **Scikit-learn** – Model Training & Preprocessing
- **Streamlit** – Web UI Framework

---

## 📂 Project Structure

```
car-price-prediction/
│
├── car_price_prediction_app.py       # Streamlit App
├── car_price_model.pkl               # Trained Model
├── preprocessing_pipeline.pkl        # Encoders + Scaler
├── requirements.txt                  # Python Dependencies
└── README.md                         # Project Documentation
```

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/suraj/car-price-prediction.git
cd car-price-prediction
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit App

```bash
streamlit run car_price_prediction_app.py
```

The app will automatically open in your browser at `http://localhost:8501`.

---

## 🧠 How It Works

1. **User Input:** Fill in car details using dropdowns and input fields.
2. **Preprocessing:** Input is processed using saved encoders and scalers.
3. **Prediction:** Model predicts car price based on processed input.
4. **Output:** Estimated car price is displayed instantly.

---

## 📸 Screenshots

![APP SCREENSHOT]("Page1.png")

---

## ✅ Future Enhancements

- Add support for other models (e.g., Random Forest, XGBoost).
- CSV upload for batch prediction.
- Improve UI with animations and branding.
- Deploy to **Streamlit Cloud**, **Render**, or **Heroku**.

---

## 🤝 Contributing

Have ideas or improvements? Contributions are welcome!

```bash
# Fork the repository
# Make your changes
# Submit a pull request
```

---

## 📃 License

This project is licensed under the **MIT License**.

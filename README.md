
# 🚗 Car Price Prediction Web App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://car-price-prediction-web.streamlit.app/)
[![GitHub stars](https://img.shields.io/github/stars/Git-Suraj-hub/Car-Price-Prediction?style=social)](https://github.com/Git-Suraj-hub/Car-Price-Prediction.git)

A machine learning-powered web app built with **Python** and **Streamlit** that predicts the resale value of a car based on input features like car name, model, fuel type, and kilometers driven. Uses a trained **Linear Regression** model with real-time predictions and interactive UI.

---

## 🚀 Features

* 📥 **User Input**: Enter car details like name, model, fuel type, and kilometers.
* ⚙️ **Preprocessing**: Applies encoding and scaling using saved transformers.
* 📈 **Price Prediction**: Predicts car price using a trained regression model.
* 🎯 **Real-Time Output**: Instant price estimates displayed on the app.
* 🧠 **Model Logic**: Based on a Linear Regression model trained on historical data.

---

## 📂 Project Structure

```text
car-price-prediction/
├── new.py     # Streamlit application code
├── feautre_columns.sav             # Feautre Column Model
├── Label_encoder.sav               # Label Encoding Model
├── LICENSE                         # MIT License
├── model_columns.pkl               # Column model
├── quick_car_csv                   # Car Price Dataset
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
├── trained_model.pkl             # Trained Linear Regression model
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Git-Suraj-hub/Car-Price-Prediction.git
   cd car-price-prediction
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   streamlit run new.py
   ```

---

## 🌐 Deployment

You can deploy this app on **Streamlit Cloud**:

1. Push your code to GitHub (if not already):

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and log in.

3. Click **New app** and select your GitHub repository.

4. Specify:
   * **Branch**: `main`
   * **File path**: `car_price_prediction_app.py`

5. Click **Deploy**.

Your app will be live at `https://<your-username>-car-price-prediction.streamlit.app`.

---
## 📸 Screenshots

![Screenshot](Page1.png)

---

## 🛠️ Usage

1. **Launch the app** in your browser.
2. **Fill in car details** in the form (e.g., fuel type, kilometers driven).
3. **View prediction** displayed instantly on the right.
4. **Try with different inputs** to compare results.

---

## 🔧 Configuration

You can customize the behavior in `car_price_prediction_app.py`:

* Add or modify preprocessing steps.
* Replace the model with Random Forest, XGBoost, etc.
* Enhance UI/UX using Streamlit components.

---

## 🤝 Contributing

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📫 Contact

Created by **Suraj**. For questions or feedback, reach out at `suraj773714@gmail.com`.

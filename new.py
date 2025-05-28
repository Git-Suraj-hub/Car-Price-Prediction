import numpy as np
import streamlit as st
import pandas as pd
import pickle
import sklearn

# Load CSV to get dropdown options
dataframe = pd.read_csv('quikr_car.csv')
dataframe.columns = dataframe.columns.str.strip()  # Strip column name spaces

import os
st.write(os.path.exists('trained_model.sav'))  # Should print True


# Load model and preprocessing tools
trained_model = pickle.load(open('trained_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))
label_encoder = pickle.load(open('Label_encoder.sav', 'rb'))
feature_columns = pickle.load(open('feature_columns.sav', 'rb'))

# Prepare select box options
car_names = sorted(dataframe['name'].dropna().unique())
models = sorted(dataframe['company'].dropna().unique())
fuel_types = ['Petrol', 'Diesel', 'LPG']  # Map to 0, 1, 2

# Fuel mapping
fuel_map = {'Petrol': 0, 'Diesel': 1, 'LPG': 2}

def CarPrediction(car_name, model_name, fuel_type, kms_driven, year):
    # Encode fuel type
    if fuel_type not in fuel_map:
        return "❌ Unknown fuel type!"
    fuel_encoded = fuel_map[fuel_type]

    # Encode model using LabelEncoder (company)
    try:
        model_encoded = label_encoder.transform([model_name])[0]
    except ValueError:
        return "❌ Unknown model!"

    # One-hot encode car name
    one_hot = {col: 0 for col in feature_columns if col.startswith("name_")}
    car_col = f"name_{car_name}"
    if car_col in one_hot:
        one_hot[car_col] = 1
    else:
        return "❌ Unknown car name!"

    # Create full input row
    input_dict = {
        'company': model_encoded,
        'fuel_type': fuel_encoded,
        'kms_driven': kms_driven,
        'year': year
    }
    input_dict.update(one_hot)
    input_df = pd.DataFrame([input_dict])

    # Reorder columns to match training
    input_df = input_df[feature_columns]

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = trained_model.predict(input_scaled)
    return f"✅ Predicted Price: ₹{prediction[0]:,.2f}"

# Streamlit UI
def main():
    st.title("🚗 Car Price Prediction App")

    car_name = st.selectbox("Select Car Name", car_names)
    model_name = st.selectbox("Select Company Name", models)
    fuel_type = st.selectbox("Select Fuel Type", fuel_types)
    year = st.number_input("Enter Year", min_value=1990, max_value=2025, value=2015)
    kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, value=30000)

    if st.button("Predict Price"):
        result = CarPrediction(car_name, model_name, fuel_type, kms_driven, year)
        st.success(result)

if __name__ == '__main__':
    main()

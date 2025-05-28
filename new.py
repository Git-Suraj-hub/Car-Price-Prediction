import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import os

# Get the absolute path to the directory where new.py is located
current_dir = Path(__file__).parent

# --- Debugging additions (keep these for now, remove later once fixed) ---
st.write(f"Current script directory: {current_dir}")
st.write(f"Contents of current directory: {list(current_dir.iterdir())}")

# Construct paths - CORRECTED 'Label_encoder.sav'
trained_model_path = current_dir / 'trained_model.sav'
scaler_path = current_dir / 'scaler.sav'
label_encoder_path = current_dir / 'Label_encoder.sav' # FIXED CAPITALIZATION HERE
feature_columns_path = current_dir / 'feature_columns.sav'
car_data_path = current_dir / 'quikr_car.csv'

st.write(f"Looking for trained_model at: {trained_model_path}")
st.write(f"Looking for scaler at: {scaler_path}")
st.write(f"Looking for label_encoder at: {label_encoder_path}")
st.write(f"Looking for feature_columns at: {feature_columns_path}")
st.write(f"Looking for quikr_car.csv at: {car_data_path}")

# Check if files exist individually
st.write(f"trained_model.sav exists: {trained_model_path.exists()}")
st.write(f"scaler.sav exists: {scaler_path.exists()}")
st.write(f"label_encoder.sav exists: {label_encoder_path.exists()}") # This will now be True
st.write(f"feature_columns.sav exists: {feature_columns_path.exists()}")
st.write(f"quikr_car.csv exists: {car_data_path.exists()}")
# --- End Debugging additions ---


# Load model and preprocessing tools
try:
    trained_model = pickle.load(open(trained_model_path, 'rb'))
    scaler = pickle.load(open(scaler_path, 'rb'))
    label_encoder = pickle.load(open(label_encoder_path, 'rb')) # This line will now find the file
    feature_columns = pickle.load(open(feature_columns_path, 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading required files: {e}.")
    st.error(f"**Double-check that these files are in your GitHub repo and are correctly capitalized:**")
    st.error(f"  - trained_model.sav")
    st.error(f"  - scaler.sav")
    st.error(f"  - Label_encoder.sav (Note the capital 'L')") # Highlight the fix
    st.error(f"  - feature_columns.sav")
    st.stop() # Stop the app if crucial files are missing

# Load csv to get dropdown options
try:
    dataFrame = pd.read_csv(car_data_path)
    dataFrame.columns = dataFrame.columns.str.strip() # Strip column name spaces
except FileNotFoundError as e:
    st.error(f"Error loading 'quikr_car.csv': {e}.")
    st.error(f"**Double-check that 'quikr_car.csv' is in your GitHub repo and is correctly capitalized.**")
    st.stop()

# ... rest of your Streamlit app code ...

import streamlit as st
import pandas as pd
import numpy as np
import librosa
from sklearn.ensemble import RandomForestClassifier
import joblib

# Function to extract poly features from audio file
def extract_poly_features(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    poly_features = librosa.feature.poly_features(y=y, sr=sr)
    flattened_features = np.ravel(poly_features)
    return flattened_features

# Function to predict label using model and poly features
def predict_label(features, model):
    # Predict label
    label = model.predict(features.reshape(1, -1))
    return label[0]

def main():
    st.title('Predict')
    st.write('Welcome to the Predict page!')
    
    # File uploader for audio file
    uploaded_audio = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
    
    # Load the trained model
    rf_model = joblib.load('rf_model.pkl')

    if uploaded_audio is not None:
        # Save the uploaded audio file to disk
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_audio.getbuffer())
        
        # Extract poly features
        features = extract_poly_features("temp_audio.wav")
        
        # Predict label
        label = predict_label(features, rf_model)
        
        # Display prediction
        st.write('Predicted Label:', label)

if __name__ == "__main__":
    main()

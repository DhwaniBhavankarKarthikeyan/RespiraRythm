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

# Function to predict label using saved model
def predict_label(features, model):
    # Predict label
    label = model.predict(features.reshape(1, -1))
    return label[0]

def predict_page(model):
    st.title('Predict')
    st.write('Welcome to the Predict page!')
    
    # File uploader for audio file
    uploaded_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
    
    # Button to predict
    if st.button('Predict') and uploaded_file is not None:
        # Save the uploaded audio file to disk
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Extract poly features
        features = extract_poly_features("temp_audio.wav")
        
        # Predict label
        label = predict_label(features, model)
        
        # Display prediction
        st.write('Predicted Label:', label)

def main():
    # Load trained RandomForestClassifier
    classifier = joblib.load('rf_model.pkl')
    
    st.sidebar.title('Navigation')
    
    option = st.sidebar.radio('Go to', ['Home', 'Predict', 'About Us'])
    
    if option == 'Home':
        st.title('Home')
        st.write('Welcome to the Home page!')
    elif option == 'Predict':
        predict_page(classifier)
    elif option == 'About Us':
        st.title('About Us')
        st.write('Welcome to the About Us page!')

if __name__ == "__main__":
    main()

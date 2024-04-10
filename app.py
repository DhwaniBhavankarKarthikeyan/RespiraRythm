import streamlit as st
import pandas as pd
import numpy as np
import librosa
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Function to extract poly features from audio file
def extract_poly_features(audio_file, num_features):
    y, sr = librosa.load(audio_file, sr=None)
    poly_features = librosa.feature.poly_features(y=y, sr=sr)
    flattened_features = np.ravel(poly_features)[:num_features]  # Retain only specified number of features
    return flattened_features

def main():
    st.title('Predict')
    st.write('Welcome to the Predict page!')

    # Load the poly features CSV file
    csv_url = "https://github.com/DhwaniBhavankarKarthikeyan/RespiraRythm/blob/main/POLY_Final.csv"  # Update with your GitHub URL
    df = pd.read_csv(csv_url, encoding='utf-8', delimiter=',')


    # Extract the number of features
    num_features = len(df.columns) - 2  # Exclude the 'Label' column

    # File uploader for audio file
    uploaded_audio = st.file_uploader("Upload Audio File", type=["wav", "mp3"])

    if uploaded_audio is not None:
        # Save the uploaded audio file to disk
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_audio.getbuffer())

        # Extract poly features
        features = extract_poly_features("temp_audio.wav", num_features)

        # Split data into features and labels
        X = df.drop('Label','File Names', axis=1)
        y = df['Label']

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train RandomForestClassifier
        st.write('Training the model...')
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(X_train, y_train)

        # Make predictions
        y_pred = rf_model.predict(X_test)

        # Evaluate the model
        st.write('Evaluation Report:')
        st.write(classification_report(y_test, y_pred))

        # Predict label for the uploaded audio
        label = rf_model.predict([features])[0]
        st.write('Predicted Label:', label)

if __name__ == "__main__":
    main()

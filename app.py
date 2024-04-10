import streamlit as st
import pandas as pd
import numpy as np
import librosa
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Function to extract poly features from audio file
def extract_poly_features(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    poly_features = librosa.feature.poly_features(y=y, sr=sr)
    flattened_features = np.ravel(poly_features)
    return flattened_features

def main():
    st.title('Home')
    st.write('Welcome to the Home page!')

    st.sidebar.title('Navigation')
    option = st.sidebar.radio('Go to', ['Train Model', 'Predict'])

    if option == 'Train Model':
        st.title('Train Model')
        st.write('Upload CSV file containing extracted poly features and labels.')

        uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            X = df.drop(['File Names', 'Label'], axis=1)
            y = df['Label']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            st.write('Training model...')
            rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
            rf_model.fit(X_train, y_train)
            st.write('Model training complete!')

            st.write('Evaluating model...')
            y_pred = rf_model.predict(X_test)
            st.write('Classification Report:')
            st.write(classification_report(y_test, y_pred))

            st.write('Model is ready for prediction.')

            # Save trained model
            st.write('Saving model...')
            joblib.dump(rf_model, 'rf_model.pkl')
            st.write('Model saved as rf_model.pkl.')

    elif option == 'Predict':
        st.title('Predict')
        st.write('Upload an audio file for prediction.')

        uploaded_audio = st.file_uploader("Upload Audio File", type=["wav", "mp3"])

        if uploaded_audio is not None:
            # Load trained model
            st.write('Loading model...')
            rf_model = joblib.load('rf_model.pkl')
            st.write('Model loaded successfully.')

            # Save the uploaded audio file to disk
            with open("temp_audio.wav", "wb") as f:
                f.write(uploaded_audio.getbuffer())

            # Extract poly features
            st.write('Extracting poly features...')
            features = extract_poly_features("temp_audio.wav")
            
            # Check the number of features extracted
            st.write('Number of features extracted:', len(features))

            # Load X_train if it's available
            if 'X_train' in locals():
                # Check the number of features in the model
                st.write('Number of features in the model:', len(X_train.columns))

                # Ensure number of features matches
                if len(features) == len(X_train.columns):
                    # Predict label
                    st.write('Predicting label...')
                    label = rf_model.predict(features.reshape(1, -1))[0]
                    st.write('Predicted Label:', label)
                else:
                    st.write('Number of features extracted does not match the model. Please upload a file with the correct number of features.')
            else:
                st.write('Model has not been trained. Please train the model before making predictions.')

if __name__ == "__main__":
    main()

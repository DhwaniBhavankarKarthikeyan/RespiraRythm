import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Function to predict label using saved model
def predict_label(features, model):
    # Predict label
    label = model.predict(features)
    return label

def predict_page(model):
    st.title('Predict')
    st.write('Welcome to the Predict page!')
    
    # File uploader for feature values (poly features)
    uploaded_file = st.file_uploader("Upload CSV File with Poly Features", type=["csv"])
    
    # Button to predict
    if st.button('Predict') and uploaded_file is not None:
        # Load CSV file containing poly features
        df = pd.read_csv(uploaded_file)
        # Extract features
        features = df.drop(['File Names', 'Label'], axis=1).values
        
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

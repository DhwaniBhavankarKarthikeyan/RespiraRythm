# app.py
import streamlit as st

def home():
    st.title('Home')
    st.write('Welcome to the Home page!')

def predict():
    st.title('Predict')
    st.write('Welcome to the Predict page!')

def about_us():
    st.title('About Us')
    st.write('Welcome to the About Us page!')

# Main function to switch between pages
def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox('Select a page', ['Home', 'Predict', 'About Us'])

    if page == 'Home':
        home()
    elif page == 'Predict':
        predict()
    elif page == 'About Us':
        about_us()

if __name__ == "__main__":
    main()

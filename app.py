import streamlit as st

def home():
    st.title('Home')
    st.header('Welcome to Respira Rhythm Classifier!')
    st.write("""
        Thank you for using this application. By visiting this page, you've joined us in the important cause of proactively monitoring your health.
        \n\n
        Lung diseases are a major global issue, contributing to millions of deaths yearly. Respiratory problems can worsen over time.
        \n\n
        Prevention is crucial. We've developed Respira Rhythm—an ML-based model to assess your breathing health.
        It's accurate, reliable, and trustworthy, trained on authentic data for optimum accuracy.
    """)

def predict():
    st.title('Predict')
    st.write('Welcome to the Predict page!')

def about_us():
    st.title('About Us')
    st.write('Welcome to the About Us page!')
    st.write("""
        We are B.Tech students pursuing Artificial Intelligence and Machine Learning at Symbiosis Institute of Technology (SIT), Pune.
        \n\n
        **Our Mission:** To improve respiratory disease diagnostics using AI and reduce diagnostic costs.
        \n\n
        - Ananya Mehta
        - Aparna Iyer
        - Deeksha Mandal
        - Dhwani Bhavankar
    """)

def main():
    option = st.sidebar.button('Home')
    if option:
        home()
    
    option = st.sidebar.button('Predict')
    if option:
        predict()
    
    option = st.sidebar.button('About Us')
    if option:
        about_us()

if __name__ == "__main__":
    main()

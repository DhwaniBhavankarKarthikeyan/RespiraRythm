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
    st.sidebar.title('Navigation')
    
    # Apply CSS to make buttons occupy full height
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            max-width: 100%;
        }
        .sidebar .sidebar-content .block-container {
            width: 100%;
        }
        .sidebar .css-1tppvg2 {
            width: 100%;
            text-align: left;
        }
        </style>
    """, unsafe_allow_html=True)
    
    option = st.sidebar.selectbox('Select Page', ('Home', 'Predict', 'About Us'))
    
    if option == 'Home':
        home()
    elif option == 'Predict':
        predict()
    elif option == 'About Us':
        about_us()

if __name__ == "__main__":
    main()

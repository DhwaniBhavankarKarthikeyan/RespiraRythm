import streamlit as st
from streamlit_option_menu import option_menu

def home():
    st.title('Home')
    st.write('Welcome to the Home page!\n')
    st.write('Hello and welcome to Respira Rhythm Classifier!\n')
    st.write('Thank you for taking the judicious step of using this application. By visiting this page, you have joined us in a very important cause- the cause of proactively monitoring your health without waiting for symptomatic check-up, diagnosis and treatment. \n \n')
    st.write("This matters because lung diseases are the third-largest cause of death in the world. According to the World Health Organization (WHO), the five major respiratory diseases cause the death of more than 3 million people worldwide each year. Furthermore, respiratory problems are progressive in nature, worsening the respiratory potential of the human lungs over time.\n")
    st.write("We believe that prevention is better than cure. To facilitate simple, quick and virtually cost-free diagnostic access for monitoring respiratory health, we have developed Respira Rhythm- an ML-based classification model that assesses your breathing as healthy or diseased.")
    st.write("Respira Rhythm is accurate, reliable and trustworthy, just like a medical practitioner. It has been trained on authentic audio data and modelled for optimum accuracy.")

def predict():
    st.title('Predict')
    st.write('Welcome to the Predict page!')

def about_us():
    st.title('About Us')
    st.write('Welcome to the About Us page!')
    st.write('We are B.Tech students pursuing Artificial Intelligence and Machine Learning at Symbiosis Institute of Technology (SIT), Pune.\n')
    st.write('Our Mission: To help improve the diagnostic accuracy of classifying respiratory diseases based on breathing sounds, while reducing diagnostic costs. All through the power of data and ML.\n')
    st.write('Ananya Mehta \n \n')
    st.write('Aparna Iyer \n \n')
    st.write('Deeksha Mandal \n \n')
    st.write('Dhwani Bhavankar \n \n')
# Main function to switch between pages
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

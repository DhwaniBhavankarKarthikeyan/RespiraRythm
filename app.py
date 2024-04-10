import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Navigator"
)

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

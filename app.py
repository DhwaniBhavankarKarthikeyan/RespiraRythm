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

def main():
    # Custom CSS for the navigation bar
    st.markdown(
        """
        <style>
        .navbar {
            overflow: hidden;
            background-color: #333;
        }

        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }

        .navbar a.active {
            background-color: #02ab21;
            color: white;
        }
        </style>
        """
    )

    # Create navigation bar
    st.markdown(
        """
        <div class="navbar">
            <a class="active" href="#home">Home</a>
            <a href="#predict">Predict</a>
            <a href="#about">About Us</a>
        </div>
        """
    )

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

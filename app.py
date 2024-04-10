import streamlit as st
from streamlit_option_menu import option_menu
import alerts
from patients import patients  # Importing the patients function

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin"

# Custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
    }
    .stButton>button {
        background-color: #02ab21;
        color: white;
    }
    .stButton>button:hover {
        background-color: #028c19;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://t3.ftcdn.net/jpg/02/81/21/10/360_F_281211036_24KPea5poawt4mXYlEjRUwsCgomtjoVc.jpg");
                background-attachment: fixed;
                background-size: cover;
                opacity: 0.9; /* Adjust the opacity value here (0.8 for 80% opacity) */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("<div align='center'><h1>Welcome to MedWatcher</h1></div>", unsafe_allow_html=True)
        st.markdown("---")
        st.write("<h2>Login</h2>", unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password. Please try again.")

    return st.session_state.logged_in

def home():
    # Displaying brand logo and another image side by side
    col1, col2, col3 ,col4, col5 ,col6= st.columns(6)
    
    # Displaying brand logo with reduced size
    with col1:
        st.image("MedWatchersLogo.jpeg", width=150)
    
    # Displaying another image
    with col2:
        st.image("https://www.siu.edu.in/images/Symbiosis-International-University-logo.png", width=800)

    # Applying custom CSS to reduce space between columns and stretch image
    st.markdown(
        """
        <style>
        .css-1l02zno {
            margin-right: -20px !important;
            margin-left: -20px !important;
        }
        .css-1s9erse img {
            object-fit: fill;
            width: 100%;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("# Home Page")
    st.write("Welcome to MedWatcher!")
    st.write("MedWatcher is a dashboard application designed to help diabetic patients and healthcare providers monitor and manage glucose levels effectively.")
    st.write("With MedWatcher, you can:")
    st.write("- View detailed patient information, including glucose data and relevant tasks.")
    st.write("- Analyze glucose trends over time with interactive charts.")
    st.write("- Receive alerts for glucose levels outside the normal range.")
    st.write("To get started, navigate using the sidebar on the left.")




def about_us():
    col1, col2, col3 ,col4, col5 ,col6= st.columns(6)
    
    # Displaying brand logo with reduced size
    with col1:
        st.image("MedWatchersLogo.jpeg", width=150)
    
    # Displaying another image
    with col2:
        st.image("https://www.siu.edu.in/images/Symbiosis-International-University-logo.png", width=800)

    # Applying custom CSS to reduce space between columns and stretch image
    st.markdown(
        """
        <style>
        .css-1l02zno {
            margin-right: -20px !important;
            margin-left: -20px !important;
        }
        .css-1s9erse img {
            object-fit: fill;
            width: 100%;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write("# About Us")
    st.write("MedWatcher is a platform dedicated to improving diabetes management for patients and healthcare providers.")
    st.write("Our mission is to provide tools and insights to empower individuals to better understand and control their glucose levels.")
    st.write("For any inquiries or feedback, please contact us at contact@medwatcher.com.")
    
    # Add your photo, name, and email ID
    st.write("## Meet the Team")
    
    # Create two columns for the photos
    col1, col2 = st.columns(2)
    
    # Photo 1
    with col1:
        st.image("img1.jpeg", caption="Dhwani Bhavankar", width=100, use_column_width=False, output_format='png')
        #st.write("**Dhwani Bhavankar**")
        st.write("dhwani.bhavankar.btech2022@sitpune.edu.in")
    
    # Photo 2
    with col2:
        st.image("img2.jpeg", caption="Ananya Mehta", width=100, use_column_width=False, output_format='png')
        #st.write("**Ananya Mehta**")
        st.write("ananya39mehta@gmail.com")

    # Photo 3
    with col1:
        st.image("img3.jpeg", caption="Harsimran Kaur", width=100, use_column_width=False, output_format='png')
        #st.write("**Harsimran Kaur**")
        st.write("harsimrankaur2493@gmail.com")
    
    # Photo 4
    with col2:
        st.image("img4.jpeg", caption="Mayank Sahai", width=100, use_column_width=False, output_format='png')
        #st.write("**Mayank Sahai**")
        st.write("smayank2412@gmail.com")
        
def add_patients():
    st.write("# Add Patients")
    


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        if not login():
            return

        with st.sidebar:
            app = option_menu(
                menu_title="MedWatcher",
                options=['Home', 'Predict', 'About Us'], 
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home()
        elif app == 'Predict':
            '''col1, col2, col3 ,col4, col5 ,col6= st.columns(6)
    
            # Displaying brand logo with reduced size
            with col1:
                st.image("MedWatchersLogo.jpeg", width=150)
            
            # Displaying another image
            with col2:
                st.image("https://www.siu.edu.in/images/Symbiosis-International-University-logo.png", width=800)
        
            # Applying custom CSS to reduce space between columns and stretch image
            st.markdown(
                """
                <style>
                .css-1l02zno {
                    margin-right: -20px !important;
                    margin-left: -20px !important;
                }
                .css-1s9erse img {
                    object-fit: fill;
                    width: 100%;
                    height: 100%;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            alerts.app()'''
               
            
        elif app == 'About Us':  # Handling 'About Us' page
            '''about_us()'''

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()

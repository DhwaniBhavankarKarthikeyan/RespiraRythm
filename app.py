import streamlit as st
from streamlit_option_menu import option_menu

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
    st.write("# Home Page")
    st.write("Welcome to MedWatcher!")
    st.write("MedWatcher is a dashboard application designed to help diabetic patients and healthcare providers monitor and manage glucose levels effectively.")
    st.write("With MedWatcher, you can:")
    st.write("- View detailed patient information, including glucose data and relevant tasks.")
    st.write("- Analyze glucose trends over time with interactive charts.")
    st.write("- Receive alerts for glucose levels outside the normal range.")
    st.write("To get started, navigate using the sidebar on the left.")

def predict():
    st.write("# Predict")

def about_us():
    st.write("# About Us")
    st.write("MedWatcher is a platform dedicated to improving diabetes management for patients and healthcare providers.")
    st.write("Our mission is to provide tools and insights to empower individuals to better understand and control their glucose levels.")
    st.write("For any inquiries or feedback, please contact us at contact@medwatcher.com.")

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
                options=['Home', 'Predict', 'About Us'],  # Added 'About Us' option
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
            predict()
        elif app == 'About Us':
            about_us()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()

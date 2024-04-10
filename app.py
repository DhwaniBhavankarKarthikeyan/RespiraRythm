import streamlit as st
from streamlit_option_menu import option_menu

def home():
    

    st.write("# Home Page")
    st.write("Welcome to MedWatcher!")
    st.write("MedWatcher is a dashboard application designed to help diabetic patients and healthcare providers monitor and manage glucose levels effectively.")
    st.write("With MedWatcher, you can:")
    st.write("- View detailed patient information, including glucose data and relevant tasks.")
    st.write("- Analyze glucose trends over time with interactive charts.")
    st.write("- Receive alerts for glucose levels outside the normal range.")
    st.write("To get started, navigate using the sidebar on the left.")




def about_us():
    
    st.write("# About Us")
    st.write("MedWatcher is a platform dedicated to improving diabetes management for patients and healthcare providers.")
    st.write("Our mission is to provide tools and insights to empower individuals to better understand and control their glucose levels.")
    st.write("For any inquiries or feedback, please contact us at contact@medwatcher.com.")
    
    # Add your photo, name, and email ID
    st.write("## Meet the Team")
    
   
        
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
            
               
            
        elif app == 'About Us':  # Handling 'About Us' page
            '''about_us()'''

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()

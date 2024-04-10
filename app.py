def predict():
    st.write("# Predict")
    st.write("This page will contain functionalities related to predicting glucose levels.")
    # Add your prediction functionalities here

def add_patients():
    st.write("# Add Patients")
    # Add your functionalities for adding patients here

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

        for app_item in self.apps:
            if app_item['title'] == app:
                app_item['function']()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.add_app("Home", home)
    multi_app.add_app("Predict", predict)  # Add the 'Predict' page
    multi_app.add_app("About Us", about_us)
    multi_app.run()

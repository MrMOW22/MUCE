import streamlit as st
from pages import Home, Signup, Login, AdminDashboard
from config import set_page_config

set_page_config()

page = st.sidebar.selectbox("Navigate", ["Home", "Sign Up", "Login", "Admin Dashboard"])

if page == "Home":
    Home.show()
elif page == "Sign Up":
    Signup.show()
elif page == "Login":
    Login.show()
elif page == "Admin Dashboard":
    AdminDashboard.show()

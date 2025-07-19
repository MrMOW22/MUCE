import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Mufulira College of Education",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

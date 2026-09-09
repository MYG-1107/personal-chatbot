import os
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Injection
def load_css(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles/main.css")

# Import Page Controllers & Components
from components.sidebar import render_sidebar
from pages.home import render_home_page
from pages.chat import render_chat_page
from pages.history import render_history_page
from pages.settings import render_settings_page
from pages.profile import render_profile_page

# Router Execution
render_sidebar()

current_page = st.session_state.get("current_page", "Home")

if current_page == "Home":
    render_home_page()
elif current_page == "Chat":
    render_chat_page()
elif current_page == "History":
    render_history_page()
elif current_page == "Settings":
    render_settings_page()
elif current_page == "Profile":
    render_profile_page()
else:
    render_home_page()
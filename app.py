import os
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS & Dynamic Font Size Injection
def apply_custom_styles():
    # Load main CSS file
    if os.path.exists("styles/main.css"):
        with open("styles/main.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Dynamic Font Size Mapping
    font_size_setting = st.session_state.get("font_size", "Medium")
    font_map = {
        "Small": "13px",
        "Medium": "16px",
        "Large": "19px"
    }
    selected_size = font_map.get(font_size_setting, "16px")

    dynamic_css = f"""
    <style>
        html, body, .stApp, p, div, span, button, input, textarea {{
            font-size: {selected_size} !important;
        }}
    </style>
    """
    st.markdown(dynamic_css, unsafe_allow_html=True)

apply_custom_styles()

# Import Page Controllers
from components.sidebar import render_sidebar
from views.home import render_home_page
from views.chat import render_chat_page
from views.history import render_history_page
from views.settings import render_settings_page
from views.profile import render_profile_page

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
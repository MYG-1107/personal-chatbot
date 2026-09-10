import os
import time
import streamlit as st

st.set_page_config(
    page_title="Maya",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session Telemetry Metrics
if "session_start_time" not in st.session_state:
    st.session_state["session_start_time"] = time.time()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Detect User Device Environment from Browser Headers
def detect_user_device():
    headers = st.context.headers
    user_agent = headers.get("User-Agent", "") if headers else ""
    
    if "Macintosh" in user_agent or "Mac OS" in user_agent:
        return "macOS User"
    elif "Windows" in user_agent:
        return "Windows User"
    elif "Android" in user_agent:
        return "Android User"
    elif "iPhone" in user_agent or "iPad" in user_agent:
        return "iOS User"
    elif "Linux" in user_agent:
        return "Linux User"
    return "Guest User"

if "user_name" not in st.session_state:
    st.session_state["user_name"] = detect_user_device()

# Apply CSS
if os.path.exists("styles/main.css"):
    with open("styles/main.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation
from components.sidebar import render_sidebar
from views.home import render_home_page
from views.chat import render_chat_page
from views.history import render_history_page
from views.settings import render_settings_page
from views.profile import render_profile_page

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
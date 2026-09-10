import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar():
    with st.sidebar:
        st.markdown("<h3 style='margin-bottom: 1rem; font-weight: 600; color: #000000;'>Maya</h3>", unsafe_allow_html=True)
        
        # Pure Black New Chat Button
        if st.button("+ New Chat", use_container_width=True):
            st.session_state["messages"] = []
            st.session_state["current_page"] = "Chat"
            st.rerun()

        st.markdown("<hr style='margin: 1rem 0; border: none; border-top: 1px solid #e4e4e7;'>", unsafe_allow_html=True)

        # Black & White Navigation Menu
        selected = option_menu(
            menu_title=None,
            options=["Home", "Chat", "History", "Settings", "Profile"],
            icons=["house", "chat", "clock", "gear", "person"],
            default_index=["Home", "Chat", "History", "Settings", "Profile"].index(
                st.session_state.get("current_page", "Chat")
            ),
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#000000", "font-size": "14px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "2px 0",
                    "border-radius": "6px",
                    "color": "#000000"
                },
                "nav-link-selected": {"background-color": "#000000", "color": "#ffffff"},
            }
        )

        st.session_state["current_page"] = selected
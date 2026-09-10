import streamlit as st
from streamlit_option_menu import option_menu
from data.mock_data import USER_PROFILE

def render_sidebar():
    with st.sidebar:
        st.markdown("### 🤖 Personal AI")
        
        if st.button("➕ New Chat", use_container_width=True, type="primary"):
            st.session_state["messages"] = []
            st.session_state["current_page"] = "Chat"
            st.rerun()

        st.divider()

        # Navigation Options
        selected = option_menu(
            menu_title=None,
            options=["Home", "Chat", "History", "Settings", "Profile"],
            icons=["house", "chat-dots", "clock-history", "gear", "person-circle"],
            default_index=["Home", "Chat", "History", "Settings", "Profile"].index(
                st.session_state.get("current_page", "Home")
            ),
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#6366f1", "font-size": "16px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "4px 0",
                    "border-radius": "8px"
                },
                "nav-link-selected": {"background-color": "#6366f1", "color": "white"},
            }
        )

        st.session_state["current_page"] = selected

        st.divider()
        
        # Pull display name dynamically from session_state or fall back to mock data
        display_name = st.session_state.get("user_name", USER_PROFILE.get("name", "Sandya"))

        # User Mini Card
        st.markdown(
            f"""
            <div style='padding: 10px; border-radius: 10px; background: rgba(150,150,150,0.1); display: flex; align-items: center; gap: 10px;'>
                <img src='{USER_PROFILE["avatar"]}' width='36' height='36' style='border-radius: 50%;'>
                <div>
                    <div style='font-weight: 600; font-size: 14px;'>{display_name}</div>
                    <div style='font-size: 11px; color: gray;'>{USER_PROFILE["plan"]}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
import streamlit as st
from streamlit_option_menu import option_menu
from data.mock_data import USER_PROFILE

def render_sidebar():
    with st.sidebar:
        st.markdown("<h3 style='color: #0056b4; margin-bottom: 0;'>🤖 AI Assistant</h3>", unsafe_allow_html=True)
        st.caption("Public Testing Environment")
        
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
                "icon": {"color": "#0056b4", "font-size": "16px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "4px 0",
                    "border-radius": "6px"
                },
                "nav-link-selected": {"background-color": "#0056b4", "color": "white"},
            }
        )

        st.session_state["current_page"] = selected

        st.divider()
        
        display_name = st.session_state.get("user_name", USER_PROFILE.get("name", "Guest User"))
        avatar_url = USER_PROFILE.get("avatar", "https://api.dicebear.com/7.x/avataaars/svg?seed=Guest")
        plan_name = USER_PROFILE.get("plan", "Public Tester")

        # User Mini Card
        st.markdown(
            f"""
            <div style='padding: 10px; border-radius: 6px; background: #ffffff; border: 1px solid #cbd5e1; display: flex; align-items: center; gap: 10px;'>
                <img src='{avatar_url}' width='36' height='36' style='border-radius: 50%;'>
                <div>
                    <div style='font-weight: 600; font-size: 14px; color: #262626;'>{display_name}</div>
                    <div style='font-size: 11px; color: #595959;'>{plan_name}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
import streamlit as st
from components.header import render_header
from components.footer import render_footer

def render_home_page():
    user_name = st.session_state.get("user_name", "Guest")
    render_header("AI Assistant", f"Welcome, {user_name}.")

    st.markdown(
        """
        <div class="custom-card">
            <h3 style="margin-top:0; color: #0056b4;">Public Testing Workspace</h3>
            <p>Welcome to the AI testing environment. You can ask questions, generate code, or draft content directly through the chat tab.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💬 Start Chatting Now", type="primary", use_container_width=True, key="home_start_chat_btn"):
            st.session_state["current_page"] = "Chat"
            st.rerun()
    with col2:
        if st.button("⚙️ Configure Settings", use_container_width=True, key="home_settings_btn"):
            st.session_state["current_page"] = "Settings"
            st.rerun()

    render_footer()
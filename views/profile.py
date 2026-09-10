import time
import streamlit as st
from components.header import render_header
from components.footer import render_footer

def render_profile_page():
    render_header("User Profile & Telemetry", "Live metrics and session information.")

    # Calculate Real Session Duration
    elapsed_seconds = int(time.time() - st.session_state.get("session_start_time", time.time()))
    minutes, seconds = divmod(elapsed_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    if hours > 0:
        duration_str = f"{hours}h {minutes}m"
    elif minutes > 0:
        duration_str = f"{minutes}m {seconds}s"
    else:
        duration_str = f"{seconds}s"

    # Calculate Total Messages and Estimated Tokens
    messages = st.session_state.get("messages", [])
    user_msgs = [m for m in messages if m["role"] == "user"]
    total_chars = sum(len(m.get("content", "")) for m in messages)
    estimated_tokens = round(total_chars / 4)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 👤 User Information")
        st.info(f"**Identified Device:** {st.session_state.get('user_name', 'Guest')}")

    with col2:
        current_name = st.text_input("Personalized Name", value=st.session_state.get("user_name", "Guest"), key="profile_name_input")
        if current_name != st.session_state.get("user_name"):
            st.session_state["user_name"] = current_name
            st.toast("✅ Name updated!")
            st.rerun()

    st.divider()
    st.subheader("📊 Real-Time Active Session Statistics")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Session Time", duration_str)
    m2.metric("Messages Sent", f"{len(user_msgs)}")
    m3.metric("Total Messages", f"{len(messages)}")
    m4.metric("Est. Tokens Used", f"{estimated_tokens:,}")

    st.caption("Note: All session metrics and conversation logs are temporary and cleared upon closing this browser tab.")
    render_footer()
import streamlit as st
from components.header import render_header
from components.cards import render_feature_card
from components.footer import render_footer
from data.mock_data import FEATURE_CARDS

def render_home_page():
    render_header("Personal AI", "Your private AI companion for thinking, creating, and getting things done.")

    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Think faster. Build smarter.")
        st.write(
            "Designed for seamlessly managing workflows, organizing daily plans, and unlocking creative velocity "
            "with context-aware artificial intelligence."
        )
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("🚀 Start Chatting", type="primary", use_container_width=True):
                st.session_state["current_page"] = "Chat"
                st.rerun()
        with btn_col2:
            if st.button("✨ Explore Features", use_container_width=True):
                st.toast("Explore feature cards below!")

    st.space(2)
    st.subheader("Core Capabilities")
    
    # Feature Cards Grid
    cols = st.columns(3)
    for idx, feature in enumerate(FEATURE_CARDS):
        with cols[idx % 3]:
            render_feature_card(feature["title"], feature["description"])

    render_footer()
import streamlit as st
from components.header import render_header
from components.footer import render_footer

def render_settings_page():
    render_header("Settings", "Manage preferences, interface styles, and system properties.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Appearance", "Chat Preferences", "Personalization", "Privacy", "About"])

    with tab1:
        st.selectbox("Theme Mode", ["System Default", "Light Mode", "Dark Mode"])
        st.select_slider("Font Size", options=["Small", "Medium", "Large"], value="Medium")

    with tab2:
        st.checkbox("Press Enter to Send", value=True)
        st.checkbox("Display Timestamps", value=True)
        st.checkbox("Enable Streaming Responses", value=True)
        st.checkbox("Audio Feedback", value=False)

    with tab3:
        st.text_input("Assistant Custom Name", value="Personal AI")
        st.text_input("User Name", value="Alex Morgan")
        st.text_area("Custom System Instructions", placeholder="e.g., Keep technical answers concise and formatted with tables.")

    with tab4:
        st.button("Export Chat History")
        st.button("Clear All Active Sessions", type="primary")
        st.button("Delete Account & Data", type="primary")

    with tab5:
        st.markdown("**Application:** Personal Chatbot Shell")
        st.markdown("**Version:** 1.0.0-phase1")
        st.markdown("**Environment:** GitHub Codespaces / Streamlit")

    render_footer()
import streamlit as st

def render_footer():
    st.markdown(
        """
        <div class="footer-text">
            Personal AI v1.0.0 Frontend Shell • AI can make mistakes. Verify important information.
        </div>
        """,
        unsafe_allow_html=True
    )
import streamlit as st

def render_footer():
    st.markdown(
        """
        <div class="footer-text">
             AI can make mistakes. Verify important information.
        </div>
        """,
        unsafe_allow_html=True
    )
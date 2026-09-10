import streamlit as st

def render_header(title: str, subtitle: str = ""):
    st.markdown(f"<h2 style='margin:0; font-weight: 600; color: #000000;'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p style='margin-top:0.2rem; color: #71717a; font-size: 0.875rem;'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 1rem 0; border: none; border-top: 1px solid #e4e4e7;'>", unsafe_allow_html=True)
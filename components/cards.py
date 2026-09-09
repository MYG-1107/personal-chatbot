import streamlit as st

def render_feature_card(title: str, description: str):
    st.markdown(
        f"""
        <div class="custom-card">
            <h4 style="margin-top: 0; color: #6366f1;">{title}</h4>
            <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 0;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_prompt_card(title: str, desc: str, icon: str):
    return st.button(f"{icon} **{title}**\n\n_{desc}_", use_container_width=True)
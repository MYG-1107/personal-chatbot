import streamlit as st

def render_header(title: str, subtitle: str = ""):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"<h2 style='margin:0; font-weight: 600; color: #0f172a;'>{title}</h2>", unsafe_allow_html=True)
        if subtitle:
            st.markdown(f"<p style='margin:0; color: #64748b; font-size: 0.9rem;'>{subtitle}</p>", unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div style="text-align: right;">
                <span class="status-pill">● Gemini 2.0 Active</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("<hr style='margin: 1rem 0 1.5rem 0; border: none; border-top: 1px solid #e2e8f0;'>", unsafe_allow_html=True)
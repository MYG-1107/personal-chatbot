import streamlit as st

def render_header(title: str, subtitle: str = ""):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"<h2 style='margin-bottom: 0px;'>{title}</h2>", unsafe_allow_html=True)
        if subtitle:
            st.caption(subtitle)
    with col2:
        st.markdown(
            """
            <div style="text-align: right; padding-top: 10px;">
                <span class="status-badge">● Engine Active</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()
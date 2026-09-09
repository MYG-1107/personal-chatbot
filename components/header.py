import streamlit as st

def render_header(title: str, subtitle: str = ""):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title(title)
        if subtitle:
            st.caption(subtitle)
    with col2:
        st.markdown(
            """
            <div style="text-align: right; padding-top: 15px;">
                <span class="status-indicator"></span> System Ready
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()
import streamlit as st
from components.header import render_header
from components.footer import render_footer
from data.mock_data import MOCK_CONVERSATION_HISTORY

def render_history_page():
    render_header("Conversation History", "Search and manage past conversation sessions.")

    # Search Bar
    st.text_input("🔍 Search conversations...", key="history_search")

    # Categories Timeline
    for category, threads in MOCK_CONVERSATION_HISTORY.items():
        st.subheader(category)
        for item in threads:
            col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
            with col1:
                pin = "⭐ " if item["favorite"] else ""
                st.write(f"{pin}**{item['title']}**")
            with col2:
                st.caption(item["time"])
            with col3:
                if st.button("✏️", key=f"edit_{item['id']}"):
                    st.toast(f"Rename {item['id']}")
            with col4:
                if st.button("🗑️", key=f"del_{item['id']}"):
                    st.toast(f"Deleted thread {item['id']}")
        st.divider()

    render_footer()
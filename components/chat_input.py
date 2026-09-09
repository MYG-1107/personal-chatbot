import streamlit as st

def render_chat_input():
    with st.container():
        user_input = st.chat_input("Type your message here...")
        
        col1, col2, col3 = st.columns([1, 1, 6])
        with col1:
            st.button("📎 Attach", help="Upload images or documents")
        with col2:
            st.button("🎙️ Voice", help="Voice input mode")
        with col3:
            st.caption("Press Enter to send • Token counter: ~240/8000")
            
    return user_input
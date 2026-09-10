import streamlit as st

def render_message(role: str, content: str, timestamp: str = "Just now", msg_index: int = 0):
    # Black and white text indicators instead of colored emojis
    label = "YOU" if role == "user" else "AI"
    
    with st.chat_message(role, avatar=None):
        st.markdown(f"**{label}**")
        st.markdown(content)
        
        if role == "assistant":
            col1, col2, _ = st.columns([0.15, 0.15, 0.70])
            with col1:
                st.button("Copy", key=f"copy_{msg_index}", help="Copy response")
            with col2:
                st.button("Retry", key=f"retry_{msg_index}", help="Regenerate response")
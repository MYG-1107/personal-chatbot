import streamlit as st

def render_message(role: str, content: str, timestamp: str = "Just now", msg_index: int = 0):
    avatar = "👤" if role == "user" else "✨"
    
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)
        
        # Action row for Assistant responses
        if role == "assistant":
            col1, col2, col3, _ = st.columns([0.08, 0.08, 0.08, 0.76])
            with col1:
                st.button("📋", key=f"copy_{msg_index}", help="Copy response")
            with col2:
                st.button("🔄", key=f"retry_{msg_index}", help="Regenerate")
            with col3:
                st.button("👍", key=f"like_{msg_index}", help="Good response")
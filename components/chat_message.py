import streamlit as st

def render_message(role: str, content: str, timestamp: str = "Just now", msg_index: int = 0):
    if role == "user":
        st.markdown(
            f"""
            <div class="chat-bubble-user">
                <div>{content}</div>
                <div style="font-size: 0.7rem; opacity: 0.8; text-align: right; margin-top: 4px;">{timestamp}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-bubble-assistant">
                <div>{content}</div>
                <div style="font-size: 0.7rem; color: #595959; margin-top: 4px;">{timestamp}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Action Toolbar with unique keys based on msg_index
        col1, col2, col3, _ = st.columns([1, 1, 1, 10])
        with col1:
            st.button("📋", key=f"copy_{msg_index}", help="Copy message")
        with col2:
            st.button("🔄", key=f"regen_{msg_index}", help="Regenerate response")
        with col3:
            st.button("👍", key=f"like_{msg_index}", help="Helpful")
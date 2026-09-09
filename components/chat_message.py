import streamlit as st

def render_message(role: str, content: str, timestamp: str = "Just now"):
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
                <div style="font-size: 0.7rem; color: #64748b; margin-top: 4px;">{timestamp}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Action Toolbar
        col1, col2, col3, _ = st.columns([1, 1, 1, 10])
        with col1:
            st.button("📋", key=f"copy_{hash(content)}", help="Copy message")
        with col2:
            st.button("🔄", key=f"regen_{hash(content)}", help="Regenerate")
        with col3:
            st.button("👍", key=f"like_{hash(content)}", help="Helpful")
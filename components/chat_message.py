import streamlit as st

def render_message(role: str, content: str, timestamp: str = "Just now", msg_index: int = 0):
    if role == "user":
        st.markdown(
            f"""
            <div class="chat-container-user">
                <div class="chat-bubble-user">
                    <div>{content}</div>
                    <span class="message-time" style="text-align: right; color: #94a3b8;">{timestamp}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-container-assistant">
                <div class="chat-bubble-assistant">
                    <div>{content}</div>
                    <span class="message-time">{timestamp}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Subtle Action Buttons
        cols = st.columns([1, 1, 1, 12])
        with cols[0]:
            st.button("📋", key=f"copy_{msg_index}", help="Copy response")
        with cols[1]:
            st.button("🔄", key=f"regen_{msg_index}", help="Retry query")
        with cols[2]:
            st.button("👍", key=f"like_{msg_index}", help="Good response")
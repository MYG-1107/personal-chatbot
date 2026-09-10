import streamlit as st
from components.header import render_header
from components.footer import render_footer

def render_history_page():
    render_header("Conversation History", "Active session log (cleared automatically on window close)")

    # Fetch active session messages
    messages = st.session_state.get("messages", [])

    # Search & Clear Actions
    col_search, col_clear = st.columns([4, 1])
    with col_search:
        search_query = st.text_input("🔍 Search active session...", key="history_search", label_visibility="collapsed", placeholder="Search active session...")
    with col_clear:
        if st.button("🗑️ Clear History", type="primary", use_container_width=True):
            st.session_state["messages"] = []
            st.toast("Active session history cleared!")
            st.rerun()

    st.divider()

    if not messages:
        st.info("No active conversation history found in this session. Go to the **Chat** workspace to start a conversation!")
    else:
        st.subheader("Active Session Log")
        
        # Filter messages if search query is entered
        filtered_messages = [
            msg for msg in messages 
            if not search_query or search_query.lower() in msg.get("content", "").lower()
        ]

        if not filtered_messages:
            st.warning("No messages matched your search query.")
        else:
            for idx, msg in enumerate(filtered_messages):
                role_label = "👤 **User**" if msg["role"] == "user" else "🤖 **Assistant**"
                timestamp = msg.get("timestamp", "Just now")
                
                with st.container():
                    col1, col2 = st.columns([6, 1])
                    with col1:
                        st.markdown(f"{role_label}: {msg['content']}")
                    with col2:
                        st.caption(timestamp)
                    st.divider()

    render_footer()

# Execute page render
render_history_page()
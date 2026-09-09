import streamlit as st
from components.header import render_header
from components.chat_message import render_message
from components.chat_input import render_chat_input
from components.cards import render_prompt_card
from components.footer import render_footer
from data.mock_data import SUGGESTED_PROMPTS, INITIAL_CHAT_MESSAGES

def render_chat_page():
    render_header("Chat Workspace", "Active Session: General Context")

    if "messages" not in st.session_state:
        st.session_state["messages"] = INITIAL_CHAT_MESSAGES.copy()

    # Empty State Configuration
    if len(st.session_state["messages"]) == 0:
        st.markdown("<h3 style='text-align: center;'>How can I help you today?</h3>", unsafe_allow_html=True)
        st.caption("Choose a suggested prompt or type your query below to begin.")
        st.space(1)
        
        cols = st.columns(2)
        for idx, prompt in enumerate(SUGGESTED_PROMPTS):
            with cols[idx % 2]:
                if render_prompt_card(prompt["title"], prompt["desc"], prompt["icon"]):
                    st.session_state["messages"].append({
                        "role": "user",
                        "content": prompt["title"],
                        "timestamp": "Just now"
                    })
                    st.session_state["messages"].append({
                        "role": "assistant",
                        "content": f"Here is a mock structure for: **{prompt['title']}**. How would you like to customize it?",
                        "timestamp": "Just now"
                    })
                    st.rerun()
    else:
        # Render Active Conversation
        for msg in st.session_state["messages"]:
            render_message(msg["role"], msg["content"], msg.get("timestamp", "Just now"))

    # Chat Input Handler
    user_query = render_chat_input()
    if user_query:
        st.session_state["messages"].append({"role": "user", "content": user_query, "timestamp": "Just now"})
        st.session_state["messages"].append({
            "role": "assistant",
            "content": f"I received: '{user_query}'. (Frontend mock response - Phase 2 will execute live LLM inference).",
            "timestamp": "Just now"
        })
        st.rerun()

    render_footer()
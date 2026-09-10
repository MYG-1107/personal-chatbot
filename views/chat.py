import streamlit as st
import google.generativeai as genai
from components.header import render_header
from components.chat_message import render_message
from components.chat_input import render_chat_input
from components.cards import render_prompt_card
from components.footer import render_footer
from data.mock_data import SUGGESTED_PROMPTS

def generate_ai_response(prompt: str, model_name: str = "gemini-1.5-flash") -> str:
    """Rotates through GEMINI_KEYS from secrets.toml if quota/rate errors occur."""
    api_keys = st.secrets.get("GEMINI_KEYS", [])
    
    if not api_keys:
        return "⚠️ Error: No API keys configured in .streamlit/secrets.toml."

    if "active_key_index" not in st.session_state:
        st.session_state["active_key_index"] = 0

    total_keys = len(api_keys)
    attempts = 0

    while attempts < total_keys:
        current_index = st.session_state["active_key_index"]
        current_key = api_keys[current_index]

        try:
            genai.configure(api_key=current_key)
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            # Rotate to next key on failure
            st.session_state["active_key_index"] = (current_index + 1) % total_keys
            attempts += 1
            st.toast(f"⚠️ Key #{current_index + 1} limit reached. Switched to Key #{st.session_state['active_key_index'] + 1}...")

    return "❌ All API keys in your rotation pool have reached their rate limits or failed."


def render_chat_page():
    render_header("Chat Workspace", "Active Session: Live Gemini AI Engine")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Empty State Configuration
    if len(st.session_state["messages"]) == 0:
        st.markdown("<h3 style='text-align: center;'>How can I help you today?</h3>", unsafe_allow_html=True)
        st.caption("Choose a suggested prompt or type your query below to begin.")
        
        cols = st.columns(2)
        for idx, prompt in enumerate(SUGGESTED_PROMPTS):
            with cols[idx % 2]:
                if render_prompt_card(prompt["title"], prompt["desc"], prompt["icon"]):
                    st.session_state["messages"].append({
                        "role": "user",
                        "content": prompt["title"],
                        "timestamp": "Just now"
                    })
                    
                    with st.spinner("Generating AI response..."):
                        response_text = generate_ai_response(prompt["title"])
                        
                    st.session_state["messages"].append({
                        "role": "assistant",
                        "content": response_text,
                        "timestamp": "Just now"
                    })
                    st.rerun()
    else:
        # Render Active Conversation with unique widget index
        for idx, msg in enumerate(st.session_state["messages"]):
            render_message(
                role=msg["role"],
                content=msg["content"],
                timestamp=msg.get("timestamp", "Just now"),
                msg_index=idx
            )

    # Chat Input Handler
    user_query = render_chat_input()
    if user_query:
        st.session_state["messages"].append({
            "role": "user",
            "content": user_query,
            "timestamp": "Just now"
        })
        
        with st.spinner("Generating AI response..."):
            response_text = generate_ai_response(user_query)
            
        st.session_state["messages"].append({
            "role": "assistant",
            "content": response_text,
            "timestamp": "Just now"
        })
        st.rerun()

    render_footer()
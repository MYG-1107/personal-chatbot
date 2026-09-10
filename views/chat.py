import streamlit as st
import google.generativeai as genai
from components.header import render_header
from components.chat_message import render_message
from components.chat_input import render_chat_input
from components.cards import render_prompt_card
from components.footer import render_footer
from data.mock_data import SUGGESTED_PROMPTS

def generate_ai_response(prompt: str, model_name: str = "gemini-3.6-flash") -> str:
    """Generates an AI response using a single API key."""
    # Retrieve key (falls back to first element of GEMINI_KEYS if GEMINI_API_KEY isn't set)
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        keys_list = st.secrets.get("GEMINI_KEYS", [])
        if keys_list:
            api_key = keys_list[0]

    if not api_key:
        return "⚠️ Error: No API key found in .streamlit/secrets.toml."

    # Clean whitespace and accidental surrounding quotes
    clean_key = str(api_key).strip().strip('"').strip("'")

    try:
        genai.configure(api_key=clean_key)
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Google API Error: `{str(e)}`"


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
        # Render Active Conversation
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
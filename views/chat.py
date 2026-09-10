import streamlit as st
import google.generativeai as genai
from components.header import render_header
from components.chat_message import render_message
from components.chat_input import render_chat_input
from data.mock_data import SUGGESTED_PROMPTS

def generate_ai_response(prompt: str) -> str:
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        keys_list = st.secrets.get("GEMINI_KEYS", [])
        if keys_list:
            api_key = keys_list[0]

    if not api_key:
        return "Error: No API key configured in .streamlit/secrets.toml."

    clean_key = str(api_key).strip().strip('"').strip("'")

    try:
        genai.configure(api_key=clean_key)
        model = genai.GenerativeModel("gemini-3.6-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Google API Error: `{str(e)}`"

def render_chat_page():
    render_header("Chat", "Direct Text Workspace")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Clean Welcome Canvas
    if len(st.session_state["messages"]) == 0:
        st.markdown(
            """
            <div style='padding: 2rem 0 1rem 0;'>
                <h3 style='font-weight: 600; color: #000000; margin-bottom: 0.5rem;'>How can I help you today?</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Minimalist Prompt Cards
        cols = st.columns(2)
        for idx, prompt in enumerate(SUGGESTED_PROMPTS):
            with cols[idx % 2]:
                if st.button(f"**{prompt['title']}**\n\n{prompt['desc']}", use_container_width=True, key=f"card_{idx}"):
                    st.session_state["messages"].append({"role": "user", "content": prompt["title"]})
                    st.rerun()

    # Conversation History
    for idx, msg in enumerate(st.session_state["messages"]):
        render_message(
            role=msg["role"],
            content=msg["content"],
            timestamp=msg.get("timestamp", "Just now"),
            msg_index=idx
        )

    # Simple Single Input Bar
    user_query = render_chat_input()
    if user_query:
        st.session_state["messages"].append({"role": "user", "content": user_query})
        st.rerun()

    # Generate Response on New Prompt
    if st.session_state["messages"] and st.session_state["messages"][-1]["role"] == "user":
        latest_prompt = st.session_state["messages"][-1]["content"]
        with st.spinner("Processing..."):
            response_text = generate_ai_response(latest_prompt)
        st.session_state["messages"].append({"role": "assistant", "content": response_text})
        st.rerun()
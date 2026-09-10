import streamlit as st
import google.generativeai as genai
from components.header import render_header
from components.chat_message import render_message
from components.footer import render_footer
from data.mock_data import SUGGESTED_PROMPTS

def generate_ai_response(prompt: str) -> str:
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        keys_list = st.secrets.get("GEMINI_KEYS", [])
        if keys_list:
            api_key = keys_list[0]

    if not api_key:
        return "⚠️ Error: No API key configured in .streamlit/secrets.toml."

    clean_key = str(api_key).strip().strip('"').strip("'")

    try:
        genai.configure(api_key=clean_key)
        # Using Google's flash model for high speed
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Google API Error: `{str(e)}`"

def render_chat_page():
    render_header("AI Workspace", "Personal Companion")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Empty State Canvas (Gemini / ChatGPT Welcome Style)
    if len(st.session_state["messages"]) == 0:
        st.markdown(
            """
            <div style='text-align: center; padding: 2rem 0 1.5rem 0;'>
                <h1 style='font-size: 2.2rem; font-weight: 600; color: #0f172a; margin-bottom: 0.5rem;'>What can I help with today?</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Suggested Prompt Cards Grid
        cols = st.columns(2)
        for idx, prompt in enumerate(SUGGESTED_PROMPTS):
            with cols[idx % 2]:
                if st.button(f"{prompt['icon']} **{prompt['title']}**\n\n_{prompt['desc']}_", use_container_width=True, key=f"card_{idx}"):
                    st.session_state["messages"].append({"role": "user", "content": prompt["title"]})
                    with st.spinner("Thinking..."):
                        response_text = generate_ai_response(prompt["title"])
                    st.session_state["messages"].append({"role": "assistant", "content": response_text})
                    st.rerun()

    # Active Conversation History
    for idx, msg in enumerate(st.session_state["messages"]):
        render_message(
            role=msg["role"],
            content=msg["content"],
            timestamp=msg.get("timestamp", "Just now"),
            msg_index=idx
        )

    # Sticky Floating Chat Input
    user_query = st.chat_input("Ask anything...")
    if user_query:
        st.session_state["messages"].append({"role": "user", "content": user_query})
        st.rerun()

    # Trigger API response on new prompt submission
    if st.session_state["messages"] and st.session_state["messages"][-1]["role"] == "user":
        latest_prompt = st.session_state["messages"][-1]["content"]
        with st.spinner("Generating response..."):
            response_text = generate_ai_response(latest_prompt)
        st.session_state["messages"].append({"role": "assistant", "content": response_text})
        st.rerun()

    render_footer()
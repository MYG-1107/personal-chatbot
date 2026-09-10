import os
import streamlit as st
from google import genai
from components.header import render_header
from components.chat_message import render_message
from components.chat_input import render_chat_input
from components.cards import render_prompt_card
from components.footer import render_footer
from data.mock_data import SUGGESTED_PROMPTS

def get_ai_response(prompt_text):
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ **API Key Missing**: Add your `GEMINI_API_KEY` into `.streamlit/secrets.toml`."
    
    # Read Personalization Settings
    assistant_name = st.session_state.get("assistant_name", "Personal AI")
    user_name = st.session_state.get("user_name", "Alex")
    custom_instructions = st.session_state.get("custom_instructions", "")

    # Construct System Prompt Context
    system_prompt = f"Your name is '{assistant_name}'. You are assisting '{user_name}'."
    if custom_instructions.strip():
        system_prompt += f" Follow these special instructions: {custom_instructions}"
        
    full_prompt = f"System Context: {system_prompt}\n\nUser Question: {prompt_text}"

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
        )
        return response.text
    except Exception as e:
        return f"⚠️ **AI Error**: {str(e)}"

def render_chat_page():
    assistant_title = st.session_state.get("assistant_name", "Personal AI Workspace")
    render_header(assistant_title, "Active Session: Live Gemini AI Engine")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Handle Active Regeneration Trigger
    if "regen_target" in st.session_state:
        target_idx = st.session_state.pop("regen_target")
        if target_idx > 0 and st.session_state["messages"][target_idx - 1]["role"] == "user":
            user_prompt = st.session_state["messages"][target_idx - 1]["content"]
            with st.spinner("Regenerating AI response..."):
                new_reply = get_ai_response(user_prompt)
            st.session_state["messages"][target_idx]["content"] = new_reply
            st.toast("🔄 Response regenerated!")
            st.rerun()

    # Display Empty State
    if len(st.session_state["messages"]) == 0:
        user_name = st.session_state.get("user_name", "Alex")
        st.markdown(f"<h3 style='text-align: center;'>Hello {user_name}, how can I help you today?</h3>", unsafe_allow_html=True)
        st.caption("Choose a suggested prompt or type your query below to begin.")
        
        cols = st.columns(2)
        for idx, prompt in enumerate(SUGGESTED_PROMPTS):
            with cols[idx % 2]:
                if render_prompt_card(prompt["title"], prompt["desc"], prompt["icon"]):
                    st.session_state["messages"].append({"role": "user", "content": prompt["title"], "timestamp": "Just now"})
                    with st.spinner("AI is thinking..."):
                        reply = get_ai_response(prompt["title"])
                    st.session_state["messages"].append({"role": "assistant", "content": reply, "timestamp": "Just now"})
                    st.rerun()
    else:
        # Display Message History
        for idx, msg in enumerate(st.session_state["messages"]):
            render_message(
                role=msg["role"], 
                content=msg["content"], 
                msg_index=idx, 
                timestamp=msg.get("timestamp", "Just now")
            )

    # Process New Input
    user_query = render_chat_input()
    if user_query:
        st.session_state["messages"].append({"role": "user", "content": user_query, "timestamp": "Just now"})
        st.rerun()

    # Trigger AI response
    if st.session_state["messages"] and st.session_state["messages"][-1]["role"] == "user":
        latest_user_msg = st.session_state["messages"][-1]["content"]
        with st.spinner("AI is thinking..."):
            reply = get_ai_response(latest_user_msg)
        st.session_state["messages"].append({"role": "assistant", "content": reply, "timestamp": "Just now"})
        st.rerun()

    render_footer()

# Execute page
render_chat_page()
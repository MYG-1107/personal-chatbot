import json
import streamlit as st
from components.header import render_header
from components.footer import render_footer

def init_settings_state():
    """Ensure default settings exist in session_state."""
    defaults = {
        "theme_mode": "System Default",
        "font_size": "Medium",
        "enter_to_send": True,
        "show_timestamps": True,
        "enable_streaming": True,
        "audio_feedback": False,
        "assistant_name": "Maya",
        "user_name": "Sandya",
        "custom_instructions": "Be helpful, concise, and structured in responses."
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def render_settings_page():
    init_settings_state()
    render_header("Settings", "Manage preferences, UI styling, and AI personalization.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎨 Appearance", 
        "💬 Chat Preferences", 
        "🧠 Personalization", 
        "🔒 Privacy & Data", 
        "ℹ️ About"
    ])

    # ------------------ TAB 1: APPEARANCE ------------------
    with tab1:
        st.subheader("Visual Preferences")
        
        theme = st.selectbox(
            "Theme Mode", 
            ["System Default", "Light Mode", "Dark Mode"],
            index=["System Default", "Light Mode", "Dark Mode"].index(st.session_state["theme_mode"])
        )
        st.session_state["theme_mode"] = theme

        font_size = st.select_slider(
            "Font Size", 
            options=["Small", "Medium", "Large"], 
            value=st.session_state["font_size"],
            help="Adjust text scaling across the entire workspace."
        )
        if font_size != st.session_state["font_size"]:
            st.session_state["font_size"] = font_size
            st.toast(f"Font size updated to {font_size}!")
            st.rerun()

    # ------------------ TAB 2: CHAT PREFERENCES ------------------
    with tab2:
        st.subheader("Interaction Controls")
        
        st.session_state["enter_to_send"] = st.checkbox(
            "Press Enter to Send Messages", 
            value=st.session_state["enter_to_send"]
        )
        st.session_state["show_timestamps"] = st.checkbox(
            "Display Timestamps in Messages", 
            value=st.session_state["show_timestamps"]
        )
        st.session_state["enable_streaming"] = st.checkbox(
            "Enable Response Streaming Simulator", 
            value=st.session_state["enable_streaming"]
        )
        st.session_state["audio_feedback"] = st.checkbox(
            "Audio Feedback (Chimes on completion)", 
            value=st.session_state["audio_feedback"]
        )

    # ------------------ TAB 3: PERSONALIZATION ------------------
    with tab3:
        st.subheader("AI Companion Identity")
        
        new_assistant_name = st.text_input(
            "Assistant Name", 
            value=st.session_state["assistant_name"],
            help="The AI will address itself by this name."
        )
        
        new_user_name = st.text_input(
            "Your Name", 
            value=st.session_state["user_name"],
            help="How the assistant should address you."
        )

        new_instructions = st.text_area(
            "Custom System Instructions", 
            value=st.session_state["custom_instructions"],
            height=120,
            placeholder="e.g. Always format responses in Markdown with bullet points. Speak in a friendly tone.",
            help="These instructions are sent to Gemini to shape every AI response."
        )

        if st.button("💾 Save Personalization Profile", type="primary"):
            st.session_state["assistant_name"] = new_assistant_name
            st.session_state["user_name"] = new_user_name
            st.session_state["custom_instructions"] = new_instructions
            st.toast("✅ Personalization saved! Gemini will now use these instructions.")

    # ------------------ TAB 4: PRIVACY & DATA ------------------
    with tab4:
        st.subheader("Data Management")
        
        messages = st.session_state.get("messages", [])
        
        # 1. EXPORT CHAT HISTORY
        json_data = json.dumps(messages, indent=2)
        st.download_button(
            label="📥 Export Session Chat History (JSON)",
            data=json_data,
            file_name="chat_history.json",
            mime="application/json",
            disabled=len(messages) == 0
        )

        st.divider()

        col_clear, col_delete = st.columns(2)
        
        # 2. CLEAR ACTIVE CHAT SESSION
        with col_clear:
            if st.button("🧹 Clear Current Active Chat", use_container_width=True):
                st.session_state["messages"] = []
                st.toast("Active session chat messages cleared!")
                st.rerun()

        # 3. RESET ENTIRE APP STATE
        with col_delete:
            if st.button("🚨 Reset All Settings & Data", type="primary", use_container_width=True):
                st.session_state.clear()
                st.toast("All settings and session data reset to defaults.")
                st.rerun()

    # ------------------ TAB 5: ABOUT ------------------
    with tab5:
        st.markdown("**Application:** Personal AI Workspace")
        st.markdown("**Version:** 1.2.0")
        st.markdown("**AI Engine:** Google Gemini 2.5 Flash")
        st.markdown("**Environment:** GitHub Codespaces / Streamlit")

    render_footer()

# Execute page
render_settings_page()
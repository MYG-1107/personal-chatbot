import json
import streamlit as st
import streamlit.components.v1 as components

def render_message(role: str, content: str, msg_index: int, timestamp: str = "Just now"):
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
        
        # 1. DIRECT HTML/JS COPY BUTTON
        with col1:
            js_text = json.dumps(content)
            copy_html = f"""
            <div style="display: flex; align-items: center; margin-top: -2px;">
                <button id="btn_{msg_index}" onclick="copyText_{msg_index}()" style="
                    background: #ffffff;
                    border: 1px solid #cbd5e1;
                    border-radius: 6px;
                    padding: 3px 8px;
                    cursor: pointer;
                    font-size: 13px;
                " title="Copy to clipboard">📋</button>
            </div>
            <script>
            function copyText_{msg_index}() {{
                const text = {js_text};
                const btn = document.getElementById("btn_{msg_index}");
                
                function onSuccess() {{
                    btn.innerText = "✅";
                    setTimeout(() => {{ btn.innerText = "📋"; }}, 1500);
                }}

                if (navigator.clipboard && window.isSecureContext) {{
                    navigator.clipboard.writeText(text).then(onSuccess).catch(() => {{
                        fallbackCopy(text, onSuccess);
                    }});
                }} else {{
                    fallbackCopy(text, onSuccess);
                }}
            }}

            function fallbackCopy(text, cb) {{
                const textArea = document.createElement("textarea");
                textArea.value = text;
                textArea.style.position = "fixed";
                textArea.style.left = "-999999px";
                document.body.appendChild(textArea);
                textArea.focus();
                textArea.select();
                try {{
                    document.execCommand('copy');
                    cb();
                }} catch (err) {{
                    console.error('Copy failed', err);
                }}
                textArea.remove();
            }}
            </script>
            """
            components.html(copy_html, height=35)

        # 2. REGENERATE BUTTON
        with col2:
            if st.button("🔄", key=f"regen_{msg_index}", help="Regenerate this response"):
                st.session_state["regen_target"] = msg_index
                st.rerun()

        # 3. LIKE BUTTON
        with col3:
            is_liked = st.session_state.get(f"liked_{msg_index}", False)
            like_icon = "❤️" if is_liked else "👍"
            if st.button(like_icon, key=f"like_{msg_index}", help="Helpful response"):
                st.session_state[f"liked_{msg_index}"] = not is_liked
                if not is_liked:
                    st.toast("👍 Feedback saved: Marked as helpful!")
                else:
                    st.toast("Feedback updated.")
                st.rerun()
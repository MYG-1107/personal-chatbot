import streamlit as st
from components.header import render_header
from components.footer import render_footer
from data.mock_data import USER_PROFILE

def render_profile_page():
    render_header("User Profile", "Manage your credentials and subscription metrics.")

    # Fetch user name dynamically from session state
    current_name = st.session_state.get("user_name", USER_PROFILE.get("name", "Sandya"))

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(USER_PROFILE["avatar"], width=120)
        st.button("Change Avatar")

    with col2:
        # Interactive Name Input field linked to session state
        updated_name = st.text_input("Full Name", value=current_name)
        if updated_name != current_name:
            st.session_state["user_name"] = updated_name
            st.toast("✅ Profile name updated successfully!")
            st.rerun()

        st.text_input("Email", value=USER_PROFILE["email"])
        st.text_input("Current Plan", value=USER_PROFILE["plan"], disabled=True)
        st.caption(f"Member since {USER_PROFILE['joined']}")

    st.divider()
    st.subheader("Usage Statistics")
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Chats", "128")
    m2.metric("Tokens Consumed", "45.2k")
    m3.metric("Saved Prompts", "12")

    st.divider()
    if st.button("Log Out", type="primary"):
        st.info("User session terminated.")

    render_footer()

# Execute page render
render_profile_page()
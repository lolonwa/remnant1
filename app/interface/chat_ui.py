"""
Streamlit chatbot UI for the Remnant Migration Assistant
"""

import streamlit as st
from chat_manager import ChatManager
from auth import login_screen
from firebase_verify import verify_firebase_token

st.set_page_config(page_title="Remnant Migration Assistant", page_icon="🌏")

# --- Authentication ---
if "user" not in st.session_state:
    login_method = st.radio(
        "Choose login method:",
        ["Email/Password", "Social (Google/Yahoo/Facebook/Phone)"]
    )
    if login_method == "Email/Password":
        st.info("Use your email and password to log in or sign up below.")
        logged_in = login_screen()
        if not logged_in:
            st.stop()
    else:
        st.caption("Paste your Firebase ID token from Google/Yahoo/Facebook/Phone login below.")
        st.info("Don't have a token? Use the Email/Password option above to log in or sign up directly.")

        # --- Google Sign-In Button (shows token in alert) ---
        GOOGLE_CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com"  # Replace with your client ID
        st.markdown(f"""
            <div id="g_id_onload"
                 data-client_id="{GOOGLE_CLIENT_ID}"
                 data-context="signin"
                 data-ux_mode="popup"
                 data-callback="handleCredentialResponse"
                 data-auto_prompt="false">
            </div>
            <div class="g_id_signin"
                 data-type="standard"
                 data-shape="rectangular"
                 data-theme="outline"
                 data-text="sign_in_with"
                 data-size="large"
                 data-logo_alignment="left">
            </div>
            <script src="https://accounts.google.com/gsi/client" async defer></script>
            <script>
              function handleCredentialResponse(response) {{
                alert("Google ID Token: " + response.credential);
              }}
            </script>
        """, unsafe_allow_html=True)

        id_token = st.text_input("Firebase ID Token")
        if st.button("Login with Token"):
            user_info = verify_firebase_token(id_token)
            if user_info:
                st.session_state["user"] = user_info
                st.success(f"Login successful! Welcome {user_info.get('email', 'user')}")
                st.experimental_rerun()
            else:
                st.error("Invalid or expired token. Please try again.")
        st.stop()  # Stop here if not logged in

# --- Chat UI ---
if "chat" not in st.session_state:
    st.session_state.chat = ChatManager()

chat = st.session_state.chat

# Session state to control ongoing chat
if "chat_active" not in st.session_state:
    st.session_state.chat_active = True

st.title("🧭 Remnant Migration Assistant")
st.caption("Ask me anything about migrating abroad, visas, scholarships, scams, or country options.")

# Stop conversation button
if st.button("🛑 Stop Conversation"):
    st.session_state.chat_active = False
    st.success("Conversation ended. You can start again anytime.")

# Restart conversation button (only if stopped)
if not st.session_state.chat_active:
    if st.button("🔄 Restart Conversation"):
        st.session_state.chat_active = True
        chat.context.clear()  # Reset memory if supported
        st.success("New conversation started!")

# Only show chat if conversation is active
if st.session_state.chat_active:
    user_input = st.chat_input("Ask me anything...")

    if user_input:
        # Display user's message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get LLM response
        response = chat.handle_user_input(user_input)

        # Display assistant's message
        with st.chat_message("assistant"):
            st.markdown(response)
else:
    st.info("🛑 Chat is stopped. Use 'Restart' to begin a new conversation.")

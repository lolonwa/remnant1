"""
Streamlit chatbot UI for the Remnant Migration Assistant
"""

import streamlit as st
from chat_manager import ChatManager
from auth import login_screen
from firebase_verify import verify_firebase_token
import os
from dotenv import load_dotenv
import time

st.set_page_config(page_title="Remnant Migration Assistant", page_icon="🌏")

# --- Load environment variables ---
load_dotenv()

def is_valid_jwt(token):
    # A JWT has three segments separated by dots
    return isinstance(token, str) and token.count('.') == 2

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
        st.info(
            "Don't have a token? "
            "Open the [Get Firebase ID Token page](http://localhost:8083/get_firebase_token.html), sign in with Google, "
            "copy the token (it will be a long string with dots), and paste it here. "
            "Do NOT paste your client ID. Or use the Email/Password option above."
        )

        id_token = st.text_input("Firebase ID Token")
        if st.button("Login with Token"):
            if not is_valid_jwt(id_token):
                st.error("Please paste a valid Firebase ID Token (not your client ID). It should be a long string with two dots.")
            else:
                user_info = verify_firebase_token(id_token)
                if user_info:
                    st.session_state["user"] = user_info
                    st.success(f"Login successful! Welcome {user_info.get('email', 'user')}")
                    time.sleep(5)  # Pause for 2 seconds so user sees the message
                    st.rerun()
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
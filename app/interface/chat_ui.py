"""
Streamlit chatbot UI for the Remnant Migration Assistant
"""

import streamlit as st
from chat_manager import ChatManager

# Set page config
st.set_page_config(page_title="Remnant Migration Assistant", page_icon="🌏")

# Initialize ChatManager once
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

# app/interface/streamlit/chat_ui.py

import streamlit as st
from chat_manager import ChatManager

# Set page config
st.set_page_config(page_title="Remnant Chatbot", page_icon="🧭")

st.title("🧭 Remnant Migration Assistant")

# Initialize session state for chat history and manager
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "manager" not in st.session_state:
    st.session_state.manager = ChatManager()

# Input box for user
user_input = st.chat_input("Say something...")

if user_input:
    # Append user message to history
    st.session_state.chat_history.append(("You", user_input))

    # Get response from chat manager
    response = st.session_state.manager.handle_user_input(user_input)
    st.session_state.chat_history.append(("Remnant", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)

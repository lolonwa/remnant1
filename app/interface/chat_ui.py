"""
Streamlit chatbot UI for the Remnant Migration Assistant
"""

import streamlit as st
from chat_manager import ChatManager
import streamlit as st


# Initialize chat state
if "chat_router" not in st.session_state:
    st.session_state.chat_router = ChatManager()
    st.session_state.messages = []

# Page title
st.set_page_config(page_title="Remnant Migration Chatbot", page_icon="🛂")
st.title("🛂 Remnant Migration Chatbot")
st.write("Ask me anything about moving abroad, visas, scholarships, or avoiding scams!")

# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user's message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from ChatRouter
    response = st.session_state.chat_router.handle_input(user_input)

    # Show bot reply
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Optional: Add a "Stop" button
if st.button("❌ End Conversation"):
    st.session_state.clear()
    st.rerun()

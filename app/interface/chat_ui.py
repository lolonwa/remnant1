import streamlit as st
from chat_manager import ChatManager

# Set page config
st.set_page_config(page_title="Remnant Chatbot", page_icon="🧭")

st.title("🧭 Remnant Migration Assistant")

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "manager" not in st.session_state:
    st.session_state.manager = ChatManager()
if "menu_selected" not in st.session_state:
    st.session_state.menu_selected = False

# 💥 Add Return to Menu Button
if st.button("🔁 Return to Menu"):
    st.session_state.chat_history = []
    st.session_state.manager = ChatManager()
    st.session_state.menu_selected = False
    st.rerun()

# Show menu if not selected yet
if not st.session_state.menu_selected:
    options = [
        "Migration Advice",
        "Scam Detector",
        "Scholarship Finder",
        "Visa Info"
    ]
    choice = st.selectbox("Please choose an option:", options)
    if st.button("Continue"):
        st.session_state.chat_history.append(("You", choice))
        response = st.session_state.manager.handle_user_input(str(options.index(choice) + 1))
        st.session_state.chat_history.append(("Remnant", response))
        st.session_state.menu_selected = True
        st.rerun()

# Chat Input and History
if st.session_state.menu_selected:
    user_input = st.chat_input("Type your answer here...")
    if user_input:
        st.session_state.chat_history.append(("You", user_input))
        response = st.session_state.manager.handle_user_input(user_input)
        st.session_state.chat_history.append(("Remnant", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)

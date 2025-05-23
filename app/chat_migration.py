import streamlit as st
from services.llm_service import LLMService
from core.migration_advisor import MigrationAdvisor
from utils.user_context import UserContext

st.set_page_config(page_title="Remnant Migration Chat", layout="centered", page_icon="")
st.title("Remnant Migration Chatbot")

if "context_data" not in st.session_state:
    st.session_state.context_data = {}
if "question_idx" not in st.session_state:
    st.session_state.question_idx = 0
if "advice" not in st.session_state:
    st.session_state.advice = None

questions = [
    ("name", "What is your name?"),
    ("goal", "What is your migration goal? (study/work/asylum)?"),
    ("country", "Which country are you considering?"),
    ("age", "What is your age?"),
    ("budget", "What is your budget in USD?")
]

# Only ask one question at a time
idx = st.session_state.question_idx
if idx < len(questions):
    key, text = questions[idx]
    st.chat_message("assistant").markdown(text)
    user_input = st.chat_input("", key=f"chat_input_{key}")
    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.context_data[key] = user_input
        st.session_state.question_idx += 1
        st.experimental_rerun()
else:
    # All questions answered, show advice
    if st.session_state.advice is None:
        data = st.session_state.context_data
        context = UserContext(**data)
        advisor = MigrationAdvisor(LLMService())
        st.session_state.advice = advisor.advise(context)
    st.chat_message("assistant").markdown(
        f"Thanks {st.session_state.context_data['name']}, here's your migration advice:"
    )
    st.chat_message("assistant").markdown(st.session_state.advice)

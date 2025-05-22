# streamlit_app.py

import streamlit as st
from app.services.llm_service import LLMService
from app.core.migration_advisor import MigrationAdvisor
from app.utils.user_context import UserContext

st.set_page_config(page_title="Remnant Migration Advisor", page_icon="🌍")
st.title("🌍 Remnant Migration Advisor")

with st.form("migration_form"):
    name = st.text_input("What is your name?")
    goal = st.selectbox("What is your migration goal?", ["study", "work", "asylum", "relocate"])
    country = st.text_input("Which country are you considering?")
    age = st.number_input("What is your age?", min_value=10, max_value=100, value=25)
    budget = st.number_input("What is your budget in USD?", min_value=100, value=2000)

    submitted = st.form_submit_button("Get Migration Advice")

if submitted:
    context = UserContext(name, goal, country, str(age), str(budget))
    advisor = MigrationAdvisor(LLMService())
    response = advisor.advise(context)

    st.markdown("### 🧭 Your Personalized Advice")
    st.markdown(response)

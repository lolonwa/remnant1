# cli.py - Auto-generated module in remnant/interface

"""
Module: cli.py
Location: remnant/interface
Purpose: Describe the functionality here.
"""


from services.llm_service import LLMService
from core.migration_advisor import MigrationAdvisor
from utils.user_context import UserContext

def run_cli():
    """
    Entry point for CLI interaction. Asks user questions and advises on migration.
    """
    print("Welcome to Remnant Migration Advisor CLI")
    name = input("What is your name? ")
    goal = input("What is your migration goal? (study/work/asylum): ")
    country = input("Which country are you considering? ")
    age = input("What is your age? ")
    budget = input("What is your budget in USD? ")

    context = UserContext(name, goal, country, age, budget)
    advisor = MigrationAdvisor(LLMService())
    advice = advisor.advise(context)
    print(f"\nAdvice for {name}: {advice}")

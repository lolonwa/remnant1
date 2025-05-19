# cli.py - Entry point for Remnant CLI interface

"""
Module: cli.py
Location: app/interface
Purpose: Collect user input and route it to the appropriate core advisor.
"""

# Corrected imports based on your structure
from app.services.llm_service import LLMService
from app.core.migration_advisor import MigrationAdvisor
from app.utils.user_context import UserContext

def run_cli():
    """
    Entry point for CLI interaction.
    Prompts user for migration preferences and uses LLM to give personalized advice.
    """
    print("Welcome to Remnant Migration Advisor CLI")
    
    # Collect basic user information
    name = input("What is your name? ")
    goal = input("What is your migration goal? (study/work/asylum): ")
    country = input("Which country are you considering? ")
    age = input("What is your age? ")
    budget = input("What is your budget in USD? ")

    # Build user context object
    context = UserContext(name, goal, country, age, budget)

    # Instantiate LLMService and core advisor
    advisor = MigrationAdvisor(LLMService())

    # Get migration advice using the advisor logic
    advice = advisor.advise(context)

    # Display result
    print(f"\nAdvice for {name}: {advice}")

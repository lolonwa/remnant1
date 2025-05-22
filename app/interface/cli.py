# cli.py - in remnant/interface

from app.services.llm_service import LLMService
from core.migration_advisor import MigrationAdvisor
from core.pathway_explorer import PathwayExplorer
from utils.user_context import UserContext


def collect_user_context():
    """
    Helper function to collect user context from CLI inputs.
    """
    print("\n--- Tell us about yourself ---")
    name = input("What is your name? ")
    goal = input("What is your migration goal? (study/work/asylum): ")
    country = input("Which country are you considering? ")
    age = input("What is your age? ")
    budget = input("What is your budget in USD? ")
    return UserContext(name, goal, country, age, budget)


def run_migration_advisor():
    """
    Advises user based on their context.
    """
    context = collect_user_context()
    advisor = MigrationAdvisor(LLMService())
    advice = advisor.advise(context)
    print(f"\n📌 Advice for {context.name}:\n{advice}")


def run_pathway_explorer():
    """
    Explores realistic migration pathways (trades, study+work, job demand).
    """
    context = collect_user_context()
    explorer = PathwayExplorer(LLMService())
    pathways = explorer.explore_paths(context)
    print(f"\n🚀 Suggested Migration Pathways for {context.name}:\n{pathways}")


def run_cli():
    """
    Entry menu for CLI interaction.
    """
    print("Welcome to Remnant Migration Advisor CLI")
    print("What would you like to do?\n")
    print("1. Get migration advice")
    print("2. Explore migration pathways (e.g. trades or in-demand jobs)")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_migration_advisor()
    elif choice == "2":
        run_pathway_explorer()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice.")

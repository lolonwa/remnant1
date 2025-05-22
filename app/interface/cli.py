from app.services.llm_service import LLMService
from app.core.migration_advisor import MigrationAdvisor
from app.core.scam_detection import ScamDetector
from app.utils.user_context import UserContext
from app.core.scholarship_finder import ScholarshipFinder
from app.core.visa_info import VisaInfoAdvisor

def run_migration_advisor():
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

def run_scam_detection():
    print("\nScam Detection Mode")
    offer_text = input("Paste the job/visa offer text you want to analyze:\n")
    detector = ScamDetector(LLMService())
    result = detector.analyze_offer(offer_text)
    print("\nScam Detection Result:")
    print(result)
def run_scholarship_finder():
    print("\nScholarship Finder Mode")
    country = input("Enter the country you want scholarships for: ")
    level = input("Enter the level of study (e.g., undergraduate, masters): ")
    finder = ScholarshipFinder(LLMService())
    scholarships = finder.find(country, level)
    print("\nScholarship Results:")
    print(scholarships)

def run_visa_info_advisor():
    print("\nVisa Info Advisor Mode")
    country = input("Enter the country you want visa information for: ")
    purpose = input("Enter the purpose (study/work/asylum/etc.): ")
    visa_advisor = VisaInfoAdvisor(LLMService())
    info = visa_advisor.get_requirements(country, purpose)
    print("\nVisa Information:")
    print(info)

def run_cli():
    while True:
        print("\nRemnant CLI - Choose an option:")
        print("1. Migration Advice")
        print("2. Scam Detection")
        print("3. Scholarship Finder")
        print("4. Visa Info Advisor")
        print("5. Exit")
        choice = input("Enter choice number: ")

        if choice == "1":
            run_migration_advisor()
        elif choice == "2":
            run_scam_detection()
        elif choice == "3":
            run_scholarship_finder()
        elif choice == "4":
            run_visa_info_advisor()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

"""
PromptFactory helps format consistent prompts for different use cases.
"""

class PromptFactory:
    @staticmethod
    def migration_advice_prompt(user_context) -> str:
        return f"What is the best migration option for: {user_context}?"

    @staticmethod
    def scam_check_prompt(text: str) -> str:
        return f"Is this a scam? Analyze this offer: {text}"

    @staticmethod
    def scholarship_prompt(country: str, level: str) -> str:
        return f"Find scholarships in {country} for {level} level."

    @staticmethod
    def visa_prompt(country: str, purpose: str) -> str:
        return f"What are the visa requirements for {country} for {purpose}?"
    @staticmethod
    def build_migration_prompt(user_context):
        """
        Builds a structured prompt to guide the LLM for migration recommendations.
        """
        return f"""
    You are an expert migration advisor. Your job is to help users make informed migration decisions.

    UserProfile:
    Name: {user_context.name}
    Age: {user_context.age}
    Budget: {user_context.budget} USD
    Goal: {user_context.goal}
    Country: {user_context.country}

    Task: Recommend realistic migration options, next steps, and potential risks based on the user's goal and budget.

    Respond in this YAML format:
    recommended_paths:
    - name: string
        description: string
        estimated_cost: string
        risks: string
    advice: string
    warnings: string
    """
    @staticmethod
    def build_scam_prompt(offer_text):
        """
        Builds a structured prompt to detect scams in an offer.
        """
        return f"""
    You are an AI trained to detect scam or fraudulent offers for visas, jobs, or admissions.

    OfferText:
    \"\"\"
    {offer_text}
    \"\"\"

    Task: Analyze the above text for scam indicators.

    Respond in this format (YAML):
    analysis:
    is_scam: true/false
    reasons:
        - string
    red_flags:
        - string
    advice: string
    """
    @staticmethod
    def build_scholarship_prompt(country, level):
        """
        Builds a prompt to find scholarships based on location and education level.
        """
        return f"""
    You are an educational funding assistant. Find scholarships for students.

    UserQuery:
    Country: {country}
    StudyLevel: {level}

    Task: Find realistic scholarship programs and their details.

    Respond in YAML format:
    scholarships:
    - name: string
        provider: string
        description: string
        website: string
        deadline: string
    notes: string
    """
    @staticmethod
    def build_visa_prompt(country, purpose):
        """
        Builds a structured prompt to retrieve visa requirements.
        """
        return f"""
               you are a visa requirement assistant.

        VisaQuery:
        Country: {country}
        Purpose: {purpose}

        Task: List the visa types available, requirements, processing time, and costs.

        Respond in YAML format:
        visa_options:
        - type: string
            requirements:
            - string
            processing_time: string
            cost: string
            link: string
        summary: string
        """
    @staticmethod
    def build_migration_advice_prompt(user_context: dict) -> str:
        """
        Builds an enhanced prompt for migration advice.
        """
        return f"""
    You are an experienced migration advisor with deep knowledge of global visa pathways.

    User details:
    - Name: {user_context['name']}
    - Goal: {user_context['goal']} (e.g. study, work, asylum, relocate)
    - Country of Interest: {user_context['country']}
    - Age: {user_context['age']}
    - Budget: {user_context['budget']} USD

    Your task is to:
    1. Recommend the most realistic migration pathways based on their goal, budget, and age.
    2. If 'work' is selected, suggest high-demand trades or job roles for {user_context['country']} that may qualify for visas.
    3. Provide examples of real job websites or programs in {user_context['country']} they can explore.
    4. Offer optional next steps, such as how to upskill or apply for scholarships, work permits, or asylum.
    5. If possible, guide them on affordable or government-sponsored options.

    Format your response with clear sections:
    - 🌍 Summary of Suggested Path
    - 🔧 High-Demand Skills or Job Roles
    - 🔗 Useful Links
    - 💡 Next Steps or Advice
        """

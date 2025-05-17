# user_context.py - Auto-generated module in remnant/utils

"""
Module: user_context.py
Location: remnant/utils
Purpose: Describe the functionality here.
"""


class UserContext:
    """
    Stores user context needed to generate personalized migration advice.
    """

    def __init__(self, name, goal, country, age, budget):
        self.name = name
        self.goal = goal
        self.country = country
        self.age = age
        self.budget = budget

    def __str__(self):
        return f"{self.name}, age {self.age}, wants to {self.goal} in {self.country} with budget {self.budget}"

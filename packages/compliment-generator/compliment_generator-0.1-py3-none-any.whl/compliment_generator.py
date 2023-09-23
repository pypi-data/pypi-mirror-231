# compliment_generator.py
import random

def generate_compliment():
    compliments = [
        "You look great today!",
        "You're a smart cookie!",
        "I like your style!",
        "You're the bee's knees!"
    ]
    return random.choice(compliments)

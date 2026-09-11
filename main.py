import json
import random

def load_questions():
    with open("questions.json") as file:
        result = json.load(file)
    return result

def run_quiz(questions):
    random.shuffle(questions)
    for quiz in questions:
        print(quiz['question'])
        for option in quiz['options']:
            print(option)

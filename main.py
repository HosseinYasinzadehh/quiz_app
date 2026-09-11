import json

def load_questions():
    with open("questions.json") as file:
        result = json.load(file)

    return result

questions = load_questions()
print(questions)
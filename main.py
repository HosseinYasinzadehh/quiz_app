import json
import random

def load_questions():
    with open("questions.json") as file:
        result = json.load(file)
    return result


def ask_question(quiz):
    choice = 1
    print(quiz['question'])
    for option in quiz['options']:
        print(f"{choice}. {option}")
        choice += 1
    while True:
        try:
            user_choice = int(input("please enter your choice: "))
            if user_choice > 4 or user_choice < 1:
                print("please enter number between 1 to 4!!!")
                continue
            print(f"your choice is {user_choice}")
            if user_choice == quiz["answer"]:
                print("your choice is correct")
                return True
            else:
                print("your choice is not correct")
                return False

        except ValueError:
            print("please enter number between 1 to 4!!!")


def show_result(score,total):
    print("Quiz Finished! 🎉")
    print(f"Correct: {score}")
    print(f"Incorrect: {total - score}")
    percentage = (score * 100) / total
    print(f"percentage: {percentage}%")

def run_quiz(questions):
    random.shuffle(questions)
    score = 0
    for quiz in questions:
       result = ask_question(quiz)
       if result:
           score += 1
    show_result(score, len(questions))
    return score


questions = load_questions()
run_quiz(questions)

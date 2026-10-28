# Python Quiz
# Project 4 of my "Python Basics" series: loops
#
# A quiz with 10 questions about Python basics.
# The program asks each question, checks the answer and keeps the score.

# Each question is a dictionary, and all the questions are in a list
QUESTIONS = [
    {
        "text": "What does input() always return?",
        "choices": ["A number", "A string", "A boolean"],
        "answer": 2,
    },
    {
        "text": "Which keyword creates a function?",
        "choices": ["def", "function", "func"],
        "answer": 1,
    },
    {
        "text": "What is the type of 3.14?",
        "choices": ["int", "str", "float"],
        "answer": 3,
    },
    {
        "text": "What does round(7.456, 1) give?",
        "choices": ["7.5", "7.4", "7.46"],
        "answer": 1,
    },
    {
        "text": "Which operator checks if two values are equal?",
        "choices": ["=", "!=", "=="],
        "answer": 3,
    },
    {
        "text": "What is the result of 10 % 3?",
        "choices": ["1", "3", "3.33"],
        "answer": 1,
    },
    {
        "text": "Which loop repeats as long as a condition is True?",
        "choices": ["for", "while", "match"],
        "answer": 2,
    },
    {
        "text": 'What does len(["a", "b", "c"]) give?',
        "choices": ["2", '"abc"', "3"],
        "answer": 3,
    },
    {
        "text": "How many times does the loop for i in range(3) run?",
        "choices": ["3 times", "2 times", "4 times"],
        "answer": 1,
    },
    {
        "text": "Which keyword stops a loop right away?",
        "choices": ["stop", "end", "break"],
        "answer": 3,
    },
]


def main():
    print("============ PYTHON QUIZ ============")
    print(f"{len(QUESTIONS)} questions about Python basics.")

    # The game starts again until the player answers "no"
    while True:
        score = play_quiz()
        show_result(score)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes" and again != "y":
            break

    print("Thanks for playing!")


# Asks every question and returns the number of correct answers
def play_quiz():
    score = 0
    number = 1

    for question in QUESTIONS:
        print()
        print(f"Question {number}/{len(QUESTIONS)}: {question['text']}")

        choices = question["choices"]
        for i in range(len(choices)):
            print(f"  {i + 1}. {choices[i]}")

        answer = ask_answer()
        correct = question["answer"]
        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Right answer: {correct}. {choices[correct - 1]}")

        number += 1

    return score


# Asks again until the player types 1, 2 or 3
def ask_answer():
    while True:
        answer = input("Your answer (1, 2 or 3): ").strip()
        if answer == "1" or answer == "2" or answer == "3":
            return int(answer)
        print("Please type 1, 2 or 3.")


def show_result(score):
    total = len(QUESTIONS)
    percent = round(score / total * 100)

    print()
    print("====================================")
    print(f"Your score: {score}/{total} ({percent}%)")

    # Draws a bar: one # for each right answer, one - for each wrong answer
    print("Score bar: ", end="")
    for i in range(score):
        print("#", end="")
    for i in range(total - score):
        print("-", end="")
    print()

    if score == total:
        print("Perfect! You know your Python basics.")
    elif percent >= 70:
        print("Great job!")
    elif percent >= 50:
        print("Not bad, keep practicing.")
    else:
        print("Keep learning, you will get there!")
    print("====================================")


main()

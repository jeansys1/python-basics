# Python Quiz

[Version française](README.fr.md)

A command-line quiz with 10 questions about Python basics. The program asks each question, checks the answer, keeps the score and lets you play again.

Project 4 of my **Python Basics** series, about **loops**.

## Features

- 10 multiple-choice questions about variables, functions, conditionals and loops
- If the answer is not 1, 2 or 3, the program asks again
- Shows the right answer after a mistake
- Final score with a percentage, a score bar and a message
- You can play again as many times as you want

## Example

```text
============ PYTHON QUIZ ============
10 questions about Python basics.

Question 1/10: What does input() always return?
  1. A number
  2. A string
  3. A boolean
Your answer (1, 2 or 3): 2
Correct!

Question 2/10: Which keyword creates a function?
  1. def
  2. function
  3. func
Your answer (1, 2 or 3): abc
Please type 1, 2 or 3.
Your answer (1, 2 or 3): 2
Wrong! Right answer: 1. def

...

====================================
Your score: 8/10 (80%)
Score bar: ########--
Great job!
====================================
Play again? (yes/no): no
Thanks for playing!
```

## How to run

You only need Python 3, nothing to install.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/4-loops
python3 python_quiz.py
```

## What I learned

- Repeating code with a `for` loop: one turn for each question
- Using `range()` and `len()` to number the choices
- Repeating code with a `while` loop until the input is valid
- Stopping an endless `while True` loop with `break` when the player does not want to play again
- Storing data in a list of dictionaries: each question has a text, choices and an answer
- Counting with `score += 1`
- Printing on the same line with `print(..., end="")` to draw the score bar

## Ideas for improvement

- **Exceptions**: handle unexpected input in a cleaner way
- **Libraries**: ask the questions in a random order with `random`
- **Files**: load the questions from a file

## Python Basics series

1. Variables: [Monthly Budget](../1-variables)
2. Functions: [Trip Cost](../2-functions)
3. Conditionals: [Shipping Cost](../3-conditionals)
4. **Loops: Python Quiz** (this project)
5. Exceptions: [Grade Book](../5-exceptions)

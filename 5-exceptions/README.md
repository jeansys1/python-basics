# Grade Book

[Version française](README.fr.md)

A command-line grade book. You type the name and the grade of each student, and the program prints a report: the level of each student, the class average, the best and lowest grades, and how many students passed. If you type something that is not a number, the program does not crash: it asks again.

Project 5 of my **Python Basics** series, about **exceptions**.

## Features

- Add as many students as you want, and finish with an empty name
- If the grade is not a number (like `abc`), the program catches the error and asks again instead of crashing
- If the grade is not between 0 and 100, the program asks again
- A comma or a dot is fine for decimals (`87,5` or `87.5`)
- A level for each student: Excellent, Very good, Good, Pass or Fail
- Class average, best grade, lowest grade and number of students who passed

## Example

```text
============ GRADE BOOK ============
Grades go from 0 to 100 (a comma or a dot is fine).
Leave the name empty to finish.

Student name: emma
Emma's grade: abc
That is not a number, please try again.
Emma's grade: 150
The grade must be between 0 and 100.
Emma's grade: 87,5

Student name: leo
Leo's grade: 42

Student name: sara
Sara's grade: 91

Student name:

============== REPORT ==============
  Emma: 87.5 (Very good)
  Leo: 42.0 (Fail)
  Sara: 91.0 (Excellent)
------------------------------------
  Class average: 73.5
  Best grade: Sara (91.0)
  Lowest grade: Leo (42.0)
  Passed: 2 out of 3
====================================
```

## How to run

You only need Python 3, nothing to install.

```bash
git clone https://github.com/jeansys1/python-basics.git
cd python-basics/5-exceptions
python3 grade_book.py
```

## What I learned

- Catching an error with `try` and `except`: `float()` raises a `ValueError` when the text is not a number
- Using `else` after `except` to run code only when there was no error
- Repeating a question with `while True` until the answer is valid, in a function that only returns a good value
- Checking a range with a chained comparison: `0 <= grade <= 100`
- Storing the students in a list of dictionaries (a name and a grade) and looping through it
- Keeping the total, the best and the lowest grade in variables that are updated inside the loop

## Ideas for improvement

- **Libraries**: use the `statistics` module to get the average and the median
- **Files**: save the grades in a file and load them next time
- **Unit tests**: test `get_level()` with a few grades

## Python Basics series

1. Variables: [Monthly Budget](../1-variables)
2. Functions: [Trip Cost](../2-functions)
3. Conditionals: [Shipping Cost](../3-conditionals)
4. Loops: [Python Quiz](../4-loops)
5. **Exceptions: Grade Book** (this project)

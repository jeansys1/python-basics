# Grade Book
# Project 5 of my "Python Basics" series: exceptions
#
# The program asks for the name and the grade of each student,
# then prints a report: the level of each student, the class average,
# the best and the lowest grades, and how many students passed.

# Constants (in capital letters because their value never changes)
MAX_GRADE = 100
PASS_MARK = 50    # a student passes with 50 or more


def main():
    print("============ GRADE BOOK ============")
    print(f"Grades go from 0 to {MAX_GRADE} (a comma or a dot is fine).")
    print("Leave the name empty to finish.")
    print()

    # Each student is a dictionary, and all the students are in a list
    students = []
    while True:
        name = input("Student name: ").strip().title()
        if name == "":
            break
        grade = ask_grade(f"{name}'s grade: ")
        students.append({"name": name, "grade": grade})
        print()

    if len(students) == 0:
        print("No students, nothing to show.")
    else:
        print_report(students)


# Asks again until the person types a number between 0 and 100.
# float() raises a ValueError when the text is not a number,
# so we catch it with try/except instead of letting the program crash.
def ask_grade(question):
    while True:
        try:
            grade = float(input(question).replace(",", "."))
        except ValueError:
            print("That is not a number, please try again.")
        else:
            if 0 <= grade <= MAX_GRADE:
                return grade
            print(f"The grade must be between 0 and {MAX_GRADE}.")


def print_report(students):
    total = 0
    passed = 0
    best = students[0]
    lowest = students[0]

    print()
    print("============== REPORT ==============")
    for student in students:
        grade = student["grade"]
        print(f"  {student['name']}: {grade} ({get_level(grade)})")

        # Keep track of the numbers we need for the summary
        total += grade
        if grade >= PASS_MARK:
            passed += 1
        if grade > best["grade"]:
            best = student
        if grade < lowest["grade"]:
            lowest = student

    average = round(total / len(students), 1)

    print("------------------------------------")
    print(f"  Class average: {average}")
    print(f"  Best grade: {best['name']} ({best['grade']})")
    print(f"  Lowest grade: {lowest['name']} ({lowest['grade']})")
    print(f"  Passed: {passed} out of {len(students)}")
    print("====================================")


def get_level(grade):
    if grade >= 90:
        return "Excellent"
    elif grade >= 75:
        return "Very good"
    elif grade >= 60:
        return "Good"
    elif grade >= PASS_MARK:
        return "Pass"
    else:
        return "Fail"


main()

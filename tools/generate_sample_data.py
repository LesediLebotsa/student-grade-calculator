import sys
import os
import random
from database import add_student

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

first_names = [
    "John", "Sarah", "Michael", "David", "Emma",
    "James", "Liam", "Noah", "Olivia", "Sophia",
    "Ava", "Mia", "Lucas", "Daniel", "Ethan" ,
    "Kgosi", "Lesego" , "Tshepo" , "Khanyisile",
    "Lusanda" , "Rivoningo", "Thando" , "Lindokuhle"
]

surnames = [
    "Smith", "Johnson", "Brown", "Williams",
    "Jones", "Miller", "Davis", "Wilson",
    "Taylor", "Anderson", "Thomas", "Moore",
    "Lebotsa" , "Mdlalose" , "Ndlovu" , "Moodley"
]

modules = [
    "Python Programming",
    "Database Systems",
    "Cloud Computing",
    "Computer Networks",
    "Software Engineering"
]

for i in range(1000):

    student_no = f"EDUV{10000 + i}"

    name = random.choice(first_names)
    surname = random.choice(surnames)
    module = random.choice(modules)

    quiz = random.randint(30, 100)
    project = random.randint(30, 100)
    exam = random.randint(20, 100)
    practical = random.randint(30, 100)

    overall_grade = round(
        quiz * 0.10 +
        project * 0.20 +
        exam * 0.50 +
        practical * 0.20,
        2
    )

    student = {
        "Student No": student_no,
        "Name": name,
        "Surname": surname,
        "Module": module,
        "Quiz(10%)": quiz,
        "Project(20%)": project,
        "Final Exam(50%)": exam,
        "Practical(20%)": practical,
        "Overall Grade": overall_grade
    }

    try:
        add_student(student)
    except Exception as e:
        print(e)


print("1000 students generated.")
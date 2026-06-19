import csv
import os

def load_students(filename):
    students = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

        return students

def save_results(students):
    with open("results.csv", "w", newline="") as file:
        fieldnames = [
            "Student No",
            "Name",
            "Surname",
            "Module",
            "Calculated Grade",
            "Status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for student in students:
            writer.writerow({
                "Student No": student["Student No"],
                "Name": student["Name"],
                "Surname": student["Surname"],
                "Module": student["Module"],
                "Calculated Grade": student["Calculated Grade"],
                "Status": student["Status"]
            })

def add_students(student):
    file_exists = os.path.isfile("student_data.csv")
    with open("student_data.csv", "a", newline="") as file:

        fieldnames = [
            "Students No",
            "Name",
            "Surname",
            "Module",
            "Quiz(10%)",
            "Project(20%)",
            "Final Exam(50%)",
            "Practical(20%)",
            "Overall Grade"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames )

        if not file_exists:
            writer.writeheader()

        writer.writerow(student)

def delete_student(student_no):
    students = load_students("student_data.csv")
    updated_students = []

    for student in students:
        if student["Student No"] != student_no:
            updated_students.append(student)

    with open("student_data.csv", "w", newline="") as file:
        fieldnames = [
            "Student No",
            "Name",
            "Surname",
            "Module",
            "Quiz(10%)",
            "Project(20%)",
            "Final Exam(50%)",
            "Practical(20%)",
            "Overall Grade"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(updated_students)

def update_student(student_no, assessment, new_mark):
    students = load_students("student_data.csv")

    for student in students:
        if student["Student No"] == student_no:

            student[assessment] = new_mark

            quiz = float(student["Quiz(10%)"])
            project = float(student["Project(20%)"])
            exam = float(student["Final Exam(50%)"])
            practical = float(student["Practical(20%)"])

            overall_grade = (
                quiz * 0.10 +
                project * 0.20 +
                exam * 0.50 +
                practical * 0.20
            )

            student["Overall Grade"] = round(
                overall_grade,
                2
            )

    with open("student_data.csv", "w", newline="") as file:
        fieldnames = [
            "Student No",
            "Name",
            "Surname",
            "Module",
            "Quiz(10%)",
            "Project(20%)",
            "Final Exam(50%)",
            "Practical(20%)",
            "Overall Grade"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(students)

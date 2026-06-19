import csv

from database import (
    create_table,
    add_student,
    student_exists
)

create_table()

with open(
        "legacy_code/student_data.csv",
        "r",
        newline=""
) as file:

    reader = csv.DictReader(file)

    imported = 0

    for row in reader:

        if not student_exists(
                row["Student No"]
        ):

            student = {

                "Student No":
                    row["Student No"],

                "Name":
                    row["Name"],

                "Surname":
                    row["Surname"],

                "Module":
                    row["Module"],

                "Quiz(10%)":
                    float(
                        row["Quiz(10%)"]
                    ),

                "Project(20%)":
                    float(
                        row["Project(20%)"]
                    ),

                "Final Exam(50%)":
                    float(
                        row["Final Exam(50%)"]
                    ),

                "Practical(20%)":
                    float(
                        row["Practical(20%)"]
                    ),

                "Overall Grade":
                    float(
                        row["Overall Grade"]
                    )
            }

            add_student(student)

            imported += 1

print(
    f"{imported} students imported."
)

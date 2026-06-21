import csv
from tkinter import messagebox
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from database import get_students

def export_csv():

    students = get_students()

    with open(
        "student_report.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student No",
            "Name",
            "Surname",
            "Module",
            "Grade"
        ])

        for student in students:

            writer.writerow([
                student[0],
                student[1],
                student[2],
                student[3],
                student[8]
            ])

    print("CSV Report Created")

    messagebox.showinfo(
        "Success",
        "CSV report exported"
    )
def export_pdf():
    document = SimpleDocTemplate(
        "student_report.pdf"
    )
    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Student Report",
            styles["Title"]
        )
    )
    content.append(
        Spacer(1, 12)
    )
    students = get_students()
    for student in students:
        content.append(
            Paragraph(
                f"{student[0]} - "
                f"{student[1]} "
                f"{student[2]} - "
                f"{student[8]}%",
                styles["Normal"]
            )
        )
    document.build(content)
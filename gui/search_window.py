import tkinter as tk
from tkinter import messagebox
from csv_handler import load_students, update_student


def create_search_window():
    window = tk.Toplevel()

    window.title("Search / Update Records")
    window.geometry("600x500")

# Student Number

    tk.Label(
        window,
        text="Search by Student No:"
    ).pack(pady=10)

    student_no_entry = tk.Entry(
        window,
        width=30
    )

    student_no_entry.pack()

# Results Display

    result_label = tk.Label(
        window,
        text="",
        justify="left",
        font=("Arial", 10)
    )

    result_label.pack(pady=20)

# Assessment Dropdown

    tk.Label(
        window,
        text="Select Assessment:"
    ).pack()

    selected_assessment = tk.StringVar()

    selected_assessment.set("Quiz(10%)")

    assessment_combo = tk.OptionMenu(
        window,
        selected_assessment,
        "Quiz(10%)",
        "Project(20%)",
        "Final Exam(50%)",
        "Practical(20%)"
    )

    assessment_combo.pack()


# New Mark

    tk.Label(
        window,
        text="New Mark:"
    ).pack()

    new_mark_entry = tk.Entry(
        window,
        width=20
    )

    new_mark_entry.pack()

# Search Function

    def search_student():
        student_no = student_no_entry.get().strip()

        students = load_students(
            "student_data.csv"
        )

        for student in students:

            if student["Student No"].strip() == student_no:

                result_label.config(
                    text=f"""
                Student No: {student['Student No']}
                
                Name: {student['Name']}
                Surname: {student['Surname']}
                Module: {student['Module']}
                
                Quiz: {student['Quiz(10%)']}
                Project: {student['Project(20%)']}
                Exam: {student['Final Exam(50%)']}
                Practical: {student['Practical(20%)']}
                
                Overall Grade: {student['Overall Grade']}
                """
                )

                return

        messagebox.showerror(
            "Not Found",
            "Student not found."
        )

# Update Function

    def update_record():
        student_no = student_no_entry.get().strip()

        assessment = selected_assessment.get()

        try:
            new_mark = float(
                new_mark_entry.get()
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid mark."
            )
            return

        update_student(
            student_no,
            assessment,
            new_mark
        )

        messagebox.showinfo(
            "Success",
            "Record updated successfully."
        )

        search_student()

# Buttons

    search_btn = tk.Button(
        window,
        text="Search",
        width=15,
        command=search_student
    )

    search_btn.pack(pady=10)

    update_btn = tk.Button(
        window,
        text="Update Mark",
        width=15,
        command=update_record
    )

    update_btn.pack(pady=10)
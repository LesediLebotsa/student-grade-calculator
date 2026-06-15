import tkinter as tk
from tkinter import ttk, messagebox
from validation import validate_mark
from calculations import calculate_grade
from csv_handler import add_students

def create_capture_window():
    window = tk.Toplevel()

    window.title("Capture Student Marks")

    window.geometry("600x500")

    def save_student():
        student_no = student_no_entry.get()
        name = name_entry.get()
        surname = surname_entry.get()
        module = module_combo.get()

        quiz = validate_mark(
            quiz_entry.get(),
            name,
            "Quiz" )

        project = validate_mark(
            project_entry.get(),
            name,
            "Project" )

        exam = validate_mark(
            exam_entry.get(),
            name,
            "Final Exam" )

        practical = validate_mark(
            practical_entry.get(),
            name,
            "Practical" )

        overall_grade = calculate_grade(
            quiz,
            project,
            exam,
            practical )

        if overall_grade is None:
            messagebox.showerror(
                "Invalid Data",
                "Please enter marks correctly."
            )
            return

        result_label.config(
            text=f"Overall Grade: {overall_grade}"
        )

        student = {

            "Students No": student_no,
            "Name": name,
            "Surname": surname,
            "Module": module,
            "Quiz(10%)": quiz,
            "Project(20%)": project,
            "Final Exam(50%)": exam,
            "Practical(20%)": practical,
            "Overall Grade": overall_grade
        }

        add_students(student)

        messagebox.showinfo(
            "Success",
            "Student saved successfully." )

# Heading
    heading = tk.Label(
        window,
        text="Capture Student Marks",
        font=("Arial", 16, "bold")
    )

    heading.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=15 )

# Student Number
    tk.Label(window, text="Student No:").grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    student_no_entry = tk.Entry(window, width=30)
    student_no_entry.grid(row=1, column=1)

# Name
    tk.Label(window, text="Name:").grid(
        row=2,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    name_entry = tk.Entry(window, width=30)
    name_entry.grid(row=2, column=1)

# Surname
    tk.Label(window, text="Surname:").grid(
        row=3,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    surname_entry = tk.Entry(window, width=30)
    surname_entry.grid(row=3, column=1)

# Module
    tk.Label(window, text="Module:").grid(
        row=4,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    module_combo = ttk.Combobox(
        window,
        values=[
            "Python Programming",
            "Java Programming",
            "Database Systems",
            "Cloud Computing"
        ],
        width=27 )

    module_combo.grid(row=4, column=1)

# Quiz
    tk.Label(window, text="Quiz (10%):").grid(
        row=5,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    quiz_entry = tk.Entry(window, width=30)
    quiz_entry.grid(row=5, column=1)

# Project
    tk.Label(window, text="Project (20%):").grid(
        row=6,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    project_entry = tk.Entry(window, width=30)
    project_entry.grid(row=6, column=1)

# Final Exam
    tk.Label(window, text="Final Exam (50%):").grid(
        row=7,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    exam_entry = tk.Entry(window, width=30)
    exam_entry.grid(row=7, column=1)

# Practical
    tk.Label(window, text="Practical (20%):").grid(
        row=8,
        column=0,
        padx=10,
        pady=5,
        sticky="w" )

    practical_entry = tk.Entry(window, width=30)
    practical_entry.grid(row=8, column=1)

# Save Button
    save_button = tk.Button(
        window,
        text="Save",
        width=15,
        bg="lightgreen",
        command=save_student )

    save_button.grid(
        row=9,
        column=0,
        columnspan=2,
        pady=20 )

# Result Label
    result_label = tk.Label(
        window,
        text="Overall Grade: ",
        font=("Arial", 10, "bold"))

    result_label.grid(
        row=10,
        column=0,
        columnspan=2 )

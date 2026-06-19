import tkinter as tk
from tkinter import ttk
import graphs
from services.student_analytics import (
    total_students,
    average_grade,
    pass_rate,
    failure_rate,
    distinction_rate,
    best_module,
    worst_module,
    module_averages, top_10_students
)

def create_analytics_window():

    window = tk.Toplevel()

    window.title("Analytics Dashboard")

    window.geometry("800x700")

    tk.Label(
        window,
        text="Analytics Dashboard",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tk.Label(
        window,
        text=f"Total Students: {total_students()}"
    ).pack(pady=5)

    tk.Label(
        window,
        text=f"Average Grade: {average_grade()}%"
    ).pack(pady=5)

    tk.Label(
        window,
        text=f"Pass Rate: {pass_rate()}%"
    ).pack(pady=5)

    tk.Label(
        window,
        text=f"Failure Rate: {failure_rate()}%"
    ).pack(pady=5)

    tk.Label(
        window,
        text=f"Distinction Rate: {distinction_rate()}%"
    ).pack(pady=5)

    tk.Label(
        window,
        text=f"Best Module: {best_module()}"
    ).pack(pady=5)

    tk.Label(
        window,
        text=f"Worst Module: {worst_module()}"
    ).pack(pady=5)

    tk.Label(
        window,
        text="Module Averages",
        font=("Arial", 12, "bold")
    ).pack(pady=10)
    module_frame = tk.Frame(window)
    module_frame.pack()
    averages = module_averages()

    for module, average in averages.items():
        tk.Label(
            module_frame,
            text=f"{module}: {average}%"
        ).pack(anchor="w")

    tk.Label(
        window,
        text="Top 10 Students",
        font=("Arial", 12, "bold")
    ).pack(pady=10)
    table = ttk.Treeview(
        window,
        columns=("Student No", "Name", "Grade"),
        show="headings",
        height=10
    )

    table.heading("Student No", text="Student No")
    table.heading("Name", text="Name")
    table.heading("Grade", text="Grade")

    table.column("Student No", width=120)
    table.column("Name", width=200)
    table.column("Grade", width=80)

    table.pack(fill="both", expand=True)

    for student in top_10_students():
        table.insert(
            "",
            "end",
            values=(
                student[0],
                f"{student[1]} {student[2]}",
                student[8]
            )
        )
    tk.Button(
        window,
        text="Show Module Chart",
        command=graphs.show_module_chart()
    ).pack(pady=10)

import tkinter as tk
from database import get_weightings,update_weighting
from database import recalculate_all_students

def create_weighting_window():
    window = tk.Toplevel()

    window.title("Weighting Settings")
    window.geometry("350x300")

    weights = get_weightings()

    tk.Label(
        window,
        text="Weighting Configuration",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    # Quiz

    tk.Label(window, text="Quiz").pack()

    quiz_entry = tk.Entry(window)
    quiz_entry.insert(0, weights["Quiz"])
    quiz_entry.pack()

    # Project

    tk.Label(window, text="Project").pack()

    project_entry = tk.Entry(window)
    project_entry.insert(0, weights["Project"])
    project_entry.pack()

    # Exam

    tk.Label(window, text="Exam").pack()

    exam_entry = tk.Entry(window)
    exam_entry.insert(0, weights["Exam"])
    exam_entry.pack()

    # Practical

    tk.Label(window, text="Practical").pack()

    practical_entry = tk.Entry(window)
    practical_entry.insert(0, weights["Practical"])
    practical_entry.pack()

    def save_weightings():
        update_weighting(
            "Quiz",
            float(quiz_entry.get())
        )

        update_weighting(
            "Project",
            float(project_entry.get())
        )

        update_weighting(
            "Exam",
            float(exam_entry.get())
        )

        update_weighting(
            "Practical",
            float(practical_entry.get())
        )
        recalculate_all_students()

        tk.Label(
            window,
            text="New weightings Saved"
        ).pack()

    tk.Button(
        window,
        text="Save",
        command=save_weightings
    ).pack(pady=15)
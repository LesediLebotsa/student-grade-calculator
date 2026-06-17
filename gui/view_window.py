import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import get_students, delete_student

def create_view_window():
    window = tk.Toplevel()

    window.title("View/Delete Records")

    window.geometry("1000x500")

    columns = (
        "Student No",
        "Name",
        "Surname",
        "Module",
        "Overall Grade"
    )

    tree = ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=150)

    tree.pack(fill="both", expand=True)

    def load_data():

        for row in tree.get_children():
            tree.delete(row)

        students = get_students()

        for student in students:

            tree.insert(
                "",
                "end",
                values=student
            )


    def delete_selected():

        selected = tree.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a student." )
            return

        values = tree.item(selected[0])["values"]

        student_no = values[0]

        delete_student(student_no)

        load_data()

        messagebox.showinfo(
            "Success",
            "Student deleted." )


    delete_btn = tk.Button(
        window,
        text="Delete Selected",
        command=delete_selected )


    delete_btn.pack(pady=10)

    load_data()
import tkinter as tk
from gui.capture_window import create_capture_window
from gui.view_window import create_view_window
from gui.search_window import create_search_window

def open_capture():
    create_capture_window()

def open_view():
    create_view_window()

def open_search():
    create_search_window()

def create_main_menu():
    root = tk.Tk()

    root.title("Student Grade Calculator")

    root.geometry("500x400")

    title = tk.Label(
        root,
        text="Student Grades Calculator",
        font=("Arial", 16, "bold")
    )

    title.pack(pady=20)

    capture_btn = tk.Button(
        root,
        text="Capture Student Marks",
        width=25,
        height=2,
        command=open_capture )


    capture_btn.pack(pady=10)

    view_btn = tk.Button(
        root,
        text="View/Delete Records",
        width=25,
        height=2,
        command=open_view )


    view_btn.pack(pady=10)

    search_btn = tk.Button(
        root,
        text="Search/Update Records",
        width=25,
        height=2,
        command=open_search )


    search_btn.pack(pady=10)

    exit_btn = tk.Button(
        root,
        text="Close Application",
        width=25,
        height=2,
        command=root.destroy )

    exit_btn.pack(pady=10)

    root.mainloop()
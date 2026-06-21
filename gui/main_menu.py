import tkinter as tk
from gui.weighting_window import create_weighting_window
from gui.analytics_window import create_analytics_window
from gui.capture_window import create_capture_window
from gui.view_window import create_view_window
from gui.search_window import create_search_window
from gui.users_window import create_user_window
from reports import export_csv, export_pdf

def open_capture():
    create_capture_window()

def open_view():
    create_view_window()

def open_search():
    create_search_window()

def create_main_menu(role):
    root = tk.Tk()

    root.title("Student Grade Calculator")

    root.geometry("500x400")

    title = tk.Label(
        root,
        text="Student Grades Calculator",
        font=("Arial", 16, "bold")
    )

    title.pack(pady=20)

    tk.Label(
        root,
        text=f"Role:{role}",
        font=("Arial", 10, "bold")
    ).pack(pady=5)

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

    analytics_btn =tk.Button(
        root,
        text="Analytics Dashboard",
        width=25,
        height=2,
        command=create_analytics_window
    )
    analytics_btn.pack(pady=10)

    if role == "admin":

        weights_btn = tk.Button(
            root,
            text="Weighting Settings",
            width=25,
            height=2,
            command=create_weighting_window
        )
        weights_btn.pack(pady=5)

        user_management_btn = tk.Button(
            root,
            text="Manage users",
            width=25,
            height=2,
            command=create_user_window
        )
        user_management_btn.pack(pady=5)

        tk.Button(
            root,
            text="Export CSV Report",
            command=export_csv
        ).pack(pady=5)

        tk.Button(
            root,
            text="Export PDF Report",
            command=export_pdf
        ).pack(pady=5)

    exit_btn = tk.Button(
        root,
        text="Close Application",
        width=25,
        height=2,
        command=root.destroy )

    exit_btn.pack(pady=10)

    root.mainloop()


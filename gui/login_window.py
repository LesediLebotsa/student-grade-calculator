import tkinter as tk
from tkinter import messagebox

from database import verify_user
from gui.main_menu import create_main_menu

def create_login_window():
    window = tk.Tk()
    window.title("Student Management System")
    window.geometry("350x250")

    tk.Label(
        window,
        text="Username"
    ).pack(pady=5)

    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(
        window,
        text="Password"
    ).pack(pady=5)

    password_entry = tk.Entry(
        window,
        show="*"
    )
    password_entry.pack()

    def login():
        username = (
            username_entry.get()
            .strip()
        )

        password = (
            password_entry.get()
            .strip()
        )

        result = verify_user(
            username,
            password
        )

        if result:

            role = result[0]

            messagebox.showinfo(
                title= "Login successful",
                message=f"You are logged in as {role}"
            )

            window.destroy()

            create_main_menu(role)

        else:

            messagebox.showerror(
                title="Login Failed",
                message="Invalid username or password"
            )

    login_btn = tk.Button(
        window,
        text="Login",
        command=login
    )
    login_btn.pack(pady=15)

    window.mainloop()
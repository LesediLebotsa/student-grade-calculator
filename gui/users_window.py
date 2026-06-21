import tkinter as tk
from database import create_user
from tkinter import messagebox

def create_user_window():

    window =tk.Toplevel()
    window.title("User Management")
    window.geometry("300x250")

    tk.Label(
        window,
        text="Username"
    ).pack()

    username_entry =tk.Entry(window)
    username_entry.pack()

    tk.Label(
        window,
        text="Password"
    ).pack()

    password_entry = tk.Entry(
        window,
        show="*"
    )
    password_entry.pack()

    tk.Label(
        window,
        text="Role"
    ).pack()

    role_entry= tk.Entry(window)
    role_entry.pack()

    def save_user():
        try:
            create_user(
                username_entry.get(),
                password_entry.get(),
                role_entry.get()
            )
            messagebox.showinfo(
                "Success",
                "User created"
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
             str(e)
            )

    tk.Button(
        window,
        text="Create user",
        command=save_user
    ).pack(pady=10)


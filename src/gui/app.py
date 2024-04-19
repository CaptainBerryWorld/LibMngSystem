import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from common.authentication import login
from admin.admin_menu import AdminMenu
from librarian.librarian_menu import LibrarianMenu
from reader.reader_menu import ReaderMenu

class LibraryManagementApp(CTk):
    def __init__(self):
        super().__init__()

        self.title("Library Management Application")
        self.geometry("800x600")

        self.login_frame = CTkFrame(self)
        self.login_frame.pack(pady=20, padx=20, fill="both", expand=True)

        CTkLabel(self.login_frame, text="Login", font=("Arial", 24)).pack(pady=20)
        self.username_entry = CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)
        self.password_entry = CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)
        self.login_button = CTkButton(self.login_frame, text="Login", command=self.handle_login)
        self.login_button.pack(pady=10)

        self.main_frame = None

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_info = login(username, password)
        print(user_info) 

        if user_info:
            self.login_frame.pack_forget()
            self.main_frame = CTkFrame(self)
            self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

            if user_info["role_id"] == 1:  # Admin
                self.admin_menu = AdminMenu(self.main_frame, user_info)
                self.admin_menu.pack(fill="both", expand=True)
            elif user_info["role_id"] == 2:  # Librarian
                self.librarian_menu = LibrarianMenu(self.main_frame, user_info)
                self.librarian_menu.pack(fill="both", expand=True)
            elif user_info["role_id"] == 3:  # Reader
                self.reader_menu = ReaderMenu(self.main_frame, user_info)
                self.reader_menu.pack(fill="both", expand=True)
        else:
            # Show an error message using messagebox
            messagebox.showerror("Error", "Invalid username or password")
            pass

if __name__ == "__main__":
    app = LibraryManagementApp()
    app.mainloop()
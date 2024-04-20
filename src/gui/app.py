import os
import sys
from tkinter import messagebox, PhotoImage, Label
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from common.authentication import login
from admin.admin_menu import AdminMenu
from librarian.librarian_menu import LibrarianMenu
from reader.reader_menu import ReaderMenu

class LibraryManagementApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("800x800")  # Set the desired window size
        self.resizable(False, False)  # Prevent resizing

        # Set background color
        self.configure(bg_color="#3B5998")  # Replace with your desired background color

        # Create login frame
        self.login_frame = CTkFrame(self, corner_radius=20, bg_color="transparent")  # Define login_frame as an instance variable
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add title label
        title_label = CTkLabel(self.login_frame, text="Login", font=("Arial", 24), fg_color="transparent")
        title_label.pack(pady=20)

        # Add instructions label
        instructions_label = CTkLabel(self.login_frame, text="Please enter you Login and your Password", font=("Arial", 14), fg_color="transparent")
        instructions_label.pack(pady=10)

        # Add username entry
        self.username_entry = CTkEntry(self.login_frame, placeholder_text="Username or E-mail", width=300, height=40, border_width=1, corner_radius=5, text_color="white", fg_color="transparent")
        self.username_entry.pack(padx=10,pady=10)

        # Add password entry
        self.password_entry = CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=300, height=40, border_width=1, corner_radius=5, text_color="white", fg_color="transparent")
        self.password_entry.pack(padx=10, pady=10)

        # Add login button
        login_button = CTkButton(self.login_frame, text="Login", width=300, height=40, corner_radius=5, fg_color="#3B5998", text_color="white", hover_color="#2D4373", command=self.handle_login)
        login_button.pack(pady=20)

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
            messagebox.showerror("Error", "Invalid username or password")  # Use the messagebox module to show an error message

if __name__ == "__main__":
    app = LibraryManagementApp()
    app.mainloop()

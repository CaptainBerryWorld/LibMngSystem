import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry
# from customtkinter import CTkFrame, CTkLabel, CTkButton
from reader.book_search import search_books, get_book_details, get_available_books
from reader.loan_operations import get_user_loans, request_book, return_book_by_user

class ReaderMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)

        self.user_info = user_info

        self.button_frame = CTkFrame(self)
        self.button_frame.pack(side="top", fill="x")
        
        self.book_search_button = CTkButton(self.button_frame, text="Search Books", command=self.show_book_search_menu)
        self.book_search_button.pack(side="left", padx=10, pady=10)

        self.loans_button = CTkButton(self.button_frame, text="Manage Loans", command=self.show_loans_menu)
        self.loans_button.pack(side="left", padx=10, pady=10)
        
        #Logout Button
        self.logout_button = CTkButton(self.button_frame, text="Logout", fg_color= "red", command=self.logout)
        self.logout_button.pack(side="left", padx=10, pady=10)
        
        self.current_menu = None
        
    #Logout Function to login
    def logout(self):
        self.master.destroy()
        # from gui.app import LibraryManagementApp
        app = LibraryManagementApp()
        app.mainloop()

    def show_book_search_menu(self):
        if self.current_menu:
            self.current_menu.pack_forget()

        self.current_menu = BookSearchMenu(self, self.user_info)
        self.current_menu.pack(fill="both", expand=True)

    def show_loans_menu(self):
        if self.current_menu:
            self.current_menu.pack_forget()

        self.current_menu = LoansMenu(self, self.user_info)
        self.current_menu.pack(fill="both", expand=True)

class SearchBar(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.entry = tk.Entry(self)
        self.entry.pack(fill="both", expand=True)

        self.search_button = ttk.Button(self, text="Search")
        self.search_button.pack(side="right")


class BookSearchMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)

        self.user_info = user_info

        # Implement book search and management functionality here
        # Add Search Bar
        self.search_bar = SearchBar(self)
        self.search_bar.pack(fill="x", expand=True)
        
        # Add Search Results Frame
        self.search_results_frame = CTkFrame(self)
        self.search_results_frame.pack(fill="both", expand=True)
        
        # Add Search Results Label
        self.search_results_label = CTkLabel(self.search_results_frame, text="Search Results")
        self.search_results_label.pack(pady=10)
        
        # Add Search Results Listbox
        self.search_results_listbox = tk.Listbox(self.search_results_frame)
        self.search_results_listbox.pack(fill="both", expand=True)
        
        # Add Search Button Click Event
        self.search_bar.search_button.config(command=self.search_books)
        
    def search_books(self):
        search_text = self.search_bar.entry.get()
        books = search_books(search_text)
        
        self.search_results_listbox.delete(0, tk.END)
        
        for book in books:
            self.search_results_listbox.insert(tk.END, book[1])


class LoansMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)

        self.user_info = user_info

        # Implement loan management functionality here
        #See books they have loaned
        self.loans_listbox = tk.Listbox(self)
        self.loans_listbox.pack(fill="both", expand=True)
        
        # Get user loans
        loans = get_user_loans(self.user_info["user_id"])
        
        for loan in loans:
            self.loans_listbox.insert(tk.END, loan[1])
            
        # Add Request Book Button
        self.request_button = CTkButton(self, text="Request Book", command=self.request_book)
        self.request_button.pack(pady=10)
        
        # Add Return Book Button
        self.return_button = CTkButton(self, text="Return Book", command=self.return_book)
        self.return_button.pack(pady=10)
        
    def request_book(self):
        selected_book = self.loans_listbox.get(self.loans_listbox.curselection())
        book_id = get_book_id(selected_book)
        
        request_book(self.user_info["user_id"], book_id)
        
        self.loans_listbox.delete(tk.ACTIVE)
        
    def return_book(self):
        selected_book = self.loans_listbox.get(self.loans_listbox.curselection())
        book_id = get_book_id(selected_book)
        
        return_book_by_user(self.user_info["user_id"], book_id)
        
        self.loans_listbox.delete(tk.ACTIVE)
        
def get_book_id(book_title):
    book_details = get_book_details(book_title)
    return book_details[0]


        
        
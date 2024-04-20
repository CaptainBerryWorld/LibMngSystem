import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry
from customtkinter import CTkFrame, CTkLabel, CTkButton
from librarian.book_operations import search_books, get_available_books, issue_book, return_book
from librarian.loan_management import get_all_loans, extend_loan_due_date, calculate_fine

class SearchBar(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.entry = tk.Entry(self)
        self.entry.pack(fill="both", expand=True)

        self.search_button = ttk.Button(self, text="Search")
        self.search_button.pack(side="right")

class LibrarianMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)

        self.user_info = user_info

        self.button_frame = CTkFrame(self)
        self.button_frame.pack(side = "top", fill="x")
        
        self.book_search_button = CTkButton(self.button_frame, text="Search Books", command=self.show_book_search_menu)
        self.book_search_button.pack(side="left", padx=10, pady=10)
        
        self.books_button = CTkButton(self.button_frame, text="Manage Books", command=self.show_books_menu)
        self.books_button.pack(side="left", padx=10, pady=10)

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
        
    def show_books_menu(self):
        if self.current_menu:
            self.current_menu.pack_forget()

        self.current_menu = BooksMenu(self, self.user_info)
        self.current_menu.pack(fill="both", expand=True)

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
        # Managing books to given and returned by readers
        self.loans_listbox = tk.Listbox(self)
        self.loans_listbox.pack(fill="both", expand=True)
        
        self.loans = get_all_loans()
        
        for loan in self.loans:
            self.loans_listbox.insert(tk.END, f"{loan[1]} - {loan[2]}")
            
        self.extend_loan_button = CTkButton(self, text="Extend Loan Due Date", command=self.extend_loan_due_date)
        self.extend_loan_button.pack(pady=10)
        
        self.calculate_fine_button = CTkButton(self, text="Calculate Fine", command=self.calculate_fine)
        self.calculate_fine_button.pack(pady=10)
        
    def extend_loan_due_date(self):
        selected_index = self.loans_listbox.curselection()
        
        if selected_index:
            loan_id = self.loans[selected_index[0]][0]
            extend_loan_due_date(loan_id)
            
            self.loans = get_all_loans()
            self.loans_listbox.delete(0, tk.END)
            
            for loan in self.loans:
                self.loans_listbox.insert(tk.END, f"{loan[1]} - {loan[2]}")
                
    def calculate_fine(self):
        selected_index = self.loans_listbox.curselection()
        
        if selected_index:
            loan_id = self.loans[selected_index[0]][0]
            fine = calculate_fine(loan_id)
            
            messagebox.showinfo("Fine", f"The fine for loan {loan_id} is {fine}")
        
        
class BooksMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)
        self.user_info = user_info
        self.notebook = ttk.Notebook(self)

        # Add Charges Tab
        self.add_charges_tab = CTkFrame(self.notebook)
        self.notebook.add(self.add_charges_tab, text='Add Charges')

        # Add New Charges Widgets
        self.charge_no_label = CTkLabel(self.add_charges_tab, text="Charge No")
        self.charge_no_entry = CTkEntry(self.add_charges_tab)
        self.charge_desc_label = CTkLabel(self.add_charges_tab, text="Charge Desc")
        self.charge_desc_entry = CTkEntry(self.add_charges_tab)
        self.charge_label = CTkLabel(self.add_charges_tab, text="Charge")
        self.charge_entry = CTkEntry(self.add_charges_tab)
        self.add_button = CTkButton(self.add_charges_tab, text="Add", command=lambda: print("New charge added"))
        self.ignore_button = CTkButton(self.add_charges_tab, text="Ignore")
        self.exit_button = CTkButton(self.add_charges_tab, text="Exit", command=self.add_charges_tab.destroy)

        # Grid the widgets in the "Add New Charges" tab
        self.charge_no_label.grid(row=0, column=0)
        self.charge_no_entry.grid(row=0, column=1)
        self.charge_desc_label.grid(row=1, column=0)
        self.charge_desc_entry.grid(row=1, column=1)
        self.charge_label.grid(row=2, column=0)
        self.charge_entry.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0)
        self.ignore_button.grid(row=3, column=1)
        self.exit_button.grid(row=4, column=0, columnspan=2)

        # Add New Book Type Tab
        self.add_book_type_tab = CTkFrame(self.notebook)
        self.notebook.add(self.add_book_type_tab, text='Add New Book Type')

        # Add New Book Type Widgets
        self.type_no_label = CTkLabel(self.add_book_type_tab, text="Type No")
        self.type_no_entry = CTkEntry(self.add_book_type_tab)
        self.description_label = CTkLabel(self.add_book_type_tab, text="Description")
        self.description_entry = CTkEntry(self.add_book_type_tab)
        self.add_button = CTkButton(self.add_book_type_tab, text="Add", command=lambda: print("New book type added"))
        self.ignore_button = CTkButton(self.add_book_type_tab, text="Ignore")
        self.exit_button = CTkButton(self.add_book_type_tab, text="Exit", command=self.add_book_type_tab.destroy)

        # Grid the widgets in the "Add New Book Type" tab
        self.type_no_label.grid(row=0, column=0)
        self.type_no_entry.grid(row=0, column=1)
        self.description_label.grid(row=1, column=0)
        self.description_entry.grid(row=1, column=1)
        self.add_button.grid(row=2, column=0)
        self.ignore_button.grid(row=2, column=1)
        self.exit_button.grid(row=3, column=0, columnspan=2)

        # Add New Book Code Tab
        self.add_book_code_tab = CTkFrame(self.notebook)
        self.notebook.add(self.add_book_code_tab, text='Add New Book Code')

        # Add New Book Code Widgets
        self.book_code_label = CTkLabel(self.add_book_code_tab, text="Book Code")
        self.book_code_entry = CTkEntry(self.add_book_code_tab)
        self.description_label = CTkLabel(self.add_book_code_tab, text="Description")
        self.description_entry = CTkEntry(self.add_book_code_tab)
        self.add_button = CTkButton(self.add_book_code_tab, text="Add", command=lambda: print("New book code added"))
        self.ignore_button = CTkButton(self.add_book_code_tab, text="Ignore")
        self.exit_button = CTkButton(self.add_book_code_tab, text="Exit", command=self.add_book_code_tab.destroy)

        # Grid the widgets in the "Add New Book Code" tab
        self.book_code_label.grid(row=0, column=0)
        self.book_code_entry.grid(row=0, column=1)
        self.description_label.grid(row=1, column=0)
        self.description_entry.grid(row=1, column=1)
        self.add_button.grid(row=2, column=0)
        self.ignore_button.grid(row=2, column=1)
        self.exit_button.grid(row=3, column=0, columnspan=2)

        self.notebook.pack(fill="both", expand=True)

import tkinter as tk
from tkinter import ttk, messagebox
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry
from admin.user_management import get_all_users, add_user, update_user, delete_user
from admin.book_management import get_all_books, add_book, update_book, delete_book
from admin.reports import get_user_report, get_book_code_report, get_book_type_report, get_loan_report
from tkinter import Text

class AdminMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)

        self.user_info = user_info

        self.users_button = CTkButton(self, text="Manage Users", command=self.show_users_menu)
        self.users_button.pack(pady=10)

        self.books_button = CTkButton(self, text="Manage Books", command=self.show_books_menu)
        self.books_button.pack(pady=10)

        self.reports_button = CTkButton(self, text="View Reports", command=self.show_reports_menu)
        self.reports_button.pack(pady=10)
        
        #Logout Button
        self.logout_button = CTkButton(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

        self.current_menu = None

    #Logout Function to login
    def logout(self):
        self.pack_forget()
        self.master.login_frame.pack(fill="both", expand=True)

    def show_users_menu(self):
        if self.current_menu:
            self.current_menu.pack_forget()

        self.current_menu = UsersMenu(self, self.user_info)
        self.current_menu.pack(fill="both", expand=True)

    def show_books_menu(self):
        if self.current_menu:
            self.current_menu.pack_forget()

        self.current_menu = BooksMenu(self, self.user_info)
        self.current_menu.pack(fill="both", expand=True)

    def show_reports_menu(self):
        if self.current_menu:
            self.current_menu.pack_forget()

        self.current_menu = ReportsMenu(self, self.user_info)
        self.current_menu.pack(fill="both", expand=True)


class UsersMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)
        self.user_info = user_info
        self.notebook = ttk.Notebook(self)

        # Add a New User Tab
        self.add_user_tab = CTkFrame(self.notebook)
        self.notebook.add(self.add_user_tab, text='Add a New User')

        self.name_label = CTkLabel(self.add_user_tab, text="Name")
        self.name_label.pack()
        self.name_entry = CTkEntry(self.add_user_tab)
        self.name_entry.pack()

        self.email_label = CTkLabel(self.add_user_tab, text="Email")
        self.email_label.pack()
        self.add_email_entry = CTkEntry(self.add_user_tab)
        self.add_email_entry.pack()

        self.password_label = CTkLabel(self.add_user_tab, text="Password")
        self.password_label.pack()
        self.password_entry = CTkEntry(self.add_user_tab, show="*")
        self.password_entry.pack()
        
        self.confirm_password_label = CTkLabel(self.add_user_tab, text="Confirm Password")
        self.confirm_password_label.pack()
        self.confirm_password_entry = CTkEntry(self.add_user_tab, show="*")
        self.confirm_password_entry.pack()

        self.add_user_button = CTkButton(self.add_user_tab, text="Add User", command=self.add_user)
        self.add_user_button.pack()
        

        # Unlock User Utility Tab
        self.unlock_user_tab = CTkFrame(self.notebook)
        self.notebook.add(self.unlock_user_tab, text='Unlock User Utility')

        self.locked_users_label = CTkLabel(self.unlock_user_tab, text="Locked Users")
        self.locked_users_label.pack(pady=10)

        self.locked_users_listbox = tk.Listbox(self.unlock_user_tab, width=30)
        self.locked_users_listbox.pack(pady=10)

        self.unlock_user_button = CTkButton(self.unlock_user_tab, text="Unlock User", command=self.unlock_user)
        self.unlock_user_button.pack(pady=10)

        self.exit_button = CTkButton(self.unlock_user_tab, text="Exit", command=self.unlock_user_tab.destroy)
        self.exit_button.pack(pady=10)

        # Change User Password Tab
        self.change_password_tab = CTkFrame(self.notebook)
        self.notebook.add(self.change_password_tab, text='Change User Password')

        self.change_password_label = CTkLabel(self.change_password_tab, text="Change User Password")
        self.change_password_label.pack()

        self.user_id_label = CTkLabel(self.change_password_tab, text="User ID")
        self.user_id_label.pack()
        self.user_id_entry = CTkEntry(self.change_password_tab)
        self.user_id_entry.pack()

        self.old_password_label = CTkLabel(self.change_password_tab, text="Old Password")
        self.old_password_label.pack()
        self.old_password_entry = CTkEntry(self.change_password_tab, show="*")
        self.old_password_entry.pack()

        self.new_password_label = CTkLabel(self.change_password_tab, text="New Password")
        self.new_password_label.pack()
        self.new_password_entry = CTkEntry(self.change_password_tab, show="*")
        self.new_password_entry.pack()

        self.confirm_password_label = CTkLabel(self.change_password_tab, text="Confirm Password")
        self.confirm_password_label.pack()
        self.confirm_password_entry = CTkEntry(self.change_password_tab, show="*")
        self.confirm_password_entry.pack()

        self.change_password_button = CTkButton(self.change_password_tab, text="Change Password", command=self.change_password)
        self.change_password_button.pack()

        # User Maintenance Tab
        self.user_maintenance_tab = CTkFrame(self.notebook)
        self.notebook.add(self.user_maintenance_tab, text='User Maintenance')

        self.user_id_label = CTkLabel(self.user_maintenance_tab, text="User ID")
        self.user_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.user_id_entry = CTkEntry(self.user_maintenance_tab)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.user_name_label = CTkLabel(self.user_maintenance_tab, text="User Name")
        self.user_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.user_name_entry = CTkEntry(self.user_maintenance_tab)
        self.user_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.address_line1_label = CTkLabel(self.user_maintenance_tab, text="Address Line 1")
        self.address_line1_label.grid(row=2, column=0, padx=10, pady=10)
        self.address_line1_entry = CTkEntry(self.user_maintenance_tab)
        self.address_line1_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_line2_label = CTkLabel(self.user_maintenance_tab, text="Address Line 2")
        self.address_line2_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_line2_entry = CTkEntry(self.user_maintenance_tab)
        self.address_line2_entry.grid(row=3, column=1, padx=10, pady=10)

        self.phone_label = CTkLabel(self.user_maintenance_tab, text="Phone")
        self.phone_label.grid(row=4, column=0, padx=10, pady=10)
        self.phone_entry = CTkEntry(self.user_maintenance_tab)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=10)

        self.email_label = CTkLabel(self.user_maintenance_tab, text="Email")
        self.email_label.grid(row=5, column=0, padx=10, pady=10)
        self.email_entry = CTkEntry(self.user_maintenance_tab)
        self.email_entry.grid(row=5, column=1, padx=10, pady=10)

        self.update_button = CTkButton(self.user_maintenance_tab, text="Update", command=self.update_user)
        self.update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Backup Tab
        self.backup_tab = CTkFrame(self.notebook)
        self.notebook.add(self.backup_tab, text='Take Backup')
        # Implement backup functionality here

        self.notebook.pack(fill="both", expand=True)

    def add_user(self):
        username = self.name_entry.get()
        password = self.password_entry.get()
        email = self.add_email_entry.get()
        address = ""  # or some default value
        phone = ""  # or some default value
        role_id = 3  # or some default value
        
        if not username or not password or not email:
            messagebox.showerror("Error", "Please enter all required fields")
            return
        
        if add_user(username, password, email, address, phone, role_id):
            messagebox.showinfo("Success", "User added successfully")
        else:
            messagebox.showerror("Error", "Failed to add user")
            
        if password!=self.confirm_password_entry.get():
            messagebox.showerror("Error", "Password does not match")
            return

    def unlock_user(self):
        # Implement unlock user functionality here
        self.locked_users_listbox.delete(0, tk.END)
        locked_users = get_all_users(locked=True)
        for user in locked_users:
            self.locked_users_listbox.insert(tk.END, f"{user[0]} - {user[1]}")
            
        pass

    def change_password(self):
        # Change password functionality
        self.user_id = self.user_id_entry.get()
        self.old_password = self.old_password_entry.get()
        self.new_password = self.new_password_entry.get()
        self.confirm_password = self.confirm_password_entry.get()
        
        if not self.user_id or not self.old_password or not self.new_password or not self.confirm_password:
            messagebox.showerror("Error", "Please enter all required fields")
            return
        
        if self.new_password != self.confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        pass

    def update_user(self):
        # Update user functionality
        self.user_id = self.user_id_entry.get()
        self.user_name = self.user_name_entry.get()
        self.address_line1 = self.address_line1_entry.get()
        self.address_line2 = self.address_line2_entry.get()
        self.phone = self.phone_entry.get()
        self.email = self.email_entry.get()
        
        if not self.user_id or not self.user_name or not self.address_line1 or not self.address_line2 or not self.phone or not self.email:
            messagebox.showerror("Error", "Please enter all required fields")
            return
        
        if update_user(self.user_id, self.user_name, self.address_line1, self.address_line2, self.phone, self.email):
            messagebox.showinfo("Success", "User updated successfully")
        else:
            messagebox.showerror("Error", "Failed to update user")
            
        pass

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
        self.add_button = CTkButton(self.add_charges_tab, text="Add", command=self.add_charges)
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
        self.book_type_description_entry = CTkEntry(self.add_book_type_tab)
        self.add_button = CTkButton(self.add_book_type_tab, text="Add", command=self.add_book_type)
        self.ignore_button = CTkButton(self.add_book_type_tab, text="Ignore")
        self.exit_button = CTkButton(self.add_book_type_tab, text="Exit", command=self.add_book_type_tab.destroy)

        # Grid the widgets in the "Add New Book Type" tab
        self.type_no_label.grid(row=0, column=0)
        self.type_no_entry.grid(row=0, column=1)
        self.description_label.grid(row=1, column=0)
        self.book_type_description_entry.grid(row=1, column=1)
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
        self.add_button = CTkButton(self.add_book_code_tab, text="Add", command=self.add_book_code)
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
        
    def add_charges(self):
        # Add charges functionality
        self.charge_no = self.charge_no_entry.get()
        self.charge_desc = self.charge_desc_entry.get()
        self.charge = self.charge_entry.get()
        
        # Check if the fields are filled
        if not self.charge_no or not self.charge_desc or not self.charge:
            messagebox.showerror("Error", "All fields must be filled")
            return
        
        messagebox.showinfo("Success","Charge added sucessfully")
        pass
    
    def add_book_type(self):
        # Add book type functionality
        self.type_no = self.type_no_entry.get()
        self.descr_entry = self.book_type_description_entry.get()
        
        if not self.type_no or not self.descr_entry:
            messagebox.showerror("Error", "All fields must be filled")
            return
        
        messagebox.showinfo("Success","Book type added successfully")
               
        pass
    
    def add_book_code(self):
        # Add book code functionality
        self.book_code = self.book_code_entry.get()
        self.desc_entry = self.description_entry.get()
        
        if not book_code or not desc_entry:
            messagebox.showerror("Error", "All fields must be filled")
            return
        
        messagebox.showinfo("Success","Book code added successfully")
        
        pass
    
    
    
    def delete_charges(self):
        # Delete charges functionality
        pass
    
    def delete_book_type(self):
        # Delete book type functionality
        pass
    
    def delete_book_code(self):
        # Delete book code functionality
        pass
    
    def view_charges(self):
        # View charges functionality
        pass
    
    


class ReportsMenu(CTkFrame):
    def __init__(self, master, user_info, **kwargs):
        super().__init__(master, **kwargs)

        self.user_info = user_info

        self.notebook = ttk.Notebook(self)

        # View Book Code Listing Tab
        self.view_book_code_listing_tab = CTkFrame(self.notebook)
        self.notebook.add(self.view_book_code_listing_tab, text='View Book Code Listing')

        self.book_code_tree = ttk.Treeview(self.view_book_code_listing_tab, columns=("Book Code", "Description"), show="headings")
        self.book_code_tree.heading("Book Code", text="Book Code")
        self.book_code_tree.heading("Description", text="Description")
        self.book_code_tree.pack()

        # View User Listing Tab
        self.view_user_listing_tab = CTkFrame(self.notebook)
        self.notebook.add(self.view_user_listing_tab, text='View User Listing')

        self.user_tree = ttk.Treeview(self.view_user_listing_tab, columns=("User ID", "User Name"), show="headings")
        self.user_tree.heading("User ID", text="User ID")
        self.user_tree.heading("User Name", text="User Name")
        self.user_tree.pack()

        # View Book Type Listing Tab
        self.view_book_type_listing_tab = CTkFrame(self.notebook)
        self.notebook.add(self.view_book_type_listing_tab, text='View Book Type Listing')

        self.book_type_tree = ttk.Treeview(self.view_book_type_listing_tab, columns=("Book Type ID", "Book Type"), show="headings")
        self.book_type_tree.heading("Book Type ID", text="Book Type ID")
        self.book_type_tree.heading("Book Type", text="Book Type")
        self.book_type_tree.pack()

        self.notebook.pack(fill="both", expand=True)

        def view_book_code_listing(self):
            # View book code listing
            self.book_code_tree.delete(*self.book_code_tree.get_children())
            book_codes = get_all_books()
            for book_code in book_codes:
                # Assuming book_code is an object with 'code' and 'description' attributes
                self.book_code_tree.insert("", tk.END, values=(book_code.code, book_code.description))
        
        def view_user_listing(self):
            # View user listing functionality
            self.user_tree.delete(*self.user_tree.get_children())
            users = get_all_users()
            for user in users:
                # Assuming user is an object with 'id' and 'name' attributes
                self.user_tree.insert("", tk.END, values=(user.id, user.name))
        
        def view_book_type_listing(self):
            # View book type listing functionality
            self.book_type_tree.delete(*self.book_type_tree.get_children())
            book_types = get_all_books()
            for book_type in book_types:
                # Assuming book_type is an object with 'id' and 'type' attributes
                self.book_type_tree.insert("", tk.END, values=(book_type.id, book_type.type))
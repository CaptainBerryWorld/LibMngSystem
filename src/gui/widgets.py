import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton

class SearchBar(CTkFrame):
    def __init__(self, master, on_search, **kwargs):
        super().__init__(master, **kwargs)

        self.search_entry = CTkEntry(self, placeholder_text="Search...")
        self.search_entry.pack(side="left", padx=10, pady=10)

        self.search_button = CTkButton(self, text="Search", command=self.on_search_click)
        self.search_button.pack(side="left", padx=10, pady=10)

        self.on_search = on_search

    def on_search_click(self):
        search_text = self.search_entry.get()
        self.on_search(search_text)

        self.search_entry.delete(0, tk.END)

class BookDetailsCard(CTkFrame):
    def __init__(self, master, book_info, **kwargs):
        super().__init__(master, **kwargs)

        self.title_label = CTkLabel(self, text=book_info[1], font=("Arial", 16))
        self.title_label.pack(pady=5)

        self.author_label = CTkLabel(self, text=f"Author: {book_info[2]}")
        self.author_label.pack(pady=5)

        self.isbn_label = CTkLabel(self, text=f"ISBN: {book_info[3]}")
        self.isbn_label.pack(pady=5)

        self.type_label = CTkLabel(self, text=f"Type: {book_info[4]}")
        self.type_label.pack(pady=5)

        self.genre_label = CTkLabel(self, text=f"Genre: {book_info[5]}")
        self.genre_label.pack(pady=5)

        self.publisher_label = CTkLabel(self, text=f"Publisher: {book_info[6]}")
        self.publisher_label.pack(pady=5)

        self.language_label = CTkLabel(self, text=f"Language: {book_info[7]}")
        self.language_label.pack(pady=5)

        self.edition_label = CTkLabel(self, text=f"Edition: {book_info[8]}")
        self.edition_label.pack(pady=5)

        self.copies_label = CTkLabel(self, text=f"Copies: {book_info[9]}")
        self.copies_label.pack(pady=5)
from common.database import execute_query, execute_non_query

def get_all_books():
    """
    Retrieve all books from the database.
    
    Returns:
        list: A list of tuples containing book information.
    """
    query = "SELECT * FROM Books"
    return execute_query(query)

def get_book_by_id(book_id):
    """
    Retrieve a book from the database by its book_id.
    
    Args:
        book_id (int): The ID of the book to retrieve.
    
    Returns:
        tuple: A tuple containing the book information, or None if the book is not found.
    """
    query = "SELECT * FROM Books WHERE book_id = %s"
    result = execute_query(query, (book_id,))
    if result:
        return result[0]
    else:
        return None

def add_book(title, author, publication_date, isbn, book_type_id, genre_id, publisher_id, language_id, edition, total_copies):
    """
    Add a new book to the database.
    
    Args:
        title (str): The title of the new book.
        author (str): The author of the new book.
        publication_date (str): The publication date of the new book.
        isbn (str): The ISBN of the new book.
        book_type_id (int): The ID of the book type.
        genre_id (int): The ID of the book genre.
        publisher_id (int): The ID of the book publisher.
        language_id (int): The ID of the book language.
        edition (str): The edition of the new book.
        total_copies (int): The total number of copies of the new book.
    
    Returns:
        int: The ID of the newly added book, or 0 if the addition failed.
    """
    query = """
        INSERT INTO Books (title, author, publication_date, isbn, book_type_id, genre_id, publisher_id, language_id, edition, total_copies, available_copies)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (title, author, publication_date, isbn, book_type_id, genre_id, publisher_id, language_id, edition, total_copies, total_copies)
    result = execute_non_query(query, values)
    if result > 0:
        return execute_query("SELECT LAST_INSERT_ID()")[0][0]
    else:
        return 0

def update_book(book_id, title, author, publication_date, isbn, book_type_id, genre_id, publisher_id, language_id, edition, total_copies):
    """
    Update an existing book in the database.
    
    Args:
        book_id (int): The ID of the book to update.
        title (str): The new title of the book.
        author (str): The new author of the book.
        publication_date (str): The new publication date of the book.
        isbn (str): The new ISBN of the book.
        book_type_id (int): The new ID of the book type.
        genre_id (int): The new ID of the book genre.
        publisher_id (int): The new ID of the book publisher.
        language_id (int): The new ID of the book language.
        edition (str): The new edition of the book.
        total_copies (int): The new total number of copies of the book.
    
    Returns:
        int: The number of rows affected by the update, or 0 if the update failed.
    """
    query = """
        UPDATE Books
        SET title = %s, author = %s, publication_date = %s, isbn = %s, book_type_id = %s, genre_id = %s, publisher_id = %s, language_id = %s, edition = %s, total_copies = %s, available_copies = %s
        WHERE book_id = %s
    """
    values = (title, author, publication_date, isbn, book_type_id, genre_id, publisher_id, language_id, edition, total_copies, total_copies, book_id)
    return execute_non_query(query, values)

def delete_book(book_id):
    """
    Delete a book from the database.
    
    Args:
        book_id (int): The ID of the book to delete.
    
    Returns:
        int: The number of rows affected by the deletion, or 0 if the deletion failed.
    """
    query = "DELETE FROM Books WHERE book_id = %s"
    return execute_non_query(query, (book_id,))

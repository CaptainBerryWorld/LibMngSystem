from common.database import execute_query, execute_non_query
from admin.book_management import get_all_books, get_book_by_id, add_book, update_book, delete_book

def search_books(title=None, author=None, isbn=None):
    """
    Search for books based on the provided criteria.
    
    Args:
        title (str, optional): The title of the book to search for.
        author (str, optional): The author of the book to search for.
        isbn (str, optional): The ISBN of the book to search for.
    
    Returns:
        list: A list of tuples containing book information.
    """
    query = "SELECT * FROM Books WHERE 1=1"
    params = []
    
    if title:
        query += " AND title LIKE %s"
        params.append(f"%{title}%")
    if author:
        query += " AND author LIKE %s"
        params.append(f"%{author}%")
    if isbn:
        query += " AND isbn = %s"
        params.append(isbn)
    
    return execute_query(query, tuple(params))

def get_available_books():
    """
    Retrieve all books that are currently available for loan.
    
    Returns:
        list: A list of tuples containing book information.
    """
    query = "SELECT * FROM Books WHERE available_copies > 0"
    return execute_query(query)

def issue_book(user_id, book_id, issue_date, due_date):
    """
    Issue a book to a user.
    
    Args:
        user_id (int): The ID of the user borrowing the book.
        book_id (int): The ID of the book being borrowed.
        issue_date (str): The date the book was issued.
        due_date (str): The date the book is due to be returned.
    
    Returns:
        bool: True if the book was issued successfully, False otherwise.
    """
    query = """
        INSERT INTO Loans (user_id, book_id, issue_date, due_date)
        VALUES (%s, %s, %s, %s)
    """
    params = (user_id, book_id, issue_date, due_date)
    
    if execute_non_query(query, params) > 0:
        query = "UPDATE Books SET available_copies = available_copies - 1 WHERE book_id = %s"
        execute_non_query(query, (book_id,))
        return True
    else:
        return False

def return_book(loan_id):
    """
    Return a book that has been borrowed.
    
    Args:
        loan_id (int): The ID of the loan being returned.
    
    Returns:
        bool: True if the book was returned successfully, False otherwise.
    """
    query = """
        UPDATE Loans
        SET return_date = CURDATE()
        WHERE loan_id = %s
    """
    if execute_non_query(query, (loan_id,)) > 0:
        query = "UPDATE Books SET available_copies = available_copies + 1 WHERE book_id = (SELECT book_id FROM Loans WHERE loan_id = %s)"
        execute_non_query(query, (loan_id,))
        return True
    else:
        return False
from common.database import execute_query, execute_non_query
from librarian.book_operations import issue_book, return_book
from datetime import datetime, timedelta

def get_user_loans(user_id):
    """
    Retrieve all loans for the specified user.
    
    Args:
        user_id (int): The ID of the user.
    
    Returns:
        list: A list of tuples containing loan information.
    """
    query = """
        SELECT l.loan_id, b.title, l.issue_date, l.due_date, l.return_date, l.fine_amount
        FROM Loans l
        JOIN Books b ON l.book_id = b.book_id
        WHERE l.user_id = %s
    """
    return execute_query(query, (user_id,))

def request_book(user_id, book_id):
    """
    Request a book for checkout.
    
    Args:
        user_id (int): The ID of the user requesting the book.
        book_id (int): The ID of the book being requested.
    
    Returns:
        bool: True if the book was successfully checked out, False otherwise.
    """
    issue_date = datetime.now().strftime('%Y-%m-%d')
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    return issue_book(user_id, book_id, issue_date, due_date)

def return_book_by_user(user_id, loan_id):
    """
    Return a book that has been borrowed by the specified user.
    
    Args:
        user_id (int): The ID of the user returning the book.
        loan_id (int): The ID of the loan being returned.
    
    Returns:
        bool: True if the book was successfully returned, False otherwise.
    """
    return return_book(loan_id)
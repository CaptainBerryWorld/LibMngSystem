from common.database import execute_query

def get_user_report():
    """
    Retrieve a report of all users.
    
    Returns:
        list: A list of tuples containing user information.
    """
    query = """
        SELECT u.user_id, u.username, u.email, u.phone, r.role_name
        FROM Users u
        JOIN Roles r ON u.role_id = r.role_id
    """
    return execute_query(query)

def get_book_code_report():
    """
    Retrieve a report of all book codes.
    
    Returns:
        list: A list of tuples containing book code information.
    """
    query = "SELECT * FROM BookCodes"
    return execute_query(query)

def get_book_type_report():
    """
    Retrieve a report of all book types.
    
    Returns:
        list: A list of tuples containing book type information.
    """
    query = "SELECT * FROM BookTypes"
    return execute_query(query)

def get_loan_report(user_id=None, book_id=None, from_date=None, to_date=None):
    """
    Retrieve a report of all loans, optionally filtered by user, book, and date range.
    
    Args:
        user_id (int, optional): The ID of the user to filter by.
        book_id (int, optional): The ID of the book to filter by.
        from_date (str, optional): The start date of the date range to filter by.
        to_date (str, optional): The end date of the date range to filter by.
    
    Returns:
        list: A list of tuples containing loan information.
    """
    query = """
        SELECT l.loan_id, u.username, b.title, l.issue_date, l.due_date, l.return_date, l.fine_amount
        FROM Loans l
        JOIN Users u ON l.user_id = u.user_id
        JOIN Books b ON l.book_id = b.book_id
        WHERE 1=1
    """
    params = []
    
    if user_id:
        query += " AND l.user_id = %s"
        params.append(user_id)
    if book_id:
        query += " AND l.book_id = %s"
        params.append(book_id)
    if from_date:
        query += " AND l.issue_date >= %s"
        params.append(from_date)
    if to_date:
        query += " AND l.issue_date <= %s"
        params.append(to_date)
    
    return execute_query(query, tuple(params))
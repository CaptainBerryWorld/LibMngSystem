from common.database import execute_query, execute_non_query
from datetime import datetime, timedelta
from datetime import datetime

def get_all_loans():
    """
    Retrieve all loans from the database.
    
    Returns:
        list: A list of tuples containing loan information.
    """
    query = """
        SELECT l.loan_id, u.username, b.title, l.issue_date, l.due_date, l.return_date, l.fine_amount
        FROM Loans l
        JOIN Users u ON l.user_id = u.user_id
        JOIN Books b ON l.book_id = b.book_id
    """
    return execute_query(query)

def get_loan_by_id(loan_id):
    """
    Retrieve a loan from the database by its loan_id.
    
    Args:
        loan_id (int): The ID of the loan to retrieve.
    
    Returns:
        tuple: A tuple containing the loan information, or None if the loan is not found.
    """
    query = """
        SELECT l.loan_id, u.username, b.title, l.issue_date, l.due_date, l.return_date, l.fine_amount
        FROM Loans l
        JOIN Users u ON l.user_id = u.user_id
        JOIN Books b ON l.book_id = b.book_id
        WHERE l.loan_id = %s
    """
    result = execute_query(query, (loan_id,))
    if result:
        return result[0]
    else:
        return None

def extend_loan_due_date(loan_id, new_due_date):
    """
    Extend the due date of a loan.
    
    Args:
        loan_id (int): The ID of the loan to extend.
        new_due_date (str): The new due date for the loan.
    
    Returns:
        bool: True if the loan was extended successfully, False otherwise.
    """
    query = "UPDATE Loans SET due_date = %s WHERE loan_id = %s"
    return execute_non_query(query, (new_due_date, loan_id)) > 0

def calculate_fine(loan_id):
    """
    Calculate the fine for a late book return.
    
    Args:
        loan_id (int): The ID of the loan to calculate the fine for.
    
    Returns:
        float: The amount of the fine, or 0 if the book was returned on time.
    """
    query = "SELECT issue_date, due_date, return_date FROM Loans WHERE loan_id = %s"
    result = execute_query(query, (loan_id,))[0]
    issue_date = datetime.strptime(str(result[0]), "%Y-%m-%d")
    due_date = datetime.strptime(str(result[1]), "%Y-%m-%d")  # Convert to string before parsing
    return_date = datetime.strptime(result[2].strftime("%Y-%m-%d"), "%Y-%m-%d")  # Convert date to string
    
    if return_date > due_date:
        days_late = (return_date - due_date).days
        fine_amount = days_late * 0.5  # Assuming a fine of $0.50 per day
        return fine_amount
    else:
        return 0.0
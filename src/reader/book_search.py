from common.database import execute_query

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

def get_book_details(book_id):
    """
    Retrieve the details of a specific book.
    
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

def get_available_books():
    """
    Retrieve all books that are currently available for loan.
    
    Returns:
        list: A list of tuples containing book information.
    """
    query = "SELECT * FROM Books WHERE available_copies > 0"
    return execute_query(query)
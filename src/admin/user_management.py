from common.database import execute_query, execute_non_query
from common.authentication import register

def get_all_users():
    """
    Retrieve all users from the database.
    
    Returns:
        list: A list of tuples containing user information.
    """
    query = "SELECT * FROM Users"
    return execute_query(query)

def get_user_by_id(user_id):
    """
    Retrieve a user from the database by their user_id.
    
    Args:
        user_id (int): The ID of the user to retrieve.
    
    Returns:
        tuple: A tuple containing the user information, or None if the user is not found.
    """
    query = "SELECT * FROM Users WHERE user_id = %s"
    result = execute_query(query, (user_id,))
    if result:
        return result[0]
    else:
        return None

def add_user(username, password, email, address, phone, role_id):
    """
    Add a new user to the database.
    
    Args:
        username (str): The username of the new user.
        password (str): The password of the new user.
        email (str): The email of the new user.
        address (str): The address of the new user.
        phone (str): The phone number of the new user.
        role_id (int): The role ID of the new user.
    
    Returns:
        bool: True if the user was added successfully, False otherwise.
    """
    return register(username, password, email, address, phone)

def update_user(user_id, username, email, address, phone, role_id):
    """
    Update an existing user in the database.
    
    Args:
        user_id (int): The ID of the user to update.
        username (str): The new username of the user.
        email (str): The new email of the user.
        address (str): The new address of the user.
        phone (str): The new phone number of the user.
        role_id (int): The new role ID of the user.
    
    Returns:
        int: The number of rows affected by the update, or 0 if the update failed.
    """
    query = """
        UPDATE Users
        SET username = %s, email = %s, address = %s, phone = %s, role_id = %s
        WHERE user_id = %s
    """
    return execute_non_query(query, (username, email, address, phone, role_id, user_id))

def delete_user(user_id):
    """
    Delete a user from the database.
    
    Args:
        user_id (int): The ID of the user to delete.
    
    Returns:
        int: The number of rows affected by the deletion, or 0 if the deletion failed.
    """
    query = "DELETE FROM Users WHERE user_id = %s"
    return execute_non_query(query, (user_id,))
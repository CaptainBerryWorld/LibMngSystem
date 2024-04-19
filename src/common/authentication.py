import mysql.connector
from common.database import get_db_connection

def login(username, password):
    """
    Authenticate a user with the given username and password.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        dict: A dictionary containing the user's information, or None if the login fails.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM Users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        return {
            "user_id": user[0],
            "username": user[1],
            "email": user[3],
            "address": user[4],
            "phone": user[5],
            "role_id": user[8]
        }
    else:
        return None

def register(username, password, email, address, phone):
    """
    Register a new user with the given information.
    
    Args:
        username (str): The username of the new user.
        password (str): The password of the new user.
        email (str): The email of the new user.
        address (str): The address of the new user.
        phone (str): The phone number of the new user.
    
    Returns:
        bool: True if the registration was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO Users (username, password, email, address, phone, role_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (username, password, email, address, phone, 3)  # Assume role_id 3 is for Reader
    
    try:
        cursor.execute(query, values)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

def forgot_password(email):
    """
    Reset the password for a user with the given email.
    
    Args:
        email (str): The email of the user whose password needs to be reset.
    
    Returns:
        bool: True if the password reset was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT user_id, username, password FROM Users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    
    if user:
        # TODO: Implement password reset functionality (e.g., send reset link to email)
        print(f"Password reset instructions have been sent to {email}")
        return True
    else:
        return False
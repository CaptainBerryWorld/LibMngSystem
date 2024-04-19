import mysql.connector
from mysql.connector import errorcode

def get_db_connection():
    """
    Establish a connection to the MySQL database.
    
    Returns:
        mysql.connector.connection.MySQLConnection: A database connection object.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library_mng"
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return None

def execute_query(query, params=None):
    """
    Execute a SQL query and return the result.
    
    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters to pass to the query.
    
    Returns:
        list: A list of tuples containing the query results.
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result
    else:
        return []

def execute_non_query(query, params=None):
    """
    Execute a SQL query that doesn't return any results (e.g., INSERT, UPDATE, DELETE).
    
    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters to pass to the query.
    
    Returns:
        int: The number of rows affected by the query.
    """
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        affected_rows = cursor.rowcount
        conn.commit()
        conn.close()
        return affected_rows
    else:
        return 0
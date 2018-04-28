"""A MSSQL query script

    Example:
        python connect.py

    Todo:
        * N/A
"""
import json        # Provide Json format operations
import pypyodbc    # The connector lib

def connect_to_db(table='test')
    """Database connection handler

    Define the database connection string and connect
    to the database server. After a successful connection, a database query
    will be executed and the query result will saved to a JSON file

    Args:
        table (str): The table name
    
    Returns:
        N/A
    """
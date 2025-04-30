from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine, text
import pandas as pd
import datetime
from decimal import Decimal


# List all available databases in MySQL
def list_mysql_databases(username, password, host="localhost", port=3307):
    """
    Function to list all databases in the MySQL server.
    
    Args:
        username (str): MySQL username
        password (str): MySQL password
        host (str): MySQL host, default is localhost
        
    Returns:
        list: A list of all database names.
    """

    # Create connection string using the provided credentials
    uri = f"mysql+pymysql://{username}:{password}@{host}:{port}"
    engine = create_engine(uri)

    # Connect to MySQL and fetch all databases
    with engine.connect() as conn:
        dbs = conn.execute(text("SHOW DATABASES")).fetchall() 
    
    # Return the list of databases
    return [db[0] for db in dbs]


# Connect to a selected MySQL database
def connect_to_mysql_database(username, password, db_name, host="localhost", port=3307):
    """
    Function to connect to a specific database on MySQL.
    
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database to connect to
        host (str): MySQL host, default is localhost
        
    Returns:
        SQLDatabase: A connection object for the selected database.
    """

    uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"
    
    # Connect to the selected database using SQLDatabase from langchain
    db = SQLDatabase.from_uri(uri)
    return db


# Run the generated SQL query against the selected database
def run_query(db, sql_query):
    """
    Function to run an SQL query against the selected MySQL database.
    
    Args:
        db (SQLDatabase): The connected database object
        sql_query (str): The SQL query to execute
        
    Returns:
        DataFrame: A pandas DataFrame containing the query results.
    """
    sql_query = sql_query.strip().replace("```sql", "").replace("```", "").strip()
    result = db.run(sql_query, include_columns=True)
    
    safe_globals = {
    '__builtins__': None,
    'datetime': datetime,
    'Decimal': Decimal
    }

    result = eval(result, safe_globals)
    
    df = pd.DataFrame(result)

    return df

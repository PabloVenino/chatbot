import pyodbc
import sys

def connect_to_database(): ##dsn, uid=None, pwd=None):
  """Connects to a SQL Server database instance, using the providen dsn, username and password.

  Args:
      dsn (String): The configured name of the DSN.
      uid (String, optional): The username for SQL Server Authentication. Defaults to None.
      pwd (String, optional): The password for SQL Server Authentication. Defaults to None.

  Returns:
      Tuple (pyodc.Cursor, pyodc.Connection): Returns a tuple, with the SQL Server instance, with a Cursor and a Connection
  """
  try:
    connection: pyodbc.Connection = pyodbc.connect(r'Driver=SQL Server;Server=DESKTOP-1MTKL8P\PABLO;Database=tavares_confeitaria;Trusted_Connection=yes;', autocommit=True) ##;UID={uid};PWD={pwd}')
    cursor: pyodbc.Cursor = connection.cursor()
  except Exception as e:
    print(e)
    sys.exit(1)
  return cursor, connection


def close_connection(connection):
  """
    Closes a SQL Server Connection

  Args:
      connection (pyodbc Connection): Connection to close
  """
  connection.close()


def read_dataset(cursor: pyodbc.Cursor):
  columns = [column[0] for column in cursor.description]
  rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

  return rows
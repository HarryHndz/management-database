import pyodbc
from typing import Generator
SERVER = 'HARRY'
DATABASE = 'airbus380_acad'
USERNAME = 'arturo'
PASSWORD = '12345'

def get_db(
  database:str = DATABASE, 
  username:str = USERNAME, 
  password:str = PASSWORD
  )-> Generator[pyodbc.Connection, None, None]:
  connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={database};UID={username};PWD={password}'
  db = pyodbc.connect(connection_string)
  try:
    yield db
  finally:
    db.close()

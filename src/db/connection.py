import pyodbc

SERVER = 'HARRY'
DATABASE = 'master'
USERNAME = 'pepe2'
PASSWORD = '12345'

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

db = pyodbc.connect(connection_string)

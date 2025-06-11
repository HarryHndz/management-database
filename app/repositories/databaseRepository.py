from pyodbc import Connection


class DatabaseRepository:
  def __init__(self,db:Connection):
    self.db= db

  def get_databases(self,query:str):
    cursor = None
    try:
      cursor = self.db.cursor()
      cursor.execute(query)
      return cursor.fetchall()
    except Exception as e:
      raise e
    finally:
      if cursor:
        cursor.close()

  def execute_query(self, query:str):
    cursor = None
    try:
      cursor = self.db_connection.cursor()
      cursor.execute(query)
      self.db_connection.commit()
    except Exception as e:
      self.db_connection.rollback()
      raise e
    finally:
      if cursor:
        cursor.close()







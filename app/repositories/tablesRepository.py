from pyodbc import Connection

class TableRepository:
  def __init__(self, db:Connection):
    self.db = db

  async def get_tables(self):
    try:
      cursor = self.db.cursor()
      databases = cursor.execute("SELECT name,database_id,create_date FROM sys.databases WHERE database_id  NOT IN(1,2,3,4)")
      return databases.fetchall()
    except Exception as e:
      raise e
    finally:
      if cursor:
        cursor.close()
  async def get_table_by_id(self, table_name:str):
    cursor = None
    try:
      cursor = self.db.cursor()
      query = f"SELECT name,database_id,create_date FROM "
      cursor.execute(query)
      return cursor.fetchall()
    except Exception as e:
      raise e
    finally:
      if cursor:
        cursor.close()

  async def create_table(self,query:str):
    cursor = None
    try:
      cursor = self.db.cursor()
      cursor.execute(query)
      self.db.commit()
    except Exception as e:
      self.db.rollback()
      raise e
    finally:
      if cursor:
        cursor.close()

  async def update_table(self, table_id, table_data):
    return self.db.tables.update_one({"_id": table_id}, {"$set": table_data})

  async def delete_table(self, table_name:str):
    cursor = None
    try:
      cursor= self.db.cursor()
      cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
      self.db.commit()
    except Exception as e:
      self.db.rollback()
      raise e
    finally:
      if cursor:
        cursor.close()
        
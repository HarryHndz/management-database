from pyodbc import Connection

class TableRepository:
  def __init__(self, db:Connection):
    self.db = db

  def get_tables(self):
    return self.db.tables.find()

  def get_table_by_id(self, table_id):
    return self.db.tables.find_one({"_id": table_id})

  def create_table(self,query:str):
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
      self.db.close()

  def update_table(self, table_id, table_data):
    return self.db.tables.update_one({"_id": table_id}, {"$set": table_data})

  def delete_table(self, table_id):
    return self.db.tables.delete_one({"_id": table_id})
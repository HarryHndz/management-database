from pyodbc import Connection

class QueryRepository:
  def __init__(self, db:Connection):
    self.db = db
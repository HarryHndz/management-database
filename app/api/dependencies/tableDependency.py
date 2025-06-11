from pyodbc import Connection
from fastapi import Depends
from app.db.connection import get_db
from app.repositories.tablesRepository import TableRepository
from app.services.tableService import TableService


def get_table_dependency(db:Connection =Depends(get_db)) -> TableService:
  """
  Returns the table service for made operations in the tables.
  """
  table_repository = TableRepository(db=db)
  return TableService(repository=table_repository)
  
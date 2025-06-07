from app.repositories.tablesRepository import TableRepository
from pyodbc import Connection
from app.api.models.tableModel import TableModel
class TableService:
  def __init__(self, db:Connection):
    self.tableRepository = TableRepository(db=db)

  async def get_table(self, table_name):
    """Retrieve a table by its name."""
    repository = await self.tableRepository.get_tables()
    return repository

  async def create_table(self,schema:TableModel):
    table_name = schema.table_name
    columns = schema.schema
    query = " CREATE TABLE IF NOT EXISTS {} (".format(table_name)
    for column in columns:
      columnData = "{} {},".format(column.name, column.data_type)
      columnForeignKey = ""
      if column.isnullable:
        columnData += "NULL "
      else:
        columnData += "NOT NULL "
      if column.isPrimaryKey:
        columnData += "PRIMARY KEY "
      if column.isForeignKey and column.reference:
        name_ref = column.reference.name_table
        input_ref = column.reference.input_table
        columnForeignKey = "FOREING KEY ({}) REFERENCES {}({}),".format(column.name,column.reference,name_ref,input_ref)
        columnData += "\n {}".format(columnForeignKey)
      query += "\n {}".format(columnData)
    await self.tableRepository.create_table(query)
    

  async def delete_table(self, table_name):
    """Delete a table by its name."""
    repository = await self.tableRepository.delete_table()
    return repository

  async def update_table(self):
    """List all tables in the database."""
    repository = await self.tableRepository.update_table()
    return repository
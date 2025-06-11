from app.repositories.tablesRepository import TableRepository
from app.api.models.tableModel import TableModel

class TableService:
  def __init__(self,repository:TableRepository):
    self.tableRepository = repository

  async def get_table(self, table_name):
    """Retrieve a table by its name."""
    repository = await self.tableRepository.get_tables()
    return repository

  async def create_table(self,schemaDB:TableModel):
    """Create a table based on the provided schema."""
    table_name = schemaDB.table_name
    columns = schemaDB.columns
    query = " CREATE TABLE IF NOT EXISTS {} (".format(table_name)
    for column in columns:
      columnData = "{} {}".format(column.name, column.data_type)
      columnForeignKey = ""
      if column.isPrimaryKey == 1:
        columnData += " PRIMARY KEY IDENTITY(1,1)"
      if column.isForeignKey == 1 and column.reference:
        name_ref = column.reference.name_table
        input_ref = column.reference.input_table
        columnForeignKey = " FOREING KEY ({}) REFERENCES {}({})".format(column.name,name_ref,input_ref)
        columnData += columnForeignKey
      if column.isnullable == 1:
        columnData += " NULL,"
      else:
        columnData += " NOT NULL,"
      query += "\n {}".format(columnData)
    query = query[:-1]
    query += ")"
    await self.tableRepository.create_table(query)
    return query
    

  async def delete_table(self, table_name:str):
    """Delete a table by its name."""
    repository = await self.tableRepository.delete_table()
    return repository

  async def update_table(self):
    """List all tables in the database."""
    repository = await self.tableRepository.update_table()
    return repository
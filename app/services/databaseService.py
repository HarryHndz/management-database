from ..repositories.databaseRepository import DatabaseRepository

class DatabaseService:
  def __init__(self, repository:DatabaseRepository):
    self.databaseRepository = repository
  
  async def get_databases(self):
    """Retrieve a list of databases."""
    try:
      query = "SELECT name, database_id, create_date FROM sys.databases WHERE database_id NOT IN (1, 2, 3, 4)"
      databases = await self.databaseRepository.get_databases(query)
      return databases
    except Exception as e:
      raise e
  
  async def create_database(self, database_name: str):
    """Create a new database."""
    try:
      query = f"CREATE DATABASE {database_name}"
      await self.databaseRepository.execute_query(query)
      return {"message": "Database created successfully"}
    except Exception as e:
      raise e
  
  async def delete_database(self, database_name: str):
    """Delete a database."""
    try:
      query = f"DROP DATABASE IF EXISTS {database_name}"
      await self.databaseRepository.execute_query(query)
      return {"message": "Database deleted successfully"}
    except Exception as e:
      raise e
  
  async def update_name_database(self, old_name: str, new_name: str):
    """Update the name of an existing database."""
    try:
      query = f"""
        USE master;
        GO
        ALTER DATABASE {old_name}
        SET SINGLE_USER 
        WITH ROLLBACK IMMEDIATE;
        GO
        ALTER DATABASE {old_name}
        MODIFY NAME = {new_name};
        GO
        ALTER DATABASE {new_name}
        SET MULTI_USER;
        GO
      """
      await self.databaseRepository.execute_query(query)
      return {"message": "Database name updated successfully"}
    except Exception as e:
      raise e
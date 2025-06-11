from fastapi import APIRouter, Depends, HTTPException
from app.services.tableService import TableService
from app.db.connection import get_db
from app.api.models.tableModel import TableModel
from app.api.dependencies.tableDependency import get_table_dependency

router = APIRouter(
  prefix="/tables",
  tags=["tables"],
  responses={404: {"description": "Not found"}},
  dependencies=[Depends(lambda: None)]
)


@router.post("/create")
async def create_tables(schemaDB:TableModel,service:TableService = Depends(get_table_dependency)):
  """ 
  Create the necessary tables in the database.
  """
  try:
    query = await service.create_table(schemaDB)
    return{
      "message": "Tables created successfully",
      "table": query
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
      

@router.get("/status")
async def get_tables_status():
  """
  Get the status of the tables in the database.
  This is a placeholder function and should be implemented with actual logic.
  """
  try:
    status = {"status": "All tables are up to date"}
    return status
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
    

@router.delete("/delete")
async def delete_tables():
  """
  Delete the tables in the database.
  This is a placeholder function and should be implemented with actual logic.
  """
  try:
    return {"message": "Tables deleted successfully"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


@router.put("/update")
async def update_tables():
  """
  Update the tables in the database.
  This is a placeholder function and should be implemented with actual logic.
  """
  try:
    # Here you would typically call your database update logic
    # For example: await update_all_tables()
    return {"message": "Tables updated successfully"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
from pydantic import BaseModel


class ReferenceKeyModel(BaseModel):
  input_table: str
  name_table:str


class ColumnModel(BaseModel):
  name:str
  data_type:str
  isnullable:int = 1
  isPrimaryKey:int = 0
  isForeignKey:int = 0
  reference:ReferenceKeyModel | None = None

class TableModel(BaseModel):
  table_name:str
  columns: list[ColumnModel]
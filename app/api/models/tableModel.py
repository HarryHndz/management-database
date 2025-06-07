from pydantic import BaseModel


class ReferenceKeyModel(BaseModel):
  input_table: str
  name_table:str


class ColumnModel(BaseModel):
  name:str
  data_type:str
  isnullable:bool = True
  isPrimaryKey:bool = False
  isForeignKey:bool = False
  reference:ReferenceKeyModel | None = None

class TableModel(BaseModel):
  table_name:str
  schema: list[ColumnModel]
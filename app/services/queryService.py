

class QueryService:
  def __init__(self, db):
    self.db = db

  def get_query(self, query_id):
    query = self.db.get_query_by_id(query_id)
    if not query:
        raise ValueError("Query not found")
    return query

  def execute_query(self, query_id, params=None):
    query = self.get_query(query_id)
    return self.db.execute(query, params)

  def list_queries(self):
    return self.db.list_all_queries()
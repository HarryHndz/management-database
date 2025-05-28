from fastapi import FastAPI, HTTPException
from db.connection import db

app = FastAPI()

@app.get("/")
def reed_root():
  try:
    cursor = db.cursor()
    cursor.execute("SELECT 1")
    return {"message": "Database connection successful!"}
  except Exception as e:
    print(f"Error connecting to the database: {e}")
    raise HTTPException(status_code=500, detail="Database connection error")
  finally: 
    cursor.close()
    
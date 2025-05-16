# backend/main.py
from fastapi import FastAPI
from .database import crud, connection # Adjusted import
# from .database.connection import engine # Not directly needed here now
# from .database.models import Base # Not directly needed here now

# This was moved to crud.py
# Base.metadata.create_all(bind=engine) # Create tables

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    crud.create_db_and_tables() # Call the function from crud.py

@app.get("/")
async def root():
    return {"message": "Hello from Ancestry Explorer Backend!"}

@app.get("/api/ping")
async def ping():
    return {"message": "pong"}

# We will add more API endpoints later
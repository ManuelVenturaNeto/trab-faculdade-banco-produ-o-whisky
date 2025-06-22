# src/infra/config/init_db.py
from .db_config import DBConnectionHandler
from .db_base import Base  # Import the single Base instance

# IMPORT ALL MODELS FIRST TO REGISTER THEM WITH BASE
from src.infra.entities import *

def init_db():
    """Initialize the database by creating all tables."""
    print("Creating database tables...")
    
    # Debug: Show registered tables
    print(f"Registered tables: {list(Base.metadata.tables.keys())}")
    
    db_handler = DBConnectionHandler()
    db_handler.create_tables()
    print("Tables created successfully!")

if __name__ == "__main__":
    init_db()
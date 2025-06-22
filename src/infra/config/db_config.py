# src/infra/config/db_config.py
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from typing import Generator
import pymysql

# Import the single Base instance
from .db_base import Base

# Import all models to ensure they're registered
from src.infra.entities import *

class DBConnectionHandler:
    """Class to manage MySQL database connections using SQLAlchemy."""
    
    def __init__(self):
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "3306")
        db_user = os.getenv("DB_USER", "root")
        db_password = os.getenv("DB_PASSWORD", "")
        db_name = os.getenv("DB_NAME", "whisky_db")
        
        # MySQL connection string
        self.__connection_string = (
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        
        # Create database if it doesn't exist
        self.__ensure_database_exists()
        
        self.__engine = self.__create_database_engine()
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.__engine
        )

    def __ensure_database_exists(self):
        """Create database if it doesn't exist"""
        # Create temporary engine without database name
        temp_engine = create_engine(
            f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/"
        )
        
        # Create database if not exists
        with temp_engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {self.db_name}"))
            conn.commit()
        
        temp_engine.dispose()

    def __create_database_engine(self):
        return create_engine(
            self.__connection_string,
            pool_pre_ping=True,
            pool_recycle=3600,
            echo=True
        )

    @contextmanager
    def get_db(self) -> Generator:
        """Provide a database session for dependency injection."""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_engine(self):
        return self.__engine

    def create_tables(self):
        """Create all tables in the database."""
        print(f"Creating tables with engine: {self.__engine}")
        print(f"Tables to create: {list(Base.metadata.tables.keys())}")
        Base.metadata.create_all(bind=self.__engine)
        
    def __enter__(self):
        self.session = self.SessionLocal()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
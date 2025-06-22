# src/infra/config/base.py
from sqlalchemy.orm import declarative_base

# Single Base instance for the entire application
Base = declarative_base()
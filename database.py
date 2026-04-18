import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Python reads DATABASE_URL from .env file
load_dotenv()

# Location of database
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy central connection manager between fastAPI and Postgre, an instance of class create_engine. 
engine = create_engine(DATABASE_URL)

# Defines the structure (class) for individual queries
SessionLocal = sessionmaker(
    autocommit=False,  # changes are not saved accidentally
    autoflush=False,   # to avoid partial automatic writes
    bind=engine        # links sessions to the engine (database connection system)
)

# A Python class that defines a database table, instance of which correspond to a row in that table.
# SQLAlchemy uses this definition to create and interact with a real PostgreSQL table.
Base = declarative_base()

# Needed because FastAPI must give each request its own database session
# Prevents shared state between requests and avoids data conflicts
def get_db():
    db = SessionLocal()  # creates a new session (for querying dataset with methods built into SessionLocal() class), instance of SessionLocal
    try:
        yield db        # gives session to FastAPI route for queries
    finally:
        db.close()      # ensures session is always cleaned up after request
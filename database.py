import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy central connection manager between fastAPI and Postgre
engine = create_engine(DATABASE_URL)

# Session factory for database interactions
SessionLocal = sessionmaker(
    autocommit=False,  
    autoflush=False,   
    bind=engine        
)

# Base for ORM models (maps Python classes to database tables)
Base = declarative_base()

# Provide FastAPI a per-request DB session (avoids shared state across requests)
def get_db():
    db = SessionLocal()  # new session for this request
    try:
        yield db        # used by FastAPI dependency injection
    finally:
        db.close()      
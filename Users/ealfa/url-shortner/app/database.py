from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer

# 1. Connect to SQLite
DATABASE_URL = "sqlite:///./shortener.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 2. Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base class
Base = declarative_base()

# 4. Define the table model
class URL(Base):
    __tablename__ = "urls"
    short_id = Column(String, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    clicks = Column(Integer, default=0)
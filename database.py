from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://arcane_user:arcane123@localhost/arcane"

engine = create_engine(DATABASE_URL) # Connexion à la base PostgreSQL via DATABASE_URL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Créer des sessions 

Base = declarative_base() # Base de déclaration

from sqlalchemy import Column, Integer, String
from database import Base

class Personnage(Base):
    __tablename__ = "personnages"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, index=True)
    alias = Column(String)
    affiliation = Column(String)
    lieu_origine_id = Column(Integer)

class Relation(Base):
    __tablename__ = "relations"

    
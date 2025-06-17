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

    perso_1_id = Column(Integer, primary_key=True,)
    perso_2_id = Column(Integer, primary_key=True)
    type_relation = Column(String, nullable=False)



class Lieu(Base):
    __tablename__ = "lieux"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    
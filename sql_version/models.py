# TABLES SQLALCHEMY

from sqlalchemy import Column, Integer, String, ForeignKey
from sql_version.database import Base
from sqlalchemy.orm import relationship

# Classes python : Personnage, Relation, Lieu héritent de Base -> tables SQL avec colonnes

class Personnage(Base):
    __tablename__ = "personnages"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, index=True)
    alias = Column(String)
    affiliation = Column(String)
    images = relationship("Image", back_populates="personnages", cascade="all, delete-orphan")

    # lieu_origine_id = Column(Integer)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)  # Ex: "images/perso1.jpg"
    personnage_id = Column(Integer, ForeignKey("personnages.id"), nullable=False)

    personnage = relationship("Personnage", back_populates="images")






class Relation(Base):
    __tablename__ = "relations"

    perso_1_id = Column(Integer, ForeignKey("personnages.id"), primary_key=True,)
    perso_2_id = Column(Integer, ForeignKey("personnages.id"), primary_key=True)
    type_relation = Column(String, nullable=False)

# class RelationByName(Base):
#     __tablename__ = "relationsByName"

#     perso_1_name = Column(String, ForeignKey("personnages.name"), primary_key=True,)
#     perso_2_name = Column(String, ForeignKey("personnages.name"), primary_key=True)
#     type_relation = Column(String, nullable=False)






class Lieu(Base):
    __tablename__ = "lieux"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    
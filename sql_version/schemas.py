# MODÈLES PYDANTIC : définie les formes de données que l'API attend ou envoie

from pydantic import BaseModel

class PersonnageBase(BaseModel): # sans id pour la création (POST)
    nom: str
    alias: str
    affiliation: str
    # lieu_origine_id: int

class Personnage(PersonnageBase): # pour la lecture (GET)
    id: int

    class Config:
        from_attributes = True # converti les objets SQLAlchemy en dicts pour FastAPI




class LieuBase(BaseModel): # sans id pour la création (POST)
    nom: str
    description: str
    type: str

class Lieu(LieuBase): # pour la lecture (GET)
    id: int

    class Config:
        from_attributes = True







class RelationBase(BaseModel):
    perso_1_id: int
    perso_2_id: int
    type_relation: str

    class Config:
        from_attributes = True


# class RelationName(BaseModel):
#     perso_1_name: str
#     perso_2_name: str
#     type_relation: str

#     class Config:
#         from_attributes = True
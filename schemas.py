from pydantic import BaseModel

class PersonnageBase(BaseModel):
    nom: str
    alias: str
    affiliation: str
    lieu_origine_id: int

class Personnage(PersonnageBase):
    id: int

    class Config:
        orm_mode = True

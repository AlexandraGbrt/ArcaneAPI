
# uvicorn main_memory:app --reload    Lancer la version mémoire

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List


# app = FastAPI()




#========== PERSONNAGES =====================================================

class Personnage(BaseModel):
    id: int
    nom: str
    alias: str
    affiliation: str


personnages = [
    Personnage(id=1, nom="Powder", alias='Jinx', affiliation='Zaun'),
    Personnage(id=2, nom="Violet", alias='Vi', affiliation='Zaun'),
    Personnage(id=3, nom="Viktor", alias='Viktor', affiliation='Piltover'),
    Personnage(id=4, nom="Vander", alias='Vander', affiliation='Zaun'),
    Personnage(id=5, alias='Ekko', nom="Ekko", affiliation='Zaun'),
    Personnage(id=6, alias='Mel', nom="Mel", affiliation='Piltover'),
    Personnage(id=7, alias='Cupcake', nom="Caitlyn", affiliation='Piltover'),
]




@app.get("/personnages",  response_model=List[Personnage])
def get_personnages(affiliation: str | None = None):
    if affiliation is None:
        return personnages
    else : 
        return [p for p in personnages if p.affiliation == affiliation]
        # personnages_filtres = []
        # for p in personnages:
        #     if p.affiliation == affiliation:
        #         personnages_filtres.append(p)
        # return personnages_filtres



@app.get("/personnages/{id}")
def get_perso_by_id(id: int):
    for p in personnages : 
        if p.id == id :
            return p
    raise HTTPException(status_code=404, detail="Ce personnage n'existe pas")
       

@app.get("/total_perso")
def get_total_perso() -> dict:
    return {"total":len(personnages)} #======= longueur de la variables personnages




class PersoCreate(BaseModel):
    nom: str   
    alias: str
    affiliation: str

@app.post("/personnages", response_model=Personnage)
def add_personnages(new_perso: PersoCreate):
    max_id = 0
    for p in personnages: 
        if p.id > max_id:
            max_id = p.id 
    new_id = max_id + 1
    new = Personnage(
        id=new_id,
        nom=new_perso.nom,
        alias=new_perso.alias,
        affiliation=new_perso.affiliation
    )
    personnages.append(new)
    return new






# ============== RELATION personnage id=1 etc... ========================================

class Relation(BaseModel):
    perso_1_id: int
    perso_2_id: int
    type_relation: str

relations = [
    Relation(perso_1_id=1, perso_2_id=2, type_relation='soeurs'),
    Relation(perso_1_id=1, perso_2_id=5, type_relation='meilleurs ennemis'),

    Relation(perso_1_id=2, perso_2_id=5, type_relation='amis'),
    Relation(perso_1_id=2, perso_2_id=7, type_relation='amis ++'),

    Relation(perso_1_id=3, perso_2_id=6, type_relation='amis'),
   
    Relation(perso_1_id=4, perso_2_id=1, type_relation='père'),
    Relation(perso_1_id=4, perso_2_id=2, type_relation='père'),
    Relation(perso_1_id=4, perso_2_id=5, type_relation='amis'),
]

@app.get("/relations/{perso_id}", response_model=List[Relation])
async def get_relations_par_personnage(perso_id: int):
    relations_filtrees = []
    for rel in relations:
        if rel.perso_1_id == perso_id or rel.perso_2_id == perso_id:
            relations_filtrees.append(rel)
    return relations_filtrees

class RelationCreate(BaseModel):
    perso_1_id: int
    perso_2_id: int
    type_relation: str


@app.post("/relations", response_model=Relation)
def add_relations(new_rel: RelationCreate):
    def id_existe(id: int):
        for p in personnages:
            if p.id == id:
                return True
        return False

    if not id_existe(new_rel.perso_1_id) or not id_existe(new_rel.perso_2_id):
        raise HTTPException(status_code=404, detail="Un des personnages n'existe pas")

    newRelation = Relation(
        perso_1_id=new_rel.perso_1_id,
        perso_2_id=new_rel.perso_2_id,
        type_relation=new_rel.type_relation
    )
    relations.append(newRelation)
    return newRelation










#=================== LIEUX =============================================================

class Lieu(BaseModel):
    id: int
    nom: str
    description: str
    type: str

lieux = [
    Lieu(id=1, nom="Zaun", description="Ville souterraine sombre et industrielle", type="Ville"),
    Lieu(id=2, nom="Piltover", description="Ville brillante et avancée technologiquement", type="Ville"),
    Lieu(id=3, nom="Laboratoire de Viktor", description="Laboratoire de recherche et développement", type="Bâtiment"),
    Lieu(id=4, nom="The Last Drop", description="Le bar de Vander", type="Commerce"),
    Lieu(id=5, nom="Académie de Piltover", description="École de formation et de recherche", type="Bâtiment"),
    Lieu(id=6, nom="Marché de Zaun", description="Zone commerçante animée et chaotique", type="Quartier"),
    Lieu(id=7, nom="Maison Kiramman", description="Résidence familiale de Caitlyn", type="Bâtiment"),
    Lieu(id=8, nom="Repaire de Silco", description="Cachette secrète de Silco", type="Bâtiment"),
]

@app.get("/lieux", response_model=List[Lieu])
async def get_lieux():
    return lieux
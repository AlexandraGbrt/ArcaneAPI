# uvicorn main_sql:app --reload      Lancer la version SQL

from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import models #fichier models.py avec les tables Personnage, Relation et Lieu
from database import SessionLocal
from schemas import Personnage, PersonnageBase, RelationBase, Lieu, LieuBase  # modèle Pydantic


app = FastAPI()

# Dépendance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#========== PERSONNAGES =====================================================

@app.get("/personnages", response_model=List[Personnage])
def get_personnages(db: Session = Depends(get_db)): # crée et injecte une session de base de données à chaque requete
    personnages = db.query(models.Personnage).all() # cherche tous les personnages de la table SQL
    return personnages



@app.get("/personnages/{id}", response_model=Personnage)
def get_perso_by_id(id: int, db: Session = Depends(get_db)):
    personnage = db.query(models.Personnage).filter(models.Personnage.id == id).first()  # filter pour chercher l'id et first pour un seul résultat
    if personnage:
        return personnage
    raise HTTPException(status_code=404, detail="Ce personnage n'existe pas")



@app.post("/personnages", response_model=PersonnageBase)
def add_perso(new_perso: PersonnageBase, db: Session = Depends(get_db)):
    new = models.Personnage(
        nom=new_perso.nom,
        alias=new_perso.alias,
        affiliation=new_perso.affiliation
    )
    db.add(new)
    db.commit()
    db.refresh(new) # récupéré l'id généré
    return new








# ============== RELATION personnage id=1 etc... ===============================

@app.get("/relations/{perso_id}", response_model=List[RelationBase])
def get_relations(perso_id: int, db: Session = Depends(get_db)):
    relations = db.query(models.Relation).all()
    relations_filtrees = []
    for rel in relations:
        if rel.perso_1_id == perso_id or rel.perso_2_id == perso_id: 
            relations_filtrees.append(rel)     
    return relations_filtrees



@app.post("/relations", response_model=RelationBase)
def add_relation(new_rel: RelationBase, db: Session = Depends(get_db)):
    personnages = db.query(models.Personnage).all()
    def id_existe(id: int):
        for p in personnages:
            if p.id == id:
                return True
        return False
    if not id_existe(new_rel.perso_1_id) or not id_existe(new_rel.perso_2_id):
        raise HTTPException(status_code=404, detail="Un des personnages n'existe pas")
    
    newRelation = models.Relation(
        perso_1_id=new_rel.perso_1_id,
        perso_2_id=new_rel.perso_2_id,
        type_relation=new_rel.type_relation
    )
    db.add(newRelation)
    db.commit()
    db.refresh(newRelation)
    return newRelation












#=================== LIEUX ===============================================

@app.get("/lieux", response_model=List[Lieu])
def get_lieux(db: Session = Depends(get_db)):
    lieux = db.query(models.Lieu).all()
    return lieux
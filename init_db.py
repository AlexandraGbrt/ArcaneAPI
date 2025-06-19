from database import Base, engine, SessionLocal
from models import Personnage, Relation, Lieu
from sqlalchemy.orm import Session
import models

Base.metadata.create_all(bind=engine) # Crée physiquement les tables dans la base

def init_personnages(db: Session):
    personnages = [
        {"nom": "Powder", "alias": "Jinx", "affiliation": "Zaun", "lieu_origine_id": 1},
        {"nom": "Violet", "alias": "Vi", "affiliation": "Zaun", "lieu_origine_id": 1},
        {"nom": "Viktor", "alias": "Viktor", "affiliation": "Piltover", "lieu_origine_id": 3},
        {"nom": "Vander", "alias": "Vander", "affiliation": "Zaun", "lieu_origine_id": 4},
        {"nom": "Ekko", "alias": "Ekko", "affiliation": "Zaun", "lieu_origine_id": 6},
        {"nom": "Mel", "alias": "Mel", "affiliation": "Piltover", "lieu_origine_id": 5},
        {"nom": "Caitlyn", "alias": "Cupcake", "affiliation": "Piltover", "lieu_origine_id": 7},
    ]

    for perso_data in personnages:
        perso = models.Personnage(**perso_data)
        db.add(perso)
    db.commit()


# crée la session
db = SessionLocal()
init_personnages(db)
db.close()
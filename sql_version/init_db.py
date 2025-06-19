# INSERTION DES DONNÉES INITIALES

from database import Base, engine, SessionLocal
from models import Personnage, Relation, Lieu


# 1 - Crée physiquement les tables dans la base
Base.metadata.create_all(bind=engine) 

# 2 - Crée une session
db = SessionLocal()

# 3 - Données à insérer
personnages = [
    {"nom": "Powder", "alias": "Jinx", "affiliation": "Zaun"},
    {"nom": "Violet", "alias": "Vi", "affiliation": "Zaun"},
    {"nom": "Viktor", "alias": "Viktor", "affiliation": "Piltover"},
    {"nom": "Vander", "alias": "Vander", "affiliation": "Zaun"},
    {"nom": "Ekko", "alias": "Ekko", "affiliation": "Zaun"},
    {"nom": "Mel", "alias": "Mel", "affiliation": "Piltover"},
    {"nom": "Caitlyn", "alias": "Cupcake", "affiliation": "Piltover"},
]

lieux = [
    {"id": 1, "nom": "Zaun", "description": "Ville souterraine sombre et industrielle", "type": "Ville"},
    {"id": 2, "nom": "Piltover", "description": "Ville brillante et avancée technologiquement", "type": "Ville"},
    {"id": 3, "nom": "Laboratoire de Viktor", "description": "Laboratoire de recherche et développement", "type": "Bâtiment"},
    {"id": 4, "nom": "The Last Drop", "description": "Le bar de Vander", "type": "Commerce"},
    {"id": 5, "nom": "Académie de Piltover", "description": "École de formation et de recherche", "type": "Bâtiment"},
    {"id": 6, "nom": "Marché de Zaun", "description": "Zone commerçante animée et chaotique", "type": "Quartier"},
    {"id": 7, "nom": "Maison Kiramman", "description": "Résidence familiale de Caitlyn", "type": "Bâtiment"},
    {"id": 8, "nom": "Repaire de Silco", "description": "Cachette secrète de Silco", "type": "Bâtiment"},
]

relations = [
    {"perso_1_id": 1, "perso_2_id": 2, "type_relation": "soeurs"},
    {"perso_1_id": 1, "perso_2_id": 5, "type_relation": "meilleurs ennemis"},
    {"perso_1_id": 2, "perso_2_id": 5, "type_relation": "amis"},
    {"perso_1_id": 2, "perso_2_id": 7, "type_relation": "amis ++"},
    {"perso_1_id": 3, "perso_2_id": 6, "type_relation": "amis"},
    {"perso_1_id": 4, "perso_2_id": 1, "type_relation": "père"},
    {"perso_1_id": 4, "perso_2_id": 2, "type_relation": "père"},
    {"perso_1_id": 4, "perso_2_id": 5, "type_relation": "amis"},
]

# 4 - Insère les personnages, lieux er relations
for perso_data in personnages:
    if not db.query(Personnage).filter_by(nom=perso_data["nom"]).first():
        db.add(Personnage(**perso_data))

for lieu_data in lieux:
    if not db.query(Lieu).filter_by(nom=lieu_data["nom"]).first():
        db.add(Lieu(**lieu_data))

for rel_data in relations:
    exists = db.query(Relation).filter_by(
        perso_1_id=rel_data["perso_1_id"],
        perso_2_id=rel_data["perso_2_id"]
    ).first()
    if not exists:
        db.add(Relation(**rel_data))


# 5 - Sauvegarde et fermeture de session
db.commit()
db.close()
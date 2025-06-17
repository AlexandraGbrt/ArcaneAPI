import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_liste_personnages():
    response = client.get("/personnages") # simule la requête HTTP
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) # vérification qu'une liste est renvoyée
    assert len(data) > 0  # vérification qu’il y a au moins un personnage

def test_ajout_perso():
    response = client.post("/personnages", json={
        "nom": "Marcus",
        "alias": "Enforcer",
        "affiliation": "Piltover"
    })
    assert response.status_code == 200

def test_get_perso_erreur():
    response = client.get("/personnages/999")
    assert response.status_code == 404
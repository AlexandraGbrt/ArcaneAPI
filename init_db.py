from database import Base, engine
from models import Personnage

Base.metadata.create_all(bind=engine)
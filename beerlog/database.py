from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)




try:   
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
except RuntimeError:
    print("TOPzera")

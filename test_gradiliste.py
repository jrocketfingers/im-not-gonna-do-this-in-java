from db import session
from models import Gradiliste
from datetime import date

datum = date(2017, 1, 1)
g = Gradiliste(naziv="naziv", datum_osnivanja=datum)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

Base = declarative_base()

class Gradiliste(Base):
    __tablename__ = 'gradilista'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    datum_osnivanja = Column(DateTime)


class Objekat(Base):
    __tablename__ = 'objekti'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    id_gradilista = Column(Integer, ForeignKey('gradilista.id'))


class Sprat(Base):
    __tablename__ = 'spratovi'

    id = Column(Integer, primary_key=True)
    br_sprata = Column(Integer)
    id_objekta = Column(Integer, ForeignKey('objekat.id'))


class Zaposleni(Base):
    __tablename__ = 'zaposleni'

    id = Column(Integer, primary_key=True)
    ime = Column(String)
    prezime = Column(String)
    jmbg = Column(Integer)
    pol = Column(String)
    ziro_racun = Column(String)
    email = Column(String)
    broj_telefona = Column(String)


class Sef(Zaposleni):
    __mapper_args__ = {

    }


class Magacin(Base):
    __tablename__ = 'magacini'

    id = Column(Integer, primary_key=True)
    id_sef = Column(Integer, ForeignKey('sefovi.id')

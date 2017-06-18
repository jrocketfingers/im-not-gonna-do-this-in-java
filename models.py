from decimal import Decimal

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric, event
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class Gradiliste(Base):
    __tablename__ = 'gradilista'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    datum_osnivanja = Column(Date)
    magacin = relationship("Magacin", uselist=False, back_populates="gradiliste")


class Objekat(Base):
    __tablename__ = 'objekti'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    id_gradilista = Column(Integer, ForeignKey('gradilista.id'))


class Sprat(Base):
    __tablename__ = 'spratovi'

    id = Column(Integer, primary_key=True)
    br_sprata = Column(Integer)
    id_objekta = Column(Integer, ForeignKey('objekti.id'))


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

    ukupan_isplacen_iznos = Column(Numeric(scale=2), default=Decimal(0))
    broj_trenutno_zaduzene_opreme = Column(Integer, default=0)
    prosecna_ocena = Column(Numeric(scale=2))

    id_magacin = Column(Integer, ForeignKey('magacini.id'))
    magacin = relationship("Magacin", back_populates="zaposleni", foreign_keys=[id_magacin])

    zaduzenja = relationship("ZaduzenjeOpreme", back_populates="zaposleni")
    poslovi = relationship("ZaposleniRadiNaPoslu", back_populates="zaposleni")

    def __str__(self):
        return f"<Zaposleni id: {self.id}>"

    def __repr__(self):
        return self.__str__()


class Magacin(Base):
    __tablename__ = 'magacini'

    id = Column(Integer, primary_key=True)
    id_sef = Column(Integer, ForeignKey('zaposleni.id'))
    id_gradilista = Column(Integer, ForeignKey('gradilista.id'))
    plata = Column(Numeric(scale=2))

    gradiliste = relationship("Gradiliste", back_populates="magacin", foreign_keys=[id_gradilista])
    zaposleni = relationship("Zaposleni", primaryjoin="Zaposleni.id_magacin==Magacin.id", back_populates="magacin")
    sef = relationship("Zaposleni", primaryjoin="Zaposleni.id==Magacin.id_sef")


class Roba(Base):
    __tablename__ = 'roba'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    kod = Column(String(length=1))
    id_tip_robe = Column(Integer, ForeignKey('tipovi_robe.id'))


class TipRobe(Base):
    __tablename__ = 'tipovi_robe'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)


class NUD(Base):
    __tablename__ = 'NUD'

    id = Column(Integer, primary_key=True)
    naziv = Column(String)
    cena_izrade = Column(Numeric(scale=2))
    jedinicna_plata = Column(Numeric(scale=2))


class RobaUMagacinu(Base):
    __tablename__ = 'roba_u_magacinu'

    id_robe = Column(Integer, ForeignKey('roba.id'), primary_key=True)
    id_magacina = Column(Integer, ForeignKey('magacini.id'), primary_key=True)

    roba = relationship("Roba")
    magacin = relationship("Magacin")

    kolicina = Column(Numeric(scale=2), default=Decimal(0))
    broj_jedinica = Column(Integer, default=0)


class PotrebanMaterijal(Base):
    __tablename__ = 'potreban_materijal'

    id_robe = Column(Integer, ForeignKey('roba.id'), primary_key=True)
    id_nud = Column(Integer, ForeignKey('NUD.id'), primary_key=True)

    roba = relationship("Roba")
    NUD = relationship("NUD")

    kolicina = Column(Numeric(scale=2))
    broj_jedinica = Column(Integer)


class Posao(Base):
    __tablename__ = 'poslovi'

    id = Column(Integer, primary_key=True)

    id_norma_ugradnog_dela = Column(Integer, ForeignKey('NUD.id'))
    id_sprat = Column(Integer, ForeignKey('spratovi.id'))
    datum_pocetka = Column(Date)

    zaposleni_na_poslu = relationship("ZaposleniRadiNaPoslu", back_populates="posao")
    nud = relationship("NUD", foreign_keys=[id_norma_ugradnog_dela])


class ZaposleniRadiNaPoslu(Base):
    __tablename__ = 'zaposleni_radi_na_poslu'

    id = Column(Integer, primary_key=True)

    id_posla = Column(Integer, ForeignKey('poslovi.id'))
    id_zaposlenog = Column(Integer, ForeignKey('zaposleni.id'))
    datum_pocetka = Column(Date)
    datum_kraja = Column(Date)

    zaposleni = relationship("Zaposleni", back_populates="poslovi", foreign_keys=[id_zaposlenog])
    ocena = Column(Numeric(scale=2))

    posao = relationship("Posao", back_populates="zaposleni_na_poslu", foreign_keys=[id_posla])


class ZaduzenjeOpreme(Base):
    __tablename__ = 'zaduzenje_opreme'

    id = Column(Integer, primary_key=True)

    id_zaposlenog = Column(Integer, ForeignKey('zaposleni.id'))
    id_magacina = Column(Integer, ForeignKey('roba_u_magacinu.id_magacina'))
    id_robe = Column(Integer, ForeignKey('roba_u_magacinu.id_robe'))
    datum_zaduzenja = Column(Date)
    datum_razduzenja = Column(Date)
    napomena = Column(String)

    zaposleni = relationship("Zaposleni", back_populates="zaduzenja", foreign_keys=[id_zaposlenog])
    roba_u_magacinu = relationship("RobaUMagacinu",
                                   primaryjoin="and_(ZaduzenjeOpreme.id_robe==RobaUMagacinu.id_robe,"
                                               "ZaduzenjeOpreme.id_magacina==RobaUMagacinu.id_magacina)",
                                   foreign_keys=[id_robe, id_magacina])


@event.listens_for(ZaduzenjeOpreme, 'after_insert')
def zaduzenje_opreme_start(mapper, connection, target):
    roba_u_magacinu = RobaUMagacinu.__table__
    zaposleni = Zaposleni.__table__
    connection.execute(
        roba_u_magacinu.update().where(roba_u_magacinu.c.id_magacina==target.id_magacina)
                       .where(roba_u_magacinu.c.id_robe==target.id_robe)
                       .values(broj_jedinica=roba_u_magacinu.c.broj_jedinica - 1)
    )

    connection.execute(
        zaposleni.update().where(zaposleni.c.id==target.id_zaposlenog)
                 .values(broj_trenutno_zaduzene_opreme=zaposleni.c.broj_trenutno_zaduzene_opreme + 1)
    )


@event.listens_for(ZaduzenjeOpreme.datum_razduzenja, 'set')
def zaduzenje_opreme_stop(target, value, oldvalue, initiator):
    target.roba_u_magacinu.broj_jedinica += 1
    target.zaposleni.broj_trenutno_zaduzene_opreme -= 1


@event.listens_for(ZaposleniRadiNaPoslu, 'after_update')
def ocena_data(mapper, connection, target):
    session = sessionmaker()(bind=connection)
    zaposleni = session.query(Zaposleni).get(target.id_zaposlenog)
    result = session.query(func.avg(ZaposleniRadiNaPoslu.ocena)).filter_by(id_zaposlenog=target.id_zaposlenog).first()[0]
    zaposleni.prosecna_ocena = result
    session.commit()

from decimal import Decimal

from sqlalchemy.sql.expression import update

from models import (Gradiliste, Objekat, Sprat, Zaposleni, TipRobe, Magacin, NUD, Roba, RobaUMagacinu,
                    PotrebanMaterijal, Posao, ZaposleniRadiNaPoslu, ZaduzenjeOpreme)
from db import session


def formula_za_isplatu(prosecna_ocena, br_dana, trajanje, jedinicna_plata):
    return prosecna_ocena * br_dana / trajanje * jedinicna_plata


class SUT:
    def unesi_gradiliste(self, naziv, datum_osnivanja):
        gradiliste = Gradiliste(naziv=naziv, datum_osnivanja=datum_osnivanja)
        session.add(gradiliste)
        session.flush()
        return gradiliste.id

    def obrisi_gradiliste(self, id_gradiliste):
        session.query(Gradiliste).filter_by(id=id_gradiliste).delete()
        return True

    def dohvati_sva_gradilista(self):
        return list(session.query(Gradiliste))

    def unesi_objekat(self, naziv, id_gradiliste):
        objekat = Objekat(naziv=naziv, id_gradilista=id_gradiliste)
        session.add(objekat)
        session.flush()
        return objekat.id

    def obrisi_objekat(self, id_objekat):
        session.query(Objekat).filtery_by(id=id_objekat).delete()
        return True

    def unesi_sprat(self, br_sprata, id_objekat):
        sprat = Sprat(br_sprata=br_sprata, id_objekta=id_objekat)
        session.add(sprat)
        session.flush()
        return sprat.id

    def obrisi_sprat(self, id_sprat):
        session.query(Sprat).filter_by(id=id_sprat).delete()
        return True

    def unesi_zaposlenog(self, ime, prezime, jmbg, pol, ziro_racun, email, broj_telefona):
        zaposleni = Zaposleni(ime=ime,
                              prezime=prezime,
                              jmbg=jmbg,
                              pol=pol,
                              ziro_racun=ziro_racun,
                              email=email,
                              broj_telefona=broj_telefona)
        session.add(zaposleni)
        session.flush()
        return zaposleni.id

    def obrisi_zaposlenog(self, id_zaposleni):
        session.query(Zaposleni).filter_by(id=id_zaposleni).delete()
        return True

    def dohvati_ukupan_isplacen_iznos_za_zaposlenog(self, id_zaposleni):
        zaposleni = session.query(Zaposleni).get(id_zaposleni)
        return zaposleni.ukupan_isplacen_iznos

    def dohvati_prosecnu_ocenu_za_zaposlenog(self, id_zaposleni):
        zaposleni = session.query(Zaposleni).get(id_zaposleni)
        if zaposleni.prosecna_ocena:
            return zaposleni.prosecna_ocena
        else:
            return 10

    def dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(self, id_zaposleni):
        zaposleni = session.query(Zaposleni).get(id_zaposleni)
        return zaposleni.broj_trenutno_zaduzene_opreme

    def dohvati_sve_zaposlene(self):
        return [id for (id, ) in session.query(Zaposleni.id).all()]

    def unesi_magacin(self, id_sef, plata, id_gradiliste):
        magacin = Magacin(id_sef=id_sef, plata=plata, id_gradilista=id_gradiliste)
        session.add(magacin)
        session.flush()
        sef = session.query(Zaposleni).get(id_sef)
        sef.id_magacin = magacin.id
        session.flush()
        return magacin.id

    def obrisi_magacin(self, id_magacin):
        session.query(Magacin).filter_by(id=id_magacin).delete()
        return True

    def izmeni_sefa_za_magacin(self, id_magacin, id_sef_novo):
        magacin = session.query(Magacin).get(id_magacin)
        magacin.id_sef = id_sef_novo
        return True

    def izmeni_platu_za_magacin(self, id_magacin, plata_novo):
        magacin = session.query(Magacin).get(id_magacin)
        magacin.plata = plata_novo
        return True

    def isplati_plate_zaposlenima_u_magacinu(self, id_magacin):
        magacin = session.query(Magacin).get(id_magacin)
        for zaposlen in magacin.zaposleni:
            zaposlen.ukupan_isplacen_iznos += zaposlen.magacin.plata

    def isplati_plate_zaposlenima_u_svim_magacinima(self):
        session.flush()
        for magacin in session.query(Magacin).all():
            self.isplati_plate_zaposlenima_u_magacinu(magacin.id)

    def unesi_robu_u_magacin_po_kolicini(self, id_roba, id_magacin, kolicina):
        roba_u_magacinu = session.query(RobaUMagacinu).get((id_roba, id_magacin))
        if roba_u_magacinu is None:
            roba_u_magacinu = RobaUMagacinu(id_robe=id_roba, id_magacina=id_magacin, kolicina=Decimal('0'))
        roba_u_magacinu.kolicina += kolicina
        session.merge(roba_u_magacinu)

    def unesi_robu_u_magacin_po_broju_jedinica(self, id_roba, id_magacin, broj_jedinica):
        roba_u_magacinu = session.query(RobaUMagacinu).get((id_roba, id_magacin))
        if roba_u_magacinu is None:
            roba_u_magacinu = RobaUMagacinu(id_robe=id_roba, id_magacina=id_magacin, broj_jedinica=0)
        roba_u_magacinu.broj_jedinica += broj_jedinica
        session.merge(roba_u_magacinu)

    def uzmi_robu_iz_magacina_po_kolicini(self, id_roba, id_magacin, kolicina):
        roba_u_magacinu = session.query(RobaUMagacinu).get((id_roba, id_magacin))
        if roba_u_magacinu is None:
            raise Exception("Roba mora postojati u magacinu")

        if(roba_u_magacinu.kolicina - kolicina >= 0):
            roba_u_magacinu.kolicina -= kolicina
        else:
            raise Exception("Pokusana je uzeti veca jedinica nego sto je dostupna")

    def uzmi_robu_iz_magacina_po_broju_jedinica(self, id_roba, id_magacin, broj_jedinica):
        roba_u_magacinu = session.query(RobaUMagacinu).get((id_roba, id_magacin))
        if roba_u_magacinu is None:
            raise Exception("Roba mora postojati u magacinu")

        if(roba_u_magacinu.broj_jedinica - broj_jedinica >= 0):
            roba_u_magacinu.broj_jedinica -= broj_jedinica
        else:
            raise Exception("Pokusano je uzeti vise jedinica nego sto je dostupno")

    def pogledaj_kolicinu_robe_u_magacinu(self, id_roba, id_magacin):
        roba_u_magacinu = session.query(RobaUMagacinu).filter_by(id_robe=id_roba, id_magacina=id_magacin).first()
        return roba_u_magacinu.kolicina

    def pogledaj_broj_jedinica_robe_u_magacinu(self, id_roba, id_magacin):
        roba_u_magacinu = session.query(RobaUMagacinu).filter_by(id_robe=id_roba, id_magacina=id_magacin).first()
        return roba_u_magacinu.broj_jedinica


    def unesi_tip_robe(self, naziv):
        session.add(TipRobe(naziv=naziv))
        return True

    def obrisi_tip_robe(self, id_tip_robe):
        session.query(TipRobe).filter_by(id=id_tip_robe).delete()
        return True

    def unesi_robu(self, naziv, kod, id_tip_robe):
        roba = Roba(naziv=naziv, kod=kod, id_tip_robe=id_tip_robe)
        session.add(roba)
        session.flush()
        return roba.id

    def obrisi_robu(self, id_roba):
        session.query(Roba).filter_by(id=id_roba).delete()
        return True

    def dohvati_svu_robu(self):
        return list(session.query(Roba))

    def zaposleni_radi_u_magacinu(self, id_zaposleni, id_magacin):
        zaposleni = session.query(Zaposleni).get(id_zaposleni)
        zaposleni.id_magacin = id_magacin

    def zaposleni_ne_radi_u_magacinu(self, id_zaposleni):
        zaposleni = session.query(Zaposleni).get(id_zaposleni)
        zaposleni.id_magacin = None

    def zaposleni_zaduzuje_opremu(self, id_zaposlenog_koji_zaduzuje, id_magacin, id_roba, datum_zaduzenja, napomena):
        zaduzenje = ZaduzenjeOpreme(id_zaposlenog=id_zaposlenog_koji_zaduzuje,
                                    id_magacina=id_magacin,
                                    id_robe=id_roba,
                                    datum_zaduzenja=datum_zaduzenja,
                                    napomena=napomena)
        session.add(zaduzenje)
        session.flush()
        return zaduzenje.id

    def zaposleni_razduzuje_opremu(self, id_zaduzenja_opreme, datum_razduzenja):
        zaduzenje = session.query(ZaduzenjeOpreme).filter_by(id=id_zaduzenja_opreme).first()
        zaduzenje.datum_razduzenja = datum_razduzenja

    def unesi_normu_ugradnog_dela(self, naziv, cena_izrade, jedinicna_plata_radnika):
        nud = NUD(naziv=naziv, cena_izrade=cena_izrade, jedinicna_plata=jedinicna_plata_radnika)
        session.add(nud)
        session.flush()
        return nud.id

    def obrisi_normu_ugradnog_dela(self, id_norma_ugradnog_dela):
        session.query(NUD).filter_by(id=id_norma_ugradnog_dela).delete()

    def dohvati_jedinicnu_platu_radnika_norme_ugradnog_dela(self, id_n_r):
        nud = session.query(NUD).get(id_n_r)
        return nud.jedinicna_plata

    def unesi_potreban_materijal_po_broju_jedinica(self, id_roba_koja_je_potrosni_materijal, id_norma_ugradnog_dela, broj_jedinica):
        potreban_materijal = PotrebanMaterijal(id_robe=id_roba_koja_je_potrosni_materijal,
                                               id_nud=id_norma_ugradnog_dela,
                                               broj_jedinica=broj_jedinica)
        session.add(potreban_materijal)

    def unesi_potreban_materijal_po_kolicini(self, id_roba_koja_je_potrosni_materijal, id_norma_ugradnog_dela, kolicina):
        potreban_materijal = PotrebanMaterijal(id_robe=id_roba_koja_je_potrosni_materijal,
                                               id_nud=id_norma_ugradnog_dela,
                                               kolicina=kolicina)
        session.add(potreban_materijal)

    def obrisi_potreban_materijal(self, id_roba_koja_je_potrosni_materijal, id_norma_ugradnog_dela):
        session.query(PotrebanMaterijal).filter_by(id_robe=id_roba_koja_je_potrosni_materijal,
                                                   id_nud=id_norma_ugradnog_dela) \
                                        .delete()

    def unesi_posao(self, id_norma_ugradnog_dela, id_sprat, datum_pocetka):
        posao = Posao(id_norma_ugradnog_dela=id_norma_ugradnog_dela, id_sprat=id_sprat, datum_pocetka=datum_pocetka)
        session.add(posao)
        session.flush()
        return posao.id

    def obrisi_posao(self, id_posao):
        session.query(Posao).filter_by(id=id_posao).delete()

    def izmeni_datum_pocetka_za_posao(self, id_posao, datum_pocetka):
        posao = session.query(Posao).get(id_posao)
        posao.datum_pocetka = datum_pocetka

    def zavrsi_posao(self, id_posao, datum_kraja):
        posao = session.query(Posao).get(id_posao)
        posao.datum_kraja = datum_kraja

        trajanje_posla = (posao.datum_kraja - posao.datum_pocetka).days + 1

        for zaposleni_radi_na_poslu in posao.zaposleni_na_poslu:
            dana_na_poslu = (zaposleni_radi_na_poslu.datum_kraja - zaposleni_radi_na_poslu.datum_pocetka).days + 1
            plata = zaposleni_radi_na_poslu.posao.nud.jedinicna_plata

            zaposleni = zaposleni_radi_na_poslu.zaposleni

            zaposleni.ukupan_isplacen_iznos += formula_za_isplatu(zaposleni.prosecna_ocena,
                                                                  dana_na_poslu,
                                                                  trajanje_posla,
                                                                  plata)

    def zaposleni_radi_na_poslu(self, id_zaposleni, id_posao, datum_pocetka):
        zaposleni_radi_na_poslu = ZaposleniRadiNaPoslu(id_zaposlenog=id_zaposleni,
                                                       id_posla=id_posao,
                                                       datum_pocetka=datum_pocetka)
        session.add(zaposleni_radi_na_poslu)
        session.flush()
        return zaposleni_radi_na_poslu.id

    def zaposleni_je_zavrsio_sa_radom_na_poslu(self, id_zaposleni_na_poslu, datum_kraja):
        zaposleni_radi_na_poslu = session.query(ZaposleniRadiNaPoslu).get(id_zaposleni_na_poslu)
        zaposleni_radi_na_poslu.datum_kraja = datum_kraja

    def izmeni_datum_pocetka_rada_zaposlenog_na_poslu(self, id_zaposleni_na_poslu, datum_pocetka_novo):
        zaposleni_radi_na_poslu = session.query(ZaposleniRadiNaPoslu).get(id_zaposleni_na_poslu)
        zaposleni_radi_na_poslu.datum_pocetka = datum_pocetka_novo

    def izmeni_datum_kraja_rada_zaposlenog_na_poslu(self, id_zaposleni_na_poslu, datum_kraja_novo):
        zaposleni_radi_na_poslu = session.query(ZaposleniRadiNaPoslu).get(id_zaposleni_na_poslu)
        zaposleni_radi_na_poslu.datum_kraja = datum_pocetka_kraja

    def zaposleni_dobija_ocenu(self, id_zaposleni_na_poslu, ocena):
        zaposleni_radi_na_poslu = session.query(ZaposleniRadiNaPoslu).get(id_zaposleni_na_poslu)
        zaposleni_radi_na_poslu.ocena = ocena

    def obrisi_ocenu_zaposlenom(self, id_zaposleni_na_poslu):
        zaposleni_radi_na_poslu = session.query(ZaposleniRadiNaPoslu).get(id_zaposleni_na_poslu)
        zaposleni_radi_na_poslu.ocena = None

    def izmeni_ocenu_za_zaposlenog_na_poslu(self, id_zaposleni_na_poslu, ocena_novo):
        zaposleni_radi_na_poslu = session.query(ZaposleniRadiNaPoslu).get(id_zaposleni_na_poslu)
        zaposleni_radi_na_poslu.ocena = ocena_novo

import math

from implementation import SUT
from datetime import date
from decimal import Decimal

from db import engine
from models import Base


def formula_za_isplatu(prosecna_ocena, br_dana, trajanje, jedinicna_plata):
    return prosecna_ocena * br_dana / trajanje * jedinicna_plata


def test(f):
    procenata = 0

    id_gradilista = f.unesi_gradiliste("Gradiliste 1", date(2015, 8, 25))
    id_objekat = f.unesi_objekat("Stambena zgrada 1", id_gradilista)
    id_sprat0 = f.unesi_sprat(0, id_objekat)
    id_sprat1 = f.unesi_sprat(1, id_objekat)
    f.unesi_sprat(2, id_objekat)
    f.unesi_sprat(3, id_objekat)
    id_htz = f.unesi_tip_robe("HTZ")
    id_alat = f.unesi_tip_robe("alat")
    id_materijal = f.unesi_tip_robe("materijal")

    f.unesi_zaposlenog("Milos", "Milosevic", "2503989720031", "M", "370-11032274-01", "milos@google.com", "069/1245301")
    f.unesi_zaposlenog("Jovan", "Jovanovic", "2403989720031", "M", "370-11032274-02", "jovan@google.com", "069/1245302")
    f.unesi_zaposlenog("Marko", "Markovic", "2402989720031", "M", "370-11032274-03", "marko@google.com", "069/1245303")
    f.unesi_zaposlenog("Magdalena", "Despotovic", "2403987720031", "Z", "370-11032274-03", "magdalena@google.com", "069/1245303")
    f.unesi_zaposlenog("Katarina", "Vasic", "1204990720031", "Z", "370-11032274-04", "katarina@google.com", "069/1245304")

    lista_zaposlenih = f.dohvati_sve_zaposlene()
    id_magacin = f.unesi_magacin(lista_zaposlenih[0], Decimal(500.00), id_gradilista)
    f.zaposleni_radi_u_magacinu(lista_zaposlenih[1], id_magacin)

    id_nud = f.unesi_normu_ugradnog_dela("Ugradni deo 1", Decimal(800), Decimal(50))

    id_roba = f.unesi_robu("Pesak", "0001", id_materijal)
    f.unesi_robu_u_magacin_po_kolicini(id_roba, id_magacin, Decimal(3000))
    f.unesi_potreban_materijal_po_kolicini(id_roba, id_nud, Decimal(500))

    id_roba = f.unesi_robu("Cigla", "0002", id_materijal)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 3000)
    f.unesi_potreban_materijal_po_broju_jedinica(id_roba, id_nud, 500)

    id_roba = f.unesi_robu("Cement", "0003", id_materijal)
    f.unesi_robu_u_magacin_po_kolicini(id_roba, id_magacin, Decimal(3000))
    f.unesi_potreban_materijal_po_kolicini(id_roba, id_nud, Decimal(500))

    id_roba = f.unesi_robu("Keramicka plocica", "0004", id_materijal)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 3000)
    f.unesi_potreban_materijal_po_broju_jedinica(id_roba, id_nud, 500)

    id_roba = f.unesi_robu("Crep", "0005", id_materijal)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 3000)
    f.unesi_potreban_materijal_po_broju_jedinica(id_roba, id_nud, 500)

    id_roba = f.unesi_robu("Armatura", "0006", id_materijal)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 3000)
    f.unesi_potreban_materijal_po_broju_jedinica(id_roba, id_nud, 500)

    alat = []

    id_roba = f.unesi_robu("Busilica", "0007", id_alat)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 30)
    alat.append(id_roba)

    id_roba = f.unesi_robu("Cekic", "0008", id_alat)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 30)
    alat.append(id_roba)

    id_roba = f.unesi_robu("Elektricni odvijac", "0009", id_alat)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 30)
    alat.append(id_roba)

    id_roba = f.unesi_robu("Kruzna testera", "0010", id_alat)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 30)
    alat.append(id_roba)

    htz_oprema = []

    id_roba = f.unesi_robu("Rukavice", "0011", id_htz)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 50)
    htz_oprema.append(id_roba)

    id_roba = f.unesi_robu("Naocare", "0012", id_htz)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 50)
    htz_oprema.append(id_roba)

    id_roba = f.unesi_robu("Cipele", "0013", id_htz)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 50)
    htz_oprema.append(id_roba)

    id_roba = f.unesi_robu("Stitnik za kolena", "0014", id_htz)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 50)
    htz_oprema.append(id_roba)

    id_roba = f.unesi_robu("Kaciga", "0015", id_htz)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, 50)
    htz_oprema.append(id_roba)

    trenutno_vreme = date(2016, 1, 1)
    pocetak_posla1 = trenutno_vreme
    id_posao1 = f.unesi_posao(id_nud, id_sprat0, trenutno_vreme)
    id_z2_p1 = f.zaposleni_radi_na_poslu(lista_zaposlenih[2], id_posao1, trenutno_vreme)
    pocetak_rada_z2_p1 = trenutno_vreme
    trenutno_vreme = date(2016, 1, 10)
    id_z3_p1 = f.zaposleni_radi_na_poslu(lista_zaposlenih[3], id_posao1, trenutno_vreme)
    pocetak_rada_z3_p1 = trenutno_vreme

    f.zaposleni_dobija_ocenu(id_z2_p1, 7)
    f.zaposleni_dobija_ocenu(id_z3_p1, 9)

    zaduzenja_opreme: [int] = []

    trenutno_vreme = date(2016, 6, 10)
    id_zo = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[2], id_magacin, htz_oprema[0], trenutno_vreme, "...")
    zaduzenja_opreme.append(id_zo)

    trenutno_vreme = date(2016, 6, 10)
    id_zo = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[2], id_magacin, htz_oprema[1], trenutno_vreme, "...")
    zaduzenja_opreme.append(id_zo)

    trenutno_vreme = date(2016, 7, 10)
    id_zo = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[2], id_magacin, htz_oprema[2], trenutno_vreme, "...")
    zaduzenja_opreme.append(id_zo)

    trenutno_vreme = date(2016, 7, 15)
    id_zo = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[3], id_magacin, htz_oprema[1], trenutno_vreme, "...")
    zaduzenja_opreme.append(id_zo)

    trenutno_vreme = date(2016, 7, 15)
    id_zo = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[3], id_magacin, htz_oprema[3], trenutno_vreme, "...")
    zaduzenja_opreme.append(id_zo)

    if(f.dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(lista_zaposlenih[2]) == 3
       and f.dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(lista_zaposlenih[3]) == 2):
        procenata += 10
    else:
        raise "Failed test"

    if(f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[0], id_magacin) == 49
       and f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[1], id_magacin) == 48
       and f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[2], id_magacin) == 49
       and f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[3], id_magacin) == 49):
        procenata += 10
    else:
        raise "Failed test"

    trenutno_vreme = date(2016, 8, 1)
    for id_zo in zaduzenja_opreme:
        f.zaposleni_razduzuje_opremu(id_zo, trenutno_vreme)

    if(f.dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(lista_zaposlenih[2]) == 0
       and f.dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(lista_zaposlenih[3]) == 0):
        procenata += 5
    else:
        raise "Failed test"

    if(f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[0], id_magacin) == 50
       and f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[1], id_magacin) == 50
       and f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[2], id_magacin) == 50
       and f.pogledaj_broj_jedinica_robe_u_magacinu(htz_oprema[3], id_magacin) == 50):
        procenata += 5
    else:
        raise "Failed test"

    trenutno_vreme = date(2016, 11, 10)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z2_p1, trenutno_vreme)
    kraj_rada_z2_p1 = trenutno_vreme
    trenutno_vreme = date(2016, 11, 15)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z3_p1, trenutno_vreme)
    kraj_rada_z3_p1 = trenutno_vreme

    trenutno_vreme = date(2016, 11, 25)
    kraj_posla1 = trenutno_vreme
    f.zavrsi_posao(id_posao1, trenutno_vreme)

    jedinicna_plata_norme_ugradnog_dela = f.dohvati_jedinicnu_platu_radnika_norme_ugradnog_dela(id_nud)

    trajanje_posla1 = Decimal((pocetak_posla1 - kraj_posla1).days)
    trajanje_rada_z2_p1 = Decimal((pocetak_rada_z2_p1 - kraj_rada_z2_p1).days)
    trajanje_rada_z3_p1 = Decimal((pocetak_rada_z3_p1 - kraj_rada_z3_p1).days)
    prosek_z2 = f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[2])
    prosek_z3 = f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[3])

    isplaceno_zaposlenom2 = formula_za_isplatu(prosek_z2,
                                               trajanje_rada_z2_p1,
                                               trajanje_posla1,
                                               jedinicna_plata_norme_ugradnog_dela)
    isplaceno_zaposlenom3 = formula_za_isplatu(prosek_z3,
                                               trajanje_rada_z3_p1,
                                               trajanje_posla1,
                                               jedinicna_plata_norme_ugradnog_dela)

    trenutno_vreme = date(2017, 2, 1)
    pocetak_posla2 = trenutno_vreme
    id_posao2 = f.unesi_posao(id_nud, id_sprat1, trenutno_vreme)
    trenutno_vreme = date(2017, 2, 1)
    id_z2_p2 = f.zaposleni_radi_na_poslu(lista_zaposlenih[2], id_posao2, trenutno_vreme)
    pocetak_rada_z2_p2 = trenutno_vreme
    trenutno_vreme = date(2017, 2, 15)
    id_z3_p2 = f.zaposleni_radi_na_poslu(lista_zaposlenih[3], id_posao2, trenutno_vreme)
    pocetak_rada_z3_p2 = trenutno_vreme

    f.zaposleni_dobija_ocenu(id_z2_p2, 10)
    f.zaposleni_dobija_ocenu(id_z3_p2, 8)

    if f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[2]) == Decimal(8.5):
        procenata += 10
    else:
        raise "Failed test"
    if f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[3]) == Decimal(8.5):
        procenata += 10
    else:
        raise "Failed test"

    f.izmeni_ocenu_za_zaposlenog_na_poslu(id_z2_p2, 8)
    f.izmeni_ocenu_za_zaposlenog_na_poslu(id_z3_p2, 4)

    if f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[2]) == Decimal(7.5):
        procenata += 10
    else:
        raise "Failed test"
    if f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[3]) == Decimal(6.5):
        procenata += 10
    else:
        raise "Failed test"

    trenutno_vreme = date(2017, 11, 20)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z2_p2, trenutno_vreme)
    kraj_rada_z2_p2 = trenutno_vreme
    trenutno_vreme = date(2017, 11, 25)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z3_p2, trenutno_vreme)
    kraj_rada_z3_p2 = trenutno_vreme

    trenutno_vreme = date(2017, 12, 10)
    kraj_posla2 = trenutno_vreme
    f.zavrsi_posao(id_posao2, trenutno_vreme)


    trajanje_posla2 = Decimal((pocetak_posla2 - kraj_posla2).days)
    trajanje_rada_z2_p2 = Decimal((pocetak_rada_z2_p2 - kraj_rada_z2_p2).days)
    trajanje_rada_z3_p2 = Decimal((pocetak_rada_z3_p2 - kraj_rada_z3_p2).days)
    prosek_z2 = f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[2])
    prosek_z3 = f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[3])

    isplaceno_zaposlenom2 = isplaceno_zaposlenom2 + formula_za_isplatu(prosek_z2,
                                                                       trajanje_rada_z2_p2,
                                                                       trajanje_posla2,
                                                                       jedinicna_plata_norme_ugradnog_dela)

    isplaceno_zaposlenom3 = isplaceno_zaposlenom3 + formula_za_isplatu(prosek_z3,
                                                                       trajanje_rada_z3_p2,
                                                                       trajanje_posla2,
                                                                       jedinicna_plata_norme_ugradnog_dela)

    f.isplati_plate_zaposlenima_u_svim_magacinima()

    if(f.dohvati_ukupan_isplacen_iznos_za_zaposlenog(lista_zaposlenih[0]) == Decimal(500.00)
       and f.dohvati_ukupan_isplacen_iznos_za_zaposlenog(lista_zaposlenih[1]) == Decimal(500.00)):
        procenata += 10
    else:
        raise "Failed test"

    if(math.isclose(f.dohvati_ukupan_isplacen_iznos_za_zaposlenog(lista_zaposlenih[2]), isplaceno_zaposlenom2, rel_tol=1)
       and math.isclose(f.dohvati_ukupan_isplacen_iznos_za_zaposlenog(lista_zaposlenih[3]), isplaceno_zaposlenom3, rel_tol=1)):
        procenata += 20
    else:
        raise "Failed test"

    return procenata

if __name__ == "__main__":
    # prepare db
    Base.metadata.create_all(engine)

    procenat = test(SUT())
    print(f"Procenat uspesnosti: {procenat}")

import math
from datetime import date
from decimal import Decimal

from implementation import SUT
from models import Base
from db import engine


def formula_za_isplatu(prosecna_ocena, br_dana, trajanje, jedinicna_plata):
    return prosecna_ocena * br_dana / trajanje * jedinicna_plata


def private_test(f):
    procenata = 0

    id_gradiliste = f.unesi_gradiliste("Gradiliste Novi Sad", date(2010, 1, 1))
    id_objekat_hotel = f.unesi_objekat("Hotel", id_gradiliste)

    id_sprat0 = f.unesi_sprat(0, id_objekat_hotel)
    if(f.unesi_sprat(5, id_objekat_hotel) == -1):
        procenata += 5
    else:
        raise Exception("Failing test")

    if(f.obrisi_sprat(2) == 1):
        procenata += 5
    else:
        raise Exception("Failing test")

    id_sprat1 = f.unesi_sprat(1, id_objekat_hotel)

    id_htz = f.unesi_tip_robe("HTZ")
    id_alat = f.unesi_tip_robe("alat")
    id_materijal = f.unesi_tip_robe("materijal")

    f.unesi_zaposlenog("Milos", "Milosevic", "2503989720031", "M", "370-11032274-01", "milos@google.com", "069/1245301")
    f.unesi_zaposlenog("Jovan", "Jovanovic", "2403989720031", "M", "370-11032274-02", "jovan@google.com", "069/1245302")
    f.unesi_zaposlenog("Marko", "Markovic", "2402989720031", "M", "370-11032274-03", "marko@google.com", "069/1245303")
    f.unesi_zaposlenog("Magdalena", "Despotovic", "2403989720031", "M", "370-11032274-04", "magdalena@google.com", "069/1245303")
    f.unesi_zaposlenog("Katarina", "Vasic", "1204990720031", "Z", "370-11032274-05", "katarina@google.com", "069/1245304")
    f.unesi_zaposlenog("Dejan", "Pavlovic", "2107991720031", "M", "370-11032274-06", "dejan@google.com", "069/1243134")

    lista_zaposlenih = f.dohvati_sve_zaposlene()
    id_magacin = f.unesi_magacin(lista_zaposlenih[0], Decimal(500), id_gradiliste)
    f.zaposleni_radi_u_magacinu(lista_zaposlenih[1], id_magacin)
    
    id_pesak = f.unesi_robu("Pesak", "0001", id_materijal)
    id_cigla = f.unesi_robu("Cigla", "0002", id_materijal)
    id_cement = f.unesi_robu("Cement", "0003", id_materijal)
    id_keramicka_plocica = f.unesi_robu("Keramicka plocica", "0004", id_materijal)
    id_crep = f.unesi_robu("Crep", "0005", id_materijal)
    id_armatura = f.unesi_robu("Armatura", "0006", id_materijal)

    id_busilica = f.unesi_robu("Busilica", "0007", id_alat)
    id_cekic = f.unesi_robu("Cekic", "0008", id_alat)
    id_elektricni_odvijac = f.unesi_robu("Elektricni odvijac", "0009", id_alat)
    id_kruzna_testera = f.unesi_robu("Kruzna testera", "0010", id_alat)

    id_rukavice = f.unesi_robu("Rukavice", "0011", id_alat)
    id_naocare = f.unesi_robu("Naocare", "0012", id_alat)
    id_cipele = f.unesi_robu("Cipele", "0013", id_alat)
    id_stitnik_za_kolena = f.unesi_robu("Stitnik za kolena", "0014", id_alat)
    id_kaciga = f.unesi_robu("Kaciga", "0015", id_alat)

    id_n1 = f.unesi_normu_ugradnog_dela("Norma 1", Decimal(500), Decimal(500))
    f.unesi_potreban_materijal_po_kolicini(id_pesak, id_n1, Decimal(500))
    f.unesi_potreban_materijal_po_broju_jedinica(id_cigla, id_n1, 50)
    f.unesi_potreban_materijal_po_kolicini(id_cement, id_n1, Decimal(50))

    id_n2 = f.unesi_normu_ugradnog_dela("Norma 2", Decimal(500), Decimal(50))
    f.unesi_potreban_materijal_po_kolicini(id_cement, id_n2, Decimal(30))
    f.unesi_potreban_materijal_po_broju_jedinica(id_keramicka_plocica, id_n2, 30)
    f.unesi_potreban_materijal_po_broju_jedinica(id_crep, id_n2, 30)
    f.unesi_potreban_materijal_po_broju_jedinica(id_armatura, id_n2, 30)

    f.unesi_robu_u_magacin_po_kolicini(id_pesak, id_magacin, Decimal(60))
    f.unesi_robu_u_magacin_po_broju_jedinica(id_cigla, id_magacin, 60)
    f.unesi_robu_u_magacin_po_kolicini(id_cement, id_magacin, Decimal(60))
    f.unesi_robu_u_magacin_po_broju_jedinica(id_keramicka_plocica, id_magacin, 30)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_crep, id_magacin, 40)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_armatura, id_magacin, 40)

    f.unesi_robu_u_magacin_po_broju_jedinica(id_busilica, id_magacin, 1)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_cekic, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_elektricni_odvijac, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_kruzna_testera, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_rukavice, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_naocare, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_cipele, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_stitnik_za_kolena, id_magacin, 2)
    f.unesi_robu_u_magacin_po_broju_jedinica(id_kaciga, id_magacin, 2)

    trenutno_vreme = date(2010, 2, 1)
    pocetak_posla1 = trenutno_vreme
    id_p1 = f.unesi_posao(id_n1, id_sprat0, pocetak_posla1)
    if(f.unesi_posao(id_n2, id_sprat1, trenutno_vreme) == -1):
        procenata += 20
    # else:
        # raise Exception("Failing test")
    f.unesi_robu_u_magacin_po_kolicini(id_cement, id_magacin, Decimal(60))
    pocetak_z2_p1 = trenutno_vreme
    id_z2_p1 = f.zaposleni_radi_na_poslu(lista_zaposlenih[2], id_p1, pocetak_z2_p1)
    id_zad_z2_busilica = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[2], id_magacin, id_busilica, pocetak_posla1, "...")
    id_zad_z2_cekic = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[2], id_magacin, id_cekic, pocetak_posla1, "...")

    trenutno_vreme = date(2010, 5, 1)
    pocetak_posla2 = trenutno_vreme
    id_p2 = f.unesi_posao(id_n2, id_sprat1, pocetak_posla2)
    pocetak_z3_p1 = trenutno_vreme
    id_z3_p1 = f.zaposleni_radi_na_poslu(lista_zaposlenih[3], id_p1, pocetak_z3_p1)
    pocetak_z4_p2 = trenutno_vreme
    id_z4_p2 = f.zaposleni_radi_na_poslu(lista_zaposlenih[4], id_p2, pocetak_z4_p2)
    if(f.zaposleni_zaduzuje_opremu(lista_zaposlenih[3], id_magacin, id_busilica, trenutno_vreme, "...") == -1):
        procenata += 10
    else:
        raise Exception("Failing test")
    id_zad_z3_cekic = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[3], id_magacin, id_cekic, trenutno_vreme, "...");
    id_zad_z4_elektricni_odvijac = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[4], id_magacin, id_elektricni_odvijac, trenutno_vreme, "...")

    trenutno_vreme = date(2010, 6, 1)
    kraj_z2_p1 = trenutno_vreme
    f.zaposleni_razduzuje_opremu(id_zad_z2_busilica, trenutno_vreme)
    f.zaposleni_razduzuje_opremu(id_zad_z2_cekic, trenutno_vreme)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z2_p1, kraj_z2_p1)

    trenutno_vreme = date(2010, 6, 20)
    if(f.dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(lista_zaposlenih[3]) == 1 and
       f.dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(lista_zaposlenih[4]) == 1 and
       f.pogledaj_broj_jedinica_robe_u_magacinu(id_cekic, id_magacin) == 1 and
       f.pogledaj_broj_jedinica_robe_u_magacinu(id_elektricni_odvijac, id_magacin) == 1 and
       f.pogledaj_broj_jedinica_robe_u_magacinu(id_busilica, id_magacin) == 1):
        procenata += 20
    else:
        raise Exception("Netacan broj opreme u skladistu/zaduzenjima")

    trenutno_vreme = date(2010, 7, 1)
    kraj_z3_p1 = trenutno_vreme
    f.zaposleni_razduzuje_opremu(id_zad_z3_cekic, trenutno_vreme)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z3_p1, kraj_z3_p1)
    kraj_z4_p2 = trenutno_vreme
    f.zaposleni_razduzuje_opremu(id_zad_z4_elektricni_odvijac, trenutno_vreme)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z4_p2, kraj_z4_p2)

    trenutno_vreme = date(2010, 7, 2)
    pocetak_z4_p1 = trenutno_vreme
    id_z4_p1 = f.zaposleni_radi_na_poslu(lista_zaposlenih[4], id_p1, pocetak_z4_p1)
    id_zad_z4_naocare = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[4], id_magacin, id_naocare, trenutno_vreme, "...")

    trenutno_vreme = date(2010, 8, 1)
    kraj_z4_p1 = trenutno_vreme
    f.zaposleni_razduzuje_opremu(id_zad_z4_naocare, trenutno_vreme)
    if(f.zaposleni_razduzuje_opremu(id_zad_z4_elektricni_odvijac, trenutno_vreme) == 1):
        procenata += 10
    else:
        raise Exception("Ne moze da razduzi opremu")
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z4_p1, kraj_z4_p1)
    f.izmeni_sefa_za_magacin(id_magacin, lista_zaposlenih[4])
    pocetak_z3_p2 = trenutno_vreme
    id_z3_p2 = f.zaposleni_radi_na_poslu(lista_zaposlenih[3], id_p2, pocetak_z3_p2)
    id_zad_z3_kaciga = f.zaposleni_zaduzuje_opremu(lista_zaposlenih[3], id_magacin, id_kaciga, trenutno_vreme, "...")
    kraj_posla1 = trenutno_vreme
    f.zavrsi_posao(id_p1, kraj_posla1)

    trenutno_vreme = date(2010, 10, 1)
    kraj_z3_p2 = trenutno_vreme
    f.zaposleni_razduzuje_opremu(id_zad_z3_kaciga, trenutno_vreme)
    f.zaposleni_je_zavrsio_sa_radom_na_poslu(id_z3_p2, kraj_z3_p2)
    kraj_posla2 = trenutno_vreme
    f.zavrsi_posao(id_p2, kraj_posla2)

    trenutno_vreme = date(2010, 11, 1)
    f.isplati_plate_zaposlenima_u_svim_magacinima()

    jedinicna_plata_n1 = f.dohvati_jedinicnu_platu_radnika_norme_ugradnog_dela(id_n1)
    jedinicna_plata_n2 = f.dohvati_jedinicnu_platu_radnika_norme_ugradnog_dela(id_n2)
    trajanje_posla1 = (kraj_posla1 - pocetak_posla1).days
    trajanje_posla2 = (kraj_posla2 - pocetak_posla2).days

    trajanje_rada_z4_p1 = (kraj_z4_p1 - pocetak_z4_p1).days

    trajanje_rada_z4_p2 = (kraj_z4_p2 - pocetak_z4_p2).days
    prosek_z4 = f.dohvati_prosecnu_ocenu_za_zaposlenog(lista_zaposlenih[4])

    isplaceno_z4_p1 = formula_za_isplatu(prosek_z4, Decimal(trajanje_rada_z4_p1), Decimal(trajanje_posla1), jedinicna_plata_n1)
    isplaceno_z4_p2 = formula_za_isplatu(prosek_z4, Decimal(trajanje_rada_z4_p2), Decimal(trajanje_posla2), jedinicna_plata_n2)

    if(f.dohvati_ukupan_isplacen_iznos_za_zaposlenog(math.isclose(lista_zaposlenih[4], isplaceno_z4_p1 + isplaceno_z4_p2, rel_tol=1))):
        procenata += 30
    else:
        raise Exception("Netacan isplacen iznos")

    return procenata

if __name__ == "__main__":
    # prepare db
    Base.metadata.create_all(engine)

    procenat = private_test(SUT())

    print(f"Procenat uspesnosti: {procenat}")

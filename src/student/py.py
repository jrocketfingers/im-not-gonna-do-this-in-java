class Funkcionalnosti:
    def unesi_gradiliste(naziv, datum_osnivanja):
        raise NotImplemented

    def obrisi_gradiliste(id_gradiliste):
        raise NotImplemented

    def dohvati_sva_gradilista():
        raise NotImplemented

    def unesi_objekat(naziv, id_gradiliste):
        raise NotImplemented

    def obrisi_objekat(id_objekat):
        raise NotImplemented

    def unesi_sprat(br_sprata, id_objekat):
        raise NotImplemented

    def obrisi_sprat(id_sprat):
        raise NotImplemented

    def unesi_zaposlenog(ime, prezime, jmbg, pol, ziro_racun, email, broj_telefona):
        raise NotImplemented

    def obrisi_zaposlenog(id_zaposleni):
        raise NotImplemented

    def dohvati_ukupan_isplacen_iznos_za_zaposlenog(id_zaposleni):
        raise NotImplemented

    def dohvati_prosecnu_ocenu_za_zaposlenog(id_zaposleni):
        raise NotImplemented

    def dohvati_broj_trenutno_zaduzene_opreme_za_zaposlenog(id_zaposleni):
        raise NotImplemented

    def dohvati_sve_zaposlene():
        raise NotImplemented

    def unesi_magacin(id_sef, big_decimal plata, id_gradiliste):
        raise NotImplemented

    def obrisi_magacin(id_magacin):
        raise NotImplemented

    def izmeni_sefa_za_magacin(id_magacin, id_sef_novo):
        raise NotImplemented

    def izmeni_platu_za_magacin(id_magacin, big_decimal plata_novo):
        raise NotImplemented

    def isplati_plate_zaposlenima_u_svim_magacinima():
        raise NotImplemented

    def isplati_plate_zaposlenima_u_magacinu(id_magacin):
        raise NotImplemented

    def unesi_robu_u_magacin_po_kolicini(id_roba, id_magacin, big_decimal kolicina):
        raise NotImplemented

    def unesi_robu_u_magacin_po_broju_jedinica(id_roba, id_magacin, broj_jedinica):
        raise NotImplemented

    def uzmi_robu_iz_magacina_po_kolicini(id_roba, id_magacin, big_decimal kolicina):
        raise NotImplemented

    def uzmi_robu_iz_magacina_po_broju_jedinica(id_roba, id_magacin, broj_jedinca):
        raise NotImplemented

    def pogledaj_kolicinu_robe_u_magacinu(id_roba, id_magacin):
        raise NotImplemented

    def pogledaj_broj_jedinica_robe_u_magacinu(id_roba, id_magacin):
        raise NotImplemented

    def unesi_tip_robe(naziv):
        raise NotImplemented

    def obrisi_tip_robe(id_tip_robe):
        raise NotImplemented

    def unesi_robu(naziv, kod, id_tip_robe):
        raise NotImplemented

    def obrisi_robu(id_roba):
        raise NotImplemented

    def dohvati_svu_robu():
        raise NotImplemented

    def zaposleni_radi_u_magacinu(id_zaposleni, id_magacin):
        raise NotImplemented

    def zaposleni_ne_radi_u_magacinu(id_zaposleni):
        raise NotImplemented

    def zaposleni_zaduzuje_opremu(id_zaposlenog_koji_zaduzuje, id_magacin, id_roba, datum_zaduzenja, napomena):
        raise NotImplemented

    def zaposleni_razduzuje_opremu(id_zaduzenja_opreme, datum_razduzenja):
        raise NotImplemented

    def unesi_normu_ugradnog_dela(naziv, big_decimal cena_izrade, big_decimal jedinicna_plata_radnika):
        raise NotImplemented

    def obrisi_normu_ugradnog_dela(id_norma_ugradnog_dela):
        raise NotImplemented

    def dohvati_jedinicnu_platu_radnika_norme_ugradnog_dela(id_n_r):
        raise NotImplemented

    def unesi_potreban_materijal_po_broju_jedinica(id_roba_koja_je_potrosni_materijal, id_norma_ugradnog_dela, broj_jedinica):
        raise NotImplemented

    def unesi_potreban_materijal_po_kolicini(id_roba_koja_je_potrosni_materijal, id_norma_ugradnog_dela, big_decimal kolicina):
        raise NotImplemented

    def obrisi_potreban_materijal(id_roba_koja_je_potrosni_materijal, id_norma_ugradnog_dela):
        raise NotImplemented

    def unesi_posao(id_norma_ugradnog_dela, id_sprat, datum_pocetka):
        raise NotImplemented

    def obrisi_posao(id_posao):
        raise NotImplemented

    def izmeni_datum_pocetka_za_posao(id_posao, datum_pocetka):
        raise NotImplemented

    def zavrsi_posao(id_posao, datum_kraja):
        raise NotImplemented

    def zaposleni_radi_na_poslu(id_zaposleni, id_posao, datum_pocetka):
        raise NotImplemented

    def zaposleni_je_zavrsio_sa_radom_na_poslu(id_zaposleni_na_poslu, datum_kraja):
        raise NotImplemented

    def izmeni_datum_pocetka_rada_zaposlenog_na_poslu(id_zaposleni_na_poslu, datum_pocetka_novo):
        raise NotImplemented

    def izmeni_datum_kraja_rada_zaposlenog_na_poslu(id_zaposleni_na_poslu, datum_kraja_novo):
        raise NotImplemented

    def zaposleni_dobija_ocenu(id_zaposleni_na_poslu, ocena):
        raise NotImplemented

    def obrisi_ocenu_zaposlenom(id_zaposleni_na_poslu):
        raise NotImplemented

    def izmeni_ocenu_za_zaposlenog_na_poslu(id_zaposleni_na_poslu, ocena_novo):
        raise NotImplemented


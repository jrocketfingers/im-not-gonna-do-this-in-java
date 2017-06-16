/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package funkcionalnosti;

import java.math.BigDecimal;
import java.sql.Date;
import java.util.List;

/**
 *
 * @author stefan
 */
public abstract class Funkcionalnosti {
    
    /**
     * 
     * @param naziv
     * @param datumOsnivanja
     * @return idGradiliste ili -1 u slucaju greske
     */
    public abstract int unesiGradiliste(String naziv, Date datumOsnivanja); 
    /**
     * 
     * @param idGradiliste
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiGradiliste(int idGradiliste); 
    /**
     * 
     * @return lista primarnih kljuceva svih gradilista ili null u slucaju greske ili ukoliko je lista prazna
     */
    public abstract List<Integer> dohvatiSvaGradilista();
    
    /**
     * 
     * @param naziv
     * @param idGradiliste
     * @return idObjekat ili -1 u slucaju greske
     */
    public abstract int unesiObjekat(String naziv, int idGradiliste); 
    /**
     * 
     * @param idObjekat
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiObjekat(int idObjekat); 

    /**
     * 
     * @param brSprata
     * @param idObjekat
     * @return idSprat ili -1 u slucaju greske
     */
    public abstract int unesiSprat(int brSprata, int idObjekat); 
    /**
     * 
     * @param idSprat
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiSprat(int idSprat); 

    /**
     * 
     * @param ime
     * @param prezime
     * @param jmbg
     * @param datumRodjenja
     * @param pol
     * @param datumZaposljenja
     * @param ziroRacun
     * @param email
     * @param brojTelefona
     * @param adresaPrebivalista
     * @param adresaBoravista
     * @return idZaposleni ili -1 u slucaju greske
     */
    public abstract int unesiZaposlenog(String ime, String prezime, String jmbg, String pol, String ziroRacun, String email, String brojTelefona); 
    /**
     * 
     * @param idZaposleni
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiZaposlenog(int idZaposleni); 
    /**
     * 
     * @param idZaposleni
     * @return ukupanIsplacenIznos ili -1 ukoliko zaposleni ne postoji
     */
    public abstract BigDecimal dohvatiUkupanIsplacenIznosZaZaposlenog(int idZaposleni);
    /**
     * 
     * @param idZaposleni
     * @return prosecnaOcena ili -1 ukoliko zaposleni ne postoji
     */
    public abstract BigDecimal dohvatiProsecnuOcenuZaZaposlenog(int idZaposleni);
    /**
     * 
     * @param idZaposleni
     * @return brojTrenutnoZaduzeneOpreme  ili -1 ukoliko zaposleni ne postoji
     */
    public abstract int dohvatiBrojTrenutnoZaduzeneOpremeZaZaposlenog(int idZaposleni);
    /**
     * 
     * @return lista primarnih kljuceva svih zaposlenih ili null u slucaju greske ili ukoliko nema zaposlenih
     */
    public abstract List<Integer> dohvatiSveZaposlene();
    
    /**
     * 
     * @param idSef
     * @param plata
     * @param idGradiliste
     * @return idMagacin -1 u slucaju greske
     */
    public abstract int unesiMagacin(int idSef, BigDecimal plata, int idGradiliste); 
    /**
     * Magacin se moze obrisati samo kada u njemu nema materijala, kada nema zaposlenih u njemu i kada nema sefa.
     * @param idMagacin
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiMagacin(int idMagacin); 
    /**
     * 
     * @param idMagacin
     * @param idSefNovo
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int izmeniSefaZaMagacin(int idMagacin, int idSefNovo);
    /**
     * 
     * @param idMagacin
     * @param plataNovo
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int izmeniPlatuZaMagacin(int idMagacin, BigDecimal plataNovo);
    /**
     * Isplacuje mesecnu platu svakom zaposlenom koji radi u nekom od magacina.
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int isplatiPlateZaposlenimaUSvimMagacinima();
    /**
     * Isplacuje mesecnu platu svakom zaposlenom koji radi u magacinu ciji je id prosledjen kao argument metode.
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int isplatiPlateZaposlenimaUMagacinu(int idMagacin);
    
    /**
     * 
     * @param idRoba
     * @param idMagacin
     * @param kolicina
     * @return idRobaUMagacinu ili -1 u slucaju greske
     */
    public abstract int unesiRobuUMagacinPoKolicini(int idRoba, int idMagacin, BigDecimal kolicina); 
    /**
     * 
     * @param idRoba
     * @param idMagacin
     * @param brojJedinica
     * @return idRobaUMagacinu ili -1 u slucaju greske
     */
    public abstract int unesiRobuUMagacinPoBrojuJedinica(int idRoba, int idMagacin, int brojJedinica); 
    /**
     * Ukoliko se trazi veca kolicina u odnosu na onu koja postoji u magacinu uzece se kolicina koja postoji u magacinu za tu robu.
     * Kada količina robe u magacinu postane 0 ona se u tom trenutku briše iz magacina
     * @param idZonaMagacina
     * @return kolicinaRobeUzetaIzMagacina ili -1 u slucaju greske
     */
    public abstract BigDecimal uzmiRobuIzMagacinaPoKolicini(int idRoba, int idMagacin, BigDecimal kolicina); 
    /**
     * Ukoliko se trazi veci broj jedinica u odnosu na onaj broj koji postoji u magacinu uzece se onoliko jedinica koliko postoji u magacinu za tu robu.
     * Kada broj jedinica robe u magacinu postane 0 ona se u tom trenutku briše iz magacina.
     * @param idZonaMagacina
     * @return kolicinaRobeUzetaIzMagacina ili -1 u slucaju greske
     */
    public abstract int uzmiRobuIzMagacinaPoBrojuJedinica(int idRoba, int idMagacin, int brojJedinca);
    /**
     * 
     * @param idRoba
     * @param idMagacin
     * @return kolicinaRobeUMagacinu, -1 ukoliko je roba definisana u broju jedinica ili je u pitanju druga greska
     */
    public abstract BigDecimal pogledajKolicinuRobeUMagacinu(int idRoba, int idMagacin);
    /**
     * 
     * @param idRoba
     * @param idMagacin
     * @return brojJedinicaRobeUMagacinu, -1 ukoliko je roba definisana kolicinom ili je u pitanju druga greska
     */
    public abstract int pogledajBrojJedinicaRobeUMagacinu(int idRoba, int idMagacin);
    
    /**
     * 
     * @param naziv
     * @return idTipRobe ili -1 u slucaju greske
     */
    public abstract int unesiTipRobe(String naziv); 
    /**
     * 
     * @param idTipRobe
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiTipRobe(int idTipRobe); 
    
    /**
     * 
     * @param naziv
     * @param kod
     * @param jedinicnaMasa
     * @param jedinicnaDuzina
     * @param jedinicnaSirina
     * @param jedinicnaVisina
     * @param brojJedinicaPoPakovanju
     * @param idTipRobe
     * @param idZonaMagacina
     * @return idRoba ili -1 u slucaju greske
     */
    public abstract int unesiRobu(String naziv, String kod, int idTipRobe); 
    /**
     * 
     * @param idRoba
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiRobu(int idRoba); 
    public abstract List<Integer> dohvatiSvuRobu();
    
    /**
     * 
     * @param idZaposleni
     * @param idMagacin
     * @return argument idZaposleni ili -1 u slucaju greske
     */
    public abstract int zaposleniRadiUMagacinu(int idZaposleni, int idMagacin); 
    /**
     * Brise informaciju o tome da zaposleni radi i da je ikada radio u magacinu.
     * @param idZaposleni
     * @return 0-zaposleni je radio u nekom magacinu i operacija je uspesna 1-zaposleni pre poziva metode ne radi u magacinu ili je operacija neuspesna
     */
    public abstract int zaposleniNeRadiUMagacinu(int idZaposleni);
    
    /**
     * Kada broj jedinica robe u magacinu postane 0 ona se u tom trenutku briše iz magacina.
     * @param idZaposlenogKojiZaduzuje
     * @param idZaposlenogUMagacinuOdKogaSeZaduzuje
     * @param idRobaKojaSeZaduzuje
     * @param napomena
     * @return idZaduzenjaOpreme ili -1 u slucaju greske
     */
    public abstract int zaposleniZaduzujeOpremu(int idZaposlenogKojiZaduzuje, int idMagacin, int idRoba, Date datumZaduzenja, String napomena);
    /**
     * Ne brise zaduzenje vec samo postavlja datum razduzenja.
     * @param idZaduzenjaOpreme
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int zaposleniRazduzujeOpremu(int idZaduzenjaOpreme, Date datumRazduzenja); 

    /**
     * 
     * @param id
     * @param naziv
     * @param cenaIzrade
     * @param jedinicnaPlataRadnika
     * @return idNormaUgradnogDela ili -1 u slucaju greske
     */
    public abstract int unesiNormuUgradnogDela(String naziv, BigDecimal cenaIzrade, BigDecimal jedinicnaPlataRadnika);
    /**
     * 
     * @param idNormaUgradnogDela
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiNormuUgradnogDela(int idNormaUgradnogDela);
    /**
     * 
     * @param idNR
     * @return jenicnaPlataRadnikaNormeRada ili -1 u slucaju greske
     */
    public abstract BigDecimal dohvatiJedinicnuPlatuRadnikaNormeUgradnogDela(int idNR);

    /**
     * 
     * @param idRobaKojaJePotrosniMaterijal
     * @param idNormaUgradnogDela
     * @param brojPakovanja
     * @return idPotrebanMaterijal ili -1 u slucaju greske
     */
    public abstract int unesiPotrebanMaterijalPoBrojuJedinica(int idRobaKojaJePotrosniMaterijal, int idNormaUgradnogDela, int brojJedinica);
    /**
     * 
     * @param idRobaKojaJePotrosniMaterijal
     * @param idNormaUgradnogDela
     * @param kolicina
     * @return idPotrebanMaterijal ili -1 u slucaju greske
     */
    public abstract int unesiPotrebanMaterijalPoKolicini(int idRobaKojaJePotrosniMaterijal, int idNormaUgradnogDela, BigDecimal kolicina);
    /**
     * 
     * @param idRobaKojaJePotrosniMaterijal
     * @param idNormaUgradnogDela
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiPotrebanMaterijal(int idRobaKojaJePotrosniMaterijal, int idNormaUgradnogDela);
    
    /**
     * Datum kraja ce biti postavljen kada posao bude zavrsen.
     * @param idNormaUgradnogDela
     * @param idSprat
     * @param datumKraja
     * @return idPosao ili -1 u slucaju greske
     */
    public abstract int unesiPosao(int idNormaUgradnogDela, int idSprat, Date datumPocetka); 
    /**
     * Prilikom brisanja posla sav materijal koji je bio potreban na poslu vraca se u magacin tog gradilista. Moze se obrisati posao koji nije zavrsen.
     * @param idPosao
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiPosao(int idPosao);
    /**
     * 
     * @param idPosao
     * @param datumPocetka
     * @param datumKraja
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int izmeniDatumPocetkaZaPosao(int idPosao, Date datumPocetka);
    /**
     * Postavlja status posla na zavrsen i postavlja datum kraja posla. Ova metoda ce definisati kraj rada na ovom poslu za sve radnike za koje to eksplicitno nije uradjeno za ovaj posao.
     * Ova metoda poziva metodu {@link #zaposleniJeZavrsioSaRadomNaPoslu(int, java.sql.Date) } za sve zaposlene
     * koji prethodno nisu zavrsili rad na tom poslu.
     * @param idPosao
     * @param status
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int zavrsiPosao(int idPosao, Date datumKraja);
    
    /**
     * 
     * @param idZaposleni
     * @param idPosao
     * @return idZaposleniNaPoslu ili -1 u slucaju greske
     */
    public abstract int zaposleniRadiNaPoslu(int idZaposleni, int idPosao, Date datumPocetka);
    /**
     * Ne brise informaciju o tome na kojem poslu je radio zaposleni, vec samo postavlja datum kraja.
     * @param idZaposleniNaPoslu
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int zaposleniJeZavrsioSaRadomNaPoslu(int idZaposleniNaPoslu, Date datumKraja); 
    /**
     * 
     * @param idZaposleniNaPoslu
     * @param datumPocetka
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int izmeniDatumPocetkaRadaZaposlenogNaPoslu(int idZaposleniNaPoslu, Date datumPocetkaNovo);
    /**
     * 
     * @param idZaposleniNaPoslu
     * @param datumKrajaNovo
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int izmeniDatumKrajaRadaZaposlenogNaPoslu(int idZaposleniNaPoslu, Date datumKrajaNovo);
    
    /**
     * 
     * @param idZaposleniNaPoslu
     * @param ocena
     * @return idZaposleniNaPoslu ili -1 u slucaju greske
     */
    public abstract int zaposleniDobijaOcenu(int idZaposleniNaPoslu, int ocena); 
    /**
     * 
     * @param idNormaUgradnogDela
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int obrisiOcenuZaposlenom(int idZaposleniNaPoslu);
    /**
     * Menja samo ocenu.
     * @param idZaposleniNaPoslu
     * @param ocena
     * @return 0-operacija uspesna 1-operacija neuspesna
     */
    public abstract int izmeniOcenuZaZaposlenogNaPoslu(int idZaposleniNaPoslu, int ocenaNovo);
    
}

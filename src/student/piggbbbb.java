/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package student;

import funkcionalnosti.Funkcionalnosti;
import java.math.BigDecimal;
import java.sql.Date;
import java.util.List;

/**
 *
 * @author stefan
 */
public class piggbbbb extends Funkcionalnosti{

    @Override
    public int unesiGradiliste(String naziv, Date datumOsnivanja) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiGradiliste(int idGradiliste) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public List<Integer> dohvatiSvaGradilista() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiObjekat(String naziv, int idGradiliste) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiObjekat(int idObjekat) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiSprat(int brSprata, int idObjekat) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiSprat(int idSprat) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiZaposlenog(String ime, String prezime, String jmbg, String pol, String ziroRacun, String email, String brojTelefona) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiZaposlenog(int idZaposleni) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public BigDecimal dohvatiUkupanIsplacenIznosZaZaposlenog(int idZaposleni) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public BigDecimal dohvatiProsecnuOcenuZaZaposlenog(int idZaposleni) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int dohvatiBrojTrenutnoZaduzeneOpremeZaZaposlenog(int idZaposleni) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public List<Integer> dohvatiSveZaposlene() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiMagacin(int idSef, BigDecimal plata, int idGradiliste) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiMagacin(int idMagacin) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int izmeniSefaZaMagacin(int idMagacin, int idSefNovo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int izmeniPlatuZaMagacin(int idMagacin, BigDecimal plataNovo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int isplatiPlateZaposlenimaUSvimMagacinima() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int isplatiPlateZaposlenimaUMagacinu(int idMagacin) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiRobuUMagacinPoKolicini(int idRoba, int idMagacin, BigDecimal kolicina) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiRobuUMagacinPoBrojuJedinica(int idRoba, int idMagacin, int brojJedinica) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public BigDecimal uzmiRobuIzMagacinaPoKolicini(int idRoba, int idMagacin, BigDecimal kolicina) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int uzmiRobuIzMagacinaPoBrojuJedinica(int idRoba, int idMagacin, int brojJedinca) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public BigDecimal pogledajKolicinuRobeUMagacinu(int idRoba, int idMagacin) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int pogledajBrojJedinicaRobeUMagacinu(int idRoba, int idMagacin) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiTipRobe(String naziv) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiTipRobe(int idTipRobe) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiRobu(String naziv, String kod, int idTipRobe) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiRobu(int idRoba) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public List<Integer> dohvatiSvuRobu() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniRadiUMagacinu(int idZaposleni, int idMagacin) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniNeRadiUMagacinu(int idZaposleni) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniZaduzujeOpremu(int idZaposlenogKojiZaduzuje, int idMagacin, int idRoba, Date datumZaduzenja, String napomena) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniRazduzujeOpremu(int idZaduzenjaOpreme, Date datumRazduzenja) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiNormuUgradnogDela(String naziv, BigDecimal cenaIzrade, BigDecimal jedinicnaPlataRadnika) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiNormuUgradnogDela(int idNormaUgradnogDela) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public BigDecimal dohvatiJedinicnuPlatuRadnikaNormeUgradnogDela(int idNR) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiPotrebanMaterijalPoBrojuJedinica(int idRobaKojaJePotrosniMaterijal, int idNormaUgradnogDela, int brojJedinica) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiPotrebanMaterijalPoKolicini(int idRobaKojaJePotrosniMaterijal, int idNormaUgradnogDela, BigDecimal kolicina) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiPotrebanMaterijal(int idRobaKojaJePotrosniMaterijal, int idNormaUgradnogDela) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int unesiPosao(int idNormaUgradnogDela, int idSprat, Date datumPocetka) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiPosao(int idPosao) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int izmeniDatumPocetkaZaPosao(int idPosao, Date datumPocetka) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zavrsiPosao(int idPosao, Date datumKraja) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniRadiNaPoslu(int idZaposleni, int idPosao, Date datumPocetka) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniJeZavrsioSaRadomNaPoslu(int idZaposleniNaPoslu, Date datumKraja) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int izmeniDatumPocetkaRadaZaposlenogNaPoslu(int idZaposleniNaPoslu, Date datumPocetkaNovo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int izmeniDatumKrajaRadaZaposlenogNaPoslu(int idZaposleniNaPoslu, Date datumKrajaNovo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int zaposleniDobijaOcenu(int idZaposleniNaPoslu, int ocena) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int obrisiOcenuZaposlenom(int idZaposleniNaPoslu) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public int izmeniOcenuZaZaposlenogNaPoslu(int idZaposleniNaPoslu, int ocenaNovo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}

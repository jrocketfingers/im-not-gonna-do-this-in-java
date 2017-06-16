/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testovi;

import funkcionalnosti.Funkcionalnosti;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.sql.Date;
import java.util.ArrayList;
import java.util.List;
import util.Util;

/**
 *
 * @author stefan
 */
public class JavniTest {
    
    public static double test(Funkcionalnosti f){
        
        double procenata = 0;
        
        Date trenutnoVreme;
        
        int idGradiliste = f.unesiGradiliste("Gradiliste 1", Date.valueOf("2015-08-25"));
        int idObjekat = f.unesiObjekat("Stambena zgrada 1", idGradiliste);
        int idSprat0 = f.unesiSprat(0, idObjekat);
        int idSprat1 = f.unesiSprat(1, idObjekat);
        f.unesiSprat(2, idObjekat);
        f.unesiSprat(3, idObjekat);
        int idHTZ = f.unesiTipRobe("HTZ");
        int idAlat = f.unesiTipRobe("alat");
        int idMaterijal = f.unesiTipRobe("materijal");
        
        f.unesiZaposlenog("Milos", "Milosevic", "2503989720031", "M", "370-11032274-01", "milos@google.com", "069/1245301");
        f.unesiZaposlenog("Jovan", "Jovanovic", "2403989720031", "M", "370-11032274-02", "jovan@google.com", "069/1245302");
        f.unesiZaposlenog("Marko", "Markovic", "2402989720031", "M", "370-11032274-03", "marko@google.com", "069/1245303");
        f.unesiZaposlenog("Magdalena", "Despotovic", "2403987720031", "Z", "370-11032274-03", "magdalena@google.com", "069/1245303");
        f.unesiZaposlenog("Katarina", "Vasic", "1204990720031", "Z", "370-11032274-04", "katarina@google.com", "069/1245304");
        
        List<Integer> listaZaposlenih = f.dohvatiSveZaposlene();
        int idMagacin = f.unesiMagacin(listaZaposlenih.get(0), new BigDecimal(500.00), idGradiliste);
        f.zaposleniRadiUMagacinu(listaZaposlenih.get(1), idMagacin);
        
        int idNUD = f.unesiNormuUgradnogDela("Ugradni deo 1", new BigDecimal(800), new BigDecimal(50));
        
        //List<Integer> materijali = new ArrayList<>();
        
        int idRoba = f.unesiRobu("Pesak", "0001", idMaterijal);
        f.unesiRobuUMagacinPoKolicini(idRoba, idMagacin, new BigDecimal(3000));
        f.unesiPotrebanMaterijalPoKolicini(idRoba, idNUD, new BigDecimal(500));
        
        idRoba = f.unesiRobu("Cigla", "0002", idMaterijal);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 3000);
        f.unesiPotrebanMaterijalPoBrojuJedinica(idRoba, idNUD, 500);
        
        idRoba = f.unesiRobu("Cement", "0003", idMaterijal);
        f.unesiRobuUMagacinPoKolicini(idRoba, idMagacin, new BigDecimal(3000));
        f.unesiPotrebanMaterijalPoKolicini(idRoba, idNUD, new BigDecimal(500));
        
        idRoba = f.unesiRobu("Keramicka plocica", "0004", idMaterijal);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 3000);
        f.unesiPotrebanMaterijalPoBrojuJedinica(idRoba, idNUD, 500);
        
        idRoba = f.unesiRobu("Crep", "0005", idMaterijal);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 3000);
        f.unesiPotrebanMaterijalPoBrojuJedinica(idRoba, idNUD, 500);
        
        idRoba = f.unesiRobu("Armatura", "0006", idMaterijal);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 3000);
        f.unesiPotrebanMaterijalPoBrojuJedinica(idRoba, idNUD, 500);
        
        List<Integer> alat = new ArrayList<>();
        
        idRoba = f.unesiRobu("Busilica", "0007", idAlat);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 30);
        alat.add(idRoba);
        
        idRoba = f.unesiRobu("Cekic", "0008", idAlat);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 30);
        alat.add(idRoba);
        
        idRoba = f.unesiRobu("Elektricni odvijac", "0009", idAlat);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 30);
        alat.add(idRoba);
        
        idRoba = f.unesiRobu("Kruzna testera", "0010", idAlat);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 30);
        alat.add(idRoba);
        
        List<Integer> htzOprema = new ArrayList<>();
        
        idRoba = f.unesiRobu("Rukavice", "0011", idHTZ);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 50);
        htzOprema.add(idRoba);
        
        idRoba = f.unesiRobu("Naocare", "0012", idHTZ);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 50);
        htzOprema.add(idRoba);
        
        idRoba = f.unesiRobu("Cipele", "0013", idHTZ);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 50);
        htzOprema.add(idRoba);
        
        idRoba = f.unesiRobu("Stitnik za kolena", "0014", idHTZ);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 50);
        htzOprema.add(idRoba);
        
        idRoba = f.unesiRobu("Kaciga", "0015", idHTZ);
        f.unesiRobuUMagacinPoBrojuJedinica(idRoba, idMagacin, 50);
        htzOprema.add(idRoba);
        
        trenutnoVreme = Date.valueOf("2016-01-01");
        Date pocetakPosla1 = trenutnoVreme;
        int idPosao1 = f.unesiPosao(idNUD, idSprat0, trenutnoVreme);
        int idZ2P1 = f.zaposleniRadiNaPoslu(listaZaposlenih.get(2), idPosao1, trenutnoVreme);
        Date pocetakRadaZ2P1 = trenutnoVreme;
        trenutnoVreme = Date.valueOf("2016-01-10");
        int idZ3P1 = f.zaposleniRadiNaPoslu(listaZaposlenih.get(3), idPosao1, trenutnoVreme);
        Date pocetakRadaZ3P1 = trenutnoVreme;
        
        f.zaposleniDobijaOcenu(idZ2P1, 7);
        f.zaposleniDobijaOcenu(idZ3P1, 9);
        
        List<Integer> zaduzenjaOpreme = new ArrayList<>();
        
        trenutnoVreme = Date.valueOf("2016-06-10");
        int idZO = f.zaposleniZaduzujeOpremu(listaZaposlenih.get(2), idMagacin, htzOprema.get(0), trenutnoVreme, "...");
        zaduzenjaOpreme.add(idZO);
        
        trenutnoVreme = Date.valueOf("2016-06-10");
        idZO = f.zaposleniZaduzujeOpremu(listaZaposlenih.get(2), idMagacin, htzOprema.get(1), trenutnoVreme, "...");
        zaduzenjaOpreme.add(idZO);
        
        trenutnoVreme = Date.valueOf("2016-07-10");
        idZO = f.zaposleniZaduzujeOpremu(listaZaposlenih.get(2), idMagacin, htzOprema.get(2), trenutnoVreme, "...");
        zaduzenjaOpreme.add(idZO);
        
        trenutnoVreme = Date.valueOf("2016-07-15");
        idZO = f.zaposleniZaduzujeOpremu(listaZaposlenih.get(3), idMagacin, htzOprema.get(1), trenutnoVreme, "...");
        zaduzenjaOpreme.add(idZO);
        
        trenutnoVreme = Date.valueOf("2016-07-15");
        idZO = f.zaposleniZaduzujeOpremu(listaZaposlenih.get(3), idMagacin, htzOprema.get(3), trenutnoVreme, "...");
        zaduzenjaOpreme.add(idZO);
        
        if(f.dohvatiBrojTrenutnoZaduzeneOpremeZaZaposlenog(listaZaposlenih.get(2)) == 3
                && f.dohvatiBrojTrenutnoZaduzeneOpremeZaZaposlenog(listaZaposlenih.get(3)) == 2)
            procenata += 10;
        
        if(f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(0), idMagacin) == 49
            && f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(1), idMagacin) == 48
            && f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(2), idMagacin) == 49
            && f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(3), idMagacin) == 49)
            procenata += 10;
        
        trenutnoVreme = Date.valueOf("2016-08-01");
        for (Integer idZo : zaduzenjaOpreme) {
            f.zaposleniRazduzujeOpremu(idZo, trenutnoVreme);
        }
        
        if(f.dohvatiBrojTrenutnoZaduzeneOpremeZaZaposlenog(listaZaposlenih.get(2)) == 0
                && f.dohvatiBrojTrenutnoZaduzeneOpremeZaZaposlenog(listaZaposlenih.get(3)) == 0)
            procenata += 5;
        
        if(f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(0), idMagacin) == 50
            && f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(1), idMagacin) == 50
            && f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(2), idMagacin) == 50
            && f.pogledajBrojJedinicaRobeUMagacinu(htzOprema.get(3), idMagacin) == 50)
            procenata += 5;
        
        trenutnoVreme = Date.valueOf("2016-11-10");
        f.zaposleniJeZavrsioSaRadomNaPoslu(idZ2P1, trenutnoVreme);
        Date krajRadaZ2P1 = trenutnoVreme;
        trenutnoVreme = Date.valueOf("2016-11-15");
        f.zaposleniJeZavrsioSaRadomNaPoslu(idZ3P1, trenutnoVreme);
        Date krajRadaZ3P1 = trenutnoVreme;
        
        trenutnoVreme = Date.valueOf("2016-11-25");
        Date krajPosla1 = trenutnoVreme;
        f.zavrsiPosao(idPosao1, trenutnoVreme);
        
        BigDecimal jedinicnaPlataNormeUgradnogDela = f.dohvatiJedinicnuPlatuRadnikaNormeUgradnogDela(idNUD);
        
        BigDecimal trajanjePosla1 = new BigDecimal(Util.periodUDanima(pocetakPosla1, krajPosla1));
        BigDecimal trajanjeRadaZ2P1 = new BigDecimal(Util.periodUDanima(pocetakRadaZ2P1, krajRadaZ2P1));
        BigDecimal trajanjeRadaZ3P1 = new BigDecimal(Util.periodUDanima(pocetakRadaZ3P1, krajRadaZ3P1));
        BigDecimal prosekZ2 = f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(2));
        BigDecimal prosekZ3 = f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(3));
        
        BigDecimal isplacenoZaposlenom2 = prosekZ2.multiply(trajanjeRadaZ2P1.divide(trajanjePosla1,50,RoundingMode.HALF_UP)).multiply(jedinicnaPlataNormeUgradnogDela).setScale(3,RoundingMode.HALF_UP);
        BigDecimal isplacenoZaposlenom3 = prosekZ3.multiply(trajanjeRadaZ3P1.divide(trajanjePosla1,50,RoundingMode.HALF_UP)).multiply(jedinicnaPlataNormeUgradnogDela).setScale(3,RoundingMode.HALF_UP);
        
        trenutnoVreme = Date.valueOf("2017-02-01");
        Date pocetakPosla2 = trenutnoVreme;
        int idPosao2 = f.unesiPosao(idNUD, idSprat1, trenutnoVreme);
        trenutnoVreme = Date.valueOf("2017-02-01");
        int idZ2P2 = f.zaposleniRadiNaPoslu(listaZaposlenih.get(2), idPosao2, trenutnoVreme);
        Date pocetakRadaZ2P2 = trenutnoVreme;
        trenutnoVreme = Date.valueOf("2017-02-15");
        int idZ3P2 = f.zaposleniRadiNaPoslu(listaZaposlenih.get(3), idPosao2, trenutnoVreme);
        Date pocetakRadaZ3P2 = trenutnoVreme;
        
        f.zaposleniDobijaOcenu(idZ2P2, 10);
        f.zaposleniDobijaOcenu(idZ3P2, 8);
        
        if(f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(2)).compareTo(new BigDecimal(8.5)) == 0)
            procenata += 10;
        if(f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(3)).compareTo(new BigDecimal(8.5)) == 0)
            procenata += 10;
        
        f.izmeniOcenuZaZaposlenogNaPoslu(idZ2P2, 8);
        f.izmeniOcenuZaZaposlenogNaPoslu(idZ3P2, 4);
        
        if(f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(2)).compareTo(new BigDecimal(7.5)) == 0)
            procenata += 10;
        if(f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(3)).compareTo(new BigDecimal(6.5)) == 0)
            procenata += 10;
        
        trenutnoVreme = Date.valueOf("2017-11-20");
        f.zaposleniJeZavrsioSaRadomNaPoslu(idZ2P2, trenutnoVreme);
        Date krajRadaZ2P2 = trenutnoVreme;
        trenutnoVreme = Date.valueOf("2017-11-25");
        f.zaposleniJeZavrsioSaRadomNaPoslu(idZ3P2, trenutnoVreme);
        Date krajRadaZ3P2 = trenutnoVreme;
        
        trenutnoVreme = Date.valueOf("2017-12-10");
        Date krajPosla2 = trenutnoVreme;
        f.zavrsiPosao(idPosao2, trenutnoVreme);
        
        
        BigDecimal trajanjePosla2 = new BigDecimal(Util.periodUDanima(pocetakPosla2, krajPosla2));
        BigDecimal trajanjeRadaZ2P2 = new BigDecimal(Util.periodUDanima(pocetakRadaZ2P2, krajRadaZ2P2));
        BigDecimal trajanjeRadaZ3P2 = new BigDecimal(Util.periodUDanima(pocetakRadaZ3P2, krajRadaZ3P2));
        prosekZ2 = f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(2));
        prosekZ3 = f.dohvatiProsecnuOcenuZaZaposlenog(listaZaposlenih.get(3));
        
        isplacenoZaposlenom2 = isplacenoZaposlenom2.add(prosekZ2.multiply(trajanjeRadaZ2P2.divide(trajanjePosla2,50,RoundingMode.HALF_UP)).multiply(jedinicnaPlataNormeUgradnogDela)).setScale(3,RoundingMode.HALF_UP);
        isplacenoZaposlenom3 = isplacenoZaposlenom3.add(prosekZ3.multiply(trajanjeRadaZ3P2.divide(trajanjePosla2,50,RoundingMode.HALF_UP)).multiply(jedinicnaPlataNormeUgradnogDela)).setScale(3,RoundingMode.HALF_UP);
        
        f.isplatiPlateZaposlenimaUSvimMagacinima();
        
        if(f.dohvatiUkupanIsplacenIznosZaZaposlenog(listaZaposlenih.get(0)).compareTo(new BigDecimal(500.00)) == 0
        && f.dohvatiUkupanIsplacenIznosZaZaposlenog(listaZaposlenih.get(1)).compareTo(new BigDecimal(500.00)) == 0)
            procenata += 10;
        
        if(f.dohvatiUkupanIsplacenIznosZaZaposlenog(listaZaposlenih.get(2)).compareTo(isplacenoZaposlenom2) == 0
        && f.dohvatiUkupanIsplacenIznosZaZaposlenog(listaZaposlenih.get(3)).compareTo(isplacenoZaposlenom3) == 0)
            procenata += 20;
        
        return procenata;
    }
}

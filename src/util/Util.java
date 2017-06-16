/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package util;

import java.sql.Date;
import java.time.LocalDate;
import static java.time.temporal.ChronoUnit.DAYS;

/**
 *
 * @author stefan
 */
public class Util {
    public static long periodUDanima(Date pocetakInkluzivni, Date krajInkluzivni){
        LocalDate lDate1 = pocetakInkluzivni.toLocalDate();
        LocalDate lDate2 = krajInkluzivni.toLocalDate();
        
        return DAYS.between(lDate1, lDate2) + 1;
    }
}

package functions;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateandTine {
    public static void timeAndDate(){
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
        LocalDateTime now = LocalDateTime.now();
        System.out.println(dtf.format(now));
    }

    public static void main(String[] args) {
        timeAndDate();
    }
}

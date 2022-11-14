package Conditional_Statement_Exercise;

import java.util.Scanner;

public class Increment_ASCII {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        String incrimentedstr="";
        for (int i = 0; i < str.length(); i++) {
            if((str.charAt(i)>=97&str.charAt(i)<=122)|(str.charAt(i)>=65&str.charAt(i)<=90))
                 incrimentedstr+=(char)(str.charAt(i)+1);
            else
                incrimentedstr+=(char)(str.charAt(i));

        }
        System.out.println(incrimentedstr);
    }
}

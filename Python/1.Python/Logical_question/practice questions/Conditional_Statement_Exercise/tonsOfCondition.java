package Conditional_Statement_Exercise;

import java.util.Scanner;

public class tonsOfCondition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int anInteger = sc.nextInt();


        int count = 0; //to check the number of digits in an Integer
        int newint = anInteger;
        while (newint != 0) {
            newint /= 10;
            count++;
        }

        int anotherint = anInteger; //extracting first Digit for later use to check whether it is even or odd
        while (!(anotherint < 10 & anotherint >= 0)) {
            anotherint /= 10;
        }

        String aString = sc.next().toLowerCase();

        char schar = aString.charAt(0); //getting first alphabet of a string

        int letmecount = 0;  //checking whether the string contains x,y,z or not.
                            // If it contains x,y,z value of letmecount will be less than the size of string.
        for (int i = 0; i < aString.length(); i++) {
            if (!((aString.charAt(i) == 'x') | (aString.charAt(i) == 'y') | (aString.charAt(i) == 'z'))) {
                letmecount++;
            }
        }

        if (anInteger % 2 == 0) {
            if (aString.length() >= 5 & aString.length() <= 10) {
                if (!(schar == 'a' | schar == 'b' | schar == 's' | schar == 'p')) {
                    if (letmecount == aString.length()) {
                        if (count >= 2 & count <=4) {
                            if (anotherint % 2 != 0)
                                System.out.println("Eureka");
                        }
                    }
                }
            }
        }
    }
}
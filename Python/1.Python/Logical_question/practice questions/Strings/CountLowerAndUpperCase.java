//6.Write a program to find the number of uppercase and lower case characters in a string.

package Strings;

import java.util.Scanner;

public class CountLowerAndUpperCase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lowerCount = 0;
        int upperCount = 0;
        System.out.print("Enter a String: ");
        String inputString = sc.nextLine();
        for (int i = 0; i < inputString.length(); i++) {
            if (inputString.charAt(i) >= 97 && inputString.charAt(i) <= 122)
                lowerCount++;

            if (inputString.charAt(i) >= 65 && inputString.charAt(i) <= 90)
                upperCount++;
        }

        System.out.println("Total number of lower case alphabets in a string are: " + lowerCount);
        System.out.println("Total number of upper case alphabets in a string are: " + upperCount);
    }
}

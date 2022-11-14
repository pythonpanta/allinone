//7.Write a program to find the special characters in the string. Special characters includes !@#$

package Strings;

import java.util.Scanner;

public class CountOfSpecialCharacter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        System.out.print("Enter a String: ");
        String inputString = sc.nextLine();
        for (int i = 0; i < inputString.length(); i++) {
            if (!((inputString.charAt(i) >= 95 && inputString.charAt(i) <= 122)
                    || (inputString.charAt(i) >= 65 && inputString.charAt(i) <= 90)))
                count++;
        }
        System.out.println("Total number of special character in a String are " + count);
    }
}

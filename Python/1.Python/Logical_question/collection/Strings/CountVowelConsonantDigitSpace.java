//14.Write a program to find the number of vowels, consonants, digits and white space characters in a string.

package Strings;

import java.util.Scanner;

public class CountVowelConsonantDigitSpace {
    public static void main(String[] args) {
        int vowelCount = 0;
        int consonantCount = 0;
        int digitCount = 0;
        int spaceCount = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String inputString = sc.nextLine().toLowerCase();
        for (int i = 0; i < inputString.length(); i++) {
            boolean b = inputString.charAt(i) == 'a'
                    || inputString.charAt(i) == 'e'
                    || inputString.charAt(i) == 'i'
                    || inputString.charAt(i) == 'o'
                    || inputString.charAt(i) == 'u';
            if (b)
                vowelCount++;

            if (!b && (inputString.charAt(i) >= 95 && inputString.charAt(i) <= 122))
                consonantCount++;

            if (Character.isDigit(inputString.charAt(i)))
                digitCount++;

            if (inputString.charAt(i) == ' ')
                spaceCount++;
        }

        System.out.println("Total vowels in a String: " + vowelCount);
        System.out.println("Total consonants in a String: " + consonantCount);
        System.out.println("Total digits in a String: " + digitCount);
        System.out.println("Total space in a String: " + spaceCount);
    }
}

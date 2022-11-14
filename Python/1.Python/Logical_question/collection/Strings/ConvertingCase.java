//8.Write a program to take string input and convert it to uppercase and lowercase with out
//using the String function. [ USE ASCII Concept ]

package Strings;

import java.util.Scanner;

public class ConvertingCase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String inputString = sc.nextLine();
        StringBuilder upper = new StringBuilder();
        StringBuilder lower = new StringBuilder();
        System.out.println("Converted to Uppercase");
        for (int i = 0; i < inputString.length(); i++) {
            if (inputString.charAt(i) >= 97 && inputString.charAt(i) <= 122)
                upper.append((char) (inputString.charAt(i) - 32));
            else
                upper.append(inputString.charAt(i));
        }

        System.out.println(upper);

        System.out.println("Converted to Lowercase");
        for (int i = 0; i < inputString.length(); i++) {
            if (inputString.charAt(i) >= 65 && inputString.charAt(i) <= 90)
                lower.append((char) (inputString.charAt(i) + 32));
            else
                lower.append(inputString.charAt(i));
        }
        System.out.println(lower);
    }
}

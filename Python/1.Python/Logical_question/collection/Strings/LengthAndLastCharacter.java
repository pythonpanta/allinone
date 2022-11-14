//1.Write a program to take a string input and display its length and last character.

package Strings;

import java.util.Scanner;

public class LengthAndLastCharacter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String:");
        String inputString = sc.nextLine();
        System.out.println("Length of String = " + inputString.length());
        System.out.println("Last character of string = " + inputString.charAt(inputString.length() - 1));
    }
}


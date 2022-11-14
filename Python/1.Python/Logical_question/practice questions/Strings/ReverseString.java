//4.Write a program that takes the string input and reverse the string and display it.

package Strings;

import java.util.Scanner;

public class ReverseString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String inputString = sc.nextLine();
        StringBuilder reversedString = new StringBuilder();
        for (int i = inputString.length() - 1; i >= 0; i--) {
            reversedString.append(inputString.charAt(i));
        }

        System.out.println("Reversed String is : " + reversedString);
    }
}

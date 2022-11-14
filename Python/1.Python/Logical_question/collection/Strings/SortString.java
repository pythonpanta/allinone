//11.Write a program to take a string input and sort it alphabetically.

package Strings;

import java.util.Arrays;
import java.util.Scanner;

public class SortString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String inputString = sc.next();
        char[] charArray = inputString.toCharArray();
        Arrays.sort(charArray);
        System.out.println(new String(charArray));
    }
}

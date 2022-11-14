//5.Write a program to find the number of white spaces used in a string.

package Strings;

import java.util.Scanner;

public class CountWhiteSpace {
    public static void main(String[] args) {
        int count = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String inputString = sc.nextLine();
        for (int i = 0; i < inputString.length(); i++) {
            if (inputString.charAt(i) == ' ')
                count++;
        }

        System.out.println("Total number of white Spaces : " + count);
    }
}


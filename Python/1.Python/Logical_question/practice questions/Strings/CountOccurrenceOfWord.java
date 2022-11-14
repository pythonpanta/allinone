package Strings;

import java.util.Scanner;

public class CountOccurrenceOfWord {
    public static void main(String[] args) {
        int count = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String: ");
        String inputString = sc.nextLine();

        String[] a = inputString.split(" ");
        for (int i = 0; i < a.length; i++) {
            if (a[i].equals("life"))
                count++;
        }

        System.out.println("The number of times 'life' present in string is: " + count);
    }
}

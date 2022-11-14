package Conditional_Statement_Exercise;

import java.util.Scanner;

public class Positive_or_Not {
    public static void main(String[] args) {
        System.out.println("Enter a number:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if (num > 0)
            System.out.println("Positive");
        else
            System.out.println("Negative");
    }
}
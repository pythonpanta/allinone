package Conditional_Statement_Exercise;

import java.util.Scanner;

public class can_vote_or_not {
    public static void main(String[] args) {
        System.out.println("Enter age:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if (num < 18)
            System.out.println("Not eligible for voting");
        else
            System.out.println("eligible for voting");
    }
}

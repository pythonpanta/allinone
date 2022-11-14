package functions;

import java.util.Scanner;

public class EligibletoVote {
    public static boolean canVote(int age){
        if(age>=18)
            return true;
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter age: ");
        int age = sc.nextInt();
        if(canVote(age))
            System.out.println("Is eligible to vote");
        else
            System.out.println("Not Eligible to vote");

    }
}

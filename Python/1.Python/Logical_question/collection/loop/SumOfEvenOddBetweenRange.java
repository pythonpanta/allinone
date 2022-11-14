package loop;

import java.util.Scanner;

public class SumOfEvenOddBetweenRange {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Range of the Number: ");
        System.out.print("Initial: ");
        int initial = sc.nextInt();
        System.out.print("Final: ");
        int Final = sc.nextInt();
        int somOfEvem=0;
        int sumofOdd=0;

        for (int i = initial; i < Final; i++) {
            if(i%2==0)
                somOfEvem+=i;
            else
                sumofOdd+=i;
        }

        System.out.println("Sum of Even numbers Between the Range: "+somOfEvem);
        System.out.println("Sum of odd numbers between the Range: "+sumofOdd);

    }
}

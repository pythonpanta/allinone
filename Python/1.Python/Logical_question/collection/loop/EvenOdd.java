package loop;

import java.util.Scanner;

public class EvenOdd {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the Number: ");
            int N = sc.nextInt();
            int somOfEvem=0;
            int sumofOdd=0;

            for (int i =1; i <=N; i++) {
                if(i%2==0)
                    somOfEvem+=i;
                else
                    sumofOdd+=i;
            }

            System.out.println("Sum of Even numbers Between the Range: "+somOfEvem);
            System.out.println("Sum of odd numbers between the Range: "+sumofOdd);

        }
}

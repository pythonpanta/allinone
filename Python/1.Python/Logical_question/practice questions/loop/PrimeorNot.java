package loop;

import java.util.Scanner;

import static java.lang.Math.sqrt;

public class PrimeorNot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a Number: ");
        int num = sc.nextInt();
        int count = 0;
        for (int i = 2; i <= sqrt(num) ; i++) {
            if(num%i==0)
                count++;

        }
        if (count==0)
            System.out.println("Prime");
        else
            System.out.println("Composite");
    }
}

package functions;

import java.util.Scanner;

public class Prime {
    public static boolean checkPrime(int num){
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if(num%i == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a Number:");
        int n = sc.nextInt();
        if(checkPrime(n))
            System.out.println("The Number is prime");
        else
            System.out.println("Not Prime");
    }
}

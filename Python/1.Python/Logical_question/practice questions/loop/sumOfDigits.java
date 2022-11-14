package loop;

import java.util.Scanner;

public class sumOfDigits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Number: ");
        int num = sc.nextInt();
        int sum = 0;
        while (num!=0){
            int rem = num%10;
            sum = sum + rem;
            num/=10;
        }

        System.out.println("Sum of digits of a number: "+sum);
    }
}

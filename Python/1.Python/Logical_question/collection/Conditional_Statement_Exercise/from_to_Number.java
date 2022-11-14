package Conditional_Statement_Exercise;

import java.util.Scanner;

public class from_to_Number {
    public static void main(String[] args) {
        System.out.println("Enter From Number");
        Scanner sc = new Scanner(System.in);
        int fromNumber = sc.nextInt();
        System.out.println("Enter To Number");
        int toNumber = sc.nextInt();

        if (fromNumber<0) {
            System.out.println("Enter From Number");
            fromNumber = sc.nextInt();
        }
        if(toNumber<0){
            System.out.println("Enter To Number");
            toNumber = sc.nextInt();
        }

        if(fromNumber>toNumber) {
            int temp = fromNumber;
            fromNumber = toNumber;
            toNumber = temp;
            for (int i = fromNumber; i < toNumber; i++) {
                System.out.print(i+" ");
            }
        }
        else {
            for (int i = fromNumber; i < toNumber; i++) {
                System.out.print(i+" ");

            }
        }

    }
}

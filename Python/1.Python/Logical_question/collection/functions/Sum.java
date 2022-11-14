package functions;

import java.util.Scanner;

public class Sum {
    public static int sum(int num1 , int num2, int num3){
        return num1+num2+num3;
    }

    public static void main(String[] args) {
        System.out.println("Enter 3 Numbers: ");
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();
        System.out.println("Totsl of three Numbers is: "+sum(num1,num2,num3));
    }
}
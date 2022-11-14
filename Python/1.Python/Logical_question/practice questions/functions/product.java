package functions;

import java.util.Scanner;

public class product {
    public static int product(int a , int b){
        return a*b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two Numbers:");
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println("the product of two number is: "+product(x,y));

    }
}

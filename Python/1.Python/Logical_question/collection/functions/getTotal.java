package functions;

import java.util.Scanner;

public class getTotal {
    public static int getTotal(int a , int b){
        return a+b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        int x = sc.nextInt();
        int y =sc.nextInt();
        System.out.println("Total of two Number is : "+getTotal(x,y));
    }
}

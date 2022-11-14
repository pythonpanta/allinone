package functions;

import java.util.Scanner;

public class MultiplicationTable {
    public static void table(int n){
        for (int i = 1; i <=10 ; i++) {
            System.out.println(n+" X "+i+" = "+n*i);
        }
    }

    public static void main(String[] args) {
        System.out.println("Enter a Number:");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        table(num);
    }
}

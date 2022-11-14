package functions;

import jdk.nashorn.internal.runtime.regexp.joni.ScanEnvironment;

import java.util.Scanner;

public class Swap {
    public static void swap(int a, int b){
        int temp = a;
        a = b;
        b = temp;
        System.out.println("Numbers after getting swapped:");
        System.out.println("a = "+a);
        System.out.println("b = "+b);
    }

    public static void main(String[] args) {
        Scanner sc = new  Scanner(System.in);
        System.out.println("Enter two Numbers: ");
        System.out.print("a = ");
        int a = sc.nextInt();
        System.out.print("b = ");
        int b = sc.nextInt();
        swap(a,b);
    }
}

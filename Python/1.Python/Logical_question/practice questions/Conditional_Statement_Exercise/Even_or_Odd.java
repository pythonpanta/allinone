package Conditional_Statement_Exercise;

import java.util.Scanner;

public class Even_or_Odd {
    public static void main(String[] args){
        System.out.println("Enter a number:");
        Scanner sc =new  Scanner(System.in);
        int num = sc.nextInt();
        if(num%2==0)
            System.out.println("Even");
        else
            System.out.println("odd");
    }
}

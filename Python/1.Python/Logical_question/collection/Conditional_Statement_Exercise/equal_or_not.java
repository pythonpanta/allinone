package Conditional_Statement_Exercise;

import java.util.Scanner;

public class equal_or_not {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        int num1=sc.nextInt();
        int num2=sc.nextInt();
        if(num1==num2)
            System.out.println("Equal");
        else
            System.out.println("not equal");
    }
}

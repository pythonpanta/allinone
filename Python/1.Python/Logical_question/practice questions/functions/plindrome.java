package functions;

import jdk.nashorn.internal.runtime.regexp.joni.ScanEnvironment;

import java.util.Scanner;

public class plindrome {
    public static void plindrome(int n){
        int newNum = 0;
        int a = n;
        while (a!=0){
            int rem = a%10;
            newNum=newNum*10+rem;
            a/=10;
        }
        if (newNum==n)
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        plindrome(n);
    }
}
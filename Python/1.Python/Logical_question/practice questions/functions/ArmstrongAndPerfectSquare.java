package functions;

import java.util.Scanner;

public class ArmstrongAndPerfectSquare {
    public  static boolean Armstrong(int n){
        int a = n;
        int sum = 0;
        while (a!=0){
           int rem = a % 10;
           sum = sum*10+rem*rem*rem;
           a/=10;
        }
        return sum == n;
    }

    public static boolean PrefectSquare(int n){
        if (n >= 0) {
            int sr = (int)Math.sqrt(n);
            return ((sr * sr) == n);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Number: ");
        int n = sc.nextInt();
        if(Armstrong(n))
            System.out.println(n+" is Armstrong Number");
        else
            System.out.println("Not Armstrong Number");

        if(PrefectSquare(n))
            System.out.println(n+" is Perfect Square");
        else
            System.out.println("Not Perfect Square");
    }
}

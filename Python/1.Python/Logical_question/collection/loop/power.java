package loop;

import java.util.Scanner;

public class power {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two numbers:");
        int num1= sc.nextInt();
        int num2= sc.nextInt();
        int Exp=1;

        for (int i = 0; i < num2; i++) {
            Exp*=num1;
        }

        System.out.println("vlaue first number raised to second number is: "+Exp);
    }
}

package loop;

import java.util.Scanner;

public class doWhile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int repeat = 0;
        do {
            System.out.print("Enter two numbers: ");
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();
            int sum = num1+num2;
            System.out.println("Sum of "+num1+" and "+num2+" is: "+sum);
            System.out.println("want to repeat again: (if yes press 1) ");
            repeat = sc.nextInt();

        }while (repeat == 1);
    }
}

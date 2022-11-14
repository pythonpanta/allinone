//29.Write a program making use of all try, catch, throw, throws, and finally keywords.

package ExceptionHandelling;

import java.util.Scanner;

public class TryCatchFinallyThrowThrows {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        System.out.print("A = ");
        int a = sc.nextInt();
        System.out.print("B = ");
        int b = sc.nextInt();

        try {
            divide(a, b);
        } catch (ArithmeticException ex) {
            System.out.println(ex.getMessage());
        } finally {
            System.out.println("No matter what it will execute");
        }

    }

    static int divide(int a, int b) throws ArithmeticException {
        if (b == 0)
            throw new ArithmeticException("Do not divide by zero");
        return a / b;
    }
}

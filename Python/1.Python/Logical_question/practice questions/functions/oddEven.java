package functions;

import java.util.Scanner;

public class oddEven {
    public static boolean isEven(int Parameter){
        return Parameter % 2 == 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        System.out.println("is the Provided Number Even: "+isEven(n));
    }
}

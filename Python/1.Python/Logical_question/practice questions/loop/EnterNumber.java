package loop;

import java.util.Scanner;

public class EnterNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = -1;
        do {
            System.out.println("Enter a number: ");
            num = sc.nextInt();
        }while (num!=0);
    }
}

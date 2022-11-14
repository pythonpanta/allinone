package loop;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        while (true) {
            System.out.println("1.Continue");
            System.out.println("2.Exit");
            int n = sc.nextInt();
            switch (n) {
                case 1:
                        count++;
                        break;
                case 2:
                    System.out.println("Total number of times 1 was chosen: " + count);
                    System.exit(0);
                default:
                    System.out.println("Enter the valid option: ");
                    break;

            }

        }
    }
}
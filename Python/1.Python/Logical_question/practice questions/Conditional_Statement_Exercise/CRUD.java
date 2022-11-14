package Conditional_Statement_Exercise;

import java.util.Locale;
import java.util.Scanner;

public class CRUD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Type one of the following option:");
        System.out.println("CREATE");
        System.out.println("READ");
        System.out.println("UPDATE");
        System.out.println("DELETE");



        String Choice = sc.next().toLowerCase();

        switch (Choice){
            case "create":
                System.out.print("Number of times:");
                int num = sc.nextInt();
                for (int i = 0; i < num; i++)
                    System.out.println("CREATE");
                break;

            case "read":
                System.out.print("Number of times:");
                num = sc.nextInt();
                for (int i = 0; i < num; i++)
                    System.out.println("READ");
                break;
            case "update":
                System.out.print("Number of times:");
                num = sc.nextInt();
                for (int i = 0; i < num; i++)
                    System.out.println("UPDATE");
                break;
            case "delete":
                System.out.print("Number of times:");
                num = sc.nextInt();
                for (int i = 0; i < num; i++)
                    System.out.println("DELETE");
                break;

            default:
                System.out.println("TRY AGAIN");
        }
    }
}

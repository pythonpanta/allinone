package loop;

import java.util.Scanner;

public class multiplicationTable {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter positive Number");
        int positive_Number = sc.nextInt();
        while (positive_Number<0)
            positive_Number=sc.nextInt();

        for (int i = 1; i <=10 ; i++) {
            System.out.println(positive_Number+" x "+i+" = "+positive_Number*i);
        }
    }
}

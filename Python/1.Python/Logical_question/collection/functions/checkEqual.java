package functions;

import java.util.Scanner;

public class checkEqual {
    public static boolean isEqual(int a , int b){
        return a == b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Two Numbers: ");
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println("Are the Provided Numbers Equal: "+isEqual(x,y));
    }
}

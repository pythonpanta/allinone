package functions;

import java.util.Scanner;

public class Leep {
    public static boolean isLeep(int year){
        return ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
    }

    public static void main(String[] args) {
        System.out.print("Enter Year:");
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        System.out.println("is "+year+" a leep year: "+isLeep(year));
    }
}

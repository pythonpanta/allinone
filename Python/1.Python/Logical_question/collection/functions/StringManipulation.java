package functions;

import java.util.Scanner;

public class StringManipulation {
    public static void strManipulate(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your Name: ");
        String name = sc.next();
        System.out.println("Hello, How are you? "+name);
    }

    public static void main(String[] args) {
        strManipulate();
    }
}

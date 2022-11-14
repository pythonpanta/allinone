package Basic_Practice_Question;

import java.util.Scanner;

public class Hello_name {
    public static  void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your Name:");
        String name = input.next();
        System.out.println("Hello "+name);
    }
}

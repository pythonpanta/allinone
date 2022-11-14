package functions;

import java.util.Scanner;

public class pswwordValidity {
    public static boolean checkPassword(String password){
        if (password.length() < 10) return false;

        int charCount = 0;
        int numCount = 0;
        for (int i = 0; i < password.length(); i++) {

            char ch = password.charAt(i);

            if (is_Numeric(ch)) numCount++;
            else if (is_Letter(ch)) charCount++;
            else return false;
        }


        return (charCount >= 2 && numCount >= 2);
    }

    public static boolean is_Letter(char ch) {
        ch = Character.toUpperCase(ch);
        return (ch >= 'A' && ch <= 'Z');
    }


    public static boolean is_Numeric(char ch) {

        return (ch >= '0' && ch <= '9');
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your Password: ");
        String Pass = sc.nextLine();
        if(checkPassword(Pass)){
            System.out.println("Password is Valid: "+Pass);
        }
        else
            System.out.println("Password is Invalid!!");
    }
}

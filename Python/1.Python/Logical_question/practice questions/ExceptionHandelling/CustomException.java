package ExceptionHandelling;

import java.util.Scanner;

public class CustomException extends Exception{
    public CustomException(String message){
        super(message);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your Name: ");
        try {
            String name = sc.next();
            if (name.equals("Ravi"))
                throw  new CustomException("Yes, I am Ravi");
        }catch (CustomException ce){
            System.out.println(ce.getMessage());
        }
    }
}

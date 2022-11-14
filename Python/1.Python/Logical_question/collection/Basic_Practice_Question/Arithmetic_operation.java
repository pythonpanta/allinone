package Basic_Practice_Question;

import java.util.Scanner;

public class Arithmetic_operation {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two Numbers:");
        int num1=sc.nextInt();
        int num2=sc.nextInt();

        if(num2<=0 | num1<=0) {
            System.out.println("This is a dumb calculator so please Enter Positive Integers only");
            System.exit(0);
        }

        System.out.println("Enter Your Preferred Arithmetic Operation");
        System.out.println("Press '1' for Addition");
        System.out.println("Press '2' for Subtraction");
        System.out.println("Press '3' for Multiplication");
        System.out.println("Press '4' for Division");

        int Choice = sc.nextInt();

        switch (Choice){
            case 1:
                int result =num1+num2;
                System.out.println("The sum is "+result);
            case 2:
                result=num1-num2;
                System.out.println("The Difference is "+result);

            case 3:
                result=num1*num2;
                System.out.println("The Product is "+result);

            case 4:
                result=num1/num2;
                System.out.println("The Quotient is "+result);
            default:
                System.out.println("Please chose valid option from the above provided option");
        }


    }
}

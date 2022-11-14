package functions;

import java.util.Scanner;

public class SmallestGreatest {
    public static void averageNumber(int num1 , int num2 , int num3){
        if(num1>num2 & num1>num3) {
            System.out.println("Greatest is: "+num1);
            if(num2>num3){
                System.out.println("Smallest is: "+num3);
            }
            else
                System.out.println("Smallest is: "+num2);
        }
        else if(num2>num1 & num2>num3) {
            System.out.println("Greatest is: "+num2);
            if(num1>num3){
                System.out.println("Smallest is: "+num3);
            }
            else
                System.out.println("Smallest is: "+num1);
        }
        else {
            System.out.println("Greatest is: "+num3);
            if(num1>num2){
                System.out.println("Smallest is: "+num2);
            }
            else
                System.out.println("Smallest is: "+num1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 3 Numbers: ");
        int num1= sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();

        averageNumber(num1,num2,num3);

    }
}

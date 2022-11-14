package Basic_Practice_Question;

import java.util.Scanner;

public class Largest_num {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Please Enter 3 Numbers of your Choice:");
        int num1=sc.nextInt();
        int num3=sc.nextInt();
        int num2=sc.nextInt();

        if(num1>num2&num1>num3)
            System.out.println(num1+" is largest");
        else if (num2>num1&num2>num3)
            System.out.println(num2+" is largest");
        else
            System.out.println(num3+" is largest");

    }
}

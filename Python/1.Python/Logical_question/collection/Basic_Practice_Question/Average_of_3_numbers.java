package Basic_Practice_Question;

import java.util.Scanner;

public class Average_of_3_numbers {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter 3 numbers:");
        int num1=sc.nextInt();
        int num2=sc.nextInt();
        int num3=sc.nextInt();
        float average = (num1+num2+num3)/3;
        System.out.println("The average of provided 3 numbers is: "+average);
    }
}

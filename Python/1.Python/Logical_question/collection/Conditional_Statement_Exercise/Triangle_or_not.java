package Conditional_Statement_Exercise;

import java.util.Scanner;

public class Triangle_or_not {
    public static void main(String[] args){
        System.out.println("Enter Angles of Triangle in degree");
        Scanner sc = new Scanner(System.in);
        float angle1=sc.nextFloat();
        float angle2=sc.nextFloat();
        float angle3=sc.nextFloat();
        if(angle3+angle1+angle2==180)
            System.out.println("Triangle can be formed");
        else
            System.out.println("Triangle cannot be formed");

    }

}

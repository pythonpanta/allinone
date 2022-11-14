package Conditional_Statement_Exercise;

import java.util.Scanner;

public class feet_to_cm {
    public static void main(String[] args) {
        System.out.println("Enter height in feet:");
        Scanner sc = new Scanner(System.in);
        float height_in_feet = sc.nextFloat();
        double height_in_cm = height_in_feet*30.48;

        System.out.println("Height in Centimeter is "+height_in_cm);


    }
}

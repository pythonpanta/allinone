package Conditional_Statement_Exercise;

import java.util.Scanner;

public class Types_of_Triangle {
    public static void main(String [] args){
        System.out.println("Consider triangle ABC and Enter its sides Accordingly:");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length of side AB:");
        int AB=sc.nextInt();
        System.out.println();
        System.out.print("Enter length of side BC:");
        int BC=sc.nextInt();
        System.out.println();
        System.out.print("Enter length of side AC:");
        int AC=sc.nextInt();
        System.out.println();

        if(AB==BC&BC==AC){
            System.out.println("The triangle is equilateral");
            System.exit(0);
        }
        else if(AB==BC|AB==AC|BC==AC)
            System.out.println("The triangle is isosceles");
        else
            System.out.println("The triangle is scalene");
    }
}

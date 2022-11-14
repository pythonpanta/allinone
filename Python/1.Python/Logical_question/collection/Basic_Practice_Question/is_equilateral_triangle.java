package Basic_Practice_Question;

import java.util.Scanner;

public class is_equilateral_triangle {
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

        if(AB==BC&BC==AC)
            System.out.println("The triangle is equilateral");
        else
            System.out.println("The triangle is not equilateral");
    }
}

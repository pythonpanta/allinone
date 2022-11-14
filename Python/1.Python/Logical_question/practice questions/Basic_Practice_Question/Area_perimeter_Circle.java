package Basic_Practice_Question;

import java.util.Scanner;

public class Area_perimeter_Circle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter radius of a circle:");
        int radius = sc.nextInt();
        double perimeter = 2*Math.PI*radius;
        double area = Math.PI*radius*radius;
        System.out.println("The area of circle is: "+area);
        System.out.println("The perimeter of circle is: "+perimeter);
    }
}

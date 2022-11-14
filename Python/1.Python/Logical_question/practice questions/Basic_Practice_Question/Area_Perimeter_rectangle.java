package Basic_Practice_Question;

import java.util.Scanner;

public class Area_Perimeter_rectangle {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length and breadth of rectangle:");
        int len = sc.nextInt();
        int breadth = sc.nextInt();
        int area = len*breadth;
        int perimeter = 2*(len+breadth);
        System.out.println("The area of rectangle is: "+area);
        System.out.println("The perimeter of rectangle is: "+perimeter);
    }
}

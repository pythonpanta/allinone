package Basic_Practice_Question;

import java.util.Scanner;

public class Area_perimeter_Square {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length og a square:");
        int len = sc.nextInt();
        int perimeter = 4*len;
        int area = len*len;
        System.out.println("The area of square is: "+area);
        System.out.println("The perimeter of square is: "+perimeter);
    }
}

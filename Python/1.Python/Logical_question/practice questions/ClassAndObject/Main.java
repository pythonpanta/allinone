//Write a program to print the area of a rectangle by creating a class named 'Area' having
// two methods. First method named as 'setDim' takes length and breadth of the rectangle
// as parameters and the second method named as 'getArea' returns the area of the rectangle.
// Length and breadth of the rectangle are entered through the keyboard.

package ClassAndObject;

import java.util.Scanner;

class Area{
    int length;
    int breadth;
    public void setDim(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length of a Rectangle: ");
        length = sc.nextInt();
        System.out.print("Enter breadth of a Rectangle: ");
        breadth = sc.nextInt();
    }
    public int getArea(){
        return length*breadth;
    }
}

public class Main {
    public static void main(String[] args) {
        Area R1 = new Area();
        R1.setDim();
        System.out.println("Area of Rectangle is: "+R1.getArea());
    }


}

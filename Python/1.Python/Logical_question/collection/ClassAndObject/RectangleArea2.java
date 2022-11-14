//Write a program to print the area of a rectangle by creating a class named 'Area'
// taking the values of its length and breadth as parameters
// of its constructor and having a method named 'returnArea'
// which returns the area of the rectangle.

package ClassAndObject;

import java.util.Scanner;

class Area1{
    int length;
    int breadth;

    Area1(int l,int b){
        this.length=l;
        this.breadth=b;
    }

    public int returnArea(){
        return this.length*this.breadth;
    }
}

public class RectangleArea2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Length of a Rectangle: ");
        int l = sc.nextInt();
        System.out.print("Enter Breadth of a Rectangle: ");
        int b = sc.nextInt();

        Area1 a = new Area1(l,b);
        System.out.println("Area of Rectangle: "+a.returnArea());
    }
}

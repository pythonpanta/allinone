//Write a program to print the area of two rectangles having
// sides (4,5) and (5,8) respectively by creating a class named 'Rectangle' with a method
// named 'Area' which returns the area and length and breadth passed as parameters to its constructor.

package ClassAndObject;

import java.util.Arrays;

class Rectangle{
    int length;
    int breadth;

    Rectangle(int l,int b){
        this.length=l;
        this.breadth=b;
    }
    public int[] Area(){
        int[] a = new int[3];
        a[0]=this.length;
        a[1]=this.breadth;
        a[2]=this.length*this.breadth;

        return a;
    }
}

public class RectangleArea {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(4,5);
        Rectangle r2 = new Rectangle(5,8);
        System.out.println("Length Breadth and Area of Rectangle 1 is: "+ Arrays.toString(r1.Area()));
        System.out.println("Length Breadth and Area of Rectangle 2 is: "+ Arrays.toString(r2.Area()));


    }
}

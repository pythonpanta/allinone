//Repeat the above question for 4 rectangles, 4 squares and 5 circles.
//Hint- Use an array of objects.

package Abstraction;

import java.util.Scanner;

public class ArrayOfObjects extends Shape {
    @Override
    int rectangleArea(int l, int b) {
        this.length = l;
        this.breadth = b;
        return l * b;
    }

    @Override
    int squareArea(int s) {
        this.side = s;
        return s * s;
    }

    @Override
    double circleArea(int r) {
        this.radius = r;
        return 3.14 * r * r;
    }

    public static void main(String[] args) {
        ArrayOfObjects[] R4 = new ArrayOfObjects[4];
        ArrayOfObjects[] C5 = new ArrayOfObjects[5];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < R4.length; i++) {
            int j = i + 1;
            System.out.println("Enter length and Breadth of Rectangle " + j + ":");
            System.out.print("length = ");
            int l = sc.nextInt();
            System.out.print("Breadth = ");
            int b = sc.nextInt();
            R4[i] = new ArrayOfObjects();
            System.out.println("Area of rectangle: " + R4[i].rectangleArea(l, b));
        }
        for (int i = 0; i < R4.length; i++) {
            int j = i + 1;
            System.out.println("Enter length of Square " + j + ":");
            System.out.print("length = ");
            int s = sc.nextInt();
            R4[i] = new ArrayOfObjects();
            System.out.println("Area of square: " + R4[i].squareArea(s));
        }

        for (int i = 0; i < C5.length; i++) {
            int j = i + 1;
            System.out.println("Enter radius of circle " + j + ":");
            System.out.print("length = ");
            int r = sc.nextInt();
            C5[i] = new ArrayOfObjects();
            System.out.println("Area of square: " + C5[i].circleArea(r));
        }
    }
}

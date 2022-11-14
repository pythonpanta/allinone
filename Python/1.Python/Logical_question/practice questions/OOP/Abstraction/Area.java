//We have to calculate the area of a rectangle, a square and a circle. Create an abstract class 'Shape' with three
// abstract methods namely 'RectangleArea' taking two parameters, 'SquareArea' and 'CircleArea' taking one parameter
// each. The parameters of 'RectangleArea' are its length and breadth, that of 'SquareArea' is its side and that of
// 'CircleArea' is its radius. Now create another class 'Area' containing all the three methods 'RectangleArea',
// 'SquareArea' and 'CircleArea' for printing the area of rectangle, square and circle respectively. Create an
// object of class 'Area' and call all the three methods.


package Abstraction;

import java.util.Scanner;

abstract class Shape{
    int length,breadth,radius,side;
    abstract int rectangleArea(int l, int b);
    abstract int squareArea(int s);
    abstract double circleArea(int r);
}

public class Area extends Shape{

    Area(int l , int b){
        this.length=l;
        this.breadth=b;
    }
    Area(int r){
        this.radius=r;
    }
    @Override
    int rectangleArea(int l, int b) {
        this.length=l;
        this.breadth=b;
        return l*b;
    }

    @Override
    int squareArea(int s) {
        this.side=s;
        return s*s;
    }

    @Override
    double circleArea(int r) {
        this.radius=r;
        return 3.14*r*r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int len=sc.nextInt();
        int breadth=sc.nextInt();
        int radius = sc.nextInt();
        int side = sc.nextInt();
        Area r = new Area(len,breadth);
        Area c = new Area(radius);
        Area s = new Area(side);

        System.out.println("Area of circle: "+c.circleArea(radius));
        System.out.println("Area of rectangle: "+r.rectangleArea(len,breadth));
        System.out.println("Area of square: "+s.squareArea(side));
    }
}

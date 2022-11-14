package functions;

import java.util.Scanner;

public class AreaofTriangle {

    public static double TriangleArea(int a , int b , int c){
        int s = (a+b+c)/2;
        return Math.sqrt(s*(s-a)*(s-b)*(s-c));
    }

    public static void main(String[] args) {
        System.out.println("Enter sides of a triangle: ");
        System.out.print("Input Side - 1: ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.print("Input Side - 2: ");
        int b = sc.nextInt();
        System.out.println("Input Side - 3: ");
        int c = sc.nextInt();
        System.out.println("Area of the Triangle is: "+TriangleArea(a,b,c));
    }
}

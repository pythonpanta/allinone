//Write an object oriented programming to find the area and perimeter of the circle.

package OOP;

import java.util.Scanner;

class PerimeterArea{
    int radius;
    PerimeterArea(int r){
        this.radius=r;
    }
    public double primeter(){
        return 2*3.14*this.radius;
    }

    public double area(){
        return 3.14*this.radius*this.radius;
    }

    public void display(){
        System.out.println("Area of circle = "+area());
        System.out.println("Perimeter of circle = "+primeter());
    }
}
public class Circle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Radius of a circle: ");
        int r = sc.nextInt();
        PerimeterArea c = new PerimeterArea(r);
        c.area();
        c.primeter();
        c.display();
    }
}

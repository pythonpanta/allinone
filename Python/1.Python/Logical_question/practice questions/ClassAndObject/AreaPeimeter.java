//Write a program to print the area and perimeter of a triangle having sides of 3, 4 and 5
// units by creating a class named 'Triangle' without any parameter in its constructor.

package ClassAndObject;
class Triangle{
    int side1,side2,side3;

    Triangle(){
        side1=3;
        side2=4;
        side3=5;
    }
    public double Area(){
        int s = (side1+side2+side3)/2;
        return Math.sqrt(s*(s-side1)*(s-side2)*(s-side3));
    }

    public int Perimeter(){
        return side1+side2+side3;
    }
}


public class AreaPeimeter {
    public static void main(String[] args) {
        Triangle t = new Triangle();
        System.out.println("Area = "+t.Area());
        System.out.println("Perimerter = "+t.Perimeter());
    }
}

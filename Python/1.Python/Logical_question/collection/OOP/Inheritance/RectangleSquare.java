//2.Create a class named 'Rectangle' with two data members 'length' and 'breadth' and two methods to
// print the area and perimeter of the rectangle respectively. Its constructor having parameters for
// length and breadth is used to initialize length and breadth of the rectangle. Let class 'Square'
// inherit the 'Rectangle' class with its constructor having a parameter for its side (suppose s) calling
// the constructor of its parent class as 'super(s,s)'. Print the area and perimeter of a rectangle and a square.

package OOP.Inheritance;

class Rectangle{
    int length;
    int breadth;
    Rectangle(int l, int b){
        this.length=l;
        this.breadth=b;
    }
    Rectangle(){};

    void perimeter(){
        int peri=2*(this.length+this.breadth);
        System.out.println("Perimeter = "+peri);
    }

    void area(){
        int ar=this.length*this.breadth;
        System.out.println("Area = "+ar);
    }
}

class Square extends Rectangle{
    int side;
    Square(int s){
        super(s,s);
    }
}

public class RectangleSquare {

    public static void main(String[] args) {
        Rectangle r = new Rectangle(2,3);
        Square s = new Square(4);
        System.out.println("Perimeter and Area of Rectangle");
        r.perimeter();
        r.area();
        System.out.println("Perimeter and Area of Square");
        s.perimeter();
        s.area();
    }
}

//3.Create a class named 'Shape' with a method to print "This is This is shape". Then create two
// other classes named 'Rectangle', 'Circle' inheriting the Shape class, both having a method to
// print "This is rectangular shape" and "This is circular shape" respectively. Create a subclass
// 'Square' of 'Rectangle' having a method to print "Square is a rectangle". Now call the method of
// 'Shape' and 'Rectangle' class by the object of 'Square' class.

package OOP.Inheritance;

class Shape{
    void displayShape(){
        System.out.println("This is a shape");
    }
}

class RectangleShape extends Shape{
    void displayShapeRectangle(){
        System.out.println("This is a Rectangular Shape");
    }
}

class CircularShape extends Shape{
    void displayShapeCircle(){
        System.out.println("This is Circular Shape");
    }
}

public class SquareShape extends RectangleShape {
    void displayShapeSquare(){
        System.out.println("This is Square Shape");
    }

    public static void main(String[] args) {
        SquareShape sp = new SquareShape();
        sp.displayShape();
        sp.displayShapeRectangle();
        sp.displayShapeSquare();
    }
}

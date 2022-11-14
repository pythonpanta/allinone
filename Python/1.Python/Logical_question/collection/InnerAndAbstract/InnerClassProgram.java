//WAP to demonstrate member inner class.

package InnerAndAbstract;

class OuterClas
{
    static int outerX = 10;
    int outerY = 20;
    private int outerPrivate = 30;
    class InnerClass
    {
        void display()
        {
            System.out.println("outer_x = " + outerX);
            System.out.println("outer_y = " + outerY);
            System.out.println("outer_private = " + outerPrivate);

        }
    }
}
public class InnerClassProgram {
    public static void main(String[] args)
    {
        OuterClas outerObject = new OuterClas();
        OuterClas.InnerClass innerObject = outerObject.new InnerClass();

        innerObject.display();

    }
}

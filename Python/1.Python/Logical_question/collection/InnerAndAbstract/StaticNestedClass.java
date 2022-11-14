//WAP that contains the static nested class.

package InnerAndAbstract;
class OuterClass
{
    static int outerX = 10;
    int outerY = 20;
    private static int outerPrivate = 30;
    static class StaticNestedClass
    {
        void display()
        {
            System.out.println("outer_x = " + outerX);
            System.out.println("outer_private = " + outerPrivate);

        }
    }
}
public class StaticNestedClass {
    public static void main(String[] args)
    {
        OuterClass.StaticNestedClass nestedObject = new OuterClass.StaticNestedClass();

        nestedObject.display();

    }
}


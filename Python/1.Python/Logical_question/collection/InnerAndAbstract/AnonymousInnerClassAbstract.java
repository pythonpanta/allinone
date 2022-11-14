//12.WAP to demonstrate anonymous inner class using both techniques
// (class: may be abstract or concrete and interface) .

package InnerAndAbstract;

abstract class Example{
    abstract void display();
}

public class AnonymousInnerClassAbstract{
    void normalMethod(){
        System.out.println("This is Normal method");
    }

    public static void main(String[] args) {
        Example e = new Example() {
            @Override
            void display() {
                System.out.println("Overriding Abstract inner class Anonymously");
            }
        };

        AnonymousInnerClassAbstract an = new AnonymousInnerClassAbstract();
        e.display();
        an.normalMethod();
    }
}

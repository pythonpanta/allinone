//12.WAP to demonstrate anonymous inner class using both techniques
// (class: may be abstract or concrete and interface) .

package InnerAndAbstract;

interface Aclass{
    void show();
    void saySomething();
}

public class AnonymousInnerClassInterface {
    public static void main(String[] args) {
        Aclass ai = new Aclass(){
            @Override
            public void show(){
                System.out.println("Implementation by inner Anonymous Class");
            }
            @Override
            public void saySomething(){
                System.out.println("This is Implementing method of Anonymous Inner class");
            }
        };

        ai.show();
        ai.saySomething();
    }
}

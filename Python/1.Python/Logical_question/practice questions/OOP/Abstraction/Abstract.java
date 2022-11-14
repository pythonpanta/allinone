//An abstract class has a constructor which prints "This is constructor of abstract class",
// an abstract method named 'a_method' and a non-abstract method which prints "This is a normal method of
// abstract class". A class 'SubClass' inherits the abstract class and has a method named 'a_method' which prints
// "This is abstract method". Now create an object of 'SubClass' and call the abstract method and the non-abstract
// method. (Analyse the result)

package Abstraction;

abstract class AnAbstractClass{
    AnAbstractClass(){
        System.out.println("This is constructor of abstract class");
    }

    abstract void anAbstractMethod();
    void nonAbstract(){
        System.out.println("This is a normal method of abstract class");
    }
}

class SubClass extends AnAbstractClass{

    @Override
    void anAbstractMethod() {
        System.out.println("This is abstract method");
    }
}

public class Abstract {
    public static void main(String[] args) {
        SubClass sb = new SubClass();
        sb.anAbstractMethod();
        sb.nonAbstract();
    }
}

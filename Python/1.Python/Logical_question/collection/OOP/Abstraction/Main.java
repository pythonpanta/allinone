//Create an abstract class 'Parent' with a method 'message'. It has two subclasses each having a method
// with the same name 'message' that prints "This is first subclass" and "This is second subclass" respectively.
// Call the methods 'message' by creating an object for each subclass.

package Abstraction;

abstract class Parent {
    abstract void message();
}
class SubClass1 extends Parent{

    @Override
    void message() {
        System.out.println("This is First Sub Class");
    }
}

class SubClass2 extends Parent{

    @Override
    void message() {
        System.out.println("This is second Sub Class");
    }
}
public class Main {
    public static void main(String[] args) {
        SubClass1 s1 = new SubClass1();
        s1.message();
        SubClass2 s2 = new SubClass2();
        s2.message();
    }
}


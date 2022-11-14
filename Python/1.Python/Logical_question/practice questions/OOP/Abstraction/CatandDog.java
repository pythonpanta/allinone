//Create an abstract class 'Animals' with two abstract methods 'cats' and 'dogs'. Now create a class
// 'Cats' with a method 'cats' which prints "Cats meow" and a class 'Dogs' with a method 'dogs' which prints
// "Dogs bark", both inheriting the class 'Animals'. Now create an object for each of the subclasses and call their
// respective methods.

package Abstraction;

abstract class Animal{
    abstract void cats();
    abstract void  dogs();
}

class Cats extends Animal{
    @Override
    void cats() {
        System.out.println("Cats meow");
    }

    @Override
    void dogs() {
    }
}

class Dogs extends Animal{
    @Override
    void cats() {
    }

    @Override
    void dogs() {
        System.out.println("Dogs bark");
    }
}
public class CatandDog {
    public static void main(String[] args) {
        Dogs d = new Dogs();
        d.dogs();
        Cats c = new Cats();
        c.cats();
    }
}

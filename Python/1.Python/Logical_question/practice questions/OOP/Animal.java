
//Create an interface named AnimalEat and AnimalTravel. And create a class Animal which implements above two interfaces.
package OOP;

public class Animal implements AnimalEat,AnimalTravel{
    @Override
    public void eat() {
        System.out.println("I Eat A Lot");
    }

    @Override
    public void walk() {
        System.out.println("After Eating I need to walk  for Digestion");
    }

    public static void main(String[] args) {
        Animal A = new Animal();
        A.eat();
        A.walk();
    }
}

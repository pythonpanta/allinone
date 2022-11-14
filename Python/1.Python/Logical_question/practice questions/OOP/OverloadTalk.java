package OOP;

//Write a method that overloads the talk method by taking in a name and printing “Hello” with that name.


class A{
    public void Talk(){
        System.out.println("Some one is talking");
    }
}
class B extends A {
    public void Talk(String name){
        System.out.println("Hello "+name);
    }
}
public class OverloadTalk {
    public static void main(String[] args) {
        B b = new B();
        b.Talk("Apple");
        b.Talk();
    }
}

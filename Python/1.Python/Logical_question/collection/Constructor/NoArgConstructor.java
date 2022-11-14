package Constructor;

public class NoArgConstructor {
    int a;
    NoArgConstructor(){
        a=10;
    }

    public static void main(String[] args) {
        NoArgConstructor A = new NoArgConstructor();
        System.out.println("Value initialized from no argument constructor of 'a' is: "+A.a);
    }
}

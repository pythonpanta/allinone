//How do you achieve multiple inheritance in java? Give a suitable example for it.

package OOP;

public class MultipleInheritance extends Music implements Engine{
    @Override
    public void start() {
        System.out.println("Car Starts");
    }

    @Override
    public void stop() {
        System.out.println("Car Stops");
    }

    public static void main(String[] args) {
        MultipleInheritance m = new MultipleInheritance();
        Music M = new Music();
        m.start();
        m.stop();
        M.start();
        M.stop();
    }
}

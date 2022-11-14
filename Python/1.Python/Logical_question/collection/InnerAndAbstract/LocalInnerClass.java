//WAP that contains the local inner class.
package InnerAndAbstract;

class Outer {
    void outerMethod() {
        final int x = 5;
        System.out.println("inside outerMethod");
        class Inner {
            void innerMethod() {
                System.out.println("Inside Inner Method: x = " + x);
            }
        }
        Inner y = new Inner();
        y.innerMethod();
    }
}

class LocalInnerClass {
    public static void main(String[] args) {
        Outer x = new Outer();
        x.outerMethod();
    }
}


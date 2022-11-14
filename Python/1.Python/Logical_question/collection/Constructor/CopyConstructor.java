//Write a java program to copy the values from one object to another object. (Note: use constructor)

package Constructor;

public class CopyConstructor {
    int a,b;
    CopyConstructor(CopyConstructor c){
        this.a=c.a;
        this.b=c.b;
    }
    CopyConstructor(int x ,int y){
        this.a=x;
        this.b=y;
    }
    CopyConstructor(){}
    public void display(){
        System.out.println("The value of a and b is "+this.a+","+this.b);
    }

    public static void main(String[] args) {
        System.out.println("Initialized with Parameterized Constructor");
        CopyConstructor P = new CopyConstructor(2,3);
        CopyConstructor Q = new CopyConstructor(P);
        P.display();
        System.out.println("Initialized with Copy Constructor");
        Q.display();
    }
}

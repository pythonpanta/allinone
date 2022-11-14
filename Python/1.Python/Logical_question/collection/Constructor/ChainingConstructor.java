package Constructor;

public class ChainingConstructor {
    int Var1;
    int var2;
    int var3;
    ChainingConstructor(){
        System.out.println("This is constructor with no Argument");
    }
    ChainingConstructor(int X){
        this();
        this.Var1=X;
        System.out.println("One argument is Passes: "+Var1);
    }
    ChainingConstructor(int Y, int Z){
        this(3);
        this.var2=Y;
        this.var3=Z;
        System.out.println("Two arguments passed: "+var2+","+var3);
    }

    public static void main(String[] args) {
        ChainingConstructor c = new ChainingConstructor(4,5);
    }
}

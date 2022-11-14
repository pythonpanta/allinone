package loop;

public class whileInnerLoop {
    public static void main(String[] args) {
        int n=1;
        while (n==1){
            while (n==1){
                System.out.println("Hello, this is while inner loop");
                n++;
            }
        }
    }
}

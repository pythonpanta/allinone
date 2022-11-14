package loop;

public class dowhileInnerLoop {
    public static void main(String[] args) {
        int n=1;
        do {
            do {
                System.out.println("Hello, this is do while inner loop");
                n++;
            }while (n==1);
        }while(n==1);
    }
}

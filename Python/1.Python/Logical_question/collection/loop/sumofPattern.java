package loop;

public class sumofPattern {
    public static void main(String[] args) {
        int sum=0;
        int pattern = 0;
        for (int i = 0; i < 5; i++) {

            pattern = (pattern*10 + 2);
            sum = sum+pattern;
        }
        System.out.println("The sum is: "+sum);
    }
}

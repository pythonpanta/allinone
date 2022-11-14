package loop;

import java.util.Scanner;

public class sumofFraction {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Double fractionSum=0.0;
        for (float i = 1; i <=n ; i++) {
            double fraction = 1/i;
            fractionSum+=fraction;
        }

        System.out.println("Sum of Fractions: "+fractionSum);
    }
}

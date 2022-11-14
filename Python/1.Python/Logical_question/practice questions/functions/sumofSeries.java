package functions;
import java.util.Scanner;

public class sumofSeries {
    public static int sum(int n){
        int sum = 0;
        for (int i = 1; i <=n ; i++) {
            sum=sum+(factorial.getFactorial(i))/i;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Number: ");
        int n = sc.nextInt();
        System.out.println("Sum of series is: "+sum(n));
    }
}

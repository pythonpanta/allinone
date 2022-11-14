package functions;

import java.util.Scanner;

public class factorial {
    public static int getFactorial(int n){
        int fact =1;
        for (int i = 1; i <=n ; i++) {
            fact*=i;
        }
        return fact;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Number");
        int o = sc.nextInt();
        System.out.println("Factorial of "+o+" is: "+getFactorial(o));
    }

}

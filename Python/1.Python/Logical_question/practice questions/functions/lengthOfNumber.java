package functions;

import java.util.Scanner;

public class lengthOfNumber {
    public static int length(int n){
        int count =0;
        while (n!=0){
            n=n/10;
            count++;

        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println("Total Number of digits in Provided Number is: "+length(n));
    }
}

package loop;

import java.util.Scanner;

public class countofNegative {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ;int n=1;
        int count = 0;
        while(n >= 0){
            System.out.println("Enter a Number:");
            n=sc.nextInt();
            count++;
        }
        System.out.println("Total positive Numbers Entered: "+count);
    }
}

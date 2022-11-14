package functions;

import java.util.Scanner;

public class oddNumberBetweenTheRange {
    public static void displayOddNumbers(int start , int end){
        for (int i = start; i <=end ; i++) {
            if (i%2!=0)
                System.out.println(i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Start and End:");
        int start = sc.nextInt();
        int end = sc.nextInt();
        displayOddNumbers(start,end);
    }

}

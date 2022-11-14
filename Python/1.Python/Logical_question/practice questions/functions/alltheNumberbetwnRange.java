package functions;

import java.util.Scanner;

public class alltheNumberbetwnRange {
    public static void Dispaly(int start, int End){
        for (int i = start; i <= End; i++) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Start and End:");
        int start = sc.nextInt();
        int end = sc.nextInt();
        Dispaly(start,end);
    }
}

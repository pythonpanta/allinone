package Array;

import java.util.Scanner;

public class array_avg {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array:");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements of an array:");
        for (int i = 0; i < arr.length; i++) {
            arr[i]=sc.nextInt();
        }
        int sum=0;
        for (int i:arr) {
            sum+=i;
        }
        int avg = sum/arr.length;
        System.out.println("Average of Array elements is: "+avg);
    }
}

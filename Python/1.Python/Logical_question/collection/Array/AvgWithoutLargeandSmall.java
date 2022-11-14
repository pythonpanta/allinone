package Array;

import java.util.Scanner;

public class AvgWithoutLargeandSmall {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array:");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements of an array:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        int large = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>large){
                large=arr[i];
            }
        }

        int smallest=arr[0];
        for (int j : arr) {
            if (j<smallest)
                smallest=j;
        }


        int sum = 0;
        for (int i : arr) {
            if(i!=large & i!=smallest)
                sum += i;
        }
        int avg = sum / (arr.length-2);
        System.out.println("Average without Largest and Smallest element of an array: "+avg);
    }
}
package Array;

import java.util.Scanner;

public class pair {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the siz of an array:");
        int n = sc.nextInt();
        System.out.print("Enter the Specified sum");
        int sum = sc.nextInt();
        int [] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i]=sc.nextInt();
        }
        int count = 0;
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if(arr[i]+arr[j]==sum)
                    System.out.println("The pair whose sum is "+sum+" :"+"{"+arr[i]+","+arr[j]+"}");
            }
        }
    }
}

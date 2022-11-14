package Array;
import Array.sorting;

import java.util.Scanner;

public class Searching {

    static void binarySearch(int[] arr, int target){
        int start=0;
        int end = arr.length-1;
        for (int i = 0; i < arr.length; i++) {
            int mid = start + (end-start)/2;
            if(arr[mid]==target){
                System.out.println(target + " found at index: "+mid);
                System.exit(0);
            } else if (arr[mid]<target) {
                start=mid+1;
            }
            else
                end=mid-1;
        }
        System.out.println("target not found");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter tne number you want o search");
        int target = sc.nextInt();
        int[] arr = {4,6,7,3,57,2,8344,56,21,45,67};
        sorting.bubbleSort(arr);
        binarySearch(arr,target);

    }
}

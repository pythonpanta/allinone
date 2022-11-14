package Array;

import java.util.Arrays;

import static Array.sorting.bubbleSort;

public class diffrentSort {
    public static void main(String[] args) {
        int[] arr = {1, 5, -4, 7, 8, -6};
        int[] arr1 = new int[arr.length];
        bubbleSort(arr);
        arr1[0]=arr[arr.length-1];
        for (int i = 0; i < arr.length-1; i++) {
            arr1[i+1]=arr[i];
        }
        System.out.println("Rotated Sorted array: "+ Arrays.toString(arr1));
    }
}

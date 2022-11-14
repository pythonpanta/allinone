package Array;

import java.util.Arrays;

public class sorting {
    static void bubbleSort(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 1; j <arr.length-i ; j++) {
                if(arr[j-1]>arr[j]){
                    int temp = arr[j];
                    arr[j]=arr[j-1];
                    arr[j-1]=temp;
                }
            }
        }

        System.out.println("sorted array: "+ Arrays.toString(arr));
    }

    public static void main(String[] args) {
        int[] arr = {4, 6, 8, 2, 90, 1, 5, 7, 2};
        System.out.println("Unsorted array: " + Arrays.toString(arr));
        bubbleSort(arr);
    }
}
